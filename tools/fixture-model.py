#!/usr/bin/env python3
"""Fixture model v0.2 for the FPL 2026/27 project.

A deliberately small step up from FPL's FDR. Three changes, no more:

  1. PAIRWISE. Every club gets an attack rating and a defence rating. A fixture's
     expected goals depends on both sides, so Hull at Arsenal and City at Arsenal
     are different fixtures. FDR cannot express that.
  2. RATIO SCALE, SO IT ADDS UP. Output is expected goals and expected clean
     sheets. You sum those across a run of fixtures. You cannot meaningfully
     average an ordinal 1-5 rating, which is what a "mean FDR" column does.
  3. OPPONENT-ADJUSTED. A raw per-game average rates United's attack as elite for
     putting five past Ipswich, and cannot tell that apart from Brentford scoring
     three at Spurs. Each match is divided by what an average side would have been
     expected to produce against that opponent at that venue, then the ratings are
     re-estimated until they settle.
  4. SHRUNK TO A PRIOR. With a handful of matches played, raw per-game rates are
     noise. Each rating is a weighted blend of what we have observed and an
     FDR-derived prior, with the weight on observation growing as matches
     accumulate. Early season the answer is mostly prior, and it says so.

  ATTACK and DEFENCE difficulty are reported separately, because they are
  different questions: a forward cares about the opponent's defence, a defender
  cares about the opponent's attack.

NOT modelled yet, on purpose: player minutes, penalties, finishing over- and
under-performance, defensive contribution, Dixon-Coles low-score correction,
time decay, team-specific home advantage. Those come once there is data to
support them. Finishing (goals minus xG) is reported alongside as an eyeball
column so we can watch whether it is worth adding.

TUNABLES below are assumptions, not measurements. Refit them around GW10.
"""
import json, sys, urllib.request, math, datetime as dt
from collections import defaultdict

R = "https://raw.githubusercontent.com/Unholy-smoke/fpl-mirror/main"
g = lambda p: json.load(urllib.request.urlopen(f"{R}/{p}"))
NEXT  = g("data/events.json")["next_event"] or 1
START = int(sys.argv[1]) if len(sys.argv) > 1 else NEXT
END   = int(sys.argv[2]) if len(sys.argv) > 2 else START + 7

# --- TUNABLES ----------------------------------------------------------------
K_PSEUDO   = 6.0    # pseudo-matches of prior. Higher = trust the prior longer.
HOME_ADV   = 1.25   # league-wide home xG multiplier. Observed early-season is
                    # noisier and higher; 1.25 is a blend with the historical norm.
# FDR tier of a club -> how they play, relative to league average.
DEF_PRIOR  = {2: 1.15, 3: 1.02, 4: 0.88, 5: 0.75}   # xG they CONCEDE
ATT_PRIOR  = {2: 0.85, 3: 0.98, 4: 1.12, 5: 1.25}   # xG they CREATE
# -----------------------------------------------------------------------------

bs, fx = g("data/bootstrap-static.json"), g("data/fixtures.json")
stamp  = g("data/fetch-status.json")["run_at"]
name   = {t["id"]: t["short_name"] for t in bs["teams"]}
team_of= {e["id"]: e["team"] for e in bs["elements"]}
byid   = {e["id"]: e for e in bs["elements"]}
owned  = defaultdict(list)
for p in g("data/picks-latest.json")["picks"]:
    owned[byid[p["element"]]["team"]].append(byid[p["element"]]["web_name"])

# tier: the difficulty an opponent faces when visiting this club
tier = {}
for f in fx:
    tier.setdefault(f["team_h"], f["team_a_difficulty"])

