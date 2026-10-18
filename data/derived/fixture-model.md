# Fixture model v0.2 — GW8–15

**Generated** 2026-10-18 08:21 UTC from mirror `2026-10-18T08:20:32Z`.
**Observed** 7 gameweek(s) — [1, 2, 3, 4, 5, 6, 7]. With k=6 pseudo-matches, ratings are **46% prior / 54% data** for the 10 clubs on 7 matches, and **50% / 50%** for the 10 on 6. That weight shifts toward data every week.

League mean xG per team-match **1.52**; home 1.69 / away 1.35 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: ARS, BOU, BHA, COV, CRY, LEE, MUN, NFO, TOT, SUN on 6.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW8–11, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW7 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG8–11 | CS8–11 | xG8–15 | CS8–15 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.29 *(1.46)* | 0.89 | **7.74** | 0.99 | 14.78 | 1.97 | +3.4 | Haaland |
| ★ ARS | 1.20 *(1.19)* | 0.61 | **7.66** | 1.78 | 14.69 | 3.35 | -0.8 | Raya, Calafiori, Saka |
| ★ BHA | 1.29 *(1.42)* | 0.99 | **7.17** | 0.83 | 15.30 | 1.82 | +5.0 | De Cuyper, Groß |
| SUN | 1.15 *(1.16)* | 1.00 | **7.07** | 1.03 | 13.99 | 1.97 | -4.6 |  |
| ★ BRE | 1.05 *(1.14)* | 1.02 | **6.49** | 0.91 | 11.95 | 1.62 | +0.8 | Schade |
| ★ CHE | 1.03 *(0.94)* | 0.96 | **6.49** | 1.01 | 12.57 | 1.83 | +7.0 | Rogers, João Pedro |
| NFO | 1.10 *(1.19)* | 0.94 | **6.39** | 0.83 | 13.22 | 1.78 | -5.8 |  |
| LIV | 1.07 *(1.03)* | 0.83 | **6.35** | 1.04 | 12.74 | 2.19 | -2.0 |  |
| MUN | 1.10 *(1.21)* | 0.97 | **6.32** | 0.98 | 13.85 | 2.05 | -2.1 |  |
| CRY | 0.98 *(0.95)* | 1.21 | **6.14** | 0.81 | 12.21 | 1.58 | +0.3 |  |
| ★ FUL | 0.95 *(1.04)* | 1.00 | **5.80** | 0.93 | 11.54 | 1.91 | -4.0 | Gonzalo |
| IPS | 0.95 *(0.99)* | 1.20 | **5.76** | 0.80 | 11.98 | 1.65 | +0.4 |  |
| BOU | 0.93 *(0.90)* | 0.96 | **5.70** | 0.91 | 11.04 | 1.85 | -1.2 |  |
| TOT | 0.85 *(0.73)* | 0.99 | **5.66** | 0.93 | 10.41 | 1.85 | -3.6 |  |
| AVL | 0.87 *(0.79)* | 1.01 | **5.40** | 0.81 | 11.39 | 1.83 | -1.5 |  |
| ★ LEE | 0.95 *(0.94)* | 0.96 | **5.35** | 0.89 | 11.28 | 1.85 | -0.6 | Muharemović |
| COV | 0.77 *(0.70)* | 1.12 | **5.20** | 0.82 | 10.06 | 1.62 | -1.4 |  |
| EVE | 0.89 *(0.87)* | 1.01 | **5.09** | 0.88 | 10.26 | 1.72 | -1.2 |  |
| ★ NEW | 0.86 *(0.77)* | 1.20 | **4.89** | 0.66 | 10.27 | 1.20 | +1.8 | Hall, Barnes |
| ★ HUL | 0.73 *(0.64)* | 1.13 | **4.53** | 0.67 | 9.02 | 1.46 | +1.2 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | AVL(A) 1.8/27% (3) | BHA(H) 2.2/21% (3) | NFO(A) 1.6/19% (3) | FUL(H) 2.2/32% (2) | ARS(A) 1.1/16% (5) | LEE(H) 2.1/32% (3) | BRE(A) 1.8/21% (3) | CHE(H) 2.1/29% (4) |
| ★ ARS | EVE(H) 2.1/48% (3) | LIV(A) 1.3/33% (4) | HUL(H) 2.3/55% (2) | NEW(A) 2.0/42% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.7/34% (3) | TOT(A) 1.6/42% (3) | BOU(H) 2.0/47% (3) |
| ★ BHA | LIV(A) 1.4/17% (4) | MCI(A) 1.5/12% (5) | BRE(H) 2.2/24% (3) | HUL(A) 2.0/30% (2) | NEW(H) 2.6/32% (3) | BOU(A) 1.7/21% (3) | NFO(A) 1.6/16% (3) | EVE(H) 2.2/30% (3) |
| SUN | LEE(H) 1.9/28% (3) | COV(A) 1.7/27% (2) | CHE(H) 1.9/25% (4) | AVL(A) 1.6/23% (3) | TOT(H) 1.9/32% (2) | LIV(A) 1.3/16% (4) | NEW(A) 1.9/24% (3) | NFO(H) 1.8/22% (3) |
| ★ BRE | HUL(A) 1.6/29% (2) | NFO(H) 1.7/22% (3) | BHA(A) 1.4/11% (4) | EVE(H) 1.8/29% (3) | MUN(A) 1.4/15% (4) | ARS(H) 1.1/19% (4) | MCI(H) 1.6/17% (4) | FUL(A) 1.4/20% (3) |
| ★ CHE | TOT(H) 1.7/33% (2) | MUN(H) 1.7/24% (4) | SUN(A) 1.4/15% (3) | LEE(H) 1.7/29% (3) | NFO(A) 1.3/17% (3) | CRY(H) 2.1/28% (2) | LIV(H) 1.4/25% (4) | MCI(A) 1.2/12% (5) |
| NFO | IPS(A) 1.8/22% (2) | BRE(A) 1.5/19% (3) | MCI(H) 1.7/19% (4) | BOU(A) 1.4/23% (3) | CHE(H) 1.8/27% (4) | HUL(A) 1.7/32% (2) | BHA(H) 1.8/19% (3) | SUN(A) 1.5/16% (3) |
| LIV | BHA(H) 1.8/24% (3) | ARS(H) 1.1/26% (4) | CRY(A) 1.7/26% (3) | MUN(H) 1.7/29% (4) | EVE(A) 1.5/29% (3) | SUN(H) 1.8/28% (3) | CHE(A) 1.4/24% (4) | LEE(H) 1.7/35% (3) |
| MUN | BOU(H) 1.8/30% (3) | CHE(A) 1.4/19% (4) | AVL(H) 1.9/32% (3) | LIV(A) 1.2/18% (4) | BRE(H) 1.9/25% (3) | NEW(A) 1.8/25% (3) | COV(H) 2.1/37% (2) | CRY(A) 1.8/20% (3) |
| CRY | NEW(H) 2.0/25% (3) | TOT(A) 1.3/18% (3) | LIV(H) 1.4/18% (4) | COV(A) 1.5/21% (2) | HUL(H) 1.9/31% (2) | CHE(A) 1.3/12% (4) | AVL(A) 1.3/17% (3) | MUN(H) 1.6/17% (4) |
| ★ FUL | COV(A) 1.4/27% (2) | AVL(A) 1.3/23% (3) | NEW(H) 1.9/31% (3) | MCI(A) 1.1/11% (5) | BOU(H) 1.5/28% (3) | TOT(A) 1.3/24% (3) | EVE(A) 1.3/22% (3) | BRE(H) 1.6/24% (3) |
| IPS | NFO(H) 1.5/17% (3) | HUL(A) 1.5/23% (2) | BOU(H) 1.5/22% (3) | TOT(A) 1.3/18% (3) | AVL(H) 1.6/24% (3) | COV(A) 1.4/21% (2) | LEE(A) 1.2/15% (3) | NEW(H) 1.9/25% (3) |
| BOU | MUN(A) 1.2/17% (4) | LEE(H) 1.5/29% (3) | IPS(A) 1.5/21% (2) | NFO(H) 1.5/24% (3) | FUL(A) 1.3/21% (3) | BHA(H) 1.5/19% (3) | HUL(H) 1.8/39% (2) | ARS(A) 0.8/14% (5) |
| TOT | CHE(A) 1.1/18% (4) | CRY(H) 1.7/27% (2) | LEE(A) 1.1/20% (3) | IPS(H) 1.7/28% (2) | SUN(A) 1.1/15% (3) | FUL(H) 1.4/28% (2) | ARS(H) 0.9/20% (4) | HUL(A) 1.3/30% (2) |
| AVL | MCI(H) 1.3/17% (4) | FUL(H) 1.5/27% (2) | MUN(A) 1.1/15% (4) | SUN(H) 1.5/21% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/30% (3) | CRY(H) 1.8/26% (2) | COV(A) 1.3/27% (2) |
| ★ LEE | SUN(A) 1.3/15% (3) | BOU(A) 1.2/22% (3) | TOT(H) 1.6/33% (2) | CHE(A) 1.2/19% (4) | COV(H) 1.8/37% (2) | MCI(A) 1.1/12% (5) | IPS(H) 1.9/29% (2) | LIV(A) 1.1/18% (4) |
| COV | FUL(H) 1.3/24% (2) | SUN(H) 1.3/17% (3) | EVE(A) 1.0/18% (3) | CRY(H) 1.6/23% (2) | LEE(A) 1.0/17% (3) | IPS(H) 1.6/24% (2) | MUN(A) 1.0/13% (4) | AVL(H) 1.3/27% (3) |
| EVE | ARS(A) 0.7/13% (5) | NEW(A) 1.4/23% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/17% (3) | LIV(H) 1.2/23% (4) | AVL(A) 1.2/23% (3) | FUL(H) 1.5/27% (2) | BHA(A) 1.2/11% (4) |
| ★ NEW | CRY(A) 1.4/14% (3) | EVE(H) 1.5/24% (3) | FUL(A) 1.2/15% (3) | ARS(H) 0.9/14% (4) | BHA(A) 1.1/7% (4) | MUN(H) 1.4/17% (4) | SUN(H) 1.4/15% (3) | IPS(A) 1.4/15% (2) |
| ★ HUL | BRE(H) 1.2/20% (3) | IPS(H) 1.5/23% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.2/14% (3) | CRY(A) 1.2/15% (3) | NFO(H) 1.2/18% (3) | BOU(A) 0.9/17% (3) | TOT(H) 1.2/27% (2) |
