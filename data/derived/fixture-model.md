# Fixture model v0.2 — GW7–14

**Generated** 2026-10-10 13:37 UTC from mirror `2026-10-10T13:36:28Z`.
**Observed** 6 gameweek(s) — [1, 2, 3, 4, 5, 6]. With k=6 pseudo-matches, ratings are **50% prior / 50% data** for the 2 clubs on 6 matches, and **55% / 45%** for the 18 on 5. That weight shifts toward data every week.

League mean xG per team-match **1.53**; home 1.70 / away 1.36 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: AVL, BOU, BRE, BHA, CHE, COV, CRY, EVE, FUL, HUL, IPS, LIV, MCI, MUN, NEW, NFO, TOT, SUN on 5.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW7–10, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW6 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG7–10 | CS7–10 | xG7–14 | CS7–14 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.27 *(1.40)* | 0.87 | **8.11** | 1.07 | 15.35 | 2.08 | +2.2 | Haaland |
| ★ BHA | 1.29 *(1.51)* | 1.04 | **7.62** | 0.73 | 15.52 | 1.66 | +4.4 | De Cuyper, Groß |
| SUN | 1.22 *(1.28)* | 1.02 | **7.54** | 0.97 | 14.93 | 1.92 | -3.8 |  |
| ★ ARS | 1.20 *(1.21)* | 0.61 | **7.28** | 1.67 | 14.24 | 3.19 | -1.1 | Raya, Calafiori, Saka |
| MUN | 1.16 *(1.34)* | 0.92 | **7.20** | 1.10 | 14.46 | 2.19 | -2.3 |  |
| ★ FUL | 0.96 *(1.02)* | 1.10 | **6.62** | 1.05 | 12.07 | 1.78 | -2.8 | Gonzalo |
| ★ BRE | 1.09 *(1.33)* | 0.95 | **6.54** | 0.93 | 12.55 | 1.79 | -0.2 | Schade |
| ★ CHE | 1.04 *(0.97)* | 1.00 | **6.35** | 0.87 | 12.87 | 1.84 | +2.6 | Rogers, João Pedro |
| LIV | 1.09 *(1.09)* | 0.88 | **6.14** | 0.89 | 12.74 | 1.83 | -1.4 |  |
| ★ LEE | 0.96 *(0.94)* | 0.98 | **5.81** | 0.89 | 11.83 | 1.82 | -0.6 | Muharemović |
| CRY | 0.91 *(0.79)* | 1.11 | **5.76** | 0.78 | 11.41 | 1.68 | -0.1 |  |
| BOU | 0.92 *(0.89)* | 0.98 | **5.69** | 0.82 | 11.86 | 1.82 | -0.8 |  |
| IPS | 0.94 *(1.01)* | 1.12 | **5.58** | 0.78 | 11.31 | 1.67 | -0.8 |  |
| EVE | 0.93 *(0.93)* | 1.01 | **5.58** | 0.95 | 11.32 | 1.83 | -1.1 |  |
| ★ NEW | 0.83 *(0.69)* | 1.18 | **5.49** | 0.80 | 10.29 | 1.31 | +3.7 | Hall, Barnes |
| NFO | 0.99 *(0.98)* | 0.89 | **5.30** | 0.88 | 11.61 | 1.94 | -3.5 |  |
| TOT | 0.81 *(0.66)* | 1.04 | **5.23** | 0.95 | 10.29 | 1.76 | -3.0 |  |
| AVL | 0.82 *(0.60)* | 1.08 | **5.07** | 0.73 | 10.68 | 1.59 | -0.6 |  |
| COV | 0.77 *(0.64)* | 1.08 | **4.93** | 0.81 | 9.84 | 1.62 | -3.9 |  |
| ★ HUL | 0.78 *(0.70)* | 1.13 | **4.55** | 0.67 | 9.31 | 1.37 | +0.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW7 | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | IPS(H) 2.4/33% (2) | AVL(A) 1.9/30% (3) | BHA(H) 2.3/22% (3) | NFO(A) 1.5/23% (3) | FUL(H) 2.4/32% (2) | ARS(A) 1.1/17% (5) | LEE(H) 2.1/32% (3) | BRE(A) 1.6/20% (3) |
| ★ BHA | CRY(H) 2.4/28% (2) | LIV(A) 1.6/14% (4) | MCI(A) 1.5/10% (5) | BRE(H) 2.1/21% (3) | HUL(A) 2.0/25% (2) | NEW(H) 2.6/31% (3) | BOU(A) 1.7/20% (3) | NFO(A) 1.6/17% (3) |
| SUN | BOU(A) 1.6/20% (3) | LEE(H) 2.0/27% (3) | COV(A) 1.8/26% (2) | CHE(H) 2.1/24% (4) | AVL(A) 1.8/24% (3) | TOT(H) 2.2/32% (2) | LIV(A) 1.5/15% (4) | NEW(A) 2.0/24% (3) |
| ★ ARS | NFO(A) 1.4/36% (3) | EVE(H) 2.1/46% (3) | LIV(A) 1.4/32% (4) | HUL(H) 2.3/53% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.5/32% (3) | TOT(A) 1.7/43% (3) |
| MUN | LEE(A) 1.6/22% (3) | BOU(H) 1.9/32% (3) | CHE(A) 1.6/20% (4) | AVL(H) 2.1/36% (3) | LIV(A) 1.4/18% (4) | BRE(H) 1.9/25% (3) | NEW(A) 1.9/27% (3) | COV(H) 2.1/38% (2) |
| ★ FUL | HUL(H) 1.9/31% (2) | COV(A) 1.4/24% (2) | AVL(A) 1.4/22% (3) | NEW(H) 1.9/29% (3) | MCI(A) 1.1/9% (5) | BOU(H) 1.6/25% (3) | TOT(A) 1.4/22% (3) | EVE(A) 1.3/17% (3) |
| ★ BRE | LIV(H) 1.6/24% (4) | HUL(A) 1.7/29% (2) | NFO(H) 1.7/28% (3) | BHA(A) 1.6/12% (4) | EVE(H) 1.9/30% (3) | MUN(A) 1.4/15% (4) | ARS(H) 1.1/21% (4) | MCI(H) 1.6/19% (4) |
| ★ CHE | EVE(A) 1.4/20% (3) | TOT(H) 1.8/33% (2) | MUN(H) 1.6/21% (4) | SUN(A) 1.4/13% (3) | LEE(H) 1.7/27% (3) | NFO(A) 1.3/19% (3) | CRY(H) 2.0/29% (2) | LIV(H) 1.6/23% (4) |
| LIV | BRE(A) 1.4/19% (3) | BHA(H) 1.9/21% (3) | ARS(H) 1.1/24% (4) | CRY(A) 1.6/26% (3) | MUN(H) 1.7/25% (4) | EVE(A) 1.5/25% (3) | SUN(H) 1.9/23% (3) | CHE(A) 1.5/21% (4) |
| ★ LEE | MUN(H) 1.5/21% (4) | SUN(A) 1.3/13% (3) | BOU(A) 1.3/21% (3) | TOT(H) 1.7/34% (2) | CHE(A) 1.3/18% (4) | COV(H) 1.8/36% (2) | MCI(A) 1.1/12% (5) | IPS(H) 1.8/28% (2) |
| CRY | BHA(A) 1.3/9% (4) | NEW(H) 1.8/28% (3) | TOT(A) 1.3/22% (3) | LIV(H) 1.4/19% (4) | COV(A) 1.3/23% (2) | HUL(H) 1.7/31% (2) | CHE(A) 1.2/14% (4) | AVL(A) 1.3/21% (3) |
| BOU | SUN(H) 1.6/20% (3) | MUN(A) 1.1/14% (4) | LEE(H) 1.5/28% (3) | IPS(A) 1.4/21% (2) | NFO(H) 1.4/26% (3) | FUL(A) 1.4/20% (3) | BHA(H) 1.6/18% (3) | HUL(H) 1.8/35% (2) |
| IPS | MCI(A) 1.1/9% (5) | NFO(H) 1.4/22% (3) | HUL(A) 1.5/23% (2) | BOU(H) 1.6/25% (3) | TOT(A) 1.3/21% (3) | AVL(H) 1.7/29% (3) | COV(A) 1.4/23% (2) | LEE(A) 1.3/16% (3) |
| EVE | CHE(H) 1.6/24% (4) | ARS(A) 0.8/13% (5) | NEW(A) 1.5/24% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/15% (3) | LIV(H) 1.4/22% (4) | AVL(A) 1.4/25% (3) | FUL(H) 1.8/27% (2) |
| ★ NEW | AVL(H) 1.5/27% (3) | CRY(A) 1.3/16% (3) | EVE(H) 1.4/22% (3) | FUL(A) 1.3/14% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.2/7% (4) | MUN(H) 1.3/15% (4) | SUN(H) 1.4/14% (3) |
| NFO | ARS(H) 1.0/24% (4) | IPS(A) 1.5/24% (2) | BRE(A) 1.3/19% (3) | MCI(H) 1.5/21% (4) | BOU(A) 1.3/25% (3) | CHE(H) 1.7/29% (4) | HUL(A) 1.5/31% (2) | BHA(H) 1.8/21% (3) |
| TOT | COV(H) 1.5/34% (2) | CHE(A) 1.1/16% (4) | CRY(H) 1.5/28% (2) | LEE(A) 1.1/18% (3) | IPS(H) 1.6/26% (2) | SUN(A) 1.1/11% (3) | FUL(H) 1.5/25% (2) | ARS(H) 0.8/18% (4) |
| AVL | NEW(A) 1.3/22% (3) | MCI(H) 1.2/15% (4) | FUL(H) 1.5/24% (2) | MUN(A) 1.0/12% (4) | SUN(H) 1.4/17% (3) | IPS(A) 1.2/18% (2) | EVE(H) 1.4/25% (3) | CRY(H) 1.5/26% (2) |
| COV | TOT(A) 1.1/22% (3) | FUL(H) 1.4/24% (2) | SUN(H) 1.3/17% (3) | EVE(A) 1.1/18% (3) | CRY(H) 1.4/26% (2) | LEE(A) 1.0/17% (3) | IPS(H) 1.5/25% (2) | MUN(A) 1.0/12% (4) |
| ★ HUL | FUL(A) 1.2/16% (3) | BRE(H) 1.3/18% (3) | IPS(H) 1.5/23% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.4/14% (3) | CRY(A) 1.2/17% (3) | NFO(H) 1.2/22% (3) | BOU(A) 1.0/17% (3) |
