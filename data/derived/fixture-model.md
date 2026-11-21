# Fixture model v0.2 — GW12–19

**Generated** 2026-11-21 15:19 UTC from mirror `2026-11-21T15:18:27Z`.
**Observed** 11 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. With k=6 pseudo-matches, ratings are **35% prior / 65% data** for the 2 clubs on 11 matches, and **38% / 62%** for the 18 on 10. That weight shifts toward data every week.

League mean xG per team-match **1.47**; home 1.64 / away 1.31 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, AVL, BOU, BRE, BHA, CHE, COV, CRY, EVE, HUL, IPS, LEE, LIV, MUN, NEW, NFO, TOT, SUN on 10.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW12–15, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW11 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG12–15 | CS12–15 | xG12–19 | CS12–19 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.26 *(1.34)* | 0.91 | **7.41** | 1.08 | 15.57 | 2.25 | +6.3 | De Cuyper, Groß |
| MUN | 1.08 *(1.22)* | 1.20 | **7.19** | 0.85 | 12.70 | 1.40 | -4.0 |  |
| ★ AVL | 0.96 *(0.94)* | 1.16 | **6.65** | 0.91 | 11.64 | 1.59 | +0.2 | N.Jackson |
| ★ MCI | 1.28 *(1.37)* | 0.84 | **6.46** | 1.11 | 14.35 | 2.56 | -0.2 | Haaland |
| LIV | 1.12 *(1.08)* | 0.89 | **6.44** | 1.08 | 13.36 | 2.49 | -1.9 |  |
| SUN | 1.13 *(1.07)* | 1.02 | **6.39** | 0.99 | 14.26 | 2.04 | -7.7 |  |
| ★ BOU | 1.15 *(1.23)* | 0.80 | **6.18** | 1.27 | 13.81 | 2.74 | -2.1 | Evanilson |
| ★ CHE | 1.03 *(0.96)* | 0.97 | **6.16** | 0.89 | 13.17 | 2.08 | +4.9 | Rogers |
| CRY | 0.92 *(0.94)* | 1.39 | **6.02** | 0.63 | 10.48 | 1.04 | -3.8 |  |
| ★ ARS | 1.16 *(1.10)* | 0.59 | **5.92** | 1.59 | 14.16 | 3.37 | -1.2 | Raya, Calafiori |
| ★ NFO | 1.01 *(1.09)* | 0.91 | **5.89** | 1.05 | 12.37 | 2.20 | -7.0 | Gibbs-White |
| IPS | 0.90 *(0.92)* | 1.23 | **5.75** | 0.84 | 10.34 | 1.38 | +1.5 |  |
| ★ LEE | 0.95 *(0.91)* | 0.89 | **5.70** | 1.11 | 11.62 | 2.40 | -3.4 | Muharemović |
| ★ BRE | 1.07 *(1.01)* | 0.95 | **5.58** | 0.88 | 13.31 | 2.11 | +1.1 | Schade |
| EVE | 0.96 *(0.93)* | 1.03 | **5.52** | 0.84 | 10.67 | 1.63 | -1.8 |  |
| ★ NEW | 0.85 *(0.78)* | 1.19 | **5.50** | 0.62 | 10.08 | 1.23 | +1.5 | Hall |
| COV | 0.74 *(0.65)* | 1.06 | **4.93** | 0.89 | 8.89 | 1.63 | +0.4 |  |
| FUL | 0.89 *(0.95)* | 0.99 | **4.78** | 0.94 | 9.06 | 1.77 | -4.3 |  |
| ★ TOT | 0.83 *(0.84)* | 0.90 | **4.45** | 1.15 | 8.65 | 1.98 | -2.4 | Kudus |
| ★ HUL | 0.71 *(0.65)* | 1.10 | **4.13** | 0.86 | 7.92 | 1.54 | +1.5 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 | GW19 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | NEW(H) 2.5/36% (3) | BOU(A) 1.3/18% (4) | NFO(A) 1.5/22% (2) | EVE(H) 2.1/32% (3) | IPS(H) 2.5/34% (2) | FUL(A) 1.6/27% (3) | TOT(A) 1.5/29% (3) | MUN(H) 2.5/28% (3) |
| MUN | BRE(H) 1.7/18% (3) | NEW(A) 1.7/19% (3) | COV(H) 1.9/31% (2) | CRY(A) 2.0/16% (2) | ARS(A) 0.8/10% (5) | NFO(H) 1.6/20% (3) | SUN(H) 1.8/17% (2) | BHA(A) 1.3/8% (4) |
| ★ AVL | IPS(A) 1.5/18% (2) | EVE(H) 1.6/24% (3) | CRY(H) 2.2/25% (2) | COV(A) 1.3/25% (2) | CHE(A) 1.2/14% (4) | LEE(H) 1.4/24% (3) | LIV(H) 1.4/18% (4) | BOU(A) 1.0/11% (4) |
| ★ MCI | ARS(A) 1.0/20% (5) | LEE(H) 1.9/35% (3) | BRE(A) 1.6/23% (4) | CHE(H) 2.0/33% (4) | HUL(H) 2.3/46% (2) | NEW(A) 2.0/31% (3) | EVE(A) 1.7/27% (3) | TOT(H) 1.9/40% (3) |
| LIV | EVE(A) 1.5/25% (3) | SUN(H) 1.9/27% (2) | CHE(A) 1.4/23% (4) | LEE(H) 1.6/33% (3) | TOT(H) 1.6/38% (3) | HUL(A) 1.6/36% (2) | AVL(A) 1.7/25% (3) | COV(H) 2.0/42% (2) |
| SUN | TOT(H) 1.7/33% (3) | LIV(A) 1.3/15% (4) | NEW(A) 1.7/24% (3) | NFO(H) 1.7/26% (3) | CRY(H) 2.6/29% (2) | EVE(A) 1.5/20% (3) | MUN(A) 1.8/17% (3) | HUL(H) 2.0/39% (2) |
| ★ BOU | FUL(A) 1.5/31% (3) | BHA(H) 1.7/27% (4) | HUL(H) 2.1/48% (2) | ARS(A) 0.9/22% (5) | COV(H) 2.0/46% (2) | TOT(A) 1.4/34% (3) | CRY(A) 2.1/30% (2) | AVL(H) 2.2/37% (3) |
| ★ CHE | NFO(A) 1.2/20% (2) | CRY(H) 2.3/31% (2) | LIV(H) 1.5/24% (4) | MCI(A) 1.1/13% (5) | AVL(H) 1.9/30% (3) | COV(A) 1.4/31% (2) | IPS(A) 1.7/24% (2) | NEW(H) 2.0/34% (3) |
| CRY | HUL(H) 1.7/28% (2) | CHE(A) 1.2/10% (4) | AVL(A) 1.4/11% (3) | MUN(H) 1.8/14% (3) | SUN(A) 1.2/8% (3) | ARS(H) 0.9/12% (4) | BOU(H) 1.2/12% (3) | BRE(A) 1.1/9% (4) |
| ★ ARS | MCI(H) 1.6/37% (4) | BRE(A) 1.4/36% (4) | TOT(A) 1.4/45% (3) | BOU(H) 1.5/41% (3) | MUN(H) 2.3/44% (3) | CRY(A) 2.1/41% (2) | FUL(A) 1.5/43% (3) | IPS(H) 2.3/50% (2) |
| ★ NFO | CHE(H) 1.6/29% (4) | HUL(A) 1.4/35% (2) | BHA(H) 1.5/22% (4) | SUN(A) 1.3/19% (3) | EVE(H) 1.7/32% (3) | MUN(A) 1.6/20% (3) | NEW(A) 1.6/28% (3) | FUL(H) 1.6/35% (2) |
| IPS | AVL(H) 1.7/21% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.1/15% (3) | NEW(H) 1.7/25% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/18% (3) | CHE(H) 1.4/19% (4) | ARS(A) 0.7/10% (5) |
| ★ LEE | COV(H) 1.7/42% (2) | MCI(A) 1.0/15% (5) | IPS(H) 1.9/35% (2) | LIV(A) 1.1/19% (4) | FUL(H) 1.5/35% (2) | AVL(A) 1.4/25% (3) | HUL(A) 1.4/35% (2) | EVE(H) 1.6/33% (3) |
| ★ BRE | MUN(A) 1.7/19% (3) | ARS(H) 1.0/24% (4) | MCI(H) 1.5/20% (4) | FUL(A) 1.4/25% (3) | NEW(H) 2.1/35% (3) | IPS(A) 1.7/25% (2) | COV(A) 1.5/32% (2) | CRY(H) 2.4/32% (2) |
| EVE | LIV(H) 1.4/22% (4) | AVL(A) 1.4/20% (3) | FUL(H) 1.6/30% (2) | BHA(A) 1.1/12% (4) | NFO(A) 1.1/18% (2) | SUN(H) 1.6/22% (2) | MCI(H) 1.3/18% (4) | LEE(A) 1.1/20% (3) |
| ★ NEW | BHA(A) 1.0/9% (4) | MUN(H) 1.7/19% (3) | SUN(H) 1.4/17% (2) | IPS(A) 1.4/17% (2) | BRE(A) 1.1/13% (4) | MCI(H) 1.2/14% (4) | NFO(H) 1.3/21% (3) | CHE(A) 1.1/14% (4) |
| COV | LEE(A) 0.9/19% (3) | IPS(H) 1.5/29% (2) | MUN(A) 1.2/15% (3) | AVL(H) 1.4/26% (3) | BOU(A) 0.8/13% (4) | CHE(H) 1.2/24% (4) | BRE(H) 1.2/22% (3) | LIV(A) 0.9/14% (4) |
| FUL | BOU(H) 1.2/22% (3) | TOT(A) 1.0/26% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/25% (3) | LEE(A) 1.0/21% (3) | BHA(H) 1.3/19% (4) | ARS(H) 0.9/22% (4) | NFO(A) 1.1/19% (2) |
| ★ TOT | SUN(A) 1.1/19% (3) | FUL(H) 1.4/35% (2) | ARS(H) 0.8/26% (4) | HUL(A) 1.2/35% (2) | LIV(A) 1.0/19% (4) | BOU(H) 1.1/26% (3) | BHA(H) 1.2/23% (4) | MCI(A) 0.9/15% (5) |
| ★ HUL | CRY(A) 1.3/19% (2) | NFO(H) 1.1/23% (3) | BOU(A) 0.7/13% (4) | TOT(H) 1.0/30% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/20% (4) | LEE(H) 1.0/26% (3) | SUN(A) 0.9/13% (3) |
