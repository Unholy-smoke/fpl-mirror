# Fixture model v0.2 — GW7–14

**Generated** 2026-10-10 17:49 UTC from mirror `2026-10-10T17:48:27Z`.
**Observed** 6 gameweek(s) — [1, 2, 3, 4, 5, 6]. With k=6 pseudo-matches, ratings are **50% prior / 50% data** for the 10 clubs on 6 matches, and **55% / 45%** for the 10 on 5. That weight shifts toward data every week.

League mean xG per team-match **1.51**; home 1.68 / away 1.35 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: COV, CRY, EVE, HUL, LIV, MCI, MUN, NEW, NFO, TOT on 5.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW7–10, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW6 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG7–10 | CS7–10 | xG7–14 | CS7–14 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.29 *(1.42)* | 0.89 | **8.04** | 1.06 | 15.32 | 2.05 | +2.2 | Haaland |
| ★ BHA | 1.26 *(1.39)* | 0.99 | **7.46** | 0.81 | 15.02 | 1.81 | +5.3 | De Cuyper, Groß |
| ★ ARS | 1.21 *(1.22)* | 0.62 | **7.29** | 1.66 | 14.35 | 3.17 | -1.1 | Raya, Calafiori, Saka |
| MUN | 1.16 *(1.36)* | 0.92 | **7.10** | 1.09 | 14.38 | 2.19 | -2.3 |  |
| SUN | 1.15 *(1.15)* | 0.99 | **7.04** | 1.01 | 13.92 | 2.00 | -4.5 |  |
| ★ FUL | 0.98 *(1.06)* | 1.08 | **6.69** | 1.07 | 12.19 | 1.83 | -3.6 | Gonzalo |
| ★ BRE | 1.08 *(1.26)* | 0.98 | **6.31** | 0.90 | 12.22 | 1.71 | +0.5 | Schade |
| ★ CHE | 1.02 *(0.93)* | 1.02 | **6.15** | 0.87 | 12.50 | 1.82 | +6.5 | Rogers, João Pedro |
| LIV | 1.10 *(1.11)* | 0.89 | **6.09** | 0.91 | 12.68 | 1.88 | -1.4 |  |
| ★ LEE | 0.97 *(0.95)* | 0.99 | **5.75** | 0.91 | 11.88 | 1.85 | -0.6 | Muharemović |
| BOU | 0.93 *(0.91)* | 0.95 | **5.71** | 0.90 | 11.79 | 1.94 | -1.3 |  |
| CRY | 0.91 *(0.80)* | 1.11 | **5.67** | 0.79 | 11.30 | 1.69 | -0.1 |  |
| EVE | 0.94 *(0.94)* | 1.02 | **5.61** | 0.96 | 11.32 | 1.83 | -1.1 |  |
| ★ NEW | 0.84 *(0.70)* | 1.18 | **5.43** | 0.79 | 10.13 | 1.33 | +3.7 | Hall, Barnes |
| NFO | 1.00 *(0.99)* | 0.89 | **5.40** | 0.90 | 11.59 | 1.98 | -3.5 |  |
| IPS | 0.92 *(0.98)* | 1.15 | **5.38** | 0.75 | 10.93 | 1.61 | +0.1 |  |
| TOT | 0.82 *(0.66)* | 1.05 | **5.23** | 0.96 | 10.25 | 1.79 | -3.0 |  |
| AVL | 0.84 *(0.70)* | 1.07 | **5.18** | 0.74 | 10.91 | 1.65 | -0.4 |  |
| COV | 0.78 *(0.65)* | 1.08 | **4.86** | 0.83 | 9.81 | 1.64 | -3.9 |  |
| ★ HUL | 0.78 *(0.71)* | 1.13 | **4.58** | 0.69 | 9.20 | 1.40 | +0.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW7 | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | IPS(H) 2.5/33% (2) | AVL(A) 1.9/28% (3) | BHA(H) 2.1/22% (3) | NFO(A) 1.5/22% (3) | FUL(H) 2.4/31% (2) | ARS(A) 1.1/16% (5) | LEE(H) 2.2/31% (3) | BRE(A) 1.7/20% (3) |
| ★ BHA | CRY(H) 2.4/30% (2) | LIV(A) 1.5/16% (4) | MCI(A) 1.5/12% (5) | BRE(H) 2.1/24% (3) | HUL(A) 1.9/27% (2) | NEW(H) 2.5/33% (3) | BOU(A) 1.6/21% (3) | NFO(A) 1.5/19% (3) |
| ★ ARS | NFO(A) 1.4/35% (3) | EVE(H) 2.1/46% (3) | LIV(A) 1.4/32% (4) | HUL(H) 2.3/52% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/34% (4) | BRE(A) 1.6/33% (3) | TOT(A) 1.7/43% (3) |
| MUN | LEE(A) 1.5/22% (3) | BOU(H) 1.9/31% (3) | CHE(A) 1.6/20% (4) | AVL(H) 2.1/35% (3) | LIV(A) 1.4/18% (4) | BRE(H) 1.9/26% (3) | NEW(A) 1.8/27% (3) | COV(H) 2.1/38% (2) |
| SUN | BOU(A) 1.5/21% (3) | LEE(H) 1.9/27% (3) | COV(A) 1.7/27% (2) | CHE(H) 2.0/26% (4) | AVL(A) 1.7/24% (3) | TOT(H) 2.0/34% (2) | LIV(A) 1.4/16% (4) | NEW(A) 1.8/25% (3) |
| ★ FUL | HUL(H) 1.9/32% (2) | COV(A) 1.4/24% (2) | AVL(A) 1.4/21% (3) | NEW(H) 2.0/29% (3) | MCI(A) 1.2/9% (5) | BOU(H) 1.6/26% (3) | TOT(A) 1.4/22% (3) | EVE(A) 1.3/18% (3) |
| ★ BRE | LIV(H) 1.6/23% (4) | HUL(A) 1.6/28% (2) | NFO(H) 1.6/27% (3) | BHA(A) 1.4/12% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.3/15% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/18% (4) |
| ★ CHE | EVE(A) 1.4/20% (3) | TOT(H) 1.8/33% (2) | MUN(H) 1.6/20% (4) | SUN(A) 1.4/14% (3) | LEE(H) 1.7/26% (3) | NFO(A) 1.2/18% (3) | CRY(H) 1.9/29% (2) | LIV(H) 1.5/22% (4) |
| LIV | BRE(A) 1.5/20% (3) | BHA(H) 1.8/22% (3) | ARS(H) 1.1/23% (4) | CRY(A) 1.6/26% (3) | MUN(H) 1.7/25% (4) | EVE(A) 1.5/25% (3) | SUN(H) 1.8/25% (3) | CHE(A) 1.5/22% (4) |
| ★ LEE | MUN(H) 1.5/21% (4) | SUN(A) 1.3/15% (3) | BOU(A) 1.2/21% (3) | TOT(H) 1.7/34% (2) | CHE(A) 1.3/18% (4) | COV(H) 1.8/36% (2) | MCI(A) 1.2/12% (5) | IPS(H) 1.9/29% (2) |
| BOU | SUN(H) 1.6/23% (3) | MUN(A) 1.2/15% (4) | LEE(H) 1.6/29% (3) | IPS(A) 1.4/23% (2) | NFO(H) 1.4/28% (3) | FUL(A) 1.4/21% (3) | BHA(H) 1.5/20% (3) | HUL(H) 1.8/37% (2) |
| CRY | BHA(A) 1.2/9% (4) | NEW(H) 1.8/29% (3) | TOT(A) 1.3/22% (3) | LIV(H) 1.4/19% (4) | COV(A) 1.3/24% (2) | HUL(H) 1.7/31% (2) | CHE(A) 1.3/15% (4) | AVL(A) 1.3/21% (3) |
| EVE | CHE(H) 1.6/25% (4) | ARS(A) 0.8/13% (5) | NEW(A) 1.5/24% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/16% (3) | LIV(H) 1.4/22% (4) | AVL(A) 1.4/24% (3) | FUL(H) 1.7/26% (2) |
| ★ NEW | AVL(H) 1.5/26% (3) | CRY(A) 1.3/16% (3) | EVE(H) 1.4/22% (3) | FUL(A) 1.2/14% (3) | ARS(H) 0.9/14% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.3/16% (4) | SUN(H) 1.4/16% (3) |
| NFO | ARS(H) 1.0/24% (4) | IPS(A) 1.5/25% (2) | BRE(A) 1.3/20% (3) | MCI(H) 1.5/21% (4) | BOU(A) 1.3/25% (3) | CHE(H) 1.7/30% (4) | HUL(A) 1.5/31% (2) | BHA(H) 1.7/22% (3) |
| IPS | MCI(A) 1.1/8% (5) | NFO(H) 1.4/21% (3) | HUL(A) 1.4/22% (2) | BOU(H) 1.5/24% (3) | TOT(A) 1.3/21% (3) | AVL(H) 1.7/27% (3) | COV(A) 1.4/22% (2) | LEE(A) 1.2/15% (3) |
| TOT | COV(H) 1.5/34% (2) | CHE(A) 1.1/17% (4) | CRY(H) 1.5/28% (2) | LEE(A) 1.1/18% (3) | IPS(H) 1.6/27% (2) | SUN(A) 1.1/13% (3) | FUL(H) 1.5/25% (2) | ARS(H) 0.8/18% (4) |
| AVL | NEW(A) 1.3/22% (3) | MCI(H) 1.3/16% (4) | FUL(H) 1.5/24% (2) | MUN(A) 1.0/12% (4) | SUN(H) 1.4/19% (3) | IPS(A) 1.3/19% (2) | EVE(H) 1.4/26% (3) | CRY(H) 1.6/27% (2) |
| COV | TOT(A) 1.1/22% (3) | FUL(H) 1.4/24% (2) | SUN(H) 1.3/19% (3) | EVE(A) 1.1/18% (3) | CRY(H) 1.4/26% (2) | LEE(A) 1.0/17% (3) | IPS(H) 1.5/26% (2) | MUN(A) 1.0/12% (4) |
| ★ HUL | FUL(A) 1.1/15% (3) | BRE(H) 1.3/19% (3) | IPS(H) 1.5/24% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.3/15% (3) | CRY(A) 1.2/18% (3) | NFO(H) 1.2/22% (3) | BOU(A) 1.0/17% (3) |
