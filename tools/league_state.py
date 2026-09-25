#!/usr/bin/env python3
"""League state for every Shabanga manager, as at the last deadline.

For all nine entries: rank, points, bank, free transfers into the next gameweek,
chips played and still held in the current window, and the squad with purchase
price, current price and SELLING price for every player.

  python3 tools/league_state.py                                  # print the table
  python3 tools/league_state.py --out data/derived/league-state.json

AS-OF DATE: everything here is as at the deadline of `as_of_gw` (current_event).
Transfers and chips made since then are invisible to the API until the next
deadline passes. That includes Ben's: his live squad is claude/state/squad.json in
the project, read from the FPL site. This file can't see pending moves.

Rules applied (the official 2026/27 ruleset, kept in the project's fpl-rules doc):
  * Free transfers: none accrues for GW1; 1 available for GW2; +1 per gameweek
    after that, capped at 5; transfers made are subtracted (never below 0);
    a Wildcard or Free Hit gameweek uses none, and the saved count carries over (+1).
  * Purchase price: the most recent `element_in_cost` for that player in the
    entry's transfer log; for a player held since before GW1, the start price
    (`now_cost - cost_change_start`).
  * Selling price: purchase + floor(rise / 2); a fall below purchase is taken in full.
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fplcommon import data_dir, load, m, selling_price, write_json, POS

ap = argparse.ArgumentParser()
ap.add_argument("--data")
ap.add_argument("--out")
ap.add_argument("--stamp", help="snapshot run stamp to record (default: fetch-status run_at)")
a = ap.parse_args()

d = data_dir(a.data)
bs = load(d, "bootstrap-static.json")
ev = load(d, "events.json")
cur = ev["current_event"]
nxt = ev["next_event"]
el = {e["id"]: e for e in bs["elements"]}
team = {t["id"]: t["short_name"] for t in bs["teams"]}
standings = load(d, "league-standings.json")
try:
    import json as _j
    BEN = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(d)), "config.json")))["entry_id"]
except Exception:
    BEN = None
chip_windows = [(c["name"], c["start_event"], c["stop_event"]) for c in bs.get("chips", [])]
target_gw = nxt or cur


def free_transfers(history, chips):
    chip_gw = {c["event"] for c in chips if c["name"] in ("wildcard", "freehit")}
    ft = None
    for h in sorted(history, key=lambda r: r["event"]):
        gw = h["event"]
        if gw == 1:
            ft = 1                      # none accrues for GW1; one available for GW2
            continue
        if ft is None:                  # entry joined after GW1
            ft = 1
        if gw in chip_gw:
            ft = min(5, ft + 1)
        else:
            ft = min(5, max(0, ft - h["event_transfers"]) + 1)
    return ft


out = {"schema": "league-state/1", "as_of_gw": cur, "ft_for_gw": target_gw,
       "source_run_at": a.stamp or load(d, "fetch-status.json").get("run_at"),
       "league": standings.get("league", {}).get("name"), "entries": []}

for s in standings["standings"]["results"]:
    eid = s["entry"]
    try:
        hist = load(d, f"rivals/history-entry{eid}.json")
        picks = load(d, f"rivals/gw{cur}-entry{eid}.json")
        transfers = load(d, f"transfers/entry{eid}.json")
    except FileNotFoundError as e:
        out["entries"].append({"entry": eid, "manager": s["player_name"], "error": f"missing {e.filename}"})
        continue
    bought = {}
    for t in sorted(transfers, key=lambda t: t["time"]):
        bought[t["element_in"]] = t["element_in_cost"]
    squad = []
    for p in picks["picks"]:
        e = el.get(p["element"])
        if not e:
            squad.append({"element_id": p["element"], "error": "not in bootstrap"}); continue
        start = e["now_cost"] - e["cost_change_start"]
        pur = bought.get(p["element"], start)
        squad.append({"element_id": e["id"], "web_name": e["web_name"], "team": team[e["team"]],
                      "pos": POS[e["element_type"]], "slot": p["position"], "captain": p["is_captain"],
                      "vice": p["is_vice_captain"], "purchase": m(pur), "now": m(e["now_cost"]),
                      "selling": m(selling_price(pur, e["now_cost"])),
                      "purchase_source": "transfer log" if p["element"] in bought else "start price",
                      "status": e["status"]})
    played = [{"name": c["name"], "gw": c["event"]} for c in hist.get("chips", [])]
    held = [n for n, lo, hi in chip_windows if lo <= target_gw <= hi
            and not any(c["name"] == n and lo <= c["event"] <= hi for c in hist.get("chips", []))]
    last = max(hist["current"], key=lambda r: r["event"]) if hist["current"] else {}
    out["entries"].append({
        "entry": eid, "is_ben": eid == BEN, "manager": s["player_name"], "team_name": s["entry_name"], "rank": s["rank"],
        "total": s["total"], "gw_points": s["event_total"], "bank": m(last.get("bank")),
        "free_transfers": free_transfers(hist["current"], hist.get("chips", [])),
        "transfers_total": sum(r["event_transfers"] for r in hist["current"]),
        "hits_total": sum(r["event_transfers_cost"] for r in hist["current"]),
        "active_chip_gw": picks.get("active_chip"), "chips_played": played,
        "chips_held_now": held, "selling_value": round(sum(x.get("selling") or 0 for x in squad), 1),
        "squad": squad})

if a.out:
    write_json(a.out, out)

print(f"League state as at GW{cur} deadline; free transfers are for GW{target_gw}. "
      f"Pending moves since GW{cur}'s deadline are invisible here.")
print(f"{'#':>2} {'manager':<22}{'total':>6}{'bank':>6}{'FT':>4}{'sell':>7}  chips held")
for x in out["entries"]:
    if "error" in x:
        print(f"   {x['manager']:<22} ERROR {x['error']}"); continue
    print(f"{x['rank']:>2} {(x['manager'] + (' (Ben)' if x['is_ben'] else '')):<22}{x['total']:>6}{x['bank']:>6}{x['free_transfers']:>4}"
          f"{x['selling_value']:>7}  {', '.join(x['chips_held_now']) or '-'}")
