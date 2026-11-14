# Fixture model v0.2 — GW11–18

**Generated** 2026-11-14 07:35 UTC from mirror `2026-11-14T07:35:06Z`.
**Observed** 10 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. With k=6 pseudo-matches, ratings are **38% prior / 62% data** for all 20 clubs on 10 matches. That weight shifts toward data every week.

League mean xG per team-match **1.47**; home 1.64 / away 1.31 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW11–14, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW10 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG11–14 | CS11–14 | xG11–18 | CS11–18 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.26 *(1.34)* | 0.91 | **7.09** | 1.11 | 14.90 | 2.32 | +6.3 | De Cuyper, Groß |
| ★ BOU | 1.15 *(1.23)* | 0.80 | **7.01** | 1.40 | 13.35 | 2.72 | -2.1 | Evanilson |
| LIV | 1.12 *(1.08)* | 0.88 | **7.00** | 1.04 | 13.60 | 2.36 | -1.9 |  |
| ★ AVL | 0.95 *(0.94)* | 1.15 | **6.89** | 0.85 | 12.21 | 1.67 | +0.2 | N.Jackson |
| ★ MCI | 1.29 *(1.38)* | 0.85 | **6.58** | 1.14 | 14.66 | 2.48 | +0.6 | Haaland |
| ★ CHE | 1.02 *(0.96)* | 0.96 | **6.53** | 1.06 | 12.68 | 2.05 | +4.9 | Rogers |
| MUN | 1.08 *(1.22)* | 1.20 | **6.47** | 0.79 | 12.65 | 1.44 | -4.0 |  |
| SUN | 1.12 *(1.06)* | 1.01 | **6.39** | 0.93 | 13.88 | 1.86 | -7.7 |  |
| ★ ARS | 1.16 *(1.10)* | 0.59 | **6.23** | 1.62 | 13.66 | 3.30 | -1.2 | Raya, Calafiori |
| ★ BRE | 1.07 *(1.01)* | 0.95 | **6.01** | 0.93 | 12.71 | 2.09 | +1.1 | Schade |
| ★ LEE | 0.95 *(0.91)* | 0.89 | **5.81** | 1.14 | 11.25 | 2.28 | -3.4 | Muharemović |
| ★ NFO | 1.01 *(1.08)* | 0.91 | **5.60** | 1.04 | 11.78 | 2.03 | -7.0 | Gibbs-White |
| EVE | 0.95 *(0.93)* | 1.03 | **5.58** | 0.88 | 10.77 | 1.58 | -1.8 |  |
| CRY | 0.92 *(0.93)* | 1.38 | **5.48** | 0.68 | 10.60 | 1.14 | -3.8 |  |
| COV | 0.74 *(0.65)* | 1.06 | **5.20** | 0.91 | 9.69 | 1.77 | +0.4 |  |
| IPS | 0.90 *(0.92)* | 1.23 | **5.05** | 0.78 | 10.67 | 1.48 | +1.5 |  |
| ★ NEW | 0.85 *(0.78)* | 1.19 | **4.94** | 0.61 | 9.84 | 1.26 | +1.5 | Hall, Barnes |
| TOT | 0.83 *(0.84)* | 0.90 | **4.94** | 1.14 | 9.42 | 2.17 | -2.4 |  |
| FUL | 0.90 *(0.99)* | 1.00 | **4.47** | 0.81 | 9.15 | 1.68 | -4.6 |  |
| ★ HUL | 0.71 *(0.65)* | 1.10 | **4.14** | 0.72 | 8.04 | 1.57 | +1.5 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | HUL(A) 1.8/35% (2) | NEW(H) 2.5/36% (3) | BOU(A) 1.3/18% (4) | NFO(A) 1.5/22% (2) | EVE(H) 2.1/32% (3) | IPS(H) 2.5/34% (2) | FUL(A) 1.7/26% (3) | TOT(A) 1.5/29% (3) |
| ★ BOU | NFO(H) 1.7/35% (3) | FUL(A) 1.5/31% (3) | BHA(H) 1.7/27% (4) | HUL(H) 2.1/48% (2) | ARS(A) 0.9/22% (5) | COV(H) 2.0/46% (2) | TOT(A) 1.4/34% (3) | CRY(A) 2.1/30% (2) |
| LIV | MUN(H) 2.2/29% (3) | EVE(A) 1.5/25% (3) | SUN(H) 1.9/27% (2) | CHE(A) 1.4/23% (4) | LEE(H) 1.6/33% (3) | TOT(H) 1.6/38% (3) | HUL(A) 1.6/36% (2) | AVL(A) 1.7/25% (3) |
| ★ AVL | SUN(H) 1.6/18% (2) | IPS(A) 1.5/18% (2) | EVE(H) 1.6/24% (3) | CRY(H) 2.2/25% (2) | COV(A) 1.3/25% (2) | CHE(A) 1.2/14% (4) | LEE(H) 1.4/24% (3) | LIV(H) 1.4/18% (4) |
| ★ MCI | FUL(H) 2.1/37% (2) | ARS(A) 1.0/20% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/22% (4) | CHE(H) 2.0/32% (4) | HUL(H) 2.3/45% (2) | NEW(A) 2.0/30% (3) | EVE(A) 1.7/26% (3) |
| ★ CHE | LEE(H) 1.5/30% (3) | NFO(A) 1.2/20% (2) | CRY(H) 2.3/31% (2) | LIV(H) 1.5/24% (4) | MCI(A) 1.1/13% (5) | AVL(H) 1.9/30% (3) | COV(A) 1.4/31% (2) | IPS(A) 1.6/24% (2) |
| MUN | LIV(A) 1.2/11% (4) | BRE(H) 1.7/19% (3) | NEW(A) 1.7/19% (3) | COV(H) 1.9/31% (2) | CRY(A) 2.0/16% (2) | ARS(A) 0.8/10% (5) | NFO(H) 1.6/20% (3) | SUN(H) 1.8/17% (2) |
| SUN | AVL(A) 1.7/20% (3) | TOT(H) 1.6/33% (3) | LIV(A) 1.3/16% (4) | NEW(A) 1.7/24% (3) | NFO(H) 1.7/26% (3) | CRY(H) 2.5/29% (2) | EVE(A) 1.5/20% (3) | MUN(A) 1.8/17% (3) |
| ★ ARS | NEW(A) 1.8/44% (3) | MCI(H) 1.6/37% (4) | BRE(A) 1.4/36% (4) | TOT(A) 1.4/45% (3) | BOU(H) 1.5/41% (3) | MUN(H) 2.3/44% (3) | CRY(A) 2.1/41% (2) | FUL(A) 1.5/42% (3) |
| ★ BRE | EVE(H) 1.8/31% (3) | MUN(A) 1.7/19% (3) | ARS(H) 1.0/24% (4) | MCI(H) 1.5/20% (4) | FUL(A) 1.4/25% (3) | NEW(H) 2.1/35% (3) | IPS(A) 1.7/25% (2) | COV(A) 1.5/32% (2) |
| ★ LEE | CHE(A) 1.2/22% (4) | COV(H) 1.6/42% (2) | MCI(A) 1.1/15% (5) | IPS(H) 1.9/35% (2) | LIV(A) 1.1/19% (4) | FUL(H) 1.6/35% (2) | AVL(A) 1.4/25% (3) | HUL(A) 1.4/35% (2) |
| ★ NFO | BOU(A) 1.1/18% (4) | CHE(H) 1.6/29% (4) | HUL(A) 1.4/35% (2) | BHA(H) 1.5/22% (4) | SUN(A) 1.3/19% (3) | EVE(H) 1.7/32% (3) | MUN(A) 1.6/20% (3) | NEW(A) 1.6/28% (3) |
| EVE | BRE(A) 1.2/16% (4) | LIV(H) 1.4/22% (4) | AVL(A) 1.4/20% (3) | FUL(H) 1.6/30% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.1/18% (2) | SUN(H) 1.6/22% (2) | MCI(H) 1.3/18% (4) |
| CRY | COV(A) 1.3/19% (2) | HUL(H) 1.7/28% (2) | CHE(A) 1.2/10% (4) | AVL(A) 1.4/12% (3) | MUN(H) 1.8/14% (3) | SUN(A) 1.2/8% (3) | ARS(H) 0.9/12% (4) | BOU(H) 1.2/12% (3) |
| COV | CRY(H) 1.7/28% (2) | LEE(A) 0.9/19% (3) | IPS(H) 1.5/29% (2) | MUN(A) 1.2/15% (3) | AVL(H) 1.4/26% (3) | BOU(A) 0.8/13% (4) | CHE(H) 1.2/24% (4) | BRE(H) 1.1/22% (3) |
| IPS | TOT(A) 1.1/19% (3) | AVL(H) 1.7/21% (3) | COV(A) 1.3/23% (2) | LEE(A) 1.1/15% (3) | NEW(H) 1.7/25% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/18% (3) | CHE(H) 1.4/19% (4) |
| ★ NEW | ARS(H) 0.8/16% (4) | BHA(A) 1.0/9% (4) | MUN(H) 1.7/19% (3) | SUN(H) 1.4/18% (2) | IPS(A) 1.4/18% (2) | BRE(A) 1.1/12% (4) | MCI(H) 1.2/14% (4) | NFO(H) 1.3/21% (3) |
| TOT | IPS(H) 1.7/35% (2) | SUN(A) 1.1/19% (3) | FUL(H) 1.4/35% (2) | ARS(H) 0.8/26% (4) | HUL(A) 1.2/35% (2) | LIV(A) 1.0/19% (4) | BOU(H) 1.1/26% (3) | BHA(H) 1.2/23% (4) |
| FUL | MCI(A) 1.0/12% (5) | BOU(H) 1.2/22% (3) | TOT(A) 1.1/26% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/25% (3) | LEE(A) 1.1/21% (3) | BHA(H) 1.3/19% (4) | ARS(H) 0.9/22% (4) |
| ★ HUL | BHA(H) 1.1/16% (4) | CRY(A) 1.3/19% (2) | NFO(H) 1.1/24% (3) | BOU(A) 0.7/13% (4) | TOT(H) 1.0/30% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/20% (4) | LEE(H) 1.0/26% (3) |
