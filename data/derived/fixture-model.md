# Fixture model v0.2 — GW12–19

**Generated** 2026-11-27 00:04 UTC from mirror `2026-11-27T00:03:50Z`.
**Observed** 11 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. With k=6 pseudo-matches, ratings are **35% prior / 65% data** for all 20 clubs on 11 matches. That weight shifts toward data every week.

League mean xG per team-match **1.50**; home 1.66 / away 1.33 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW12–15, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW11 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG12–15 | CS12–15 | xG12–19 | CS12–19 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.33)* | 0.94 | **7.69** | 1.00 | 16.23 | 2.13 | +4.1 | De Cuyper, Groß |
| MUN | 1.04 *(1.13)* | 1.26 | **6.90** | 0.74 | 12.37 | 1.24 | -4.6 |  |
| LIV | 1.17 *(1.23)* | 0.84 | **6.78** | 1.17 | 13.94 | 2.62 | -2.2 |  |
| ★ AVL | 0.93 *(0.90)* | 1.08 | **6.64** | 1.01 | 11.57 | 1.73 | -0.9 | N.Jackson |
| ★ BOU | 1.19 *(1.27)* | 0.84 | **6.60** | 1.18 | 14.39 | 2.55 | -3.0 | Evanilson |
| ★ MCI | 1.26 *(1.35)* | 0.84 | **6.48** | 1.08 | 14.32 | 2.48 | -0.2 | Haaland |
| ★ NFO | 1.06 *(1.09)* | 0.93 | **6.41** | 1.02 | 13.39 | 2.13 | -9.0 | Gibbs-White |
| CRY | 0.93 *(0.94)* | 1.38 | **6.30** | 0.64 | 10.89 | 1.05 | -3.5 |  |
| ★ LEE | 1.00 *(0.98)* | 0.85 | **6.15** | 1.16 | 12.47 | 2.51 | -2.2 | Muharemović |
| ★ NEW | 0.90 *(0.80)* | 1.16 | **6.01** | 0.68 | 10.96 | 1.29 | +1.8 | Hall |
| SUN | 1.05 *(0.97)* | 0.99 | **5.94** | 0.95 | 13.53 | 2.04 | -7.9 |  |
| ★ BRE | 1.09 *(1.06)* | 0.89 | **5.93** | 0.96 | 13.95 | 2.25 | +2.5 | Schade |
| ★ CHE | 0.98 *(0.90)* | 1.02 | **5.91** | 0.77 | 12.57 | 1.85 | +5.3 | Rogers |
| ★ ARS | 1.14 *(1.07)* | 0.62 | **5.85** | 1.48 | 14.25 | 3.18 | -0.7 | Raya, Calafiori |
| IPS | 0.86 *(0.85)* | 1.26 | **5.40** | 0.76 | 9.92 | 1.27 | +1.0 |  |
| EVE | 0.90 *(0.85)* | 1.04 | **5.14** | 0.80 | 10.00 | 1.54 | -2.0 |  |
| COV | 0.74 *(0.71)* | 1.08 | **5.00** | 0.88 | 9.03 | 1.58 | +1.3 |  |
| FUL | 0.89 *(0.93)* | 0.99 | **4.78** | 0.92 | 9.17 | 1.69 | -4.3 |  |
| ★ TOT | 0.85 *(0.92)* | 0.86 | **4.66** | 1.21 | 9.09 | 2.05 | -3.1 | Kudus |
| ★ HUL | 0.73 *(0.69)* | 1.11 | **4.32** | 0.78 | 8.16 | 1.43 | +1.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 | GW19 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | NEW(H) 2.5/32% (3) | BOU(A) 1.4/16% (4) | NFO(A) 1.6/19% (2) | EVE(H) 2.2/33% (3) | IPS(H) 2.7/34% (2) | FUL(A) 1.7/25% (3) | TOT(A) 1.5/26% (3) | MUN(H) 2.7/27% (3) |
| MUN | BRE(H) 1.5/16% (3) | NEW(A) 1.6/15% (3) | COV(H) 1.9/29% (2) | CRY(A) 1.9/14% (2) | ARS(A) 0.9/9% (5) | NFO(H) 1.6/17% (3) | SUN(H) 1.7/17% (2) | BHA(A) 1.3/7% (4) |
| LIV | EVE(A) 1.6/28% (3) | SUN(H) 1.9/31% (2) | CHE(A) 1.6/25% (4) | LEE(H) 1.7/32% (3) | TOT(H) 1.7/38% (3) | HUL(A) 1.7/36% (2) | AVL(A) 1.7/27% (3) | COV(H) 2.1/43% (2) |
| ★ AVL | IPS(A) 1.6/21% (2) | EVE(H) 1.6/28% (3) | CRY(H) 2.1/26% (2) | COV(A) 1.3/26% (2) | CHE(A) 1.3/17% (4) | LEE(H) 1.3/24% (3) | LIV(H) 1.3/19% (4) | BOU(A) 1.0/12% (4) |
| ★ BOU | FUL(A) 1.6/29% (3) | BHA(H) 1.9/24% (4) | HUL(H) 2.2/44% (2) | ARS(A) 1.0/20% (5) | COV(H) 2.1/44% (2) | TOT(A) 1.4/31% (3) | CRY(A) 2.2/27% (2) | AVL(H) 2.1/36% (3) |
| ★ MCI | ARS(A) 1.0/20% (5) | LEE(H) 1.8/33% (3) | BRE(A) 1.5/22% (4) | CHE(H) 2.2/34% (4) | HUL(H) 2.3/44% (2) | NEW(A) 1.9/28% (3) | EVE(A) 1.7/29% (3) | TOT(H) 1.8/39% (3) |
| ★ NFO | CHE(H) 1.8/30% (4) | HUL(A) 1.6/32% (2) | BHA(H) 1.7/20% (4) | SUN(A) 1.4/19% (3) | EVE(H) 1.8/33% (3) | MUN(A) 1.8/20% (3) | NEW(A) 1.6/25% (3) | FUL(H) 1.7/33% (2) |
| CRY | HUL(H) 1.7/26% (2) | CHE(A) 1.3/11% (4) | AVL(A) 1.3/12% (3) | MUN(H) 2.0/15% (3) | SUN(A) 1.2/9% (3) | ARS(H) 1.0/12% (4) | BOU(H) 1.3/11% (3) | BRE(A) 1.1/8% (4) |
| ★ LEE | COV(H) 1.8/43% (2) | MCI(A) 1.1/17% (5) | IPS(H) 2.1/38% (2) | LIV(A) 1.1/19% (4) | FUL(H) 1.7/37% (2) | AVL(A) 1.4/27% (3) | HUL(A) 1.5/35% (2) | EVE(H) 1.7/36% (3) |
| ★ NEW | BHA(A) 1.1/9% (4) | MUN(H) 1.9/20% (3) | SUN(H) 1.5/20% (2) | IPS(A) 1.5/19% (2) | BRE(A) 1.1/12% (4) | MCI(H) 1.3/14% (4) | NFO(H) 1.4/20% (3) | CHE(A) 1.2/15% (4) |
| SUN | TOT(H) 1.5/33% (3) | LIV(A) 1.2/15% (4) | NEW(A) 1.6/23% (3) | NFO(H) 1.6/25% (3) | CRY(H) 2.4/29% (2) | EVE(A) 1.5/23% (3) | MUN(A) 1.8/18% (3) | HUL(H) 1.9/38% (2) |
| ★ BRE | MUN(A) 1.8/21% (3) | ARS(H) 1.1/26% (4) | MCI(H) 1.5/22% (4) | FUL(A) 1.4/27% (3) | NEW(H) 2.1/34% (3) | IPS(A) 1.8/28% (2) | COV(A) 1.6/33% (2) | CRY(H) 2.5/33% (2) |
| ★ CHE | NFO(A) 1.2/17% (2) | CRY(H) 2.2/28% (2) | LIV(H) 1.4/20% (4) | MCI(A) 1.1/12% (5) | AVL(H) 1.8/28% (3) | COV(A) 1.4/28% (2) | IPS(A) 1.6/23% (2) | NEW(H) 1.9/29% (3) |
| ★ ARS | MCI(H) 1.6/35% (4) | BRE(A) 1.4/33% (4) | TOT(A) 1.3/42% (3) | BOU(H) 1.6/38% (3) | MUN(H) 2.4/43% (3) | CRY(A) 2.1/38% (2) | FUL(A) 1.5/40% (3) | IPS(H) 2.4/49% (2) |
| IPS | AVL(H) 1.5/21% (3) | COV(A) 1.2/21% (2) | LEE(A) 1.0/12% (3) | NEW(H) 1.7/22% (3) | BHA(A) 1.1/7% (4) | BRE(H) 1.3/16% (3) | CHE(H) 1.5/19% (4) | ARS(A) 0.7/9% (5) |
| EVE | LIV(H) 1.3/20% (4) | AVL(A) 1.3/20% (3) | FUL(H) 1.5/29% (2) | BHA(A) 1.1/11% (4) | NFO(A) 1.1/16% (2) | SUN(H) 1.5/23% (2) | MCI(H) 1.3/17% (4) | LEE(A) 1.0/18% (3) |
| COV | LEE(A) 0.8/17% (3) | IPS(H) 1.6/29% (2) | MUN(A) 1.2/16% (3) | AVL(H) 1.3/26% (3) | BOU(A) 0.8/12% (4) | CHE(H) 1.3/25% (4) | BRE(H) 1.1/21% (3) | LIV(A) 0.8/12% (4) |
| FUL | BOU(H) 1.2/21% (3) | TOT(A) 1.0/24% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.3/24% (3) | LEE(A) 1.0/19% (3) | BHA(H) 1.4/18% (4) | ARS(H) 0.9/22% (4) | NFO(A) 1.1/17% (2) |
| ★ TOT | SUN(A) 1.1/22% (3) | FUL(H) 1.4/36% (2) | ARS(H) 0.9/27% (4) | HUL(A) 1.3/35% (2) | LIV(A) 1.0/19% (4) | BOU(H) 1.2/26% (3) | BHA(H) 1.3/23% (4) | MCI(A) 1.0/16% (5) |
| ★ HUL | CRY(A) 1.3/18% (2) | NFO(H) 1.1/21% (3) | BOU(A) 0.8/11% (4) | TOT(H) 1.0/28% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.0/18% (4) | LEE(H) 1.0/23% (3) | SUN(A) 1.0/14% (3) |
