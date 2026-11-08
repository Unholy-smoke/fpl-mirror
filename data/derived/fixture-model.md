# Fixture model v0.2 — GW11–18

**Generated** 2026-11-08 16:23 UTC from mirror `2026-11-08T16:22:56Z`.
**Observed** 10 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. With k=6 pseudo-matches, ratings are **38% prior / 62% data** for the 18 clubs on 10 matches, and **40% / 60%** for the 2 on 9. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.62 / away 1.29 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: AVL, MUN on 9.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW11–14, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW10 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG11–14 | CS11–14 | xG11–18 | CS11–18 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.36)* | 0.92 | **7.17** | 1.10 | 15.05 | 2.29 | +6.2 | De Cuyper, Groß |
| ★ BOU | 1.16 *(1.24)* | 0.80 | **7.05** | 1.39 | 13.37 | 2.72 | -2.0 | Evanilson |
| LIV | 1.12 *(1.09)* | 0.88 | **6.81** | 1.08 | 13.30 | 2.44 | -1.9 |  |
| ★ MCI | 1.30 *(1.40)* | 0.86 | **6.63** | 1.13 | 14.77 | 2.47 | +0.6 | Haaland |
| ★ CHE | 1.03 *(0.96)* | 0.98 | **6.47** | 1.06 | 12.48 | 2.06 | +5.0 | Rogers |
| ★ AVL | 0.89 *(0.83)* | 1.10 | **6.40** | 0.93 | 11.33 | 1.83 | -0.9 | N.Jackson |
| SUN | 1.13 *(1.09)* | 1.01 | **6.30** | 0.97 | 13.67 | 1.93 | -7.9 |  |
| ★ ARS | 1.17 *(1.11)* | 0.59 | **6.25** | 1.62 | 13.52 | 3.32 | -1.2 | Raya, Calafiori |
| MUN | 1.02 *(1.10)* | 1.13 | **6.11** | 0.88 | 11.93 | 1.61 | -4.4 |  |
| ★ BRE | 1.08 *(1.04)* | 0.96 | **5.94** | 0.94 | 12.70 | 2.08 | +0.9 | Schade |
| ★ LEE | 0.95 *(0.92)* | 0.90 | **5.80** | 1.15 | 11.17 | 2.31 | -3.4 | Muharemović |
| ★ NFO | 1.02 *(1.10)* | 0.92 | **5.65** | 1.04 | 11.75 | 2.05 | -7.0 | Gibbs-White |
| EVE | 0.96 *(0.95)* | 1.03 | **5.49** | 0.90 | 10.68 | 1.60 | -1.8 |  |
| CRY | 0.91 *(0.93)* | 1.39 | **5.34** | 0.70 | 10.25 | 1.19 | -3.6 |  |
| COV | 0.74 *(0.66)* | 1.07 | **5.09** | 0.94 | 9.49 | 1.83 | +0.4 |  |
| TOT | 0.84 *(0.85)* | 0.91 | **4.97** | 1.13 | 9.48 | 2.16 | -2.4 |  |
| IPS | 0.91 *(0.93)* | 1.24 | **4.97** | 0.80 | 10.64 | 1.50 | +1.5 |  |
| ★ NEW | 0.86 *(0.79)* | 1.20 | **4.82** | 0.63 | 9.73 | 1.26 | +1.5 | Hall, Barnes |
| FUL | 0.92 *(1.00)* | 1.01 | **4.51** | 0.80 | 9.24 | 1.65 | -4.6 |  |
| ★ HUL | 0.71 *(0.66)* | 1.11 | **4.15** | 0.71 | 8.04 | 1.56 | +1.5 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | HUL(A) 1.8/34% (2) | NEW(H) 2.5/36% (3) | BOU(A) 1.3/18% (4) | NFO(A) 1.5/22% (2) | EVE(H) 2.1/32% (3) | IPS(H) 2.6/34% (2) | FUL(A) 1.7/25% (3) | TOT(A) 1.5/28% (3) |
| ★ BOU | NFO(H) 1.7/35% (3) | FUL(A) 1.5/30% (3) | BHA(H) 1.7/26% (4) | HUL(H) 2.1/48% (2) | ARS(A) 0.9/22% (5) | COV(H) 2.0/46% (2) | TOT(A) 1.4/34% (3) | CRY(A) 2.1/31% (2) |
| LIV | MUN(H) 2.1/31% (3) | EVE(A) 1.5/26% (3) | SUN(H) 1.8/28% (2) | CHE(A) 1.4/23% (4) | LEE(H) 1.6/34% (3) | TOT(H) 1.6/38% (3) | HUL(A) 1.6/36% (2) | AVL(A) 1.6/28% (3) |
| ★ MCI | FUL(H) 2.1/36% (2) | ARS(A) 1.0/20% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/22% (4) | CHE(H) 2.0/32% (4) | HUL(H) 2.3/45% (2) | NEW(A) 2.0/30% (3) | EVE(A) 1.7/26% (3) |
| ★ CHE | LEE(H) 1.5/30% (3) | NFO(A) 1.2/20% (2) | CRY(H) 2.3/32% (2) | LIV(H) 1.5/24% (4) | MCI(A) 1.1/13% (5) | AVL(H) 1.8/32% (3) | COV(A) 1.4/31% (2) | IPS(A) 1.6/24% (2) |
| ★ AVL | SUN(H) 1.5/20% (2) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/26% (3) | CRY(H) 2.0/27% (2) | COV(A) 1.2/27% (2) | CHE(A) 1.1/16% (4) | LEE(H) 1.3/26% (3) | LIV(H) 1.3/20% (4) |
| SUN | AVL(A) 1.6/23% (3) | TOT(H) 1.7/33% (3) | LIV(A) 1.3/16% (4) | NEW(A) 1.8/25% (3) | NFO(H) 1.7/26% (3) | CRY(H) 2.5/30% (2) | EVE(A) 1.5/21% (3) | MUN(A) 1.7/19% (3) |
| ★ ARS | NEW(A) 1.8/44% (3) | MCI(H) 1.6/37% (4) | BRE(A) 1.5/36% (4) | TOT(A) 1.4/45% (3) | BOU(H) 1.5/41% (3) | MUN(H) 2.1/46% (3) | CRY(A) 2.1/42% (2) | FUL(A) 1.5/42% (3) |
| MUN | LIV(A) 1.2/13% (4) | BRE(H) 1.6/21% (3) | NEW(A) 1.6/21% (3) | COV(H) 1.8/34% (2) | CRY(A) 1.8/19% (2) | ARS(A) 0.8/12% (5) | NFO(H) 1.5/23% (3) | SUN(H) 1.7/19% (2) |
| ★ BRE | EVE(H) 1.8/30% (3) | MUN(A) 1.6/20% (3) | ARS(H) 1.0/23% (4) | MCI(H) 1.5/20% (4) | FUL(A) 1.4/24% (3) | NEW(H) 2.1/34% (3) | IPS(A) 1.7/24% (2) | COV(A) 1.5/32% (2) |
| ★ LEE | CHE(A) 1.2/22% (4) | COV(H) 1.6/42% (2) | MCI(A) 1.1/15% (5) | IPS(H) 1.9/35% (2) | LIV(A) 1.1/19% (4) | FUL(H) 1.6/34% (2) | AVL(A) 1.3/27% (3) | HUL(A) 1.4/35% (2) |
| ★ NFO | BOU(A) 1.1/18% (4) | CHE(H) 1.6/30% (4) | HUL(A) 1.5/35% (2) | BHA(H) 1.5/22% (4) | SUN(A) 1.3/19% (3) | EVE(H) 1.7/32% (3) | MUN(A) 1.5/22% (3) | NEW(A) 1.6/28% (3) |
| EVE | BRE(A) 1.2/16% (4) | LIV(H) 1.4/22% (4) | AVL(A) 1.4/22% (3) | FUL(H) 1.6/29% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.1/18% (2) | SUN(H) 1.6/22% (2) | MCI(H) 1.3/18% (4) |
| CRY | COV(A) 1.3/19% (2) | HUL(H) 1.6/28% (2) | CHE(A) 1.2/10% (4) | AVL(A) 1.3/13% (3) | MUN(H) 1.7/16% (3) | SUN(A) 1.2/8% (3) | ARS(H) 0.9/12% (4) | BOU(H) 1.2/13% (3) |
| COV | CRY(H) 1.7/28% (2) | LEE(A) 0.9/19% (3) | IPS(H) 1.5/29% (2) | MUN(A) 1.1/17% (3) | AVL(H) 1.3/29% (3) | BOU(A) 0.8/14% (4) | CHE(H) 1.2/24% (4) | BRE(H) 1.2/22% (3) |
| TOT | IPS(H) 1.7/35% (2) | SUN(A) 1.1/19% (3) | FUL(H) 1.4/34% (2) | ARS(H) 0.8/25% (4) | HUL(A) 1.2/35% (2) | LIV(A) 1.0/19% (4) | BOU(H) 1.1/26% (3) | BHA(H) 1.3/22% (4) |
| IPS | TOT(A) 1.1/19% (3) | AVL(H) 1.6/24% (3) | COV(A) 1.2/23% (2) | LEE(A) 1.1/15% (3) | NEW(H) 1.8/25% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/18% (3) | CHE(H) 1.4/19% (4) |
| ★ NEW | ARS(H) 0.8/16% (4) | BHA(A) 1.0/8% (4) | MUN(H) 1.6/20% (3) | SUN(H) 1.4/17% (2) | IPS(A) 1.4/17% (2) | BRE(A) 1.1/12% (4) | MCI(H) 1.2/13% (4) | NFO(H) 1.3/21% (3) |
| FUL | MCI(A) 1.0/12% (5) | BOU(H) 1.2/22% (3) | TOT(A) 1.1/25% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/24% (3) | LEE(A) 1.1/21% (3) | BHA(H) 1.4/19% (4) | ARS(H) 0.9/22% (4) |
| ★ HUL | BHA(H) 1.1/16% (4) | CRY(A) 1.3/19% (2) | NFO(H) 1.1/23% (3) | BOU(A) 0.7/12% (4) | TOT(H) 1.0/30% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/20% (4) | LEE(H) 1.0/25% (3) |
