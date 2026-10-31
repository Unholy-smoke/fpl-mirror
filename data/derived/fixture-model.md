# Fixture model v0.2 — GW10–17

**Generated** 2026-10-31 13:37 UTC from mirror `2026-10-31T13:36:25Z`.
**Observed** 8 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8]. With k=6 pseudo-matches, ratings are **43% prior / 57% data** for all 20 clubs on 8 matches. That weight shifts toward data every week.

League mean xG per team-match **1.46**; home 1.63 / away 1.30 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW10–13, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW9 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG10–13 | CS10–13 | xG10–17 | CS10–17 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.31 *(1.42)* | 0.97 | **8.32** | 1.07 | 16.40 | 2.10 | +6.4 | Groß, De Cuyper |
| ★ ARS | 1.21 *(1.19)* | 0.61 | **7.66** | 1.66 | 14.79 | 3.34 | -0.9 | Raya, Calafiori |
| LIV | 1.07 *(1.04)* | 0.83 | **6.79** | 1.21 | 12.97 | 2.61 | -1.2 |  |
| ★ MCI | 1.30 *(1.45)* | 0.91 | **6.61** | 1.02 | 14.91 | 2.22 | +3.1 | Haaland |
| ★ BOU | 1.09 *(1.24)* | 0.89 | **6.52** | 1.02 | 12.67 | 2.35 | -2.6 | Evanilson |
| ★ NFO | 1.14 *(1.20)* | 0.90 | **6.48** | 1.06 | 13.33 | 2.05 | -8.1 | Gibbs-White |
| MUN | 1.07 *(1.13)* | 1.03 | **6.41** | 0.95 | 12.30 | 1.87 | -3.2 |  |
| ★ CHE | 1.00 *(0.89)* | 0.94 | **6.05** | 1.00 | 11.62 | 2.08 | +6.5 | Rogers |
| ★ BRE | 1.10 *(1.19)* | 1.06 | **5.77** | 0.74 | 12.76 | 1.62 | +0.1 | Schade |
| SUN | 1.05 *(0.98)* | 1.09 | **5.72** | 0.92 | 12.33 | 1.79 | -5.5 |  |
| CRY | 0.96 *(0.94)* | 1.20 | **5.62** | 0.88 | 10.83 | 1.54 | -2.0 |  |
| ★ AVL | 0.85 *(0.77)* | 1.02 | **5.47** | 0.94 | 10.62 | 2.00 | -0.1 | N.Jackson |
| FUL | 0.92 *(0.99)* | 1.00 | **5.33** | 0.96 | 10.68 | 1.83 | -3.6 |  |
| ★ LEE | 0.93 *(0.92)* | 0.92 | **5.25** | 1.16 | 10.89 | 2.30 | -1.7 | Muharemović |
| IPS | 0.92 *(0.96)* | 1.25 | **5.24** | 0.83 | 10.90 | 1.46 | +0.8 |  |
| EVE | 0.91 *(0.84)* | 1.02 | **5.22** | 1.02 | 10.50 | 1.83 | -1.9 |  |
| TOT | 0.81 *(0.70)* | 0.94 | **5.11** | 1.10 | 9.21 | 2.10 | -0.2 |  |
| COV | 0.74 *(0.66)* | 1.05 | **4.79** | 0.97 | 8.97 | 1.85 | -1.7 |  |
| ★ NEW | 0.86 *(0.78)* | 1.21 | **4.52** | 0.58 | 9.94 | 1.18 | +2.9 | Hall, Barnes |
| ★ HUL | 0.75 *(0.72)* | 1.17 | **4.06** | 0.57 | 7.98 | 1.27 | +0.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | BRE(H) 2.3/25% (3) | HUL(A) 2.0/30% (2) | NEW(H) 2.6/34% (3) | BOU(A) 1.5/18% (3) | NFO(A) 1.5/16% (3) | EVE(H) 2.2/32% (3) | IPS(H) 2.7/31% (2) | FUL(A) 1.7/23% (3) |
| ★ ARS | HUL(H) 2.3/55% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/36% (4) | BRE(A) 1.7/34% (3) | TOT(A) 1.5/45% (3) | BOU(H) 1.7/42% (3) | MUN(H) 2.0/43% (4) | CRY(A) 1.9/38% (3) |
| LIV | CRY(A) 1.7/27% (3) | MUN(H) 1.8/32% (4) | EVE(A) 1.4/29% (3) | SUN(H) 1.9/32% (3) | CHE(A) 1.3/26% (4) | LEE(H) 1.6/37% (3) | TOT(H) 1.6/42% (2) | HUL(A) 1.6/36% (2) |
| ★ MCI | NFO(A) 1.5/19% (3) | FUL(H) 2.1/34% (2) | ARS(A) 1.0/17% (5) | LEE(H) 1.9/33% (3) | BRE(A) 1.8/20% (3) | CHE(H) 2.0/31% (4) | HUL(H) 2.5/41% (2) | NEW(A) 2.0/28% (3) |
| ★ BOU | IPS(A) 1.8/26% (2) | NFO(H) 1.6/27% (3) | FUL(A) 1.4/27% (3) | BHA(H) 1.7/22% (3) | HUL(H) 2.1/42% (2) | ARS(A) 0.9/17% (5) | COV(H) 1.9/43% (2) | TOT(A) 1.3/31% (3) |
| ★ NFO | MCI(H) 1.7/22% (4) | BOU(A) 1.3/20% (3) | CHE(H) 1.8/31% (4) | HUL(A) 1.7/33% (2) | BHA(H) 1.8/22% (3) | SUN(A) 1.6/22% (3) | EVE(H) 1.9/35% (3) | MUN(A) 1.5/21% (4) |
| MUN | AVL(H) 1.8/32% (3) | LIV(A) 1.1/17% (4) | BRE(H) 1.8/23% (3) | NEW(A) 1.7/24% (3) | COV(H) 1.8/37% (2) | CRY(A) 1.7/20% (3) | ARS(A) 0.8/13% (5) | NFO(H) 1.6/22% (3) |
| ★ CHE | SUN(A) 1.4/20% (3) | LEE(H) 1.5/32% (3) | NFO(A) 1.2/17% (3) | CRY(H) 2.0/31% (2) | LIV(H) 1.4/27% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.7/35% (3) | COV(A) 1.4/32% (2) |
| ★ BRE | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.5/16% (4) | ARS(H) 1.1/19% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.4/21% (3) | NEW(H) 2.2/30% (3) | IPS(A) 1.8/20% (2) |
| SUN | CHE(H) 1.6/24% (4) | AVL(A) 1.4/22% (3) | TOT(H) 1.6/31% (2) | LIV(A) 1.1/15% (4) | NEW(A) 1.6/22% (3) | NFO(H) 1.5/20% (3) | CRY(H) 2.0/25% (2) | EVE(A) 1.4/20% (3) |
| CRY | LIV(H) 1.3/19% (4) | COV(A) 1.3/24% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/14% (4) | AVL(A) 1.3/19% (3) | MUN(H) 1.6/19% (4) | SUN(A) 1.4/13% (3) | ARS(H) 1.0/15% (4) |
| ★ AVL | MUN(A) 1.1/17% (4) | SUN(H) 1.5/25% (3) | IPS(A) 1.4/22% (2) | EVE(H) 1.4/30% (3) | CRY(H) 1.7/28% (2) | COV(A) 1.2/30% (2) | CHE(A) 1.0/19% (4) | LEE(H) 1.3/29% (3) |
| FUL | NEW(H) 1.8/33% (3) | MCI(A) 1.1/12% (5) | BOU(H) 1.3/24% (3) | TOT(A) 1.1/27% (3) | EVE(A) 1.2/23% (3) | BRE(H) 1.6/24% (3) | LEE(A) 1.1/22% (3) | BHA(H) 1.5/18% (3) |
| ★ LEE | TOT(H) 1.4/38% (2) | CHE(A) 1.1/22% (4) | COV(H) 1.6/41% (2) | MCI(A) 1.1/14% (5) | IPS(H) 1.9/33% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.5/33% (2) | AVL(A) 1.2/28% (3) |
| IPS | BOU(H) 1.3/17% (3) | TOT(A) 1.1/19% (3) | AVL(H) 1.5/25% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.1/15% (3) | NEW(H) 1.8/24% (3) | BHA(A) 1.2/7% (4) | BRE(H) 1.6/17% (3) |
| EVE | COV(H) 1.5/38% (2) | BRE(A) 1.2/16% (3) | LIV(H) 1.2/24% (4) | AVL(A) 1.2/24% (3) | FUL(H) 1.5/30% (2) | BHA(A) 1.1/11% (4) | NFO(A) 1.1/15% (3) | SUN(H) 1.6/25% (3) |
| TOT | LEE(A) 1.0/24% (3) | IPS(H) 1.7/32% (2) | SUN(A) 1.2/20% (3) | FUL(H) 1.3/33% (2) | ARS(H) 0.8/23% (4) | HUL(A) 1.2/32% (2) | LIV(A) 0.9/20% (4) | BOU(H) 1.2/26% (3) |
| COV | EVE(A) 1.0/21% (3) | CRY(H) 1.4/27% (2) | LEE(A) 0.9/20% (3) | IPS(H) 1.5/28% (2) | MUN(A) 1.0/16% (4) | AVL(H) 1.2/31% (3) | BOU(A) 0.8/15% (3) | CHE(H) 1.1/25% (4) |
| ★ NEW | FUL(A) 1.1/16% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/19% (4) | SUN(H) 1.5/19% (3) | IPS(A) 1.4/16% (2) | BRE(A) 1.2/12% (3) | MCI(H) 1.3/13% (4) |
| ★ HUL | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/16% (3) | NFO(H) 1.1/18% (3) | BOU(A) 0.9/13% (3) | TOT(H) 1.1/29% (2) | MCI(A) 0.9/8% (5) | LIV(H) 1.0/20% (4) |
