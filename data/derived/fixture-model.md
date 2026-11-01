# Fixture model v0.2 — GW10–17

**Generated** 2026-11-01 18:25 UTC from mirror `2026-11-01T18:24:21Z`.
**Observed** 9 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9]. With k=6 pseudo-matches, ratings are **40% prior / 60% data** for the 16 clubs on 9 matches, and **43% / 57%** for the 4 on 8. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.62 / away 1.30 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, EVE, LIV, NEW on 8.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW10–13, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW9 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG10–13 | CS10–13 | xG10–17 | CS10–17 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.27 *(1.34)* | 0.96 | **7.90** | 1.12 | 15.60 | 2.17 | +6.4 | Groß, De Cuyper |
| ★ ARS | 1.22 *(1.19)* | 0.61 | **7.54** | 1.70 | 14.81 | 3.37 | -0.9 | Raya, Calafiori |
| LIV | 1.09 *(1.05)* | 0.84 | **7.03** | 1.20 | 13.15 | 2.57 | -1.2 |  |
| MUN | 1.08 *(1.10)* | 1.08 | **6.52** | 0.89 | 12.54 | 1.79 | -4.4 |  |
| ★ MCI | 1.28 *(1.42)* | 0.89 | **6.46** | 1.06 | 14.52 | 2.29 | +1.4 | Haaland |
| ★ CHE | 1.06 *(1.03)* | 0.95 | **6.42** | 1.03 | 12.40 | 2.10 | +5.5 | Rogers |
| ★ BOU | 1.08 *(1.21)* | 0.87 | **6.32** | 1.07 | 12.32 | 2.43 | -1.8 | Evanilson |
| ★ NFO | 1.10 *(1.14)* | 0.86 | **6.13** | 1.13 | 12.71 | 2.18 | -8.9 | Gibbs-White |
| SUN | 1.08 *(1.01)* | 1.07 | **5.88** | 0.90 | 12.75 | 1.83 | -6.3 |  |
| ★ AVL | 0.89 *(0.83)* | 1.08 | **5.63** | 0.85 | 11.11 | 1.85 | -0.9 | N.Jackson |
| ★ BRE | 1.06 *(1.09)* | 1.02 | **5.61** | 0.79 | 12.28 | 1.71 | +1.7 | Schade |
| FUL | 0.96 *(1.06)* | 1.02 | **5.46** | 0.92 | 10.98 | 1.80 | -4.9 |  |
| TOT | 0.87 *(0.89)* | 0.89 | **5.37** | 1.16 | 9.69 | 2.26 | -1.7 |  |
| CRY | 0.92 *(0.85)* | 1.29 | **5.34** | 0.79 | 10.39 | 1.35 | -2.2 |  |
| EVE | 0.92 *(0.85)* | 1.02 | **5.34** | 1.02 | 10.59 | 1.82 | -1.9 |  |
| IPS | 0.91 *(0.93)* | 1.22 | **5.16** | 0.85 | 10.63 | 1.54 | +1.7 |  |
| ★ LEE | 0.91 *(0.87)* | 0.92 | **5.08** | 1.14 | 10.66 | 2.26 | -2.5 | Muharemović |
| COV | 0.72 *(0.64)* | 1.07 | **4.75** | 0.97 | 8.95 | 1.80 | +0.6 |  |
| ★ NEW | 0.86 *(0.78)* | 1.21 | **4.58** | 0.57 | 9.82 | 1.18 | +2.9 | Hall, Barnes |
| ★ HUL | 0.73 *(0.70)* | 1.15 | **3.94** | 0.63 | 7.64 | 1.34 | +1.8 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | BRE(H) 2.1/27% (3) | HUL(A) 1.9/32% (2) | NEW(H) 2.5/34% (3) | BOU(A) 1.4/19% (3) | NFO(A) 1.4/18% (3) | EVE(H) 2.1/32% (3) | IPS(H) 2.5/32% (2) | FUL(A) 1.7/22% (3) |
| ★ ARS | HUL(H) 2.3/56% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/36% (4) | BRE(A) 1.6/35% (3) | TOT(A) 1.4/42% (3) | BOU(H) 1.7/42% (3) | MUN(H) 2.1/43% (4) | CRY(A) 2.0/40% (3) |
| LIV | CRY(A) 1.8/29% (3) | MUN(H) 1.9/31% (4) | EVE(A) 1.4/29% (3) | SUN(H) 1.9/31% (3) | CHE(A) 1.3/24% (4) | LEE(H) 1.6/37% (3) | TOT(H) 1.6/39% (2) | HUL(A) 1.6/37% (2) |
| MUN | AVL(H) 1.9/29% (3) | LIV(A) 1.2/15% (4) | BRE(H) 1.8/23% (3) | NEW(A) 1.7/22% (3) | COV(H) 1.9/36% (2) | CRY(A) 1.8/20% (3) | ARS(A) 0.9/12% (5) | NFO(H) 1.5/22% (3) |
| ★ MCI | NFO(A) 1.4/21% (3) | FUL(H) 2.1/33% (2) | ARS(A) 1.0/17% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.7/22% (3) | CHE(H) 2.0/30% (4) | HUL(H) 2.4/43% (2) | NEW(A) 2.0/29% (3) |
| ★ CHE | SUN(A) 1.5/19% (3) | LEE(H) 1.6/33% (3) | NFO(A) 1.2/19% (3) | CRY(H) 2.2/33% (2) | LIV(H) 1.4/26% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.9/34% (3) | COV(A) 1.5/33% (2) |
| ★ BOU | IPS(A) 1.7/28% (2) | NFO(H) 1.5/29% (3) | FUL(A) 1.4/26% (3) | BHA(H) 1.7/24% (3) | HUL(H) 2.0/44% (2) | ARS(A) 0.9/18% (5) | COV(H) 1.9/44% (2) | TOT(A) 1.2/30% (3) |
| ★ NFO | MCI(H) 1.6/24% (4) | BOU(A) 1.2/22% (3) | CHE(H) 1.7/31% (4) | HUL(A) 1.6/36% (2) | BHA(H) 1.7/24% (3) | SUN(A) 1.5/22% (3) | EVE(H) 1.8/36% (3) | MUN(A) 1.5/22% (4) |
| SUN | CHE(H) 1.6/23% (4) | AVL(A) 1.5/22% (3) | TOT(H) 1.5/30% (2) | LIV(A) 1.2/15% (4) | NEW(A) 1.7/22% (3) | NFO(H) 1.5/22% (3) | CRY(H) 2.2/28% (2) | EVE(A) 1.4/21% (3) |
| ★ AVL | MUN(A) 1.2/15% (4) | SUN(H) 1.5/22% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/28% (3) | CRY(H) 1.8/28% (2) | COV(A) 1.2/28% (2) | CHE(A) 1.1/16% (4) | LEE(H) 1.3/28% (3) |
| ★ BRE | BHA(A) 1.3/12% (4) | EVE(H) 1.8/30% (3) | MUN(A) 1.5/17% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.5/18% (4) | FUL(A) 1.4/20% (3) | NEW(H) 2.1/32% (3) | IPS(A) 1.7/22% (2) |
| FUL | NEW(H) 1.9/32% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.4/24% (3) | TOT(A) 1.1/24% (3) | EVE(A) 1.3/22% (3) | BRE(H) 1.6/25% (3) | LEE(A) 1.1/22% (3) | BHA(H) 1.5/19% (3) |
| TOT | LEE(A) 1.0/27% (3) | IPS(H) 1.7/35% (2) | SUN(A) 1.2/21% (3) | FUL(H) 1.4/33% (2) | ARS(H) 0.9/25% (4) | HUL(A) 1.3/35% (2) | LIV(A) 0.9/21% (4) | BOU(H) 1.2/29% (3) |
| CRY | LIV(H) 1.2/16% (4) | COV(A) 1.3/22% (2) | HUL(H) 1.7/30% (2) | CHE(A) 1.1/11% (4) | AVL(A) 1.3/16% (3) | MUN(H) 1.6/17% (4) | SUN(A) 1.3/11% (3) | ARS(H) 0.9/13% (4) |
| EVE | COV(H) 1.6/38% (2) | BRE(A) 1.2/17% (3) | LIV(H) 1.2/24% (4) | AVL(A) 1.3/23% (3) | FUL(H) 1.5/28% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.0/16% (3) | SUN(H) 1.6/24% (3) |
| IPS | BOU(H) 1.3/18% (3) | TOT(A) 1.0/18% (3) | AVL(H) 1.6/25% (3) | COV(A) 1.3/24% (2) | LEE(A) 1.1/17% (3) | NEW(H) 1.8/26% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.5/19% (3) |
| ★ LEE | TOT(H) 1.3/36% (2) | CHE(A) 1.1/21% (4) | COV(H) 1.6/42% (2) | MCI(A) 1.1/15% (5) | IPS(H) 1.8/34% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.5/32% (2) | AVL(A) 1.3/27% (3) |
| COV | EVE(A) 1.0/20% (3) | CRY(H) 1.5/28% (2) | LEE(A) 0.9/20% (3) | IPS(H) 1.4/28% (2) | MUN(A) 1.0/15% (4) | AVL(H) 1.3/29% (3) | BOU(A) 0.8/15% (3) | CHE(H) 1.1/23% (4) |
| ★ NEW | FUL(A) 1.1/15% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.5/18% (4) | SUN(H) 1.5/18% (3) | IPS(A) 1.4/17% (2) | BRE(A) 1.1/13% (3) | MCI(H) 1.2/13% (4) |
| ★ HUL | ARS(A) 0.6/10% (5) | BHA(H) 1.1/15% (3) | CRY(A) 1.2/18% (3) | NFO(H) 1.0/20% (3) | BOU(A) 0.8/13% (3) | TOT(H) 1.0/28% (2) | MCI(A) 0.8/9% (5) | LIV(H) 1.0/20% (4) |
