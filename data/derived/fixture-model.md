# Fixture model v0.2 — GW13–20

**Generated** 2026-11-27 23:46 UTC from mirror `2026-11-27T23:45:45Z`.
**Observed** 12 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]. With k=6 pseudo-matches, ratings are **33% prior / 67% data** for the 2 clubs on 12 matches, and **35% / 65%** for the 18 on 11. That weight shifts toward data every week.

League mean xG per team-match **1.49**; home 1.66 / away 1.33 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, AVL, BOU, BRE, BHA, COV, CRY, EVE, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, TOT, SUN on 11.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW13–16, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW12 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG13–16 | CS13–16 | xG13–20 | CS13–20 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.34)* | 0.94 | **7.92** | 1.02 | 15.54 | 2.04 | +4.1 | De Cuyper, Groß |
| ★ MCI | 1.26 *(1.35)* | 0.84 | **7.75** | 1.32 | 14.68 | 2.52 | -0.2 | Haaland |
| ★ BOU | 1.19 *(1.28)* | 0.84 | **7.15** | 1.33 | 14.31 | 2.43 | -3.0 | Evanilson |
| SUN | 1.05 *(0.97)* | 0.99 | **6.86** | 0.92 | 13.51 | 1.93 | -7.9 |  |
| ★ LIV | 1.17 *(1.23)* | 0.85 | **6.81** | 1.27 | 13.83 | 2.56 | -2.2 | Jacquet, Wirtz |
| ★ ARS | 1.14 *(1.07)* | 0.62 | **6.65** | 1.55 | 14.36 | 3.23 | -0.7 | Raya, Calafiori |
| ★ CHE | 0.98 *(0.89)* | 1.01 | **6.45** | 0.90 | 13.15 | 1.92 | +6.0 | Rogers |
| ★ NFO | 1.05 *(1.08)* | 0.93 | **6.36** | 1.05 | 13.39 | 2.23 | -7.4 | Gibbs-White |
| ★ AVL | 0.93 *(0.90)* | 1.08 | **6.33** | 0.97 | 11.28 | 1.71 | -0.9 | N.Jackson |
| MUN | 1.04 *(1.13)* | 1.26 | **6.22** | 0.67 | 12.83 | 1.30 | -4.6 |  |
| BRE | 1.10 *(1.06)* | 0.89 | **6.21** | 1.09 | 13.02 | 2.22 | +2.5 |  |
| ★ LEE | 1.00 *(0.98)* | 0.85 | **6.02** | 1.10 | 12.10 | 2.32 | -2.2 | Muharemović |
| NEW | 0.90 *(0.81)* | 1.16 | **5.95** | 0.71 | 11.33 | 1.35 | +1.8 |  |
| CRY | 0.93 *(0.94)* | 1.38 | **5.79** | 0.46 | 10.72 | 0.95 | -3.5 |  |
| EVE | 0.90 *(0.85)* | 1.04 | **5.00** | 0.77 | 10.35 | 1.62 | -2.0 |  |
| COV | 0.74 *(0.71)* | 1.08 | **4.98** | 0.83 | 9.42 | 1.63 | +1.3 |  |
| IPS | 0.86 *(0.85)* | 1.27 | **4.93** | 0.62 | 9.89 | 1.35 | +1.0 |  |
| FUL | 0.89 *(0.93)* | 0.99 | **4.55** | 0.90 | 9.21 | 1.80 | -4.3 |  |
| ★ TOT | 0.85 *(0.92)* | 0.86 | **4.50** | 1.18 | 9.09 | 2.11 | -3.1 | Kudus |
| ★ HUL | 0.73 *(0.69)* | 1.11 | **3.81** | 0.70 | 7.74 | 1.40 | +1.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 | GW19 | GW20 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | BOU(A) 1.4/16% (4) | NFO(A) 1.6/20% (2) | EVE(H) 2.2/33% (3) | IPS(H) 2.7/34% (2) | FUL(A) 1.7/25% (3) | TOT(A) 1.5/26% (3) | MUN(H) 2.7/27% (3) | BOU(H) 1.8/23% (3) |
| ★ MCI | LEE(H) 1.8/32% (3) | BRE(A) 1.5/22% (4) | CHE(H) 2.1/34% (4) | HUL(H) 2.3/44% (2) | NEW(A) 1.9/28% (3) | EVE(A) 1.7/29% (3) | TOT(H) 1.8/39% (3) | LEE(A) 1.4/25% (3) |
| ★ BOU | BHA(H) 1.9/24% (4) | HUL(H) 2.2/44% (2) | ARS(A) 1.0/20% (5) | COV(H) 2.1/44% (2) | TOT(A) 1.4/31% (3) | CRY(A) 2.2/27% (2) | AVL(H) 2.1/36% (3) | BHA(A) 1.5/17% (4) |
| SUN | LIV(A) 1.2/15% (4) | NEW(A) 1.6/23% (3) | NFO(H) 1.6/25% (3) | CRY(H) 2.4/29% (2) | EVE(A) 1.5/23% (3) | MUN(A) 1.8/18% (3) | HUL(H) 1.9/38% (2) | LIV(H) 1.5/22% (4) |
| ★ LIV | SUN(H) 1.9/31% (2) | CHE(A) 1.6/25% (4) | LEE(H) 1.7/32% (3) | TOT(H) 1.7/38% (3) | HUL(A) 1.7/36% (2) | AVL(A) 1.7/27% (3) | COV(H) 2.1/43% (2) | SUN(A) 1.5/23% (3) |
| ★ ARS | BRE(A) 1.4/33% (4) | TOT(A) 1.3/42% (3) | BOU(H) 1.6/38% (3) | MUN(H) 2.4/43% (3) | CRY(A) 2.1/38% (2) | FUL(A) 1.5/40% (3) | IPS(H) 2.4/49% (2) | BRE(H) 1.7/41% (3) |
| ★ CHE | CRY(H) 2.2/28% (2) | LIV(H) 1.4/21% (4) | MCI(A) 1.1/12% (5) | AVL(H) 1.8/29% (3) | COV(A) 1.4/29% (2) | IPS(A) 1.6/24% (2) | NEW(H) 1.9/30% (3) | CRY(A) 1.8/21% (2) |
| ★ NFO | HUL(A) 1.5/32% (2) | BHA(H) 1.6/20% (4) | SUN(A) 1.4/19% (3) | EVE(H) 1.8/33% (3) | MUN(A) 1.8/20% (3) | NEW(A) 1.6/25% (3) | FUL(H) 1.7/33% (2) | HUL(H) 1.9/40% (2) |
| ★ AVL | EVE(H) 1.6/28% (3) | CRY(H) 2.1/26% (2) | COV(A) 1.3/26% (2) | CHE(A) 1.3/17% (4) | LEE(H) 1.3/24% (3) | LIV(H) 1.3/19% (4) | BOU(A) 1.0/12% (4) | EVE(A) 1.3/20% (3) |
| MUN | NEW(A) 1.6/15% (3) | COV(H) 1.9/29% (2) | CRY(A) 1.9/14% (2) | ARS(A) 0.9/9% (5) | NFO(H) 1.6/17% (3) | SUN(H) 1.7/17% (2) | BHA(A) 1.3/7% (4) | NEW(H) 2.0/22% (3) |
| BRE | ARS(H) 1.1/26% (4) | MCI(H) 1.5/22% (4) | FUL(A) 1.4/27% (3) | NEW(H) 2.1/34% (3) | IPS(A) 1.8/28% (2) | COV(A) 1.6/33% (2) | CRY(H) 2.5/33% (2) | ARS(A) 0.9/18% (5) |
| ★ LEE | MCI(A) 1.1/17% (5) | IPS(H) 2.1/38% (2) | LIV(A) 1.1/19% (4) | FUL(H) 1.7/37% (2) | AVL(A) 1.4/27% (3) | HUL(A) 1.5/35% (2) | EVE(H) 1.7/36% (3) | MCI(H) 1.4/24% (4) |
| NEW | MUN(H) 1.9/20% (3) | SUN(H) 1.5/20% (2) | IPS(A) 1.5/19% (2) | BRE(A) 1.1/12% (4) | MCI(H) 1.3/14% (4) | NFO(H) 1.4/20% (3) | CHE(A) 1.2/15% (4) | MUN(A) 1.5/14% (3) |
| CRY | CHE(A) 1.3/11% (4) | AVL(A) 1.3/12% (3) | MUN(H) 2.0/15% (3) | SUN(A) 1.2/9% (3) | ARS(H) 1.0/12% (4) | BOU(H) 1.3/11% (3) | BRE(A) 1.1/8% (4) | CHE(H) 1.6/17% (4) |
| EVE | AVL(A) 1.3/20% (3) | FUL(H) 1.5/29% (2) | BHA(A) 1.1/11% (4) | NFO(A) 1.1/16% (2) | SUN(H) 1.5/23% (2) | MCI(H) 1.3/17% (4) | LEE(A) 1.0/18% (3) | AVL(H) 1.6/28% (3) |
| COV | IPS(H) 1.6/29% (2) | MUN(A) 1.2/16% (3) | AVL(H) 1.3/26% (3) | BOU(A) 0.8/12% (4) | CHE(H) 1.3/25% (4) | BRE(H) 1.1/21% (3) | LIV(A) 0.8/12% (4) | IPS(A) 1.3/22% (2) |
| IPS | COV(A) 1.2/21% (2) | LEE(A) 1.0/12% (3) | NEW(H) 1.7/22% (3) | BHA(A) 1.1/7% (4) | BRE(H) 1.3/16% (3) | CHE(H) 1.4/19% (4) | ARS(A) 0.7/9% (5) | COV(H) 1.5/29% (2) |
| FUL | TOT(A) 1.0/24% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.3/24% (3) | LEE(A) 1.0/19% (3) | BHA(H) 1.4/18% (4) | ARS(H) 0.9/22% (4) | NFO(A) 1.1/18% (2) | TOT(H) 1.3/32% (3) |
| ★ TOT | FUL(H) 1.4/36% (2) | ARS(H) 0.9/27% (4) | HUL(A) 1.3/35% (2) | LIV(A) 1.0/19% (4) | BOU(H) 1.2/26% (3) | BHA(H) 1.3/23% (4) | MCI(A) 1.0/16% (5) | FUL(A) 1.1/28% (3) |
| ★ HUL | NFO(H) 1.1/21% (3) | BOU(A) 0.8/11% (4) | TOT(H) 1.0/28% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/18% (4) | LEE(H) 1.0/23% (3) | SUN(A) 1.0/14% (3) | NFO(A) 0.9/14% (2) |