# --- observed ----------------------------------------------------------------
played = [f for f in fx if f.get("finished_provisional") and f["event"]]
gws    = sorted({f["event"] for f in played})
xgf, xga, gf, ga = (defaultdict(float) for _ in range(4))
n = defaultdict(int)
for gw in gws:
    per = defaultdict(float)
    for el in g(f"data/live/gw{gw}.json")["elements"]:
        per[team_of[el["id"]]] += float(el["stats"].get("expected_goals", 0) or 0)
    for f in played:
        if f["event"] != gw: continue
        h, a = f["team_h"], f["team_a"]
        for t, o, sf, sa in ((h, a, f["team_h_score"], f["team_a_score"]),
                             (a, h, f["team_a_score"], f["team_h_score"])):
            xgf[t] += per[t]; xga[t] += per[o]; gf[t] += sf; ga[t] += sa; n[t] += 1

M = sum(xgf.values()) / sum(n.values())            # league mean xG per team-match
LH = 2 * M * HOME_ADV / (1 + HOME_ADV)
LA = 2 * M / (1 + HOME_ADV)

# Per-team-match records, needed for the opponent adjustment below.
matches = []   # (team, opp, is_home, xg_for, xg_against)
for gw in gws:
    per = defaultdict(float)
    for el in g(f"data/live/gw{gw}.json")["elements"]:
        per[team_of[el["id"]]] += float(el["stats"].get("expected_goals", 0) or 0)
    for f in played:
        if f["event"] != gw: continue
        h, a = f["team_h"], f["team_a"]
        matches.append((h, a, True,  per[h], per[a]))
        matches.append((a, h, False, per[a], per[h]))

# OPPONENT-ADJUSTED ratings.
#
# A raw per-game xG average says United's attack is elite because they put 5 past
# Ipswich. It cannot tell that apart from Brentford scoring three at Spurs, which
# is the harder thing to do. So each match is divided by what an average side
# would have been expected to produce against THAT opponent at THAT venue, and
# the ratings are re-estimated a few times until they stop moving. This is a
# crude stand-in for fitting attack and defence simultaneously, which is what a
# Poisson/Dixon-Coles model does properly.
w = {t: n[t] / (n[t] + K_PSEUDO) for t in name}
att = {t: ATT_PRIOR[tier[t]] for t in name}
dfn = {t: DEF_PRIOR[tier[t]] for t in name}
raw_att = {t: (xgf[t] / n[t]) / M if n[t] else 1.0 for t in name}

for _ in range(25):
    na, nd = {}, {}
    for t in name:
        af, dfv, c = 0.0, 0.0, 0
        for tt, opp, home, xf, xa in matches:
            if tt != t: continue
            base_f = LH if home else LA          # what we'd expect t to create
            base_a = LA if home else LH          # what we'd expect opp to create
            af  += xf / (base_f * dfn[opp])
            dfv += xa / (base_a * att[opp])
            c   += 1
        obs_a = af / c if c else 1.0
        obs_d = dfv / c if c else 1.0
        na[t] = w[t] * obs_a + (1 - w[t]) * ATT_PRIOR[tier[t]]
        nd[t] = w[t] * obs_d + (1 - w[t]) * DEF_PRIOR[tier[t]]
    ma = sum(na.values()) / len(na); md = sum(nd.values()) / len(nd)
    na = {t: v / ma for t, v in na.items()}     # keep the league centred on 1.00
    nd = {t: v / md for t, v in nd.items()}
    if max(abs(na[t] - att[t]) for t in name) < 1e-6: att, dfn = na, nd; break
    att, dfn = na, nd

def lam(i, j, home):
    base_f, base_a = (LH, LA) if home else (LA, LH)
    return base_f * att[i] * dfn[j], base_a * att[j] * dfn[i]

fixt = defaultdict(list)
for f in fx:
    if not f["event"] or not (START <= f["event"] <= END): continue
    fixt[f["team_h"]].append((f["event"], f["team_a"], True,  f["team_h_difficulty"]))
    fixt[f["team_a"]].append((f["event"], f["team_h"], False, f["team_a_difficulty"]))

