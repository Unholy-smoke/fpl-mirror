# Fixture model v0.2 — GW9–16

**Generated** 2026-10-24 13:39 UTC from mirror `2026-10-24T13:38:29Z`.
**Observed** 8 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8]. With k=6 pseudo-matches, ratings are **43% prior / 57% data** for the 4 clubs on 8 matches, and **46% / 54%** for the 16 on 7. That weight shifts toward data every week.

League mean xG per team-match **1.50**; home 1.67 / away 1.33 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, BOU, BRE, BHA, CHE, COV, CRY, EVE, FUL, HUL, LEE, LIV, MUN, NEW, TOT, SUN on 7.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW9–12, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW8 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG9–12 | CS9–12 | xG9–16 | CS9–16 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.29 *(1.45)* | 0.97 | **8.25** | 1.01 | 16.12 | 1.98 | +7.7 | Groß, De Cuyper |
| ★ ARS | 1.19 *(1.14)* | 0.61 | **7.25** | 1.65 | 14.14 | 3.27 | -1.0 | Raya, Calafiori |
| ★ MCI | 1.29 *(1.43)* | 0.89 | **6.86** | 0.91 | 15.20 | 2.15 | +2.8 | Haaland |
| SUN | 1.08 *(1.01)* | 1.13 | **6.52** | 0.94 | 13.20 | 1.68 | -4.6 |  |
| ★ NFO | 1.12 *(1.17)* | 0.89 | **6.31** | 0.93 | 13.40 | 2.03 | -8.1 | Gibbs-White |
| BOU | 1.04 *(1.18)* | 0.89 | **6.29** | 1.09 | 12.66 | 2.30 | -3.4 |  |
| MUN | 1.07 *(1.14)* | 0.97 | **6.22** | 0.94 | 12.48 | 1.91 | -2.0 |  |
| ★ CHE | 1.04 *(0.95)* | 0.96 | **6.16** | 0.89 | 12.72 | 1.89 | +7.0 | Rogers, João Pedro |
| ★ BRE | 1.06 *(1.16)* | 1.02 | **6.13** | 0.78 | 12.37 | 1.65 | +0.8 | Schade |
| LIV | 1.09 *(1.04)* | 0.83 | **6.08** | 1.13 | 13.01 | 2.42 | -2.0 |  |
| CRY | 0.96 *(0.90)* | 1.21 | **5.82** | 0.89 | 11.37 | 1.48 | -0.4 |  |
| ★ FUL | 0.95 *(1.05)* | 1.02 | **5.73** | 0.90 | 11.08 | 1.79 | -4.0 | Gonzalo |
| ★ LEE | 0.96 *(0.95)* | 0.95 | **5.67** | 1.12 | 11.45 | 2.04 | -1.0 | Muharemović |
| TOT | 0.83 *(0.71)* | 0.98 | **5.66** | 0.97 | 10.09 | 1.94 | -1.5 |  |
| EVE | 0.91 *(0.88)* | 1.01 | **5.59** | 0.98 | 10.61 | 1.76 | -1.2 |  |
| AVL | 0.85 *(0.75)* | 1.02 | **5.53** | 0.88 | 10.98 | 1.88 | -0.1 |  |
| IPS | 0.91 *(0.93)* | 1.23 | **5.51** | 0.83 | 11.01 | 1.49 | +0.8 |  |
| COV | 0.76 *(0.68)* | 1.09 | **4.96** | 0.82 | 9.72 | 1.68 | -1.2 |  |
| ★ NEW | 0.87 *(0.78)* | 1.20 | **4.65** | 0.61 | 10.31 | 1.24 | +1.8 | Hall, Barnes |
| ★ HUL | 0.73 *(0.65)* | 1.14 | **4.46** | 0.65 | 8.48 | 1.34 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | MCI(A) 1.5/12% (5) | BRE(H) 2.2/25% (3) | HUL(A) 2.0/31% (2) | NEW(H) 2.6/33% (3) | BOU(A) 1.5/19% (3) | NFO(A) 1.5/16% (3) | EVE(H) 2.2/31% (3) | IPS(H) 2.6/31% (2) |
| ★ ARS | LIV(A) 1.3/33% (4) | HUL(H) 2.3/55% (2) | NEW(A) 1.9/41% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/34% (3) | TOT(A) 1.6/43% (3) | BOU(H) 1.8/43% (3) | MUN(H) 1.9/42% (4) |
| ★ MCI | BHA(H) 2.1/22% (3) | NFO(A) 1.5/19% (3) | FUL(H) 2.2/32% (2) | ARS(A) 1.0/17% (5) | LEE(H) 2.0/32% (3) | BRE(A) 1.8/21% (3) | CHE(H) 2.1/29% (4) | HUL(H) 2.5/42% (2) |
| SUN | COV(A) 1.6/24% (2) | CHE(H) 1.7/21% (4) | AVL(A) 1.5/20% (3) | TOT(H) 1.8/29% (2) | LIV(A) 1.2/13% (4) | NEW(A) 1.7/20% (3) | NFO(H) 1.6/19% (3) | CRY(H) 2.2/24% (2) |
| ★ NFO | BRE(A) 1.5/21% (3) | MCI(H) 1.7/22% (4) | BOU(A) 1.3/22% (3) | CHE(H) 1.8/29% (4) | HUL(A) 1.7/34% (2) | BHA(H) 1.8/22% (3) | SUN(A) 1.7/20% (3) | EVE(H) 1.9/34% (3) |
| BOU | LEE(H) 1.6/32% (3) | IPS(A) 1.7/26% (2) | NFO(H) 1.5/26% (3) | FUL(A) 1.4/24% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.0/42% (2) | ARS(A) 0.8/17% (5) | COV(H) 1.9/40% (2) |
| MUN | CHE(A) 1.4/18% (4) | AVL(H) 1.8/33% (3) | LIV(A) 1.2/17% (4) | BRE(H) 1.8/25% (3) | NEW(A) 1.7/24% (3) | COV(H) 1.9/37% (2) | CRY(A) 1.7/21% (3) | ARS(A) 0.9/14% (5) |
| ★ CHE | MUN(H) 1.7/25% (4) | SUN(A) 1.6/18% (3) | LEE(H) 1.7/29% (3) | NFO(A) 1.2/17% (3) | CRY(H) 2.1/29% (2) | LIV(H) 1.4/25% (4) | MCI(A) 1.2/13% (5) | AVL(H) 1.8/34% (3) |
| ★ BRE | NFO(H) 1.6/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.4/20% (3) | NEW(H) 2.1/31% (3) |
| LIV | ARS(H) 1.1/27% (4) | CRY(A) 1.7/27% (3) | MUN(H) 1.8/31% (4) | EVE(A) 1.5/29% (3) | SUN(H) 2.0/30% (3) | CHE(A) 1.4/24% (4) | LEE(H) 1.7/35% (3) | TOT(H) 1.8/40% (2) |
| CRY | TOT(A) 1.3/19% (3) | LIV(H) 1.3/17% (4) | COV(A) 1.4/22% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/12% (4) | AVL(A) 1.3/18% (3) | MUN(H) 1.6/18% (4) | SUN(A) 1.4/11% (3) |
| ★ FUL | AVL(A) 1.3/24% (3) | NEW(H) 1.9/31% (3) | MCI(A) 1.1/11% (5) | BOU(H) 1.4/24% (3) | TOT(A) 1.2/24% (3) | EVE(A) 1.3/21% (3) | BRE(H) 1.6/23% (3) | LEE(A) 1.2/20% (3) |
| ★ LEE | BOU(A) 1.1/19% (3) | TOT(H) 1.6/35% (2) | CHE(A) 1.2/19% (4) | COV(H) 1.7/38% (2) | MCI(A) 1.1/13% (5) | IPS(H) 2.0/31% (2) | LIV(A) 1.1/18% (4) | FUL(H) 1.6/30% (2) |
| TOT | CRY(H) 1.7/28% (2) | LEE(A) 1.0/21% (3) | IPS(H) 1.7/30% (2) | SUN(A) 1.2/17% (3) | FUL(H) 1.4/29% (2) | ARS(H) 0.8/21% (4) | HUL(A) 1.3/30% (2) | LIV(A) 0.9/17% (4) |
| EVE | NEW(A) 1.5/23% (3) | COV(H) 1.6/36% (2) | BRE(A) 1.2/17% (3) | LIV(H) 1.3/23% (4) | AVL(A) 1.2/24% (3) | FUL(H) 1.5/28% (2) | BHA(A) 1.2/11% (4) | NFO(A) 1.1/15% (3) |
| AVL | FUL(H) 1.4/27% (2) | MUN(A) 1.1/16% (4) | SUN(H) 1.6/23% (3) | IPS(A) 1.4/21% (2) | EVE(H) 1.4/29% (3) | CRY(H) 1.7/27% (2) | COV(A) 1.2/27% (2) | CHE(A) 1.1/17% (4) |
| IPS | HUL(A) 1.4/22% (2) | BOU(H) 1.4/18% (3) | TOT(A) 1.2/18% (3) | AVL(H) 1.6/25% (3) | COV(A) 1.3/21% (2) | LEE(A) 1.2/14% (3) | NEW(H) 1.8/24% (3) | BHA(A) 1.2/7% (4) |
| COV | SUN(H) 1.4/21% (3) | EVE(A) 1.0/19% (3) | CRY(H) 1.5/25% (2) | LEE(A) 1.0/18% (3) | IPS(H) 1.6/26% (2) | MUN(A) 1.0/14% (4) | AVL(H) 1.3/29% (3) | BOU(A) 0.9/15% (3) |
| ★ NEW | EVE(H) 1.5/23% (3) | FUL(A) 1.2/15% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.6/18% (3) | IPS(A) 1.4/16% (2) | BRE(A) 1.2/12% (3) |
| ★ HUL | IPS(H) 1.5/25% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/18% (3) | BOU(A) 0.9/14% (3) | TOT(H) 1.2/28% (2) | MCI(A) 0.9/9% (5) |
