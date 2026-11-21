# Fixture model v0.2 — GW12–19

**Generated** 2026-11-21 16:59 UTC from mirror `2026-11-21T16:58:52Z`.
**Observed** 11 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. With k=6 pseudo-matches, ratings are **35% prior / 65% data** for the 8 clubs on 11 matches, and **38% / 62%** for the 12 on 10. That weight shifts toward data every week.

League mean xG per team-match **1.47**; home 1.64 / away 1.31 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, BRE, BHA, CHE, COV, CRY, EVE, HUL, LEE, LIV, MUN, NEW on 10.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW12–15, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW11 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG12–15 | CS12–15 | xG12–19 | CS12–19 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.27 *(1.34)* | 0.91 | **7.61** | 1.05 | 15.88 | 2.21 | +6.3 | De Cuyper, Groß |
| MUN | 1.08 *(1.22)* | 1.20 | **7.18** | 0.84 | 12.72 | 1.39 | -4.0 |  |
| ★ AVL | 0.93 *(0.91)* | 1.09 | **6.54** | 1.01 | 11.47 | 1.75 | -0.8 | N.Jackson |
| ★ BOU | 1.19 *(1.29)* | 0.85 | **6.44** | 1.19 | 14.17 | 2.57 | -3.0 | Evanilson |
| ★ MCI | 1.27 *(1.37)* | 0.85 | **6.44** | 1.09 | 14.23 | 2.51 | -0.2 | Haaland |
| LIV | 1.11 *(1.08)* | 0.88 | **6.34** | 1.11 | 13.05 | 2.53 | -1.9 |  |
| ★ NFO | 1.07 *(1.12)* | 0.95 | **6.22** | 1.01 | 13.12 | 2.11 | -9.1 | Gibbs-White |
| ★ CHE | 1.02 *(0.96)* | 0.96 | **6.18** | 0.88 | 13.11 | 2.09 | +4.9 | Rogers |
| SUN | 1.07 *(0.98)* | 0.99 | **6.05** | 0.99 | 13.50 | 2.08 | -7.9 |  |
| ★ ARS | 1.16 *(1.10)* | 0.59 | **6.00** | 1.56 | 14.34 | 3.34 | -1.2 | Raya, Calafiori |
| CRY | 0.92 *(0.93)* | 1.38 | **5.93** | 0.64 | 10.41 | 1.06 | -3.8 |  |
| ★ LEE | 0.95 *(0.91)* | 0.89 | **5.76** | 1.14 | 11.64 | 2.43 | -3.4 | Muharemović |
| ★ BRE | 1.08 *(1.01)* | 0.95 | **5.66** | 0.88 | 13.49 | 2.12 | +1.1 | Schade |
| ★ NEW | 0.86 *(0.78)* | 1.19 | **5.53** | 0.65 | 10.19 | 1.24 | +1.5 | Hall |
| IPS | 0.86 *(0.86)* | 1.27 | **5.43** | 0.81 | 9.84 | 1.32 | +1.1 |  |
| EVE | 0.95 *(0.93)* | 1.03 | **5.42** | 0.85 | 10.55 | 1.63 | -1.8 |  |
| COV | 0.74 *(0.65)* | 1.06 | **4.90** | 0.92 | 8.90 | 1.65 | +0.4 |  |
| FUL | 0.89 *(0.94)* | 1.00 | **4.85** | 0.90 | 9.20 | 1.69 | -4.3 |  |
| ★ TOT | 0.86 *(0.94)* | 0.86 | **4.61** | 1.22 | 9.04 | 2.09 | -3.2 | Kudus |
| ★ HUL | 0.71 *(0.65)* | 1.10 | **4.17** | 0.81 | 7.94 | 1.51 | +1.5 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 | GW19 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | NEW(H) 2.5/36% (3) | BOU(A) 1.4/17% (4) | NFO(A) 1.6/20% (2) | EVE(H) 2.1/32% (3) | IPS(H) 2.6/36% (2) | FUL(A) 1.7/26% (3) | TOT(A) 1.4/28% (3) | MUN(H) 2.5/27% (3) |
| MUN | BRE(H) 1.7/18% (3) | NEW(A) 1.7/18% (3) | COV(H) 1.9/31% (2) | CRY(A) 1.9/16% (2) | ARS(A) 0.8/10% (5) | NFO(H) 1.7/19% (3) | SUN(H) 1.8/19% (2) | BHA(A) 1.3/8% (4) |
| ★ AVL | IPS(A) 1.6/21% (2) | EVE(H) 1.6/26% (3) | CRY(H) 2.1/27% (2) | COV(A) 1.3/27% (2) | CHE(A) 1.2/16% (4) | LEE(H) 1.4/26% (3) | LIV(H) 1.3/20% (4) | BOU(A) 1.0/12% (4) |
| ★ BOU | FUL(A) 1.6/29% (3) | BHA(H) 1.8/24% (4) | HUL(H) 2.2/46% (2) | ARS(A) 0.9/20% (5) | COV(H) 2.1/44% (2) | TOT(A) 1.4/30% (3) | CRY(A) 2.2/28% (2) | AVL(H) 2.1/35% (3) |
| ★ MCI | ARS(A) 1.0/20% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/22% (4) | CHE(H) 2.0/32% (4) | HUL(H) 2.3/46% (2) | NEW(A) 2.0/31% (3) | EVE(A) 1.7/27% (3) | TOT(H) 1.8/38% (3) |
| LIV | EVE(A) 1.5/25% (3) | SUN(H) 1.8/29% (2) | CHE(A) 1.4/23% (4) | LEE(H) 1.6/34% (3) | TOT(H) 1.6/37% (3) | HUL(A) 1.6/36% (2) | AVL(A) 1.6/26% (3) | COV(H) 1.9/43% (2) |
| ★ NFO | CHE(H) 1.7/28% (4) | HUL(A) 1.5/33% (2) | BHA(H) 1.6/21% (4) | SUN(A) 1.4/19% (3) | EVE(H) 1.8/31% (3) | MUN(A) 1.7/19% (3) | NEW(A) 1.7/27% (3) | FUL(H) 1.8/33% (2) |
| ★ CHE | NFO(A) 1.3/18% (2) | CRY(H) 2.3/31% (2) | LIV(H) 1.5/24% (4) | MCI(A) 1.1/13% (5) | AVL(H) 1.8/31% (3) | COV(A) 1.4/31% (2) | IPS(A) 1.7/26% (2) | NEW(H) 2.0/34% (3) |
| SUN | TOT(H) 1.5/33% (3) | LIV(A) 1.2/16% (4) | NEW(A) 1.7/25% (3) | NFO(H) 1.7/25% (3) | CRY(H) 2.4/30% (2) | EVE(A) 1.4/21% (3) | MUN(A) 1.7/17% (3) | HUL(H) 1.9/40% (2) |
| ★ ARS | MCI(H) 1.6/37% (4) | BRE(A) 1.4/35% (4) | TOT(A) 1.3/44% (3) | BOU(H) 1.6/40% (3) | MUN(H) 2.3/43% (3) | CRY(A) 2.1/41% (2) | FUL(A) 1.5/42% (3) | IPS(H) 2.4/51% (2) |
| CRY | HUL(H) 1.7/28% (2) | CHE(A) 1.2/10% (4) | AVL(A) 1.3/12% (3) | MUN(H) 1.8/14% (3) | SUN(A) 1.2/9% (3) | ARS(H) 0.9/12% (4) | BOU(H) 1.3/12% (3) | BRE(A) 1.1/9% (4) |
| ★ LEE | COV(H) 1.7/42% (2) | MCI(A) 1.1/16% (5) | IPS(H) 2.0/37% (2) | LIV(A) 1.1/20% (4) | FUL(H) 1.6/35% (2) | AVL(A) 1.4/26% (3) | HUL(A) 1.4/36% (2) | EVE(H) 1.6/33% (3) |
| ★ BRE | MUN(A) 1.7/19% (3) | ARS(H) 1.0/23% (4) | MCI(H) 1.5/21% (4) | FUL(A) 1.4/25% (3) | NEW(H) 2.1/34% (3) | IPS(A) 1.8/26% (2) | COV(A) 1.5/32% (2) | CRY(H) 2.4/32% (2) |
| ★ NEW | BHA(A) 1.0/8% (4) | MUN(H) 1.7/19% (3) | SUN(H) 1.4/19% (2) | IPS(A) 1.4/19% (2) | BRE(A) 1.1/12% (4) | MCI(H) 1.2/14% (4) | NFO(H) 1.3/19% (3) | CHE(A) 1.1/14% (4) |
| IPS | AVL(H) 1.5/21% (3) | COV(A) 1.2/21% (2) | LEE(A) 1.0/14% (3) | NEW(H) 1.7/24% (3) | BHA(A) 1.0/7% (4) | BRE(H) 1.3/17% (3) | CHE(H) 1.4/18% (4) | ARS(A) 0.7/9% (5) |
| EVE | LIV(H) 1.4/22% (4) | AVL(A) 1.4/21% (3) | FUL(H) 1.6/30% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.2/17% (2) | SUN(H) 1.5/24% (2) | MCI(H) 1.3/18% (4) | LEE(A) 1.1/20% (3) |
| COV | LEE(A) 0.9/19% (3) | IPS(H) 1.5/30% (2) | MUN(A) 1.2/15% (3) | AVL(H) 1.3/27% (3) | BOU(A) 0.8/12% (4) | CHE(H) 1.2/24% (4) | BRE(H) 1.2/22% (3) | LIV(A) 0.9/14% (4) |
| FUL | BOU(H) 1.2/21% (3) | TOT(A) 1.0/24% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/24% (3) | LEE(A) 1.0/21% (3) | BHA(H) 1.3/19% (4) | ARS(H) 0.9/22% (4) | NFO(A) 1.1/17% (2) |
| ★ TOT | SUN(A) 1.1/22% (3) | FUL(H) 1.4/36% (2) | ARS(H) 0.8/27% (4) | HUL(A) 1.2/37% (2) | LIV(A) 1.0/21% (4) | BOU(H) 1.2/26% (3) | BHA(H) 1.3/24% (4) | MCI(A) 1.0/17% (5) |
| ★ HUL | CRY(A) 1.3/19% (2) | NFO(H) 1.1/21% (3) | BOU(A) 0.8/12% (4) | TOT(H) 1.0/29% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/20% (4) | LEE(H) 1.0/25% (3) | SUN(A) 0.9/15% (3) |
