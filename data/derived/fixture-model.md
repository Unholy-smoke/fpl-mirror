# Fixture model v0.2 — GW7–14

**Generated** 2026-10-10 19:33 UTC from mirror `2026-10-10T19:33:25Z`.
**Observed** 6 gameweek(s) — [1, 2, 3, 4, 5, 6]. With k=6 pseudo-matches, ratings are **50% prior / 50% data** for the 12 clubs on 6 matches, and **55% / 45%** for the 8 on 5. That weight shifts toward data every week.

League mean xG per team-match **1.51**; home 1.68 / away 1.34 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: COV, CRY, EVE, HUL, LIV, MCI, NEW, NFO on 5.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW7–10, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW6 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG7–10 | CS7–10 | xG7–14 | CS7–14 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.29 *(1.42)* | 0.89 | **8.00** | 1.06 | 15.21 | 2.05 | +2.2 | Haaland |
| ★ BHA | 1.29 *(1.43)* | 0.99 | **7.57** | 0.81 | 15.25 | 1.80 | +5.0 | De Cuyper, Groß |
| ★ ARS | 1.20 *(1.20)* | 0.61 | **7.20** | 1.67 | 14.07 | 3.18 | -0.8 | Raya, Calafiori, Saka |
| SUN | 1.15 *(1.17)* | 1.01 | **7.02** | 1.00 | 13.79 | 1.95 | -4.6 |  |
| MUN | 1.10 *(1.22)* | 0.96 | **6.67** | 1.04 | 13.53 | 2.07 | -2.0 |  |
| ★ FUL | 0.98 *(1.06)* | 1.09 | **6.63** | 1.07 | 12.01 | 1.81 | -3.6 | Gonzalo |
| ★ BRE | 1.09 *(1.26)* | 0.98 | **6.36** | 0.90 | 12.39 | 1.74 | +0.5 | Schade |
| ★ CHE | 1.02 *(0.94)* | 1.02 | **6.12** | 0.88 | 12.43 | 1.83 | +6.5 | Rogers, João Pedro |
| LIV | 1.11 *(1.11)* | 0.89 | **6.08** | 0.91 | 12.75 | 1.90 | -1.4 |  |
| BOU | 0.93 *(0.91)* | 0.95 | **5.77** | 0.92 | 11.85 | 1.97 | -1.3 |  |
| ★ LEE | 0.97 *(0.95)* | 0.98 | **5.70** | 0.93 | 11.81 | 1.90 | -0.6 | Muharemović |
| CRY | 0.91 *(0.81)* | 1.11 | **5.59** | 0.77 | 11.20 | 1.68 | -0.1 |  |
| EVE | 0.94 *(0.94)* | 1.02 | **5.58** | 0.96 | 11.28 | 1.84 | -1.1 |  |
| ★ NEW | 0.84 *(0.70)* | 1.18 | **5.43** | 0.79 | 10.21 | 1.36 | +3.7 | Hall, Barnes |
| NFO | 1.01 *(1.00)* | 0.88 | **5.42** | 0.92 | 11.64 | 2.00 | -3.5 |  |
| TOT | 0.85 *(0.73)* | 0.99 | **5.41** | 1.04 | 10.65 | 1.95 | -3.6 |  |
| IPS | 0.92 *(0.98)* | 1.16 | **5.32** | 0.74 | 10.72 | 1.57 | +0.1 |  |
| AVL | 0.85 *(0.70)* | 1.06 | **5.25** | 0.77 | 11.02 | 1.69 | -0.4 |  |
| COV | 0.78 *(0.65)* | 1.08 | **4.82** | 0.82 | 9.80 | 1.66 | -3.9 |  |
| ★ HUL | 0.78 *(0.71)* | 1.14 | **4.57** | 0.69 | 9.17 | 1.39 | +0.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW7 | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | IPS(H) 2.5/33% (2) | AVL(A) 1.8/28% (3) | BHA(H) 2.1/22% (3) | NFO(A) 1.5/22% (3) | FUL(H) 2.4/31% (2) | ARS(A) 1.1/17% (5) | LEE(H) 2.1/32% (3) | BRE(A) 1.7/20% (3) |
| ★ BHA | CRY(H) 2.4/30% (2) | LIV(A) 1.5/16% (4) | MCI(A) 1.5/12% (5) | BRE(H) 2.1/23% (3) | HUL(A) 2.0/27% (2) | NEW(H) 2.5/32% (3) | BOU(A) 1.6/21% (3) | NFO(A) 1.5/19% (3) |
| ★ ARS | NFO(A) 1.4/36% (3) | EVE(H) 2.1/46% (3) | LIV(A) 1.4/32% (4) | HUL(H) 2.3/53% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.8/35% (4) | BRE(A) 1.6/33% (3) | TOT(A) 1.6/42% (3) |
| SUN | BOU(A) 1.5/21% (3) | LEE(H) 1.9/27% (3) | COV(A) 1.7/27% (2) | CHE(H) 2.0/25% (4) | AVL(A) 1.6/24% (3) | TOT(H) 1.9/32% (2) | LIV(A) 1.4/15% (4) | NEW(A) 1.8/24% (3) |
| MUN | LEE(A) 1.4/21% (3) | BOU(H) 1.8/30% (3) | CHE(A) 1.5/19% (4) | AVL(H) 2.0/33% (3) | LIV(A) 1.3/17% (4) | BRE(H) 1.8/24% (3) | NEW(A) 1.7/26% (3) | COV(H) 2.0/37% (2) |
| ★ FUL | HUL(H) 1.9/32% (2) | COV(A) 1.4/24% (2) | AVL(A) 1.4/21% (3) | NEW(H) 1.9/29% (3) | MCI(A) 1.2/10% (5) | BOU(H) 1.6/26% (3) | TOT(A) 1.3/21% (3) | EVE(A) 1.3/18% (3) |
| ★ BRE | LIV(H) 1.6/23% (4) | HUL(A) 1.7/28% (2) | NFO(H) 1.6/27% (3) | BHA(A) 1.5/12% (4) | EVE(H) 1.9/29% (3) | MUN(A) 1.4/16% (4) | ARS(H) 1.1/21% (4) | MCI(H) 1.6/18% (4) |
| ★ CHE | EVE(A) 1.4/20% (3) | TOT(H) 1.7/31% (2) | MUN(H) 1.6/22% (4) | SUN(A) 1.4/14% (3) | LEE(H) 1.7/27% (3) | NFO(A) 1.2/18% (3) | CRY(H) 1.9/29% (2) | LIV(H) 1.5/22% (4) |
| LIV | BRE(A) 1.5/20% (3) | BHA(H) 1.8/22% (3) | ARS(H) 1.1/24% (4) | CRY(A) 1.6/26% (3) | MUN(H) 1.8/27% (4) | EVE(A) 1.5/25% (3) | SUN(H) 1.9/25% (3) | CHE(A) 1.5/22% (4) |
| BOU | SUN(H) 1.6/23% (3) | MUN(A) 1.2/17% (4) | LEE(H) 1.5/29% (3) | IPS(A) 1.5/23% (2) | NFO(H) 1.4/28% (3) | FUL(A) 1.4/21% (3) | BHA(H) 1.6/19% (3) | HUL(H) 1.8/37% (2) |
| ★ LEE | MUN(H) 1.6/24% (4) | SUN(A) 1.3/15% (3) | BOU(A) 1.2/22% (3) | TOT(H) 1.6/33% (2) | CHE(A) 1.3/19% (4) | COV(H) 1.8/36% (2) | MCI(A) 1.2/12% (5) | IPS(H) 1.9/30% (2) |
| CRY | BHA(A) 1.2/9% (4) | NEW(H) 1.8/28% (3) | TOT(A) 1.2/20% (3) | LIV(H) 1.4/19% (4) | COV(A) 1.3/24% (2) | HUL(H) 1.7/31% (2) | CHE(A) 1.2/15% (4) | AVL(A) 1.3/21% (3) |
| EVE | CHE(H) 1.6/25% (4) | ARS(A) 0.8/13% (5) | NEW(A) 1.5/24% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/16% (3) | LIV(H) 1.4/22% (4) | AVL(A) 1.3/24% (3) | FUL(H) 1.7/26% (2) |
| ★ NEW | AVL(H) 1.5/26% (3) | CRY(A) 1.3/16% (3) | EVE(H) 1.4/23% (3) | FUL(A) 1.2/14% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.4/18% (4) | SUN(H) 1.4/16% (3) |
| NFO | ARS(H) 1.0/24% (4) | IPS(A) 1.6/26% (2) | BRE(A) 1.3/20% (3) | MCI(H) 1.5/22% (4) | BOU(A) 1.3/25% (3) | CHE(H) 1.7/30% (4) | HUL(A) 1.5/32% (2) | BHA(H) 1.7/22% (3) |
| TOT | COV(H) 1.5/36% (2) | CHE(A) 1.2/18% (4) | CRY(H) 1.6/30% (2) | LEE(A) 1.1/20% (3) | IPS(H) 1.7/29% (2) | SUN(A) 1.2/15% (3) | FUL(H) 1.6/27% (2) | ARS(H) 0.9/20% (4) |
| IPS | MCI(A) 1.1/8% (5) | NFO(H) 1.4/21% (3) | HUL(A) 1.4/22% (2) | BOU(H) 1.5/23% (3) | TOT(A) 1.2/19% (3) | AVL(H) 1.6/27% (3) | COV(A) 1.3/22% (2) | LEE(A) 1.2/15% (3) |
| AVL | NEW(A) 1.3/22% (3) | MCI(H) 1.3/16% (4) | FUL(H) 1.5/25% (2) | MUN(A) 1.1/14% (4) | SUN(H) 1.4/19% (3) | IPS(A) 1.3/20% (2) | EVE(H) 1.4/26% (3) | CRY(H) 1.6/27% (2) |
| COV | TOT(A) 1.0/21% (3) | FUL(H) 1.4/24% (2) | SUN(H) 1.3/19% (3) | EVE(A) 1.1/18% (3) | CRY(H) 1.4/27% (2) | LEE(A) 1.0/17% (3) | IPS(H) 1.5/26% (2) | MUN(A) 1.0/14% (4) |
| ★ HUL | FUL(A) 1.1/15% (3) | BRE(H) 1.3/19% (3) | IPS(H) 1.5/25% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.3/14% (3) | CRY(A) 1.2/18% (3) | NFO(H) 1.1/22% (3) | BOU(A) 1.0/17% (3) |
