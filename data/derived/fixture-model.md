# Fixture model v0.2 — GW8–15

**Generated** 2026-10-19 09:19 UTC from mirror `2026-10-19T09:19:10Z`.
**Observed** 7 gameweek(s) — [1, 2, 3, 4, 5, 6, 7]. With k=6 pseudo-matches, ratings are **46% prior / 54% data** for the 18 clubs on 7 matches, and **50% / 50%** for the 2 on 6. That weight shifts toward data every week.

League mean xG per team-match **1.52**; home 1.69 / away 1.35 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: COV, TOT on 6.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW8–11, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW7 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG8–11 | CS8–11 | xG8–15 | CS8–15 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.29 *(1.46)* | 0.90 | **7.70** | 0.98 | 14.68 | 1.94 | +3.4 | Haaland |
| ★ ARS | 1.18 *(1.13)* | 0.61 | **7.47** | 1.77 | 14.23 | 3.30 | -1.0 | Raya, Calafiori, Saka |
| ★ BHA | 1.28 *(1.44)* | 0.96 | **7.10** | 0.86 | 14.94 | 1.85 | +7.7 | De Cuyper, Groß |
| ★ CHE | 1.04 *(0.94)* | 0.96 | **6.68** | 1.05 | 12.81 | 1.88 | +7.0 | Rogers, João Pedro |
| SUN | 1.07 *(1.00)* | 1.12 | **6.53** | 0.87 | 12.90 | 1.66 | -4.6 |  |
| ★ BRE | 1.06 *(1.14)* | 1.01 | **6.43** | 0.91 | 11.94 | 1.64 | +0.8 | Schade |
| LIV | 1.08 *(1.03)* | 0.83 | **6.36** | 1.08 | 12.98 | 2.24 | -2.0 |  |
| BOU | 1.03 *(1.17)* | 0.89 | **6.30** | 1.03 | 12.21 | 2.08 | -3.4 |  |
| NFO | 1.09 *(1.11)* | 0.93 | **6.25** | 0.82 | 13.11 | 1.80 | -6.8 |  |
| MUN | 1.07 *(1.13)* | 0.96 | **6.02** | 0.94 | 13.34 | 2.02 | -2.0 |  |
| CRY | 0.95 *(0.89)* | 1.20 | **5.96** | 0.81 | 11.87 | 1.58 | -0.4 |  |
| ★ FUL | 0.95 *(1.04)* | 1.02 | **5.80** | 0.91 | 11.41 | 1.83 | -4.0 | Gonzalo |
| TOT | 0.85 *(0.73)* | 0.99 | **5.67** | 0.94 | 10.60 | 1.89 | -3.6 |  |
| AVL | 0.88 *(0.80)* | 1.02 | **5.63** | 0.83 | 11.66 | 1.86 | -1.5 |  |
| IPS | 0.94 *(0.99)* | 1.21 | **5.60** | 0.75 | 11.75 | 1.58 | +0.4 |  |
| ★ LEE | 0.95 *(0.94)* | 0.95 | **5.42** | 0.90 | 11.40 | 1.88 | -1.0 | Muharemović |
| COV | 0.77 *(0.70)* | 1.13 | **5.38** | 0.85 | 10.27 | 1.65 | -1.4 |  |
| EVE | 0.90 *(0.87)* | 1.01 | **5.15** | 0.88 | 10.37 | 1.73 | -1.2 |  |
| ★ NEW | 0.86 *(0.77)* | 1.19 | **4.92** | 0.68 | 10.48 | 1.27 | +1.8 | Hall, Barnes |
| ★ HUL | 0.73 *(0.64)* | 1.13 | **4.52** | 0.68 | 8.94 | 1.44 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | AVL(A) 1.8/26% (3) | BHA(H) 2.1/21% (3) | NFO(A) 1.6/19% (3) | FUL(H) 2.2/32% (2) | ARS(A) 1.1/17% (5) | LEE(H) 2.1/31% (3) | BRE(A) 1.8/20% (3) | CHE(H) 2.1/28% (4) |
| ★ ARS | EVE(H) 2.0/48% (3) | LIV(A) 1.3/33% (4) | HUL(H) 2.3/55% (2) | NEW(A) 1.9/41% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/34% (3) | TOT(A) 1.6/42% (3) | BOU(H) 1.8/43% (3) |
| ★ BHA | LIV(A) 1.4/17% (4) | MCI(A) 1.6/12% (5) | BRE(H) 2.2/25% (3) | HUL(A) 1.9/31% (2) | NEW(H) 2.6/33% (3) | BOU(A) 1.5/19% (3) | NFO(A) 1.6/17% (3) | EVE(H) 2.2/31% (3) |
| ★ CHE | TOT(H) 1.7/33% (2) | MUN(H) 1.7/25% (4) | SUN(A) 1.6/18% (3) | LEE(H) 1.7/29% (3) | NFO(A) 1.3/17% (3) | CRY(H) 2.1/29% (2) | LIV(H) 1.5/25% (4) | MCI(A) 1.3/12% (5) |
| SUN | LEE(H) 1.7/24% (3) | COV(A) 1.6/23% (2) | CHE(H) 1.7/21% (4) | AVL(A) 1.5/19% (3) | TOT(H) 1.8/28% (2) | LIV(A) 1.2/13% (4) | NEW(A) 1.7/20% (3) | NFO(H) 1.7/19% (3) |
| ★ BRE | HUL(A) 1.6/29% (2) | NFO(H) 1.7/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.4/20% (3) |
| LIV | BHA(H) 1.8/24% (3) | ARS(H) 1.1/27% (4) | CRY(A) 1.7/27% (3) | MUN(H) 1.8/30% (4) | EVE(A) 1.5/28% (3) | SUN(H) 2.0/30% (3) | CHE(A) 1.4/23% (4) | LEE(H) 1.7/35% (3) |
| BOU | MUN(A) 1.3/20% (4) | LEE(H) 1.7/32% (3) | IPS(A) 1.7/24% (2) | NFO(H) 1.6/27% (3) | FUL(A) 1.4/24% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.0/42% (2) | ARS(A) 0.8/17% (5) |
| NFO | IPS(A) 1.8/23% (2) | BRE(A) 1.5/19% (3) | MCI(H) 1.7/20% (4) | BOU(A) 1.3/20% (3) | CHE(H) 1.8/27% (4) | HUL(A) 1.7/32% (2) | BHA(H) 1.8/20% (3) | SUN(A) 1.7/19% (3) |
| MUN | BOU(H) 1.6/26% (3) | CHE(A) 1.4/18% (4) | AVL(H) 1.8/32% (3) | LIV(A) 1.2/17% (4) | BRE(H) 1.8/25% (3) | NEW(A) 1.7/25% (3) | COV(H) 2.0/37% (2) | CRY(A) 1.7/21% (3) |
| CRY | NEW(H) 1.9/25% (3) | TOT(A) 1.3/18% (3) | LIV(H) 1.3/17% (4) | COV(A) 1.4/21% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/12% (4) | AVL(A) 1.3/17% (3) | MUN(H) 1.5/18% (4) |
| ★ FUL | COV(A) 1.4/27% (2) | AVL(A) 1.3/22% (3) | NEW(H) 1.9/31% (3) | MCI(A) 1.2/11% (5) | BOU(H) 1.4/24% (3) | TOT(A) 1.3/23% (3) | EVE(A) 1.3/21% (3) | BRE(H) 1.6/23% (3) |
| TOT | CHE(A) 1.1/17% (4) | CRY(H) 1.7/28% (2) | LEE(A) 1.1/20% (3) | IPS(H) 1.7/28% (2) | SUN(A) 1.3/17% (3) | FUL(H) 1.5/28% (2) | ARS(H) 0.9/21% (4) | HUL(A) 1.3/29% (2) |
| AVL | MCI(H) 1.3/17% (4) | FUL(H) 1.5/27% (2) | MUN(A) 1.1/16% (4) | SUN(H) 1.7/23% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/29% (3) | CRY(H) 1.8/27% (2) | COV(A) 1.3/27% (2) |
| IPS | NFO(H) 1.5/17% (3) | HUL(A) 1.4/22% (2) | BOU(H) 1.4/18% (3) | TOT(A) 1.3/17% (3) | AVL(H) 1.6/24% (3) | COV(A) 1.4/21% (2) | LEE(A) 1.2/14% (3) | NEW(H) 1.9/24% (3) |
| ★ LEE | SUN(A) 1.4/18% (3) | BOU(A) 1.1/19% (3) | TOT(H) 1.6/34% (2) | CHE(A) 1.2/19% (4) | COV(H) 1.8/37% (2) | MCI(A) 1.2/13% (5) | IPS(H) 1.9/30% (2) | LIV(A) 1.1/18% (4) |
| COV | FUL(H) 1.3/24% (2) | SUN(H) 1.5/20% (3) | EVE(A) 1.0/18% (3) | CRY(H) 1.6/24% (2) | LEE(A) 1.0/16% (3) | IPS(H) 1.6/24% (2) | MUN(A) 1.0/13% (4) | AVL(H) 1.3/26% (3) |
| EVE | ARS(A) 0.7/14% (5) | NEW(A) 1.5/23% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/17% (3) | LIV(H) 1.3/23% (4) | AVL(A) 1.2/23% (3) | FUL(H) 1.5/28% (2) | BHA(A) 1.2/12% (4) |
| ★ NEW | CRY(A) 1.4/15% (3) | EVE(H) 1.5/23% (3) | FUL(A) 1.2/15% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.6/18% (3) | IPS(A) 1.4/15% (2) |
| ★ HUL | BRE(H) 1.2/20% (3) | IPS(H) 1.5/24% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/19% (3) | BOU(A) 0.9/14% (3) | TOT(H) 1.2/27% (2) |
