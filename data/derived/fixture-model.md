# Fixture model v0.2 — GW8–15

**Generated** 2026-10-17 11:34 UTC from mirror `2026-10-17T11:34:00Z`.
**Observed** 6 gameweek(s) — [1, 2, 3, 4, 5, 6]. With k=6 pseudo-matches, ratings are **50% prior / 50% data** for all 20 clubs on 6 matches. That weight shifts toward data every week.

League mean xG per team-match **1.53**; home 1.70 / away 1.36 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW8–11, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW7 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG8–11 | CS8–11 | xG8–15 | CS8–15 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.25 *(1.31)* | 0.85 | **7.73** | 1.05 | 14.64 | 2.08 | +4.0 | Haaland |
| ★ ARS | 1.20 *(1.18)* | 0.61 | **7.67** | 1.73 | 14.57 | 3.29 | -0.8 | Raya, Calafiori, Saka |
| SUN | 1.15 *(1.15)* | 1.01 | **7.24** | 1.02 | 14.21 | 1.94 | -4.6 |  |
| ★ BHA | 1.28 *(1.41)* | 0.99 | **7.13** | 0.80 | 15.16 | 1.76 | +5.0 | De Cuyper, Groß |
| ★ BRE | 1.08 *(1.23)* | 1.00 | **6.70** | 0.88 | 12.38 | 1.60 | +0.7 | Schade |
| MUN | 1.10 *(1.20)* | 0.96 | **6.50** | 0.99 | 14.03 | 2.04 | -2.1 |  |
| ★ CHE | 1.02 *(0.93)* | 1.01 | **6.41** | 0.95 | 12.45 | 1.72 | +6.5 | Rogers, João Pedro |
| LIV | 1.06 *(1.01)* | 0.85 | **6.33** | 1.00 | 12.75 | 2.07 | -2.3 |  |
| NFO | 1.09 *(1.18)* | 0.94 | **6.20** | 0.85 | 13.09 | 1.76 | -5.8 |  |
| CRY | 0.97 *(0.94)* | 1.21 | **6.12** | 0.80 | 12.29 | 1.54 | +0.3 |  |
| ★ FUL | 0.96 *(1.05)* | 1.07 | **5.87** | 0.83 | 11.68 | 1.69 | -3.6 | Gonzalo |
| TOT | 0.85 *(0.72)* | 0.98 | **5.66** | 0.96 | 10.55 | 1.86 | -3.6 |  |
| BOU | 0.92 *(0.89)* | 0.95 | **5.65** | 0.93 | 11.11 | 1.85 | -1.2 |  |
| IPS | 0.91 *(0.97)* | 1.15 | **5.53** | 0.83 | 11.50 | 1.71 | +0.1 |  |
| AVL | 0.86 *(0.75)* | 1.03 | **5.43** | 0.77 | 11.34 | 1.75 | -0.9 |  |
| ★ LEE | 0.95 *(0.93)* | 0.96 | **5.42** | 0.89 | 11.29 | 1.87 | -0.6 | Muharemović |
| EVE | 0.95 *(0.96)* | 1.00 | **5.39** | 0.86 | 11.10 | 1.71 | -0.8 |  |
| COV | 0.77 *(0.70)* | 1.11 | **5.35** | 0.80 | 10.22 | 1.61 | -1.4 |  |
| ★ NEW | 0.87 *(0.78)* | 1.18 | **5.11** | 0.65 | 10.58 | 1.22 | +2.8 | Hall, Barnes |
| ★ HUL | 0.77 *(0.73)* | 1.14 | **4.77** | 0.67 | 9.56 | 1.44 | +1.3 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 | GW14 | GW15 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | AVL(A) 1.8/29% (3) | BHA(H) 2.1/23% (3) | NFO(A) 1.6/21% (3) | FUL(H) 2.3/33% (2) | ARS(A) 1.0/18% (5) | LEE(H) 2.0/33% (3) | BRE(A) 1.7/21% (3) | CHE(H) 2.1/31% (4) |
| ★ ARS | EVE(H) 2.0/46% (3) | LIV(A) 1.4/34% (4) | HUL(H) 2.3/53% (2) | NEW(A) 1.9/41% (3) | MCI(H) 1.7/36% (4) | BRE(A) 1.6/33% (3) | TOT(A) 1.6/42% (3) | BOU(H) 1.9/47% (3) |
| SUN | LEE(H) 1.9/27% (3) | COV(A) 1.8/27% (2) | CHE(H) 2.0/25% (4) | AVL(A) 1.6/23% (3) | TOT(H) 1.9/31% (2) | LIV(A) 1.3/16% (4) | NEW(A) 1.9/22% (3) | NFO(H) 1.8/22% (3) |
| ★ BHA | LIV(A) 1.5/17% (4) | MCI(A) 1.5/12% (5) | BRE(H) 2.2/23% (3) | HUL(A) 2.0/27% (2) | NEW(H) 2.6/31% (3) | BOU(A) 1.7/21% (3) | NFO(A) 1.6/16% (3) | EVE(H) 2.2/28% (3) |
| ★ BRE | HUL(A) 1.7/27% (2) | NFO(H) 1.7/22% (3) | BHA(A) 1.5/11% (4) | EVE(H) 1.8/27% (3) | MUN(A) 1.4/15% (4) | ARS(H) 1.1/20% (4) | MCI(H) 1.6/18% (4) | FUL(A) 1.6/19% (3) |
| MUN | BOU(H) 1.8/30% (3) | CHE(A) 1.5/19% (4) | AVL(H) 1.9/32% (3) | LIV(A) 1.3/18% (4) | BRE(H) 1.9/24% (3) | NEW(A) 1.8/24% (3) | COV(H) 2.1/37% (2) | CRY(A) 1.8/20% (3) |
| ★ CHE | TOT(H) 1.7/31% (2) | MUN(H) 1.7/22% (4) | SUN(A) 1.4/14% (3) | LEE(H) 1.7/27% (3) | NFO(A) 1.3/15% (3) | CRY(H) 2.1/26% (2) | LIV(H) 1.5/24% (4) | MCI(A) 1.2/12% (5) |
| LIV | BHA(H) 1.8/23% (3) | ARS(H) 1.1/25% (4) | CRY(A) 1.7/24% (3) | MUN(H) 1.7/28% (4) | EVE(A) 1.4/25% (3) | SUN(H) 1.8/26% (3) | CHE(A) 1.4/23% (4) | LEE(H) 1.7/33% (3) |
| NFO | IPS(A) 1.7/24% (2) | BRE(A) 1.5/18% (3) | MCI(H) 1.6/20% (4) | BOU(A) 1.4/23% (3) | CHE(H) 1.9/27% (4) | HUL(A) 1.7/29% (2) | BHA(H) 1.8/20% (3) | SUN(A) 1.5/16% (3) |
| CRY | NEW(H) 1.9/24% (3) | TOT(A) 1.3/18% (3) | LIV(H) 1.4/18% (4) | COV(A) 1.5/21% (2) | HUL(H) 1.9/28% (2) | CHE(A) 1.3/12% (4) | AVL(A) 1.4/17% (3) | MUN(H) 1.6/16% (4) |
| ★ FUL | COV(A) 1.5/24% (2) | AVL(A) 1.4/21% (3) | NEW(H) 1.9/28% (3) | MCI(A) 1.1/10% (5) | BOU(H) 1.6/26% (3) | TOT(A) 1.3/21% (3) | EVE(A) 1.3/18% (3) | BRE(H) 1.6/21% (3) |
| TOT | CHE(A) 1.2/18% (4) | CRY(H) 1.7/27% (2) | LEE(A) 1.1/21% (3) | IPS(H) 1.7/30% (2) | SUN(A) 1.2/15% (3) | FUL(H) 1.5/28% (2) | ARS(H) 0.9/20% (4) | HUL(A) 1.3/28% (2) |
| BOU | MUN(A) 1.2/17% (4) | LEE(H) 1.5/29% (3) | IPS(A) 1.5/23% (2) | NFO(H) 1.5/24% (3) | FUL(A) 1.4/21% (3) | BHA(H) 1.6/19% (3) | HUL(H) 1.8/37% (2) | ARS(A) 0.8/14% (5) |
| IPS | NFO(H) 1.4/18% (3) | HUL(A) 1.4/22% (2) | BOU(H) 1.5/23% (3) | TOT(A) 1.2/19% (3) | AVL(H) 1.6/26% (3) | COV(A) 1.4/22% (2) | LEE(A) 1.2/16% (3) | NEW(H) 1.8/25% (3) |
| AVL | MCI(H) 1.2/17% (4) | FUL(H) 1.6/26% (2) | MUN(A) 1.1/14% (4) | SUN(H) 1.5/20% (3) | IPS(A) 1.4/20% (2) | EVE(H) 1.5/26% (3) | CRY(H) 1.8/26% (2) | COV(A) 1.3/26% (2) |
| ★ LEE | SUN(A) 1.3/15% (3) | BOU(A) 1.2/22% (3) | TOT(H) 1.6/33% (2) | CHE(A) 1.3/19% (4) | COV(H) 1.8/37% (2) | MCI(A) 1.1/13% (5) | IPS(H) 1.9/31% (2) | LIV(A) 1.1/18% (4) |
| EVE | ARS(A) 0.8/13% (5) | NEW(A) 1.5/22% (3) | COV(H) 1.8/35% (2) | BRE(A) 1.3/16% (3) | LIV(H) 1.4/24% (4) | AVL(A) 1.3/23% (3) | FUL(H) 1.7/27% (2) | BHA(A) 1.3/11% (4) |
| COV | FUL(H) 1.4/23% (2) | SUN(H) 1.3/17% (3) | EVE(A) 1.1/17% (3) | CRY(H) 1.6/23% (2) | LEE(A) 1.0/16% (3) | IPS(H) 1.5/25% (2) | MUN(A) 1.0/12% (4) | AVL(H) 1.4/27% (3) |
| ★ NEW | CRY(A) 1.4/14% (3) | EVE(H) 1.5/22% (3) | FUL(A) 1.3/14% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.2/8% (4) | MUN(H) 1.4/17% (4) | SUN(H) 1.5/16% (3) | IPS(A) 1.4/16% (2) |
| ★ HUL | BRE(H) 1.3/19% (3) | IPS(H) 1.5/24% (2) | ARS(A) 0.6/10% (5) | BHA(H) 1.3/14% (3) | CRY(A) 1.3/15% (3) | NFO(H) 1.2/18% (3) | BOU(A) 1.0/17% (3) | TOT(H) 1.3/27% (2) |
