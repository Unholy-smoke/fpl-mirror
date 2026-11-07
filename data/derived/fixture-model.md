# Fixture model v0.2 — GW11–18

**Generated** 2026-11-07 07:05 UTC from mirror `2026-11-07T07:04:22Z`.
**Observed** 10 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. With k=6 pseudo-matches, ratings are **38% prior / 62% data** for the 2 clubs on 10 matches, and **40% / 60%** for the 18 on 9. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.62 / away 1.29 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, AVL, BOU, BRE, BHA, CHE, CRY, FUL, HUL, IPS, LEE, LIV, MCI, MUN, NEW, NFO, TOT, SUN on 9.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW11–14, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW10 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG11–14 | CS11–14 | xG11–18 | CS11–18 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.27 *(1.34)* | 0.96 | **7.29** | 1.03 | 15.07 | 2.16 | +6.4 | De Cuyper, Groß |
| ★ BOU | 1.14 *(1.21)* | 0.80 | **7.06** | 1.36 | 13.19 | 2.70 | -1.8 | Evanilson |
| ★ MCI | 1.29 *(1.42)* | 0.88 | **6.65** | 1.06 | 14.81 | 2.34 | +1.4 | Haaland |
| LIV | 1.09 *(1.01)* | 0.82 | **6.60** | 1.18 | 12.87 | 2.64 | -2.2 |  |
| ★ CHE | 1.06 *(1.03)* | 0.94 | **6.54** | 1.16 | 12.74 | 2.23 | +5.5 | Rogers |
| ★ ARS | 1.20 *(1.14)* | 0.61 | **6.50** | 1.55 | 13.89 | 3.23 | -0.9 | Raya, Calafiori |
| ★ AVL | 0.89 *(0.83)* | 1.08 | **6.34** | 0.99 | 11.13 | 1.92 | -0.9 | N.Jackson |
| ★ BRE | 1.12 *(1.09)* | 0.96 | **6.23** | 0.94 | 13.32 | 2.08 | +1.7 | Schade |
| MUN | 1.03 *(1.10)* | 1.12 | **6.11** | 0.89 | 11.96 | 1.64 | -4.4 |  |
| SUN | 1.09 *(1.02)* | 1.05 | **5.98** | 0.92 | 12.98 | 1.84 | -6.3 |  |
| ★ NFO | 1.05 *(1.14)* | 0.92 | **5.84** | 1.03 | 12.26 | 2.05 | -8.9 | Gibbs-White |
| ★ LEE | 0.92 *(0.87)* | 0.91 | **5.54** | 1.12 | 10.65 | 2.25 | -2.5 | Muharemović |
| EVE | 0.96 *(0.95)* | 1.04 | **5.37** | 0.89 | 10.68 | 1.59 | -1.8 |  |
| TOT | 0.86 *(0.89)* | 0.87 | **5.13** | 1.17 | 9.74 | 2.25 | -1.7 |  |
| CRY | 0.85 *(0.85)* | 1.34 | **4.97** | 0.73 | 9.62 | 1.25 | -2.2 |  |
| COV | 0.73 *(0.66)* | 1.06 | **4.97** | 0.98 | 9.25 | 1.86 | +0.4 |  |
| ★ NEW | 0.86 *(0.79)* | 1.26 | **4.95** | 0.58 | 9.90 | 1.14 | +1.6 | Hall, Barnes |
| IPS | 0.90 *(0.94)* | 1.22 | **4.89** | 0.83 | 10.58 | 1.52 | +1.7 |  |
| FUL | 0.96 *(1.06)* | 1.02 | **4.72** | 0.79 | 9.78 | 1.62 | -4.9 |  |
| ★ HUL | 0.73 *(0.70)* | 1.13 | **4.24** | 0.70 | 8.15 | 1.54 | +1.8 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | HUL(A) 1.9/32% (2) | NEW(H) 2.6/34% (3) | BOU(A) 1.3/17% (4) | NFO(A) 1.5/20% (2) | EVE(H) 2.1/31% (3) | IPS(H) 2.5/33% (2) | FUL(A) 1.7/23% (3) | TOT(A) 1.4/26% (3) |
| ★ BOU | NFO(H) 1.7/34% (3) | FUL(A) 1.5/29% (3) | BHA(H) 1.8/27% (4) | HUL(H) 2.1/47% (2) | ARS(A) 0.9/21% (5) | COV(H) 2.0/47% (2) | TOT(A) 1.3/33% (3) | CRY(A) 2.0/33% (2) |
| ★ MCI | FUL(H) 2.1/33% (2) | ARS(A) 1.0/18% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/20% (4) | CHE(H) 2.0/30% (4) | HUL(H) 2.4/43% (2) | NEW(A) 2.1/29% (3) | EVE(A) 1.7/25% (3) |
| LIV | MUN(H) 2.0/34% (3) | EVE(A) 1.5/28% (3) | SUN(H) 1.9/32% (2) | CHE(A) 1.3/24% (4) | LEE(H) 1.6/38% (3) | TOT(H) 1.5/40% (3) | HUL(A) 1.6/38% (2) | AVL(A) 1.5/31% (3) |
| ★ CHE | LEE(H) 1.6/33% (3) | NFO(A) 1.3/20% (2) | CRY(H) 2.3/36% (2) | LIV(H) 1.4/27% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.9/34% (3) | COV(A) 1.5/33% (2) | IPS(A) 1.7/26% (2) |
| ★ ARS | NEW(A) 1.9/43% (3) | MCI(H) 1.7/36% (4) | BRE(A) 1.5/33% (4) | TOT(A) 1.4/43% (3) | BOU(H) 1.6/41% (3) | MUN(H) 2.2/45% (3) | CRY(A) 2.1/43% (2) | FUL(A) 1.6/39% (3) |
| ★ AVL | SUN(H) 1.5/22% (2) | IPS(A) 1.4/21% (2) | EVE(H) 1.5/26% (3) | CRY(H) 1.9/30% (2) | COV(A) 1.2/28% (2) | CHE(A) 1.1/16% (4) | LEE(H) 1.3/28% (3) | LIV(H) 1.2/22% (4) |
| ★ BRE | EVE(H) 1.9/31% (3) | MUN(A) 1.6/20% (3) | ARS(H) 1.1/23% (4) | MCI(H) 1.6/20% (4) | FUL(A) 1.5/23% (3) | NEW(H) 2.3/34% (3) | IPS(A) 1.8/25% (2) | COV(A) 1.5/32% (2) |
| MUN | LIV(A) 1.1/14% (4) | BRE(H) 1.6/20% (3) | NEW(A) 1.7/21% (3) | COV(H) 1.8/35% (2) | CRY(A) 1.8/21% (2) | ARS(A) 0.8/11% (5) | NFO(H) 1.5/22% (3) | SUN(H) 1.7/21% (2) |
| SUN | AVL(A) 1.5/22% (3) | TOT(H) 1.5/31% (3) | LIV(A) 1.2/16% (4) | NEW(A) 1.8/23% (3) | NFO(H) 1.6/24% (3) | CRY(H) 2.4/31% (2) | EVE(A) 1.5/20% (3) | MUN(A) 1.6/17% (3) |
| ★ NFO | BOU(A) 1.1/18% (4) | CHE(H) 1.6/28% (4) | HUL(A) 1.5/34% (2) | BHA(H) 1.6/22% (4) | SUN(A) 1.4/20% (3) | EVE(H) 1.8/32% (3) | MUN(A) 1.5/22% (3) | NEW(A) 1.7/28% (3) |
| ★ LEE | CHE(A) 1.1/21% (4) | COV(H) 1.6/42% (2) | MCI(A) 1.0/15% (5) | IPS(H) 1.8/35% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.5/32% (2) | AVL(A) 1.3/27% (3) | HUL(A) 1.3/34% (2) |
| EVE | BRE(A) 1.2/15% (4) | LIV(H) 1.3/23% (4) | AVL(A) 1.3/23% (3) | FUL(H) 1.6/28% (2) | BHA(A) 1.2/12% (4) | NFO(A) 1.1/17% (2) | SUN(H) 1.6/23% (2) | MCI(H) 1.4/18% (4) |
| TOT | IPS(H) 1.7/36% (2) | SUN(A) 1.2/22% (3) | FUL(H) 1.4/34% (2) | ARS(H) 0.8/26% (4) | HUL(A) 1.3/36% (2) | LIV(A) 0.9/21% (4) | BOU(H) 1.1/27% (3) | BHA(H) 1.3/24% (4) |
| CRY | COV(A) 1.2/20% (2) | HUL(H) 1.6/28% (2) | CHE(A) 1.0/10% (4) | AVL(A) 1.2/14% (3) | MUN(H) 1.5/17% (3) | SUN(A) 1.2/9% (3) | ARS(H) 0.8/12% (4) | BOU(H) 1.1/14% (3) |
| COV | CRY(H) 1.6/31% (2) | LEE(A) 0.9/21% (3) | IPS(H) 1.4/29% (2) | MUN(A) 1.1/17% (3) | AVL(H) 1.3/29% (3) | BOU(A) 0.8/14% (4) | CHE(H) 1.1/23% (4) | BRE(H) 1.1/21% (3) |
| ★ NEW | ARS(H) 0.8/14% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.6/19% (3) | SUN(H) 1.5/17% (2) | IPS(A) 1.4/16% (2) | BRE(A) 1.1/10% (4) | MCI(H) 1.2/12% (4) | NFO(H) 1.3/18% (3) |
| IPS | TOT(A) 1.0/18% (3) | AVL(H) 1.6/25% (3) | COV(A) 1.2/24% (2) | LEE(A) 1.1/16% (3) | NEW(H) 1.8/26% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/17% (3) | CHE(H) 1.4/19% (4) |
| FUL | MCI(A) 1.1/12% (5) | BOU(H) 1.2/22% (3) | TOT(A) 1.1/24% (3) | EVE(A) 1.3/21% (3) | BRE(H) 1.5/23% (3) | LEE(A) 1.1/22% (3) | BHA(H) 1.5/19% (4) | ARS(H) 0.9/21% (4) |
| ★ HUL | BHA(H) 1.1/15% (4) | CRY(A) 1.3/21% (2) | NFO(H) 1.1/21% (3) | BOU(A) 0.8/12% (4) | TOT(H) 1.0/28% (3) | MCI(A) 0.8/9% (5) | LIV(H) 1.0/20% (4) | LEE(H) 1.1/26% (3) |
