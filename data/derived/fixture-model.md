# Fixture model v0.2 — GW9–16

**Generated** 2026-10-25 21:15 UTC from mirror `2026-10-25T21:14:54Z`.
**Observed** 8 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8]. With k=6 pseudo-matches, ratings are **43% prior / 57% data** for all 20 clubs on 8 matches. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.63 / away 1.30 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW9–12, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW8 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG9–12 | CS9–12 | xG9–16 | CS9–16 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.31 *(1.42)* | 0.96 | **8.43** | 1.03 | 16.33 | 2.03 | +6.4 | Groß, De Cuyper |
| ★ ARS | 1.21 *(1.19)* | 0.61 | **7.33** | 1.67 | 14.28 | 3.30 | -0.9 | Raya, Calafiori |
| ★ MCI | 1.30 *(1.45)* | 0.91 | **6.69** | 0.90 | 14.92 | 2.14 | +3.1 | Haaland |
| BOU | 1.09 *(1.24)* | 0.89 | **6.43** | 1.14 | 12.94 | 2.37 | -2.6 |  |
| ★ NFO | 1.14 *(1.20)* | 0.90 | **6.34** | 0.93 | 13.36 | 2.03 | -8.1 | Gibbs-White |
| ★ BRE | 1.10 *(1.19)* | 1.07 | **6.28** | 0.74 | 12.60 | 1.59 | +0.0 | Schade |
| MUN | 1.06 *(1.13)* | 1.03 | **6.07** | 0.91 | 12.08 | 1.85 | -3.2 |  |
| SUN | 1.05 *(0.98)* | 1.09 | **6.01** | 1.05 | 12.36 | 1.87 | -5.5 |  |
| LIV | 1.05 *(1.01)* | 0.83 | **5.85** | 1.15 | 12.19 | 2.52 | -0.8 |  |
| ★ CHE | 1.00 *(0.89)* | 0.94 | **5.79** | 0.96 | 11.95 | 2.03 | +6.5 | Rogers, João Pedro |
| CRY | 0.97 *(0.95)* | 1.20 | **5.64** | 0.94 | 11.10 | 1.59 | -2.1 |  |
| EVE | 0.91 *(0.84)* | 1.02 | **5.46** | 1.02 | 10.32 | 1.83 | -1.9 |  |
| ★ FUL | 0.92 *(0.99)* | 1.00 | **5.44** | 0.94 | 10.47 | 1.90 | -3.6 | Gonzalo |
| AVL | 0.85 *(0.77)* | 1.02 | **5.43** | 0.94 | 10.70 | 2.01 | -0.1 |  |
| IPS | 0.92 *(0.96)* | 1.26 | **5.38** | 0.82 | 10.71 | 1.50 | +0.8 |  |
| TOT | 0.81 *(0.70)* | 0.94 | **5.38** | 1.08 | 9.63 | 2.15 | -0.2 |  |
| ★ LEE | 0.93 *(0.92)* | 0.92 | **5.23** | 1.21 | 10.75 | 2.23 | -1.7 | Muharemović |
| COV | 0.74 *(0.66)* | 1.05 | **4.60** | 0.92 | 9.15 | 1.84 | -1.7 |  |
| ★ HUL | 0.76 *(0.74)* | 1.17 | **4.54** | 0.64 | 8.60 | 1.31 | +0.3 | Tzolakis, Egan |
| ★ NEW | 0.87 *(0.78)* | 1.21 | **4.50** | 0.63 | 10.11 | 1.28 | +2.9 | Hall, Barnes |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | MCI(A) 1.5/13% (5) | BRE(H) 2.3/25% (3) | HUL(A) 2.0/31% (2) | NEW(H) 2.6/34% (3) | BOU(A) 1.5/18% (3) | NFO(A) 1.5/17% (3) | EVE(H) 2.2/32% (3) | IPS(H) 2.7/32% (2) |
| ★ ARS | LIV(A) 1.3/35% (4) | HUL(H) 2.3/55% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/36% (4) | BRE(A) 1.7/33% (3) | TOT(A) 1.5/45% (3) | BOU(H) 1.8/42% (3) | MUN(H) 2.0/43% (4) |
| ★ MCI | BHA(H) 2.0/21% (3) | NFO(A) 1.5/19% (3) | FUL(H) 2.1/34% (2) | ARS(A) 1.0/17% (5) | LEE(H) 1.9/33% (3) | BRE(A) 1.8/20% (3) | CHE(H) 2.0/31% (4) | HUL(H) 2.5/41% (2) |
| BOU | LEE(H) 1.6/34% (3) | IPS(A) 1.8/26% (2) | NFO(H) 1.6/27% (3) | FUL(A) 1.4/27% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.1/41% (2) | ARS(A) 0.9/17% (5) | COV(H) 1.9/43% (2) |
| ★ NFO | BRE(A) 1.6/20% (3) | MCI(H) 1.7/22% (4) | BOU(A) 1.3/20% (3) | CHE(H) 1.7/31% (4) | HUL(A) 1.7/33% (2) | BHA(H) 1.8/21% (3) | SUN(A) 1.6/22% (3) | EVE(H) 1.9/35% (3) |
| ★ BRE | NFO(H) 1.6/20% (3) | BHA(A) 1.4/10% (4) | EVE(H) 1.8/28% (3) | MUN(A) 1.5/16% (4) | ARS(H) 1.1/18% (4) | MCI(H) 1.6/16% (4) | FUL(A) 1.4/20% (3) | NEW(H) 2.2/30% (3) |
| MUN | CHE(A) 1.3/19% (4) | AVL(H) 1.8/32% (3) | LIV(A) 1.1/17% (4) | BRE(H) 1.9/23% (3) | NEW(A) 1.7/23% (3) | COV(H) 1.8/37% (2) | CRY(A) 1.7/20% (3) | ARS(A) 0.8/13% (5) |
| SUN | COV(A) 1.4/27% (2) | CHE(H) 1.6/24% (4) | AVL(A) 1.4/22% (3) | TOT(H) 1.6/31% (2) | LIV(A) 1.1/15% (4) | NEW(A) 1.7/21% (3) | NFO(H) 1.5/20% (3) | CRY(H) 2.0/25% (2) |
| LIV | ARS(H) 1.0/27% (4) | CRY(A) 1.6/27% (3) | MUN(H) 1.8/32% (4) | EVE(A) 1.4/29% (3) | SUN(H) 1.9/32% (3) | CHE(A) 1.3/26% (4) | LEE(H) 1.6/37% (3) | TOT(H) 1.6/42% (2) |
| ★ CHE | MUN(H) 1.7/27% (4) | SUN(A) 1.4/20% (3) | LEE(H) 1.5/32% (3) | NFO(A) 1.2/17% (3) | CRY(H) 2.0/31% (2) | LIV(H) 1.4/27% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.7/35% (3) |
| CRY | TOT(A) 1.2/20% (3) | LIV(H) 1.3/19% (4) | COV(A) 1.3/24% (2) | HUL(H) 1.8/30% (2) | CHE(A) 1.2/14% (4) | AVL(A) 1.3/19% (3) | MUN(H) 1.6/19% (4) | SUN(A) 1.4/13% (3) |
| EVE | NEW(A) 1.4/24% (3) | COV(H) 1.5/38% (2) | BRE(A) 1.3/16% (3) | LIV(H) 1.2/25% (4) | AVL(A) 1.2/24% (3) | FUL(H) 1.5/30% (2) | BHA(A) 1.1/11% (4) | NFO(A) 1.1/15% (3) |
| ★ FUL | AVL(A) 1.2/25% (3) | NEW(H) 1.8/32% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.3/24% (3) | TOT(A) 1.1/27% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.6/24% (3) | LEE(A) 1.1/22% (3) |
| AVL | FUL(H) 1.4/30% (2) | MUN(A) 1.1/17% (4) | SUN(H) 1.5/25% (3) | IPS(A) 1.4/22% (2) | EVE(H) 1.4/30% (3) | CRY(H) 1.7/28% (2) | COV(A) 1.2/30% (2) | CHE(A) 1.0/19% (4) |
| IPS | HUL(A) 1.4/21% (2) | BOU(H) 1.3/17% (3) | TOT(A) 1.1/19% (3) | AVL(H) 1.5/25% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.1/15% (3) | NEW(H) 1.8/24% (3) | BHA(A) 1.1/7% (4) |
| TOT | CRY(H) 1.6/31% (2) | LEE(A) 1.0/24% (3) | IPS(H) 1.7/33% (2) | SUN(A) 1.2/20% (3) | FUL(H) 1.3/33% (2) | ARS(H) 0.8/23% (4) | HUL(A) 1.2/31% (2) | LIV(A) 0.9/20% (4) |
| ★ LEE | BOU(A) 1.1/20% (3) | TOT(H) 1.4/38% (2) | CHE(A) 1.1/22% (4) | COV(H) 1.6/41% (2) | MCI(A) 1.1/14% (5) | IPS(H) 1.9/33% (2) | LIV(A) 1.0/21% (4) | FUL(H) 1.5/33% (2) |
| COV | SUN(H) 1.3/24% (3) | EVE(A) 1.0/21% (3) | CRY(H) 1.4/27% (2) | LEE(A) 0.9/20% (3) | IPS(H) 1.5/28% (2) | MUN(A) 1.0/16% (4) | AVL(H) 1.2/31% (3) | BOU(A) 0.9/16% (3) |
| ★ HUL | IPS(H) 1.6/25% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/18% (3) | BOU(A) 0.9/13% (3) | TOT(H) 1.2/29% (2) | MCI(A) 0.9/8% (5) |
| ★ NEW | EVE(H) 1.4/24% (3) | FUL(A) 1.1/16% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/19% (4) | SUN(H) 1.5/19% (3) | IPS(A) 1.4/16% (2) | BRE(A) 1.2/11% (3) |
