# Fixture model v0.2 — GW10–17

**Generated** 2026-11-06 11:33 UTC from mirror `2026-11-06T11:32:43Z`.
**Observed** 9 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9]. With k=6 pseudo-matches, ratings are **40% prior / 60% data** for all 20 clubs on 9 matches. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.62 / away 1.30 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW10–13, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW9 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG10–13 | CS10–13 | xG10–17 | CS10–17 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.27 *(1.34)* | 0.96 | **7.76** | 1.08 | 15.57 | 2.13 | +6.4 | Groß, De Cuyper |
| ★ ARS | 1.20 *(1.14)* | 0.61 | **7.36** | 1.69 | 14.53 | 3.40 | -0.9 | Raya, Calafiori |
| LIV | 1.09 *(1.01)* | 0.82 | **7.16** | 1.25 | 13.24 | 2.65 | -2.2 |  |
| ★ BOU | 1.14 *(1.21)* | 0.80 | **6.79** | 1.20 | 13.06 | 2.68 | -1.8 | Evanilson |
| ★ MCI | 1.29 *(1.42)* | 0.89 | **6.59** | 1.08 | 14.62 | 2.30 | +1.4 | Haaland |
| ★ CHE | 1.06 *(1.03)* | 0.94 | **6.59** | 1.08 | 12.56 | 2.17 | +5.5 | Rogers |
| MUN | 1.03 *(1.10)* | 1.12 | **6.15** | 0.82 | 12.05 | 1.71 | -4.4 |  |
| ★ BRE | 1.12 *(1.09)* | 0.96 | **5.99** | 0.87 | 13.16 | 1.89 | +1.7 | Schade |
| SUN | 1.09 *(1.01)* | 1.05 | **5.85** | 0.92 | 13.02 | 1.90 | -6.3 |  |
| ★ NFO | 1.05 *(1.14)* | 0.92 | **5.73** | 1.02 | 12.04 | 1.98 | -8.9 | Gibbs-White |
| ★ AVL | 0.89 *(0.83)* | 1.08 | **5.68** | 0.85 | 11.23 | 1.87 | -0.9 | N.Jackson |
| EVE | 0.96 *(0.94)* | 1.02 | **5.50** | 1.01 | 11.08 | 1.83 | -3.3 |  |
| FUL | 0.96 *(1.06)* | 1.02 | **5.39** | 0.90 | 10.78 | 1.73 | -4.9 |  |
| TOT | 0.86 *(0.89)* | 0.88 | **5.31** | 1.18 | 9.44 | 2.28 | -1.7 |  |
| ★ LEE | 0.92 *(0.87)* | 0.91 | **5.05** | 1.14 | 10.63 | 2.28 | -2.5 | Muharemović |
| IPS | 0.90 *(0.94)* | 1.22 | **5.01** | 0.83 | 10.43 | 1.50 | +1.7 |  |
| CRY | 0.86 *(0.85)* | 1.34 | **4.93** | 0.74 | 9.69 | 1.27 | -2.2 |  |
| COV | 0.72 *(0.64)* | 1.07 | **4.80** | 0.98 | 8.95 | 1.81 | +0.6 |  |
| ★ NEW | 0.86 *(0.79)* | 1.26 | **4.63** | 0.55 | 9.78 | 1.10 | +1.6 | Hall, Barnes |
| ★ HUL | 0.73 *(0.70)* | 1.14 | **4.06** | 0.69 | 7.67 | 1.39 | +1.8 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | BRE(H) 2.0/25% (3) | HUL(A) 1.9/32% (2) | NEW(H) 2.6/34% (3) | BOU(A) 1.3/17% (4) | NFO(A) 1.5/20% (2) | EVE(H) 2.1/30% (3) | IPS(H) 2.5/33% (2) | FUL(A) 1.7/23% (3) |
| ★ ARS | HUL(H) 2.2/56% (2) | NEW(A) 2.0/43% (3) | MCI(H) 1.7/36% (4) | BRE(A) 1.5/33% (4) | TOT(A) 1.4/43% (3) | BOU(H) 1.6/41% (3) | MUN(H) 2.2/45% (3) | CRY(A) 2.1/43% (2) |
| LIV | CRY(A) 1.9/32% (2) | MUN(H) 2.0/34% (3) | EVE(A) 1.4/28% (3) | SUN(H) 1.9/32% (2) | CHE(A) 1.3/24% (4) | LEE(H) 1.6/38% (3) | TOT(H) 1.5/40% (3) | HUL(A) 1.6/38% (2) |
| ★ BOU | IPS(A) 1.8/31% (2) | NFO(H) 1.7/34% (3) | FUL(A) 1.5/29% (3) | BHA(H) 1.8/27% (4) | HUL(H) 2.1/47% (2) | ARS(A) 0.9/21% (5) | COV(H) 2.0/47% (2) | TOT(A) 1.3/33% (3) |
| ★ MCI | NFO(A) 1.5/22% (2) | FUL(H) 2.1/33% (2) | ARS(A) 1.0/18% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/20% (4) | CHE(H) 2.0/30% (4) | HUL(H) 2.4/43% (2) | NEW(A) 2.1/29% (3) |
| ★ CHE | SUN(A) 1.4/19% (3) | LEE(H) 1.6/33% (3) | NFO(A) 1.3/20% (2) | CRY(H) 2.3/35% (2) | LIV(H) 1.4/27% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.9/34% (3) | COV(A) 1.5/34% (2) |
| MUN | AVL(H) 1.8/28% (3) | LIV(A) 1.1/14% (4) | BRE(H) 1.6/20% (3) | NEW(A) 1.7/21% (3) | COV(H) 1.8/35% (2) | CRY(A) 1.8/21% (2) | ARS(A) 0.8/11% (5) | NFO(H) 1.5/22% (3) |
| ★ BRE | BHA(A) 1.4/14% (4) | EVE(H) 1.9/30% (3) | MUN(A) 1.6/20% (3) | ARS(H) 1.1/23% (4) | MCI(H) 1.6/20% (4) | FUL(A) 1.5/23% (3) | NEW(H) 2.3/34% (3) | IPS(A) 1.8/25% (2) |
| SUN | CHE(H) 1.6/24% (4) | AVL(A) 1.5/22% (3) | TOT(H) 1.5/31% (3) | LIV(A) 1.2/16% (4) | NEW(A) 1.8/23% (3) | NFO(H) 1.6/24% (3) | CRY(H) 2.4/31% (2) | EVE(A) 1.4/19% (3) |
| ★ NFO | MCI(H) 1.5/22% (4) | BOU(A) 1.1/18% (4) | CHE(H) 1.6/28% (4) | HUL(A) 1.5/34% (2) | BHA(H) 1.6/22% (4) | SUN(A) 1.4/20% (3) | EVE(H) 1.7/32% (3) | MUN(A) 1.5/22% (3) |
| ★ AVL | MUN(A) 1.3/17% (3) | SUN(H) 1.5/22% (2) | IPS(A) 1.4/21% (2) | EVE(H) 1.5/26% (3) | CRY(H) 1.9/30% (2) | COV(A) 1.2/28% (2) | CHE(A) 1.1/16% (4) | LEE(H) 1.3/28% (3) |
| EVE | COV(H) 1.7/39% (2) | BRE(A) 1.2/16% (4) | LIV(H) 1.3/24% (4) | AVL(A) 1.3/23% (3) | FUL(H) 1.6/28% (2) | BHA(A) 1.2/12% (4) | NFO(A) 1.1/18% (2) | SUN(H) 1.6/24% (2) |
| FUL | NEW(H) 2.0/32% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.2/22% (3) | TOT(A) 1.1/24% (3) | EVE(A) 1.3/20% (3) | BRE(H) 1.5/23% (3) | LEE(A) 1.1/22% (3) | BHA(H) 1.5/19% (4) |
| TOT | LEE(A) 1.0/27% (3) | IPS(H) 1.7/36% (2) | SUN(A) 1.2/21% (3) | FUL(H) 1.4/34% (2) | ARS(H) 0.8/26% (4) | HUL(A) 1.3/36% (2) | LIV(A) 0.9/21% (4) | BOU(H) 1.1/27% (3) |
| ★ LEE | TOT(H) 1.3/36% (3) | CHE(A) 1.1/21% (4) | COV(H) 1.6/43% (2) | MCI(A) 1.1/15% (5) | IPS(H) 1.8/34% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.5/32% (2) | AVL(A) 1.3/27% (3) |
| IPS | BOU(H) 1.2/16% (3) | TOT(A) 1.0/18% (3) | AVL(H) 1.6/25% (3) | COV(A) 1.2/24% (2) | LEE(A) 1.1/16% (3) | NEW(H) 1.8/26% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/17% (3) |
| CRY | LIV(H) 1.1/15% (4) | COV(A) 1.2/21% (2) | HUL(H) 1.6/28% (2) | CHE(A) 1.0/10% (4) | AVL(A) 1.2/14% (3) | MUN(H) 1.6/17% (3) | SUN(A) 1.2/9% (3) | ARS(H) 0.8/12% (4) |
| COV | EVE(A) 1.0/19% (3) | CRY(H) 1.6/31% (2) | LEE(A) 0.9/20% (3) | IPS(H) 1.4/29% (2) | MUN(A) 1.0/17% (3) | AVL(H) 1.3/29% (3) | BOU(A) 0.7/14% (4) | CHE(H) 1.1/23% (4) |
| ★ NEW | FUL(A) 1.1/14% (3) | ARS(H) 0.8/14% (4) | BHA(A) 1.1/7% (4) | MUN(H) 1.6/19% (3) | SUN(H) 1.5/17% (2) | IPS(A) 1.4/16% (2) | BRE(A) 1.1/10% (4) | MCI(H) 1.2/12% (4) |
| ★ HUL | ARS(A) 0.6/11% (5) | BHA(H) 1.1/15% (4) | CRY(A) 1.3/21% (2) | NFO(H) 1.1/21% (3) | BOU(A) 0.8/12% (4) | TOT(H) 1.0/28% (3) | MCI(A) 0.8/9% (5) | LIV(H) 1.0/20% (4) |
