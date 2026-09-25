#!/usr/bin/env python3
"""Score price-change predictions against what actually happened.

Two jobs, one ruler:

  fpl    Score FPL's own predictor, from the mirror alone. For every nightly batch in
         history/prices.csv, take the readings in history/progress/ that came before it
         and ask whether each limb called the movers:
           tonight  proj_0 at the last reading before the batch
           +1 day   proj_1 at the last reading >= 18h before that
           +2 days  proj_2 at the last reading >= 42h before that
         A value >= +100 is a predicted rise; <= -100 a predicted fall.
  calls  Score Claude's own calls (CSV files kept in the project under
         claude/data/price-calls/). Same batches, same rules, so the two are comparable.

  python3 tools/price_scores.py fpl   [--out data/derived/fpl-proj-scores.csv]
  python3 tools/price_scores.py calls CALLS.csv [MORE.csv ...] [--out scored.csv]

Calls CSV schema (one file per run, never appended):
  call_utc,element_id,web_name,call,nights,prog,proj_0,proj_1,proj_2,note
  call = rise | fall | none      nights = 1 for tonight's batch, 2 for the one after, ...

A BATCH is one distinct `observed_at` stamp in prices.csv (the fetch that first saw
the change; prices.csv and the progress files share run stamps). Limitation: a night
on which nothing in the game moved produces no batch, so predictions made for that
night are not scored. That's rare, since some player moves on almost every night.
"""
import argparse, bisect, collections, datetime as dt, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fplcommon import data_dir, read_csv, parse_utc, iso, uk, write_csv

ap = argparse.ArgumentParser()
ap.add_argument("mode", choices=["fpl", "calls"])
ap.add_argument("files", nargs="*")
ap.add_argument("--data")
ap.add_argument("--out")
a = ap.parse_args()
d = data_dir(a.data)

# batches: stamp -> {element_id: delta}
batches = collections.OrderedDict()
for r in read_csv(os.path.join(d, "history/prices.csv")):
    t = parse_utc(r["observed_at"])
    batches.setdefault(t, {})[int(r["element_id"])] = int(r["delta"])
bstamps = sorted(batches)


def sign(x, thr=100.0):
    if x in (None, ""):
        return 0
    x = float(x)
    return 1 if x >= thr else -1 if x <= -thr else 0


def score(pred, actual):
    """pred, actual: {element_id: +1/-1}. Returns (hits, false_alarms, misses)."""
    hits = sum(1 for e, s in pred.items() if actual.get(e) == s)
    return hits, len(pred) - hits, sum(1 for e, s in actual.items() if pred.get(e) != s)


if a.mode == "fpl":
    # stamp -> {element_id: row}; load lazily only the columns we need
    readings = {}
    for f in sorted(glob.glob(os.path.join(d, "history/progress/*.csv"))):
        for r in read_csv(f):
            t = parse_utc(r["snapshot_utc"])
            readings.setdefault(t, {})[int(r["element_id"])] = (r["progress_pct"], r["proj_0"], r["proj_1"], r["proj_2"])
    rstamps = sorted(readings)
    if not rstamps:
        sys.exit("no progress readings")

    def last_before(t):
        i = bisect.bisect_left(rstamps, t) - 1
        return rstamps[i] if i >= 0 else None

    rows, tot = [], collections.defaultdict(lambda: [0, 0, 0, 0])
    for b in bstamps:
        r0 = last_before(b)
        if r0 is None:
            continue
        actual = {e: (1 if v > 0 else -1) for e, v in batches[b].items()}
        for limb, idx, back in (("progress", 0, 0), ("proj_0", 1, 0), ("proj_1", 2, 18), ("proj_2", 3, 42)):
            rt = r0 if back == 0 else last_before(r0 - dt.timedelta(hours=back) + dt.timedelta(seconds=1))
            if rt is None or rt < rstamps[0]:
                continue
            pred = {e: sign(v[idx]) for e, v in readings[rt].items() if sign(v[idx])}
            h, fa, mi = score(pred, actual)
            rows.append([iso(b), uk(b), limb, iso(rt), len(actual), len(pred), h, fa, mi])
            t = tot[limb]; t[0] += 1; t[1] += h; t[2] += fa; t[3] += mi
    if a.out:
        write_csv(a.out, ["batch_utc", "batch_uk", "limb", "reading_utc", "movers", "predicted", "hits",
                          "false_alarms", "misses"], rows)
    print(f"FPL predictor, {len(bstamps)} batches in prices.csv, readings from {iso(rstamps[0])}.")
    print(f"{'limb':<9}{'batches':>8}{'hits':>6}{'false+':>8}{'missed':>8}  precision  recall")
    for limb in ("progress", "proj_0", "proj_1", "proj_2"):
        n, h, fa, mi = tot[limb]
        if n:
            p = h / (h + fa) if h + fa else float("nan"); r = h / (h + mi) if h + mi else float("nan")
            print(f"{limb:<9}{n:>8}{h:>6}{fa:>8}{mi:>8}  {p:9.0%}  {r:6.0%}")

else:
    if not a.files:
        sys.exit("calls mode needs one or more calls CSV files")
    out, tally = [], collections.Counter()
    for f in a.files:
        for c in read_csv(f):
            t = parse_utc(c["call_utc"]); n = int(c.get("nights") or 1)
            after = [b for b in bstamps if b > t]
            if len(after) < n or (after[n - 1] - t) > dt.timedelta(hours=30 + 24 * (n - 1)):
                verdict, moved = "pending", ""
            else:
                b = after[n - 1]
                moved = batches[b].get(int(c["element_id"]), 0)
                want = {"rise": 1, "fall": -1, "none": 0}[c["call"].strip().lower()]
                got = (moved > 0) - (moved < 0)
                verdict = "hit" if want == got else "miss"
            tally[verdict] += 1
            out.append([c["call_utc"], c["element_id"], c.get("web_name", ""), c["call"], n, moved, verdict, os.path.basename(f)])
    if a.out:
        write_csv(a.out, ["call_utc", "element_id", "web_name", "call", "nights", "actual_delta", "verdict", "file"], out)
    for r in out:
        print(",".join(str(x) for x in r))
    scored = tally["hit"] + tally["miss"]
    print(f"\nClaude's calls: {tally['hit']} of {scored} hits" + (f" ({tally['hit']/scored:.0%})" if scored else "")
          + f"; {tally['pending']} pending.")
