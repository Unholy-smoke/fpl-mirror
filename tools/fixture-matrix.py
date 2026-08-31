#!/usr/bin/env python3
"""Fixture matrix for the FPL 2026/27 project. Regenerates claude/reference/fixture-matrix.md.

Reads the mirror only - no FPL API, no auth, works from the cloud container and
from Ben's machine.

    python3 fixture-matrix.py [START_GW] [END_GW] > fixture-matrix.md

WHAT FDR IS. FPL's Fixture Difficulty Rating is a 20x2 lookup table: one value
per club at home, one away, applied identically against all 19 opponents. It
knows nothing about the specific matchup, either side's form, or injuries.
Measured across 26 mirror snapshots (13-31 Aug 2026) it did not change once, and
no team's strength_* ratings moved. It may be recalculated periodically - too
early to tell - so any change is worth noticing.

It earns its place for one reason: it is what most managers read, so it predicts
where ownership and prices move. It cannot carry an argument about whether a
fixture is genuinely easy. That is what the xG columns are for.
"""
import json, sys, urllib.request, datetime as dt
from collections import defaultdict

R = "https://raw.githubusercontent.com/Unholy-smoke/fpl-mirror/main"
get = lambda p: json.load(urllib.request.urlopen(f"{R}/{p}"))
START = int(sys.argv[1]) if len(sys.argv) > 1 else 3
END   = int(sys.argv[2]) if len(sys.argv) > 2 else 12

bs, fx  = get("data/bootstrap-static.json"), get("data/fixtures.json")
stamp   = get("data/fetch-status.json")["run_at"]
name    = {t["id"]: t["short_name"] for t in bs["teams"]}
team_of = {e["id"]: e["team"] for e in bs["elements"]}
picks   = get("data/picks-latest.json")
owned   = defaultdict(list)
byid    = {e["id"]: e for e in bs["elements"]}
for p in picks["picks"]:
    e = byid[p["element"]]
    owned[e["team"]].append(e["web_name"])

# --- underlying, completed fixtures only -------------------------------------
played = [f for f in fx if f.get("finished_provisional") and f["event"]]
gws    = sorted({f["event"] for f in played})
xgf, xga, gp = defaultdict(float), defaultdict(float), defaultdict(int)
for gw in gws:
    per = defaultdict(float)
    for el in get(f"data/live/gw{gw}.json")["elements"]:
        per[team_of[el["id"]]] += float(el["stats"].get("expected_goals", 0) or 0)
    for f in played:
        if f["event"] != gw: continue
        h, a = f["team_h"], f["team_a"]
        xgf[h] += per[h]; xga[h] += per[a]; gp[h] += 1
        xgf[a] += per[a]; xga[a] += per[h]; gp[a] += 1

# --- fixtures ----------------------------------------------------------------
d = defaultdict(dict)
for f in fx:
    if not f["event"]: continue
    d[f["team_h"]].setdefault(f["event"], []).append((name[f["team_a"]], "H", f["team_h_difficulty"]))
    d[f["team_a"]].setdefault(f["event"], []).append((name[f["team_h"]], "A", f["team_a_difficulty"]))

def mean(t, lo, hi):
    v = [x[2] for g in range(lo, hi + 1) for x in d[t].get(g, [])]
    return sum(v) / len(v) if v else 0.0

def cell(t, g):
    f = d[t].get(g)
    if not f: return "—"
    return " + ".join(f"{o} ({v}) **{x}**" if x <= 2 else f"{o} ({v}) {x}" for o, v, x in f)

rows = []
for t in name:
    best  = min(((mean(t, s, s + 3), s) for s in range(START, END - 2)), key=lambda x: x[0])
    worst = max(((mean(t, s, s + 3), s) for s in range(START, END - 2)), key=lambda x: x[0])
    rows.append(dict(club=name[t], tid=t,
                     m35=mean(t, START, START + 2), m36=mean(t, START, START + 3),
                     m69=mean(t, 6, 9), mall=mean(t, START, END),
                     best=best, worst=worst, swing=mean(t, 6, 9) - mean(t, START, START + 3),
                     xgf=xgf[t] / gp[t] if gp[t] else 0, xga=xga[t] / gp[t] if gp[t] else 0, gp=gp[t]))

print(f"# Fixture matrix — GW{START}–{END}\n")
print(f"**Generated** {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from mirror snapshot `{stamp}`.")
print(f"**Underlying** from {len(gws)} completed gameweek(s) — {gws}. Regenerate with `fixture-matrix.py`.\n")
print("> **FDR is a 20×2 lookup**: one value per club per venue, identical against every opponent. It knows nothing")
print("> about the matchup, form or injuries. It is what the market reads, so it predicts ownership and price moves —")
print("> it is not evidence that a fixture is actually easy. Weigh it against the xG columns, and note those are a")
print("> two-game sample. **ARS and AVL have played one game** (their GW2 fixture was outstanding at generation).\n")
print("## Difficulty by window\n")
print("Sorted by the GW%d–%d mean. **Swing** is GW6–9 minus GW%d–%d: negative means fixtures improve after the 22-day break, positive means they get worse. ★ = Ben owns a player.\n" % (START, START+3, START, START+3))
print("| Club | GW%d–%d | GW%d–%d | GW6–9 | Swing | Best 4 | Worst 4 | xGF/g | xGA/g | Owned |" % (START, START+2, START, START+3))
print("|---|---|---|---|---|---|---|---|---|---|")
for r in sorted(rows, key=lambda r: r["m36"]):
    star = "★ " if owned[r["tid"]] else ""
    who  = ", ".join(owned[r["tid"]]) if owned[r["tid"]] else ""
    sw   = f"**{r['swing']:+.2f}**" if abs(r["swing"]) >= 0.75 else f"{r['swing']:+.2f}"
    gpn  = "" if r["gp"] == max(x["gp"] for x in rows) else f" *({r['gp']}g)*"
    print(f"| {star}{r['club']} | {r['m35']:.2f} | {r['m36']:.2f} | {r['m69']:.2f} | {sw} | "
          f"{r['best'][0]:.2f} @GW{r['best'][1]} | {r['worst'][0]:.2f} @GW{r['worst'][1]} | "
          f"{r['xgf']:.2f}{gpn} | {r['xga']:.2f} | {who} |")
print("\n## The grid\n")
print("Opponent (venue) difficulty. **Bold** = difficulty 2 or lower.\n")
print("| Club | " + " | ".join(f"GW{g}" for g in range(START, END + 1)) + " |")
print("|---" * (END - START + 2) + "|")
for r in sorted(rows, key=lambda r: r["m36"]):
    star = "★ " if owned[r["tid"]] else ""
    print(f"| {star}{r['club']} | " + " | ".join(cell(r["tid"], g) for g in range(START, END + 1)) + " |")
blanks  = {name[t]: [g for g in range(START, END+1) if g not in d[t]] for t in name}
blanks  = {k: v for k, v in blanks.items() if v}
doubles = {name[t]: [g for g in range(START, END+1) if len(d[t].get(g, [])) > 1] for t in name}
doubles = {k: v for k, v in doubles.items() if v}
print(f"\n**Blanks:** {blanks or 'none in this range'}  ·  **Doubles:** {doubles or 'none in this range'}")
