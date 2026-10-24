# Fixture model v0.2 — GW9–16

**Generated** 2026-10-24 05:48 UTC from mirror `2026-10-24T05:47:47Z`.
**Observed** 8 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8]. With k=6 pseudo-matches, ratings are **43% prior / 57% data** for the 2 clubs on 8 matches, and **46% / 54%** for the 18 on 7. That weight shifts toward data every week.

League mean xG per team-match **1.51**; home 1.67 / away 1.34 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, AVL, BOU, BRE, BHA, CHE, COV, CRY, EVE, FUL, HUL, LEE, LIV, MCI, MUN, NEW, TOT, SUN on 7.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW9–12, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW8 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG9–12 | CS9–12 | xG9–16 | CS9–16 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.45)* | 0.97 | **8.30** | 1.01 | 16.18 | 1.98 | +7.7 | Groß, De Cuyper |
| ★ ARS | 1.19 *(1.14)* | 0.61 | **7.32** | 1.65 | 14.20 | 3.27 | -1.0 | Raya, Calafiori |
| ★ MCI | 1.29 *(1.46)* | 0.92 | **6.86** | 0.85 | 15.18 | 2.03 | +3.6 | Haaland |
| SUN | 1.07 *(1.01)* | 1.13 | **6.46** | 0.92 | 13.08 | 1.67 | -4.6 |  |
| ★ NFO | 1.12 *(1.17)* | 0.88 | **6.38** | 0.93 | 13.48 | 2.03 | -8.1 | Gibbs-White |
| BOU | 1.03 *(1.18)* | 0.89 | **6.29** | 1.09 | 12.65 | 2.30 | -3.4 |  |
| MUN | 1.07 *(1.14)* | 0.97 | **6.20** | 0.92 | 12.46 | 1.89 | -2.0 |  |
| ★ CHE | 1.04 *(0.95)* | 0.96 | **6.17** | 0.89 | 12.78 | 1.88 | +7.0 | Rogers, João Pedro |
| ★ BRE | 1.06 *(1.15)* | 1.02 | **6.14** | 0.78 | 12.45 | 1.66 | +0.8 | Schade |
| LIV | 1.08 *(1.04)* | 0.83 | **6.09** | 1.13 | 13.01 | 2.42 | -2.0 |  |
| CRY | 0.96 *(0.89)* | 1.20 | **5.80** | 0.89 | 11.35 | 1.47 | -0.4 |  |
| ★ FUL | 0.95 *(1.05)* | 1.02 | **5.78** | 0.88 | 11.12 | 1.77 | -4.0 | Gonzalo |
| AVL | 0.88 *(0.80)* | 1.02 | **5.77** | 0.88 | 11.46 | 1.89 | -1.5 |  |
| TOT | 0.83 *(0.71)* | 0.97 | **5.67** | 0.98 | 10.10 | 1.95 | -1.5 |  |
| ★ LEE | 0.96 *(0.95)* | 0.95 | **5.67** | 1.12 | 11.52 | 2.04 | -1.0 | Muharemović |
| EVE | 0.91 *(0.88)* | 1.01 | **5.59** | 0.98 | 10.61 | 1.75 | -1.2 |  |
| IPS | 0.91 *(0.93)* | 1.23 | **5.47** | 0.82 | 10.94 | 1.47 | +0.8 |  |
| COV | 0.76 *(0.68)* | 1.09 | **4.94** | 0.83 | 9.69 | 1.67 | -1.2 |  |
| ★ NEW | 0.87 *(0.77)* | 1.20 | **4.66** | 0.61 | 10.33 | 1.25 | +1.8 | Hall, Barnes |
| ★ HUL | 0.73 *(0.65)* | 1.14 | **4.47** | 0.66 | 8.53 | 1.35 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | MCI(A) 1.6/12% (5) | BRE(H) 2.2/25% (3) | HUL(A) 2.0/31% (2) | NEW(H) 2.6/33% (3) | BOU(A) 1.5/19% (3) | NFO(A) 1.5/16% (3) | EVE(H) 2.2/31% (3) | IPS(H) 2.6/31% (2) |
| ★ ARS | LIV(A) 1.3/33% (4) | HUL(H) 2.3/55% (2) | NEW(A) 1.9/41% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/34% (3) | TOT(A) 1.6/43% (3) | BOU(H) 1.8/43% (3) | MUN(H) 1.9/42% (4) |
| ★ MCI | BHA(H) 2.1/20% (3) | NFO(A) 1.5/18% (3) | FUL(H) 2.2/31% (2) | ARS(A) 1.0/16% (5) | LEE(H) 2.0/31% (3) | BRE(A) 1.8/19% (3) | CHE(H) 2.1/27% (4) | HUL(H) 2.5/40% (2) |
| SUN | COV(A) 1.6/24% (2) | CHE(H) 1.7/21% (4) | AVL(A) 1.5/19% (3) | TOT(H) 1.7/29% (2) | LIV(A) 1.2/13% (4) | NEW(A) 1.7/19% (3) | NFO(H) 1.6/19% (3) | CRY(H) 2.2/24% (2) |
| ★ NFO | BRE(A) 1.5/21% (3) | MCI(H) 1.7/22% (4) | BOU(A) 1.3/22% (3) | CHE(H) 1.8/29% (4) | HUL(A) 1.7/34% (2) | BHA(H) 1.8/22% (3) | SUN(A) 1.7/21% (3) | EVE(H) 1.9/34% (3) |
| BOU | LEE(H) 1.6/32% (3) | IPS(A) 1.7/26% (2) | NFO(H) 1.5/26% (3) | FUL(A) 1.4/24% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.0/42% (2) | ARS(A) 0.8/17% (5) | COV(H) 1.9/41% (2) |
| MUN | CHE(A) 1.4/18% (4) | AVL(H) 1.8/32% (3) | LIV(A) 1.2/17% (4) | BRE(H) 1.8/25% (3) | NEW(A) 1.7/24% (3) | COV(H) 1.9/37% (2) | CRY(A) 1.7/21% (3) | ARS(A) 0.9/14% (5) |
| ★ CHE | MUN(H) 1.7/25% (4) | SUN(A) 1.6/18% (3) | LEE(H) 1.7/29% (3) | NFO(A) 1.2/17% (3) | CRY(H) 2.1/29% (2) | LIV(H) 1.4/25% (4) | MCI(A) 1.3/13% (5) | AVL(H) 1.8/32% (3) |
| ★ BRE | NFO(H) 1.6/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.5/20% (3) | NEW(H) 2.1/31% (3) |
| LIV | ARS(H) 1.1/27% (4) | CRY(A) 1.7/27% (3) | MUN(H) 1.8/31% (4) | EVE(A) 1.5/29% (3) | SUN(H) 2.0/31% (3) | CHE(A) 1.4/24% (4) | LEE(H) 1.7/35% (3) | TOT(H) 1.8/40% (2) |
| CRY | TOT(A) 1.3/19% (3) | LIV(H) 1.3/17% (4) | COV(A) 1.4/22% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/12% (4) | AVL(A) 1.3/17% (3) | MUN(H) 1.6/18% (4) | SUN(A) 1.4/12% (3) |
| ★ FUL | AVL(A) 1.3/22% (3) | NEW(H) 1.9/31% (3) | MCI(A) 1.2/11% (5) | BOU(H) 1.4/24% (3) | TOT(A) 1.2/24% (3) | EVE(A) 1.3/21% (3) | BRE(H) 1.6/23% (3) | LEE(A) 1.2/20% (3) |
| AVL | FUL(H) 1.5/27% (2) | MUN(A) 1.1/16% (4) | SUN(H) 1.7/23% (3) | IPS(A) 1.5/21% (2) | EVE(H) 1.5/29% (3) | CRY(H) 1.8/27% (2) | COV(A) 1.3/28% (2) | CHE(A) 1.1/17% (4) |
| TOT | CRY(H) 1.7/29% (2) | LEE(A) 1.0/21% (3) | IPS(H) 1.7/31% (2) | SUN(A) 1.2/18% (3) | FUL(H) 1.4/29% (2) | ARS(H) 0.8/21% (4) | HUL(A) 1.3/30% (2) | LIV(A) 0.9/17% (4) |
| ★ LEE | BOU(A) 1.1/19% (3) | TOT(H) 1.6/35% (2) | CHE(A) 1.2/19% (4) | COV(H) 1.7/38% (2) | MCI(A) 1.2/13% (5) | IPS(H) 2.0/32% (2) | LIV(A) 1.1/18% (4) | FUL(H) 1.6/30% (2) |
| EVE | NEW(A) 1.5/23% (3) | COV(H) 1.6/36% (2) | BRE(A) 1.2/16% (3) | LIV(H) 1.3/23% (4) | AVL(A) 1.2/22% (3) | FUL(H) 1.5/28% (2) | BHA(A) 1.2/11% (4) | NFO(A) 1.1/15% (3) |
| IPS | HUL(A) 1.4/22% (2) | BOU(H) 1.4/18% (3) | TOT(A) 1.2/18% (3) | AVL(H) 1.5/23% (3) | COV(A) 1.3/21% (2) | LEE(A) 1.2/14% (3) | NEW(H) 1.8/24% (3) | BHA(A) 1.2/7% (4) |
| COV | SUN(H) 1.4/21% (3) | EVE(A) 1.0/19% (3) | CRY(H) 1.5/25% (2) | LEE(A) 1.0/18% (3) | IPS(H) 1.6/27% (2) | MUN(A) 1.0/14% (4) | AVL(H) 1.3/28% (3) | BOU(A) 0.9/15% (3) |
| ★ NEW | EVE(H) 1.5/23% (3) | FUL(A) 1.2/15% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.6/18% (3) | IPS(A) 1.4/16% (2) | BRE(A) 1.2/12% (3) |
| ★ HUL | IPS(H) 1.5/25% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/18% (3) | BOU(A) 0.9/14% (3) | TOT(H) 1.2/28% (2) | MCI(A) 0.9/9% (5) |
