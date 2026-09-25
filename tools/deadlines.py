#!/usr/bin/env python3
"""Deadline table, drift log and the 90-minute invariant.

Replaces the project's hand-kept deadlines.json and deadline-drift-log.md. The Action
runs it every snapshot, so drift is recorded at the fetch that saw it, in git.

  python3 tools/deadlines.py                       # print next deadline + any problems
  python3 tools/deadlines.py --out data/derived/deadlines.csv \
        --prev /tmp/prev-bootstrap.json --log data/derived/deadline-changes.csv

Outputs
  deadlines.csv         one row per gameweek: deadline UTC and UK local, first
                        kick-off, first fixture, and whether deadline == first KO - 90m
  deadline-changes.csv  append-only: a row whenever a deadline differs from the
                        previous snapshot's (only with --prev)

Exit code 0 always, so it can never fail the snapshot. Problems are printed.
"""
import argparse, csv, datetime as dt, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fplcommon import data_dir, load, parse_utc, iso, uk, write_csv

ap = argparse.ArgumentParser()
ap.add_argument("--data")
ap.add_argument("--out")
ap.add_argument("--prev", help="previous bootstrap-static.json to diff deadlines against")
ap.add_argument("--log", help="append-only CSV of deadline changes")
ap.add_argument("--stamp", help="run stamp to write in the change log (default: now)")
a = ap.parse_args()

d = data_dir(a.data)
bs = load(d, "bootstrap-static.json")
fx = load(d, "fixtures.json")
team = {t["id"]: t["short_name"] for t in bs["teams"]}

first = {}
for f in fx:
    ko = parse_utc(f.get("kickoff_time"))
    if f.get("event") and ko and (f["event"] not in first or ko < first[f["event"]][0]):
        first[f["event"]] = (ko, f"{team[f['team_h']]} v {team[f['team_a']]}")

rows, problems = [], []
for e in bs["events"]:
    dl = parse_utc(e["deadline_time"])
    ko, fixture = first.get(e["id"], (None, ""))
    gap = int((ko - dl).total_seconds() // 60) if ko else None
    ok = gap == 90
    if ko and not ok:
        problems.append(f"GW{e['id']}: deadline {uk(dl)} is {gap} min before first kick-off {uk(ko)} (expected 90)")
    rows.append([e["id"], iso(dl), uk(dl), iso(ko), uk(ko), fixture, gap if gap is not None else "", "yes" if ok else "no",
                 str(e.get("finished")).lower(), str(e.get("is_current")).lower(), str(e.get("is_next")).lower()])

if a.out:
    write_csv(a.out, ["gw", "deadline_utc", "deadline_uk", "first_kickoff_utc", "first_kickoff_uk", "first_fixture",
                      "ko_minus_deadline_min", "invariant_90_ok", "finished", "is_current", "is_next"], rows)

changes = []
if a.prev and os.path.isfile(a.prev):
    import json
    with open(a.prev, encoding="utf-8") as f:
        prev = {e["id"]: e["deadline_time"] for e in json.load(f).get("events", [])}
    stamp = a.stamp or iso(dt.datetime.now(dt.timezone.utc))
    for e in bs["events"]:
        old = prev.get(e["id"])
        if old and old != e["deadline_time"]:
            o, n = parse_utc(old), parse_utc(e["deadline_time"])
            changes.append([stamp, e["id"], iso(o), uk(o), iso(n), uk(n), first.get(e["id"], (None, ""))[1]])
    if a.log and changes:
        new = not os.path.isfile(a.log)
        os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
        with open(a.log, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["observed_utc", "gw", "old_deadline_utc", "old_deadline_uk", "new_deadline_utc",
                            "new_deadline_uk", "first_fixture_now"])
            w.writerows(changes)

nxt = next((e for e in bs["events"] if e.get("is_next")), None)
if nxt:
    t = parse_utc(nxt["deadline_time"])
    hrs = (t - dt.datetime.now(dt.timezone.utc)).total_seconds() / 3600
    print(f"Next deadline: GW{nxt['id']} {uk(t)} ({iso(t)}), {hrs:.1f}h from now; first fixture {first.get(nxt['id'], (None, '?'))[1]}")
for c in changes:
    print(f"DEADLINE MOVED: GW{c[1]} {c[3]} -> {c[5]}")
for p in problems:
    print(f"INVARIANT: {p}")
if not changes and not problems:
    print("No deadline changes; 90-minute invariant holds for every gameweek with fixtures.")
