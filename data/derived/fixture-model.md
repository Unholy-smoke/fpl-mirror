# Fixture model v0.2 — GW7–14

**Generated** 2026-10-11 15:59 UTC from mirror `2026-10-11T15:58:47Z`.
**Observed** 6 gameweek(s) — [1, 2, 3, 4, 5, 6]. With k=6 pseudo-matches, ratings are **50% prior / 50% data** for the 16 clubs on 6 matches, and **55% / 45%** for the 4 on 5. That weight shifts toward data every week.

League mean xG per team-match **1.53**; home 1.71 / away 1.36 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: COV, LIV, MCI, NEW on 5.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW7–10, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW6 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG7–10 | CS7–10 | xG7–14 | CS7–14 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.27 *(1.40)* | 0.88 | **8.03** | 1.02 | 15.24 | 2.02 | +2.2 | Haaland |
| ★ BHA | 1.28 *(1.41)* | 0.99 | **7.85** | 0.78 | 15.72 | 1.75 | +5.0 | De Cuyper, Groß |
| ★ ARS | 1.20 *(1.18)* | 0.61 | **7.34** | 1.63 | 14.31 | 3.14 | -0.8 | Raya, Calafiori, Saka |
| SUN | 1.14 *(1.15)* | 1.00 | **7.00** | 1.00 | 13.73 | 1.93 | -4.6 |  |
| MUN | 1.10 *(1.20)* | 0.96 | **6.65** | 1.02 | 13.60 | 2.05 | -2.1 |  |
| ★ FUL | 0.97 *(1.04)* | 1.08 | **6.60** | 1.06 | 11.94 | 1.81 | -3.6 | Gonzalo |
| ★ BRE | 1.08 *(1.23)* | 1.01 | **6.46** | 0.83 | 12.47 | 1.62 | +0.7 | Schade |
| LIV | 1.09 *(1.09)* | 0.87 | **6.24** | 0.90 | 12.90 | 1.90 | -1.4 |  |
| ★ CHE | 1.02 *(0.92)* | 1.01 | **6.15** | 0.87 | 12.68 | 1.79 | +6.5 | Rogers, João Pedro |
| CRY | 0.97 *(0.94)* | 1.19 | **5.96** | 0.68 | 11.95 | 1.48 | +0.4 |  |
| NFO | 1.07 *(1.14)* | 0.93 | **5.89** | 0.83 | 12.61 | 1.82 | -5.5 |  |
| BOU | 0.92 *(0.89)* | 0.95 | **5.75** | 0.92 | 11.92 | 1.94 | -1.2 |  |
| ★ LEE | 0.95 *(0.93)* | 0.96 | **5.68** | 0.94 | 11.74 | 1.92 | -0.6 | Muharemović |
| EVE | 0.95 *(0.96)* | 1.01 | **5.66** | 0.96 | 11.44 | 1.83 | -0.8 |  |
| TOT | 0.85 *(0.72)* | 0.98 | **5.53** | 1.02 | 10.78 | 1.94 | -3.6 |  |
| ★ NEW | 0.84 *(0.69)* | 1.17 | **5.52** | 0.76 | 10.34 | 1.32 | +3.7 | Hall, Barnes |
| IPS | 0.91 *(0.97)* | 1.15 | **5.41** | 0.72 | 10.74 | 1.55 | +0.1 |  |
| AVL | 0.86 *(0.75)* | 1.03 | **5.38** | 0.79 | 11.44 | 1.71 | -0.9 |  |
| COV | 0.77 *(0.64)* | 1.07 | **4.80** | 0.82 | 9.88 | 1.64 | -3.9 |  |
| ★ HUL | 0.77 *(0.73)* | 1.15 | **4.63** | 0.68 | 9.42 | 1.31 | +1.3 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW7 | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | IPS(H) 2.5/34% (2) | AVL(A) 1.8/27% (3) | BHA(H) 2.1/21% (3) | NFO(A) 1.6/20% (3) | FUL(H) 2.3/31% (2) | ARS(A) 1.1/17% (5) | LEE(H) 2.1/32% (3) | BRE(A) 1.7/20% (3) |
| ★ BHA | CRY(H) 2.6/27% (2) | LIV(A) 1.5/16% (4) | MCI(A) 1.5/12% (5) | BRE(H) 2.2/23% (3) | HUL(A) 2.0/27% (2) | NEW(H) 2.6/32% (3) | BOU(A) 1.7/21% (3) | NFO(A) 1.6/16% (3) |
| ★ ARS | NFO(A) 1.5/33% (3) | EVE(H) 2.1/46% (3) | LIV(A) 1.4/32% (4) | HUL(H) 2.3/53% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/33% (3) | TOT(A) 1.6/42% (3) |
| SUN | BOU(A) 1.5/21% (3) | LEE(H) 1.9/27% (3) | COV(A) 1.7/27% (2) | CHE(H) 2.0/25% (4) | AVL(A) 1.6/23% (3) | TOT(H) 1.9/31% (2) | LIV(A) 1.4/15% (4) | NEW(A) 1.8/24% (3) |
| MUN | LEE(A) 1.4/21% (3) | BOU(H) 1.8/30% (3) | CHE(A) 1.5/19% (4) | AVL(H) 1.9/32% (3) | LIV(A) 1.3/17% (4) | BRE(H) 1.9/24% (3) | NEW(A) 1.8/25% (3) | COV(H) 2.0/37% (2) |
| ★ FUL | HUL(H) 1.9/32% (2) | COV(A) 1.4/24% (2) | AVL(A) 1.4/21% (3) | NEW(H) 1.9/29% (3) | MCI(A) 1.2/10% (5) | BOU(H) 1.6/26% (3) | TOT(A) 1.3/21% (3) | EVE(A) 1.3/18% (3) |
| ★ BRE | LIV(H) 1.6/22% (4) | HUL(A) 1.7/27% (2) | NFO(H) 1.7/23% (3) | BHA(A) 1.5/11% (4) | EVE(H) 1.9/27% (3) | MUN(A) 1.4/15% (4) | ARS(H) 1.1/19% (4) | MCI(H) 1.6/18% (4) |
| LIV | BRE(A) 1.5/20% (3) | BHA(H) 1.8/22% (3) | ARS(H) 1.1/24% (4) | CRY(A) 1.8/24% (3) | MUN(H) 1.8/27% (4) | EVE(A) 1.5/25% (3) | SUN(H) 1.9/26% (3) | CHE(A) 1.5/22% (4) |
| ★ CHE | EVE(A) 1.4/20% (3) | TOT(H) 1.7/31% (2) | MUN(H) 1.7/22% (4) | SUN(A) 1.4/14% (3) | LEE(H) 1.7/27% (3) | NFO(A) 1.3/16% (3) | CRY(H) 2.1/27% (2) | LIV(H) 1.5/22% (4) |
| CRY | BHA(A) 1.3/7% (4) | NEW(H) 1.9/26% (3) | TOT(A) 1.3/18% (3) | LIV(H) 1.4/17% (4) | COV(A) 1.4/21% (2) | HUL(H) 1.9/29% (2) | CHE(A) 1.3/13% (4) | AVL(A) 1.4/17% (3) |
| NFO | ARS(H) 1.1/22% (4) | IPS(A) 1.7/24% (2) | BRE(A) 1.5/18% (3) | MCI(H) 1.6/20% (4) | BOU(A) 1.4/23% (3) | CHE(H) 1.8/27% (4) | HUL(A) 1.7/29% (2) | BHA(H) 1.8/20% (3) |
| BOU | SUN(H) 1.6/23% (3) | MUN(A) 1.2/17% (4) | LEE(H) 1.5/29% (3) | IPS(A) 1.4/23% (2) | NFO(H) 1.5/25% (3) | FUL(A) 1.4/21% (3) | BHA(H) 1.6/19% (3) | HUL(H) 1.8/37% (2) |
| ★ LEE | MUN(H) 1.6/24% (4) | SUN(A) 1.3/15% (3) | BOU(A) 1.2/22% (3) | TOT(H) 1.6/33% (2) | CHE(A) 1.3/19% (4) | COV(H) 1.7/36% (2) | MCI(A) 1.1/12% (5) | IPS(H) 1.9/30% (2) |
| EVE | CHE(H) 1.6/25% (4) | ARS(A) 0.8/13% (5) | NEW(A) 1.5/24% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.3/16% (3) | LIV(H) 1.4/22% (4) | AVL(A) 1.3/23% (3) | FUL(H) 1.7/27% (2) |
| TOT | COV(H) 1.5/36% (2) | CHE(A) 1.2/18% (4) | CRY(H) 1.7/27% (2) | LEE(A) 1.1/20% (3) | IPS(H) 1.7/30% (2) | SUN(A) 1.2/15% (3) | FUL(H) 1.6/27% (2) | ARS(H) 0.9/20% (4) |
| ★ NEW | AVL(H) 1.5/25% (3) | CRY(A) 1.4/14% (3) | EVE(H) 1.4/22% (3) | FUL(A) 1.2/14% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/17% (4) | SUN(H) 1.4/16% (3) |
| IPS | MCI(A) 1.1/8% (5) | NFO(H) 1.4/18% (3) | HUL(A) 1.4/22% (2) | BOU(H) 1.5/24% (3) | TOT(A) 1.2/19% (3) | AVL(H) 1.6/26% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.2/15% (3) |
| AVL | NEW(A) 1.4/23% (3) | MCI(H) 1.3/17% (4) | FUL(H) 1.6/26% (2) | MUN(A) 1.1/14% (4) | SUN(H) 1.5/20% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/26% (3) | CRY(H) 1.7/26% (2) |
| COV | TOT(A) 1.0/21% (3) | FUL(H) 1.4/24% (2) | SUN(H) 1.3/19% (3) | EVE(A) 1.1/18% (3) | CRY(H) 1.6/24% (2) | LEE(A) 1.0/18% (3) | IPS(H) 1.5/27% (2) | MUN(A) 1.0/13% (4) |
| ★ HUL | FUL(A) 1.1/15% (3) | BRE(H) 1.3/18% (3) | IPS(H) 1.5/24% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.3/13% (3) | CRY(A) 1.3/15% (3) | NFO(H) 1.2/19% (3) | BOU(A) 1.0/17% (3) |