def window(t, lo, hi):
    xg = cs = 0.0
    for ev, opp, home, _ in fixt[t]:
        if lo <= ev <= hi:
            lf, la = lam(t, opp, home)
            xg += lf; cs += math.exp(-la)
    return xg, cs

print(f"# Fixture model v0.2 — GW{START}–{END}\n")
print(f"**Generated** {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} from mirror `{stamp}`.")
wmin, wmax = min(w.values()), max(w.values())
print(f"**Observed** {len(gws)} gameweek(s) — {gws}. With k={K_PSEUDO:.0f} pseudo-matches, ratings are "
      f"**{(1-wmax)*100:.0f}% prior / {wmax*100:.0f}% data** for the {sum(1 for t in name if n[t]==max(n.values()))} clubs on "
      f"{max(n.values())} matches, and **{(1-wmin)*100:.0f}% / {wmin*100:.0f}%** for the "
      f"{sum(1 for t in name if n[t]==min(n.values()))} on {min(n.values())}. That weight shifts toward data every week.\n")
print(f"League mean xG per team-match **{M:.2f}**; home {LH:.2f} / away {LA:.2f} at an assumed home advantage of ×{HOME_ADV}.\n")
print("> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be\n"
      "> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon\n"
      "> becoming a permanent verdict. ARS and AVL have played one match.\n")
SHORT = min(START + 3, END)
WIDE  = END > START + 3          # suppress the long window when it duplicates the short one
print(f"## Next {END-START+1} gameweeks\n")
print(f"**xG / CS** = expected goals created and expected clean sheets over GW{START}\u2013{SHORT}, "
      "**summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure "
      "beside it \u2014 the gap between them is how flattering the fixtures have been. **Def** is the xG a club "
      "concedes relative to average, so *lower is better*. Both are centred on 1.00. **G\u2212xG** is finishing "
      "over/underperformance so far \u2014 not in the model, shown to see whether it is worth adding. "
      "\u2605 = Ben owns a player.\n")
hdr = f"| Club | Att *(raw)* | Def | xG{START}\u2013{SHORT} | CS{START}\u2013{SHORT}"
if WIDE: hdr += f" | xG{START}\u2013{END} | CS{START}\u2013{END}"
hdr += " | G\u2212xG | Owned |"
print(hdr)
print("|---" * (9 if WIDE else 7) + "|")
rows = []
for t in name:
    a4, c4 = window(t, START, SHORT)
    aa, ca = window(t, START, END)
    rows.append((name[t], t, att[t], dfn[t], a4, c4, aa, ca, gf[t] - xgf[t], raw_att[t]))
for nm, t, a, d, a4, c4, aa, ca, diff, ra in sorted(rows, key=lambda r: -r[4]):
    star = "\u2605 " if owned[t] else ""
    wide = f" | {aa:.2f} | {ca:.2f}" if WIDE else ""
    print(f"| {star}{nm} | {a:.2f} *({ra:.2f})* | {d:.2f} | **{a4:.2f}** | {c4:.2f}{wide} | {diff:+.1f} | {', '.join(owned[t])} |")

print(f"\n## The same fixtures, priced\n")
print("Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. "
      "FDR in brackets for comparison — note where they disagree.\n")
print("| Club | " + " | ".join(f"GW{x}" for x in range(START, END + 1)) + " |")
print("|---" * (END - START + 2) + "|")
for nm, t, *_ in sorted(rows, key=lambda r: -r[4]):
    cells = []
    for ev in range(START, END + 1):
        m = [x for x in fixt[t] if x[0] == ev]
        if not m: cells.append("—"); continue
        _, opp, home, d = m[0]
        lf, la = lam(t, opp, home)
        cells.append(f"{name[opp]}{'(H)' if home else '(A)'} {lf:.1f}/{math.exp(-la)*100:.0f}% ({d})")
    print(f"| {'★ ' if owned[t] else ''}{nm} | " + " | ".join(cells) + " |")
