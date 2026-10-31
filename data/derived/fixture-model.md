# Fixture model v0.2 — GW10–17

**Generated** 2026-10-31 17:41 UTC from mirror `2026-10-31T17:40:35Z`.
**Observed** 9 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9]. With k=6 pseudo-matches, ratings are **40% prior / 60% data** for the 12 clubs on 9 matches, and **43% / 57%** for the 8 on 8. That weight shifts toward data every week.

League mean xG per team-match **1.44**; home 1.60 / away 1.28 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, AVL, CRY, EVE, FUL, LIV, NEW, TOT on 8.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW10–13, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW9 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG10–13 | CS10–13 | xG10–17 | CS10–17 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.29 *(1.35)* | 0.97 | **8.00** | 1.11 | 15.69 | 2.16 | +6.4 | Groß, De Cuyper |
| ★ ARS | 1.22 *(1.21)* | 0.61 | **7.57** | 1.70 | 14.79 | 3.38 | -0.9 | Raya, Calafiori |
| LIV | 1.09 *(1.06)* | 0.84 | **6.89** | 1.19 | 13.10 | 2.59 | -1.2 |  |
| ★ MCI | 1.31 *(1.45)* | 0.89 | **6.49** | 1.07 | 14.71 | 2.32 | +1.1 | Haaland |
| MUN | 1.07 *(1.10)* | 1.08 | **6.40** | 0.91 | 12.25 | 1.79 | -4.3 |  |
| ★ BOU | 1.08 *(1.22)* | 0.87 | **6.26** | 1.08 | 12.31 | 2.48 | -1.8 | Evanilson |
| ★ NFO | 1.11 *(1.15)* | 0.86 | **6.20** | 1.14 | 12.85 | 2.19 | -8.9 | Gibbs-White |
| ★ CHE | 1.05 *(1.01)* | 0.95 | **6.18** | 1.00 | 11.97 | 2.08 | +5.9 | Rogers |
| SUN | 1.07 *(1.01)* | 1.07 | **5.85** | 0.94 | 12.52 | 1.85 | -6.1 |  |
| CRY | 0.98 *(0.95)* | 1.21 | **5.67** | 0.88 | 10.97 | 1.53 | -2.0 |  |
| ★ BRE | 1.05 *(1.10)* | 1.03 | **5.55** | 0.78 | 12.12 | 1.71 | +1.7 | Schade |
| ★ AVL | 0.86 *(0.79)* | 1.03 | **5.46** | 0.93 | 10.66 | 1.98 | -0.1 | N.Jackson |
| FUL | 0.92 *(1.00)* | 1.00 | **5.28** | 0.97 | 10.56 | 1.89 | -3.6 |  |
| EVE | 0.92 *(0.86)* | 1.03 | **5.24** | 1.04 | 10.44 | 1.86 | -1.9 |  |
| IPS | 0.91 *(0.94)* | 1.22 | **5.15** | 0.89 | 10.65 | 1.59 | +1.8 |  |
| ★ LEE | 0.92 *(0.88)* | 0.92 | **5.14** | 1.17 | 10.59 | 2.34 | -2.4 | Muharemović |
| TOT | 0.82 *(0.71)* | 0.95 | **4.99** | 1.10 | 9.03 | 2.11 | -0.2 |  |
| COV | 0.72 *(0.65)* | 1.07 | **4.61** | 0.96 | 8.71 | 1.81 | +0.6 |  |
| ★ NEW | 0.87 *(0.79)* | 1.22 | **4.56** | 0.58 | 9.81 | 1.19 | +2.9 | Hall, Barnes |
| ★ HUL | 0.73 *(0.70)* | 1.16 | **3.85** | 0.60 | 7.58 | 1.32 | +1.9 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | BRE(H) 2.1/27% (3) | HUL(A) 1.9/32% (2) | NEW(H) 2.5/34% (3) | BOU(A) 1.4/18% (3) | NFO(A) 1.4/18% (3) | EVE(H) 2.1/32% (3) | IPS(H) 2.5/32% (2) | FUL(A) 1.6/24% (3) |
| ★ ARS | HUL(H) 2.3/56% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/36% (4) | BRE(A) 1.6/35% (3) | TOT(A) 1.5/45% (3) | BOU(H) 1.7/43% (3) | MUN(H) 2.1/43% (4) | CRY(A) 1.9/38% (3) |
| LIV | CRY(A) 1.7/27% (3) | MUN(H) 1.9/31% (4) | EVE(A) 1.4/29% (3) | SUN(H) 1.9/31% (3) | CHE(A) 1.3/24% (4) | LEE(H) 1.6/37% (3) | TOT(H) 1.7/41% (2) | HUL(A) 1.6/38% (2) |
| ★ MCI | NFO(A) 1.4/20% (3) | FUL(H) 2.1/35% (2) | ARS(A) 1.0/17% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.7/22% (3) | CHE(H) 2.0/30% (4) | HUL(H) 2.4/43% (2) | NEW(A) 2.0/29% (3) |
| MUN | AVL(H) 1.8/30% (3) | LIV(A) 1.2/15% (4) | BRE(H) 1.8/23% (3) | NEW(A) 1.7/22% (3) | COV(H) 1.8/37% (2) | CRY(A) 1.7/18% (3) | ARS(A) 0.8/12% (5) | NFO(H) 1.5/21% (3) |
| ★ BOU | IPS(A) 1.7/28% (2) | NFO(H) 1.5/29% (3) | FUL(A) 1.4/28% (3) | BHA(H) 1.7/24% (3) | HUL(H) 2.0/44% (2) | ARS(A) 0.9/18% (5) | COV(H) 1.9/45% (2) | TOT(A) 1.3/32% (3) |
| ★ NFO | MCI(H) 1.6/24% (4) | BOU(A) 1.2/22% (3) | CHE(H) 1.7/31% (4) | HUL(A) 1.7/37% (2) | BHA(H) 1.7/24% (3) | SUN(A) 1.5/23% (3) | EVE(H) 1.8/36% (3) | MUN(A) 1.5/23% (4) |
| ★ CHE | SUN(A) 1.4/19% (3) | LEE(H) 1.5/33% (3) | NFO(A) 1.2/18% (3) | CRY(H) 2.0/30% (2) | LIV(H) 1.4/26% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.7/35% (3) | COV(A) 1.4/33% (2) |
| SUN | CHE(H) 1.6/24% (4) | AVL(A) 1.4/23% (3) | TOT(H) 1.6/32% (2) | LIV(A) 1.2/15% (4) | NEW(A) 1.7/22% (3) | NFO(H) 1.5/22% (3) | CRY(H) 2.1/26% (2) | EVE(A) 1.4/21% (3) |
| CRY | LIV(H) 1.3/18% (4) | COV(A) 1.3/25% (2) | HUL(H) 1.8/32% (2) | CHE(A) 1.2/13% (4) | AVL(A) 1.3/19% (3) | MUN(H) 1.7/19% (4) | SUN(A) 1.3/12% (3) | ARS(H) 1.0/15% (4) |
| ★ BRE | BHA(A) 1.3/12% (4) | EVE(H) 1.7/30% (3) | MUN(A) 1.5/17% (4) | ARS(H) 1.0/20% (4) | MCI(H) 1.5/18% (4) | FUL(A) 1.3/22% (3) | NEW(H) 2.1/32% (3) | IPS(A) 1.6/22% (2) |
| ★ AVL | MUN(A) 1.2/17% (4) | SUN(H) 1.5/24% (3) | IPS(A) 1.3/22% (2) | EVE(H) 1.4/30% (3) | CRY(H) 1.7/27% (2) | COV(A) 1.2/30% (2) | CHE(A) 1.1/18% (4) | LEE(H) 1.3/30% (3) |
| FUL | NEW(H) 1.8/33% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.3/25% (3) | TOT(A) 1.1/27% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.5/26% (3) | LEE(A) 1.1/23% (3) | BHA(H) 1.4/19% (3) |
| EVE | COV(H) 1.6/39% (2) | BRE(A) 1.2/18% (3) | LIV(H) 1.2/24% (4) | AVL(A) 1.2/24% (3) | FUL(H) 1.5/30% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.0/16% (3) | SUN(H) 1.6/24% (3) |
| IPS | BOU(H) 1.3/18% (3) | TOT(A) 1.1/20% (3) | AVL(H) 1.5/26% (3) | COV(A) 1.3/24% (2) | LEE(A) 1.1/17% (3) | NEW(H) 1.8/26% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.5/19% (3) |
| ★ LEE | TOT(H) 1.4/38% (2) | CHE(A) 1.1/21% (4) | COV(H) 1.6/43% (2) | MCI(A) 1.0/15% (5) | IPS(H) 1.8/34% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.5/34% (2) | AVL(A) 1.2/28% (3) |
| TOT | LEE(A) 1.0/25% (3) | IPS(H) 1.6/33% (2) | SUN(A) 1.1/20% (3) | FUL(H) 1.3/32% (2) | ARS(H) 0.8/22% (4) | HUL(A) 1.2/33% (2) | LIV(A) 0.9/19% (4) | BOU(H) 1.1/27% (3) |
| COV | EVE(A) 1.0/21% (3) | CRY(H) 1.4/26% (2) | LEE(A) 0.8/21% (3) | IPS(H) 1.4/29% (2) | MUN(A) 1.0/16% (4) | AVL(H) 1.2/30% (3) | BOU(A) 0.8/16% (3) | CHE(H) 1.1/24% (4) |
| ★ NEW | FUL(A) 1.1/16% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.5/19% (4) | SUN(H) 1.5/19% (3) | IPS(A) 1.4/17% (2) | BRE(A) 1.2/13% (3) | MCI(H) 1.2/13% (4) |
| ★ HUL | ARS(A) 0.6/10% (5) | BHA(H) 1.1/15% (3) | CRY(A) 1.1/16% (3) | NFO(H) 1.0/19% (3) | BOU(A) 0.8/13% (3) | TOT(H) 1.1/30% (2) | MCI(A) 0.8/9% (5) | LIV(H) 1.0/20% (4) |
