# Fixture model v0.2 — GW9–16

**Generated** 2026-10-23 19:34 UTC from mirror `2026-10-23T19:33:49Z`.
**Observed** 7 gameweek(s) — [1, 2, 3, 4, 5, 6, 7]. With k=6 pseudo-matches, ratings are **46% prior / 54% data** for all 20 clubs on 7 matches. That weight shifts toward data every week.

League mean xG per team-match **1.51**; home 1.68 / away 1.34 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW9–12, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW8 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG9–12 | CS9–12 | xG9–16 | CS9–16 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.45)* | 0.97 | **8.29** | 1.01 | 16.18 | 1.96 | +7.7 | Groß, De Cuyper |
| ★ ARS | 1.18 *(1.13)* | 0.61 | **7.29** | 1.65 | 14.14 | 3.26 | -1.0 | Raya, Calafiori |
| ★ MCI | 1.29 *(1.46)* | 0.92 | **6.96** | 0.86 | 15.31 | 2.05 | +3.6 | Haaland |
| SUN | 1.07 *(1.01)* | 1.12 | **6.48** | 0.93 | 13.19 | 1.69 | -4.6 |  |
| BOU | 1.03 *(1.18)* | 0.89 | **6.34** | 1.07 | 12.71 | 2.29 | -3.4 |  |
| ★ NFO | 1.10 *(1.11)* | 0.93 | **6.26** | 0.86 | 13.20 | 1.89 | -6.8 | Gibbs-White |
| MUN | 1.07 *(1.14)* | 0.97 | **6.23** | 0.93 | 12.52 | 1.91 | -2.0 |  |
| ★ CHE | 1.04 *(0.95)* | 0.96 | **6.22** | 0.90 | 12.83 | 1.89 | +7.0 | Rogers, João Pedro |
| ★ BRE | 1.06 *(1.15)* | 1.02 | **6.20** | 0.79 | 12.50 | 1.66 | +0.8 | Schade |
| LIV | 1.08 *(1.04)* | 0.83 | **6.04** | 1.13 | 12.94 | 2.42 | -2.0 |  |
| ★ FUL | 0.95 *(1.04)* | 1.02 | **5.79** | 0.88 | 11.15 | 1.77 | -4.0 | Gonzalo |
| CRY | 0.95 *(0.89)* | 1.20 | **5.77** | 0.89 | 11.28 | 1.48 | -0.4 |  |
| IPS | 0.96 *(1.02)* | 1.21 | **5.77** | 0.85 | 11.53 | 1.53 | +0.2 |  |
| AVL | 0.88 *(0.80)* | 1.02 | **5.71** | 0.86 | 11.37 | 1.87 | -1.5 |  |
| ★ LEE | 0.95 *(0.95)* | 0.95 | **5.67** | 1.12 | 11.45 | 2.02 | -1.0 | Muharemović |
| TOT | 0.82 *(0.71)* | 0.98 | **5.61** | 0.96 | 10.02 | 1.93 | -1.5 |  |
| EVE | 0.91 *(0.88)* | 1.01 | **5.60** | 0.99 | 10.70 | 1.77 | -1.2 |  |
| COV | 0.76 *(0.68)* | 1.09 | **4.92** | 0.83 | 9.62 | 1.64 | -1.2 |  |
| ★ NEW | 0.87 *(0.77)* | 1.20 | **4.65** | 0.61 | 10.27 | 1.23 | +1.8 | Hall, Barnes |
| ★ HUL | 0.73 *(0.65)* | 1.14 | **4.44** | 0.64 | 8.55 | 1.34 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | MCI(A) 1.6/12% (5) | BRE(H) 2.2/25% (3) | HUL(A) 2.0/31% (2) | NEW(H) 2.6/33% (3) | BOU(A) 1.5/19% (3) | NFO(A) 1.6/17% (3) | EVE(H) 2.2/31% (3) | IPS(H) 2.6/29% (2) |
| ★ ARS | LIV(A) 1.3/33% (4) | HUL(H) 2.3/55% (2) | NEW(A) 1.9/41% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/34% (3) | TOT(A) 1.5/43% (3) | BOU(H) 1.8/43% (3) | MUN(H) 1.9/42% (4) |
| ★ MCI | BHA(H) 2.1/21% (3) | NFO(A) 1.6/19% (3) | FUL(H) 2.2/31% (2) | ARS(A) 1.1/16% (5) | LEE(H) 2.1/31% (3) | BRE(A) 1.8/20% (3) | CHE(H) 2.1/28% (4) | HUL(H) 2.5/41% (2) |
| SUN | COV(A) 1.6/24% (2) | CHE(H) 1.7/21% (4) | AVL(A) 1.5/19% (3) | TOT(H) 1.7/29% (2) | LIV(A) 1.2/13% (4) | NEW(A) 1.7/20% (3) | NFO(H) 1.7/19% (3) | CRY(H) 2.1/24% (2) |
| BOU | LEE(H) 1.6/32% (3) | IPS(A) 1.7/24% (2) | NFO(H) 1.6/27% (3) | FUL(A) 1.4/24% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.0/42% (2) | ARS(A) 0.8/17% (5) | COV(H) 1.9/41% (2) |
| ★ NFO | BRE(A) 1.5/19% (3) | MCI(H) 1.7/20% (4) | BOU(A) 1.3/20% (3) | CHE(H) 1.8/27% (4) | HUL(A) 1.7/32% (2) | BHA(H) 1.8/20% (3) | SUN(A) 1.6/19% (3) | EVE(H) 1.9/32% (3) |
| MUN | CHE(A) 1.4/18% (4) | AVL(H) 1.8/32% (3) | LIV(A) 1.2/17% (4) | BRE(H) 1.8/25% (3) | NEW(A) 1.7/25% (3) | COV(H) 2.0/38% (2) | CRY(A) 1.7/21% (3) | ARS(A) 0.9/15% (5) |
| ★ CHE | MUN(H) 1.7/25% (4) | SUN(A) 1.6/18% (3) | LEE(H) 1.7/29% (3) | NFO(A) 1.3/17% (3) | CRY(H) 2.1/29% (2) | LIV(H) 1.4/25% (4) | MCI(A) 1.3/13% (5) | AVL(H) 1.8/32% (3) |
| ★ BRE | NFO(H) 1.7/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.4/20% (3) | NEW(H) 2.1/31% (3) |
| LIV | ARS(H) 1.1/27% (4) | CRY(A) 1.7/27% (3) | MUN(H) 1.7/30% (4) | EVE(A) 1.5/28% (3) | SUN(H) 2.0/31% (3) | CHE(A) 1.4/24% (4) | LEE(H) 1.7/35% (3) | TOT(H) 1.8/40% (2) |
| ★ FUL | AVL(A) 1.3/22% (3) | NEW(H) 1.9/31% (3) | MCI(A) 1.2/11% (5) | BOU(H) 1.4/24% (3) | TOT(A) 1.2/25% (3) | EVE(A) 1.3/21% (3) | BRE(H) 1.6/23% (3) | LEE(A) 1.2/20% (3) |
| CRY | TOT(A) 1.2/19% (3) | LIV(H) 1.3/18% (4) | COV(A) 1.4/22% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/12% (4) | AVL(A) 1.3/17% (3) | MUN(H) 1.5/18% (4) | SUN(A) 1.4/12% (3) |
| IPS | HUL(A) 1.5/23% (2) | BOU(H) 1.4/19% (3) | TOT(A) 1.3/19% (3) | AVL(H) 1.6/24% (3) | COV(A) 1.4/22% (2) | LEE(A) 1.2/15% (3) | NEW(H) 1.9/25% (3) | BHA(A) 1.2/7% (4) |
| AVL | FUL(H) 1.5/27% (2) | MUN(A) 1.1/16% (4) | SUN(H) 1.6/23% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/29% (3) | CRY(H) 1.8/27% (2) | COV(A) 1.3/28% (2) | CHE(A) 1.1/17% (4) |
| ★ LEE | BOU(A) 1.1/19% (3) | TOT(H) 1.6/35% (2) | CHE(A) 1.2/19% (4) | COV(H) 1.7/38% (2) | MCI(A) 1.2/13% (5) | IPS(H) 1.9/30% (2) | LIV(A) 1.1/18% (4) | FUL(H) 1.6/30% (2) |
| TOT | CRY(H) 1.7/29% (2) | LEE(A) 1.0/21% (3) | IPS(H) 1.7/29% (2) | SUN(A) 1.2/17% (3) | FUL(H) 1.4/29% (2) | ARS(H) 0.8/21% (4) | HUL(A) 1.3/30% (2) | LIV(A) 0.9/17% (4) |
| EVE | NEW(A) 1.5/23% (3) | COV(H) 1.7/36% (2) | BRE(A) 1.2/17% (3) | LIV(H) 1.3/23% (4) | AVL(A) 1.2/23% (3) | FUL(H) 1.5/28% (2) | BHA(A) 1.2/11% (4) | NFO(A) 1.1/16% (3) |
| COV | SUN(H) 1.4/21% (3) | EVE(A) 1.0/19% (3) | CRY(H) 1.5/25% (2) | LEE(A) 1.0/18% (3) | IPS(H) 1.5/25% (2) | MUN(A) 1.0/14% (4) | AVL(H) 1.3/28% (3) | BOU(A) 0.9/15% (3) |
| ★ NEW | EVE(H) 1.5/23% (3) | FUL(A) 1.2/15% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.6/18% (3) | IPS(A) 1.4/15% (2) | BRE(A) 1.2/12% (3) |
| ★ HUL | IPS(H) 1.5/23% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/19% (3) | BOU(A) 0.9/14% (3) | TOT(H) 1.2/29% (2) | MCI(A) 0.9/9% (5) |
