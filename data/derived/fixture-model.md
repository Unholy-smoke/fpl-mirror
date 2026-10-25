# Fixture model v0.2 — GW9–16

**Generated** 2026-10-25 06:04 UTC from mirror `2026-10-25T06:03:45Z`.
**Observed** 8 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8]. With k=6 pseudo-matches, ratings are **43% prior / 57% data** for the 10 clubs on 8 matches, and **46% / 54%** for the 10 on 7. That weight shifts toward data every week.

League mean xG per team-match **1.47**; home 1.64 / away 1.31 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: BOU, BRE, BHA, CRY, HUL, LEE, LIV, MUN, NEW, SUN on 7.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW9–12, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW8 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG9–12 | CS9–12 | xG9–16 | CS9–16 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.30 *(1.48)* | 0.98 | **8.30** | 1.00 | 16.19 | 1.97 | +7.7 | Groß, De Cuyper |
| ★ ARS | 1.20 *(1.18)* | 0.61 | **7.24** | 1.67 | 14.01 | 3.32 | -0.9 | Raya, Calafiori |
| ★ MCI | 1.29 *(1.44)* | 0.90 | **6.69** | 0.92 | 14.87 | 2.18 | +3.1 | Haaland |
| SUN | 1.09 *(1.03)* | 1.13 | **6.28** | 0.99 | 12.95 | 1.74 | -4.6 |  |
| ★ NFO | 1.13 *(1.19)* | 0.89 | **6.27** | 0.95 | 13.38 | 2.06 | -8.1 | Gibbs-White |
| BOU | 1.04 *(1.21)* | 0.90 | **6.19** | 1.11 | 12.46 | 2.34 | -3.4 |  |
| ★ BRE | 1.08 *(1.18)* | 1.03 | **6.19** | 0.78 | 12.41 | 1.68 | +0.8 | Schade |
| MUN | 1.08 *(1.16)* | 0.99 | **6.14** | 0.95 | 12.30 | 1.93 | -2.0 |  |
| LIV | 1.09 *(1.07)* | 0.83 | **6.05** | 1.14 | 12.80 | 2.47 | -2.0 |  |
| ★ CHE | 1.00 *(0.89)* | 0.95 | **5.82** | 0.92 | 12.00 | 1.96 | +6.5 | Rogers, João Pedro |
| CRY | 0.97 *(0.91)* | 1.22 | **5.67** | 0.91 | 11.17 | 1.52 | -0.4 |  |
| TOT | 0.82 *(0.70)* | 0.93 | **5.51** | 1.05 | 9.76 | 2.12 | -0.2 |  |
| AVL | 0.85 *(0.77)* | 1.01 | **5.46** | 0.92 | 10.81 | 1.98 | -0.1 |  |
| ★ FUL | 0.91 *(0.98)* | 0.99 | **5.45** | 0.96 | 10.46 | 1.92 | -3.6 | Gonzalo |
| EVE | 0.90 *(0.84)* | 1.02 | **5.44** | 1.00 | 10.32 | 1.80 | -1.9 |  |
| ★ LEE | 0.96 *(0.97)* | 0.95 | **5.43** | 1.18 | 11.10 | 2.14 | -1.0 | Muharemović |
| IPS | 0.92 *(0.95)* | 1.25 | **5.40** | 0.84 | 10.81 | 1.52 | +0.8 |  |
| COV | 0.73 *(0.65)* | 1.05 | **4.72** | 0.90 | 9.24 | 1.81 | -1.7 |  |
| ★ NEW | 0.88 *(0.79)* | 1.21 | **4.61** | 0.62 | 10.28 | 1.26 | +1.8 | Hall, Barnes |
| ★ HUL | 0.74 *(0.66)* | 1.16 | **4.46** | 0.65 | 8.40 | 1.35 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | MCI(A) 1.5/13% (5) | BRE(H) 2.2/25% (3) | HUL(A) 2.0/30% (2) | NEW(H) 2.6/32% (3) | BOU(A) 1.5/19% (3) | NFO(A) 1.5/16% (3) | EVE(H) 2.2/31% (3) | IPS(H) 2.7/31% (2) |
| ★ ARS | LIV(A) 1.3/34% (4) | HUL(H) 2.3/56% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/36% (4) | BRE(A) 1.6/34% (3) | TOT(A) 1.5/45% (3) | BOU(H) 1.8/44% (3) | MUN(H) 1.9/42% (4) |
| ★ MCI | BHA(H) 2.1/22% (3) | NFO(A) 1.5/19% (3) | FUL(H) 2.1/34% (2) | ARS(A) 1.0/17% (5) | LEE(H) 2.0/32% (3) | BRE(A) 1.7/20% (3) | CHE(H) 2.0/31% (4) | HUL(H) 2.4/42% (2) |
| SUN | COV(A) 1.5/26% (2) | CHE(H) 1.7/23% (4) | AVL(A) 1.4/21% (3) | TOT(H) 1.7/30% (2) | LIV(A) 1.2/13% (4) | NEW(A) 1.7/20% (3) | NFO(H) 1.6/19% (3) | CRY(H) 2.2/24% (2) |
| ★ NFO | BRE(A) 1.5/20% (3) | MCI(H) 1.7/22% (4) | BOU(A) 1.3/22% (3) | CHE(H) 1.8/31% (4) | HUL(A) 1.7/34% (2) | BHA(H) 1.8/22% (3) | SUN(A) 1.7/20% (3) | EVE(H) 1.9/35% (3) |
| BOU | LEE(H) 1.6/32% (3) | IPS(A) 1.7/26% (2) | NFO(H) 1.5/26% (3) | FUL(A) 1.3/26% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.0/42% (2) | ARS(A) 0.8/17% (5) | COV(H) 1.8/42% (2) |
| ★ BRE | NFO(H) 1.6/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/30% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/18% (4) | FUL(A) 1.4/21% (3) | NEW(H) 2.2/31% (3) |
| MUN | CHE(A) 1.3/20% (4) | AVL(H) 1.8/33% (3) | LIV(A) 1.2/17% (4) | BRE(H) 1.8/25% (3) | NEW(A) 1.7/24% (3) | COV(H) 1.9/39% (2) | CRY(A) 1.7/21% (3) | ARS(A) 0.9/14% (5) |
| LIV | ARS(H) 1.1/27% (4) | CRY(A) 1.7/27% (3) | MUN(H) 1.8/31% (4) | EVE(A) 1.5/29% (3) | SUN(H) 2.0/31% (3) | CHE(A) 1.4/26% (4) | LEE(H) 1.7/35% (3) | TOT(H) 1.7/41% (2) |
| ★ CHE | MUN(H) 1.6/26% (4) | SUN(A) 1.5/19% (3) | LEE(H) 1.6/30% (3) | NFO(A) 1.2/17% (3) | CRY(H) 2.0/30% (2) | LIV(H) 1.4/26% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.7/35% (3) |
| CRY | TOT(A) 1.2/20% (3) | LIV(H) 1.3/17% (4) | COV(A) 1.3/23% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/14% (4) | AVL(A) 1.3/18% (3) | MUN(H) 1.6/18% (4) | SUN(A) 1.4/11% (3) |
| TOT | CRY(H) 1.6/31% (2) | LEE(A) 1.0/23% (3) | IPS(H) 1.7/32% (2) | SUN(A) 1.2/19% (3) | FUL(H) 1.3/33% (2) | ARS(H) 0.8/23% (4) | HUL(A) 1.2/32% (2) | LIV(A) 0.9/19% (4) |
| AVL | FUL(H) 1.4/30% (2) | MUN(A) 1.1/17% (4) | SUN(H) 1.6/24% (3) | IPS(A) 1.4/22% (2) | EVE(H) 1.4/30% (3) | CRY(H) 1.7/28% (2) | COV(A) 1.2/30% (2) | CHE(A) 1.1/19% (4) |
| ★ FUL | AVL(A) 1.2/25% (3) | NEW(H) 1.8/32% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.3/26% (3) | TOT(A) 1.1/27% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.5/25% (3) | LEE(A) 1.1/21% (3) |
| EVE | NEW(A) 1.4/23% (3) | COV(H) 1.5/38% (2) | BRE(A) 1.2/16% (3) | LIV(H) 1.2/23% (4) | AVL(A) 1.2/24% (3) | FUL(H) 1.5/29% (2) | BHA(A) 1.2/11% (4) | NFO(A) 1.1/15% (3) |
| ★ LEE | BOU(A) 1.1/20% (3) | TOT(H) 1.5/36% (2) | CHE(A) 1.2/21% (4) | COV(H) 1.6/40% (2) | MCI(A) 1.1/14% (5) | IPS(H) 2.0/32% (2) | LIV(A) 1.0/18% (4) | FUL(H) 1.5/32% (2) |
| IPS | HUL(A) 1.4/22% (2) | BOU(H) 1.4/18% (3) | TOT(A) 1.1/19% (3) | AVL(H) 1.5/25% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.1/14% (3) | NEW(H) 1.8/24% (3) | BHA(A) 1.2/7% (4) |
| COV | SUN(H) 1.4/23% (3) | EVE(A) 1.0/21% (3) | CRY(H) 1.5/26% (2) | LEE(A) 0.9/19% (3) | IPS(H) 1.5/28% (2) | MUN(A) 0.9/16% (4) | AVL(H) 1.2/31% (3) | BOU(A) 0.9/17% (3) |
| ★ NEW | EVE(H) 1.5/24% (3) | FUL(A) 1.1/16% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/7% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.6/18% (3) | IPS(A) 1.4/16% (2) | BRE(A) 1.2/12% (3) |
| ★ HUL | IPS(H) 1.5/25% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/18% (3) | BOU(A) 0.9/14% (3) | TOT(H) 1.1/29% (2) | MCI(A) 0.9/9% (5) |
