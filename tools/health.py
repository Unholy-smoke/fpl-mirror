#!/usr/bin/env python3
"""Mirror health check: is the data fresh, complete and internally consistent?

Replaces the data half of the old daily reconciliation run. Prints one line per
check, OK / WARN / FAIL. Exits 0 unless --strict and something FAILed.

  python3 tools/health.py            # from the repo root, after git clone / pull
  python3 tools/health.py --json     # machine-readable
  python3 tools/health.py --out data/derived/health.json   # what the workflow runs

In the workflow it runs AFTER fetch-status.json is written, so "freshness" there is always ~0h.
A reader judges the snapshot's age itself: now minus fetch-status.json run_at.

Checks
  freshness   fetch-status run_at age (WARN > 4h, FAIL > 9h; the measured
              scheduler lateness has reached 7h20m overnight, so 4h isn't alarming)
  fetches     failed_this_run, and last_success age of the keys every task needs
  rivals      a rivals/gw<current>-entry file and a transfers file for all nine
  progress    today's (UTC) history/progress file exists; stamps distinct; every
              stamp has the same row count; the newest stamp's count equals
              len(elements) in bootstrap when that stamp IS the current run
  prices      prices.csv parses; newest batch date
  derived     data/derived/* exist and are not older than the snapshot
"""
import argparse, collections, datetime as dt, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fplcommon import data_dir, load, parse_utc, iso, uk, read_csv

ap = argparse.ArgumentParser()
ap.add_argument("--data")
ap.add_argument("--json", action="store_true")
ap.add_argument("--strict", action="store_true")
ap.add_argument("--out", help="also write the results as JSON to this path (the workflow writes data/derived/health.json)")
a = ap.parse_args()
d = data_dir(a.data)
now = dt.datetime.now(dt.timezone.utc)
res = []


def add(level, check, msg):
    res.append({"level": level, "check": check, "msg": msg})


def age_h(t):
    return (now - t).total_seconds() / 3600


fs = load(d, "fetch-status.json")
run_at = parse_utc(fs["run_at"])
h = age_h(run_at)
add("OK" if h <= 4 else "WARN" if h <= 9 else "FAIL", "freshness",
    f"last snapshot {iso(run_at)} ({uk(run_at)}), {h:.1f}h old")

need = ["data/bootstrap-static.json", "data/fixtures.json", "data/league-standings.json",
        "data/entry-history.json", "data/event-status.json"]
stale = [k for k in need if not fs["files"].get(k, {}).get("last_success")
         or age_h(parse_utc(fs["files"][k]["last_success"])) > 9]
add("OK" if fs.get("failed_this_run", 0) == 0 and not stale else "WARN", "fetches",
    f"failed_this_run={fs.get('failed_this_run')}; " + (f"stale >9h: {', '.join(stale)}" if stale else "core keys fresh"))

ev = load(d, "events.json")
cur = ev.get("current_event")
try:
    st = load(d, "league-standings.json")["standings"]["results"]
    ids = [r["entry"] for r in st]
    miss = [i for i in ids if not os.path.isfile(os.path.join(d, f"rivals/gw{cur}-entry{i}.json"))
            or not os.path.isfile(os.path.join(d, f"transfers/entry{i}.json"))]
    add("OK" if not miss else "FAIL", "rivals", f"{len(ids)} entries, GW{cur} picks + transfers " +
        ("present for all" if not miss else f"MISSING for {miss}"))
except Exception as e:
    add("FAIL", "rivals", f"could not read standings: {e}")

today = now.strftime("%Y-%m-%d")
pf = os.path.join(d, f"history/progress/{today}.csv")
files = sorted(glob.glob(os.path.join(d, "history/progress/*.csv")))
if not files:
    add("FAIL", "progress", "no history/progress files at all")
else:
    newest = files[-1]
    rows = read_csv(newest)
    counts = collections.Counter(r["snapshot_utc"] for r in rows)
    stamps = sorted(counts)
    uneven = len(set(counts.values())) > 1
    n_el = len(load(d, "bootstrap-static.json")["elements"])
    last = parse_utc(stamps[-1])
    msg = f"{os.path.basename(newest)}: {len(stamps)} stamps, rows/stamp {sorted(set(counts.values()))}"
    level = "OK"
    if not os.path.isfile(pf):
        level = "WARN"; msg = f"no file for today ({today}) yet; newest " + msg
    if uneven:
        msg += " (uneven: normal only if the player pool grew that day)"
    if last == run_at and counts[stamps[-1]] != n_el:
        level = "FAIL"; msg += f"; newest stamp has {counts[stamps[-1]]} rows but bootstrap has {n_el} elements"
    elif last == run_at:
        msg += f"; newest stamp matches bootstrap ({n_el} elements)"
    add(level, "progress", msg)

try:
    pr = read_csv(os.path.join(d, "history/prices.csv"))
    lastb = max(parse_utc(r["observed_at"]) for r in pr)
    add("OK", "prices", f"{len(pr)} rows; newest batch {iso(lastb)} ({uk(lastb)})")
except Exception as e:
    add("FAIL", "prices", f"prices.csv unreadable: {e}")

der = glob.glob(os.path.join(d, "derived/*"))
if not der:
    add("WARN", "derived", "no data/derived/ files (workflow step 5c not live yet?)")
else:
    old = [os.path.basename(p) for p in der if p.endswith(".json") and
           json.load(open(p)).get("source_run_at") not in (None, fs["run_at"])]
    add("OK" if not old else "WARN", "derived", f"{len(der)} files" + (f"; behind snapshot: {old}" if old else ""))

report = {"checked_utc": iso(now), "snapshot_run_at": fs["run_at"],
          "worst": "FAIL" if any(r["level"] == "FAIL" for r in res) else "WARN" if any(r["level"] == "WARN" for r in res) else "OK",
          "results": res}
if a.out:
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1)
if a.json:
    print(json.dumps(report, indent=1))
else:
    for r in res:
        print(f"{r['level']:<5} {r['check']:<10} {r['msg']}")
sys.exit(1 if a.strict and any(r["level"] == "FAIL" for r in res) else 0)
