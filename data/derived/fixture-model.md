# Fixture model v0.2 — GW6–13

**Generated** 2026-09-26 12:13 UTC from mirror `2026-09-26T12:12:31Z`.
**Observed** 5 gameweek(s) — [1, 2, 3, 4, 5]. With k=6 pseudo-matches, ratings are **55% prior / 45% data** for all 20 clubs on 5 matches. That weight shifts toward data every week.

League mean xG per team-match **1.53**; home 1.70 / away 1.36 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW6–9, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW5 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG6–9 | CS6–9 | xG6–13 | CS6–13 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | 1.28 *(1.40)* | 0.87 | **8.11** | 1.04 | 15.19 | 2.08 | +2.2 | Haaland |
| SUN | 1.22 *(1.28)* | 1.02 | **7.57** | 0.89 | 15.07 | 1.84 | -3.8 |  |
| ★ BHA | 1.30 *(1.51)* | 1.04 | **7.34** | 0.64 | 15.77 | 1.60 | +4.4 | Groß, Gomez, Verbruggen |
| ★ MUN | 1.16 *(1.34)* | 0.92 | **7.09** | 1.09 | 14.35 | 2.16 | -2.3 | B.Fernandes |
| ★ ARS | 1.17 *(1.11)* | 0.62 | **6.74** | 1.57 | 14.12 | 3.17 | -0.5 | Calafiori, Konsa |
| ★ CHE | 1.04 *(0.97)* | 1.00 | **6.64** | 1.03 | 12.99 | 1.89 | +2.6 | Rogers, João Pedro |
| BRE | 1.10 *(1.33)* | 0.95 | **6.62** | 1.08 | 12.59 | 1.87 | -0.2 |  |
| FUL | 0.96 *(1.02)* | 1.10 | **6.16** | 0.93 | 12.22 | 1.78 | -2.8 |  |
| LIV | 1.09 *(1.09)* | 0.88 | **6.13** | 0.86 | 12.89 | 1.84 | -1.4 |  |
| ★ IPS | 0.94 *(1.01)* | 1.12 | **5.78** | 0.76 | 11.82 | 1.74 | -0.8 | Diop |
| CRY | 0.91 *(0.79)* | 1.11 | **5.77** | 0.81 | 11.47 | 1.69 | -0.1 |  |
| BOU | 0.92 *(0.89)* | 0.98 | **5.50** | 0.79 | 11.31 | 1.64 | -0.8 |  |
| ★ NEW | 0.84 *(0.69)* | 1.18 | **5.47** | 0.87 | 10.11 | 1.39 | +3.7 | Hall, Elanga |
| COV | 0.77 *(0.64)* | 1.08 | **5.42** | 0.92 | 10.39 | 1.78 | -3.9 |  |
| AVL | 0.82 *(0.60)* | 1.08 | **5.37** | 0.81 | 10.45 | 1.52 | -0.6 |  |
| NFO | 0.99 *(0.98)* | 0.89 | **5.34** | 0.93 | 11.38 | 1.99 | -3.5 |  |
| EVE | 0.93 *(0.93)* | 1.01 | **5.31** | 0.87 | 11.02 | 1.84 | -1.1 |  |
| HUL | 0.78 *(0.70)* | 1.13 | **5.24** | 0.81 | 9.61 | 1.44 | +0.6 |  |
| ★ TOT | 0.81 *(0.66)* | 1.04 | **5.16** | 0.90 | 10.44 | 1.71 | -3.0 | Kinsky |
| ★ LEE | 0.97 *(1.04)* | 0.96 | **4.98** | 0.73 | 10.96 | 1.75 | -0.9 | Muharemović, Calvert-Lewin |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW6 | GW7 | GW8 | GW9 | GW10 | GW11 | GW12 | GW13 |
|---|---|---|---|---|---|---|---|---|
| ★ MCI | LIV(A) 1.5/20% (4) | IPS(H) 2.4/33% (2) | AVL(A) 1.9/30% (3) | BHA(H) 2.3/21% (3) | NFO(A) 1.5/23% (3) | FUL(H) 2.4/32% (2) | ARS(A) 1.1/18% (5) | LEE(H) 2.1/32% (3) |
| SUN | BHA(H) 2.2/17% (3) | BOU(A) 1.6/20% (3) | LEE(H) 2.0/26% (3) | COV(A) 1.8/26% (2) | CHE(H) 2.1/24% (4) | AVL(A) 1.8/24% (3) | TOT(H) 2.2/32% (2) | LIV(A) 1.5/15% (4) |
| ★ BHA | SUN(A) 1.8/11% (3) | CRY(H) 2.4/28% (2) | LIV(A) 1.6/14% (4) | MCI(A) 1.5/10% (5) | BRE(H) 2.1/21% (3) | HUL(A) 2.0/25% (2) | NEW(H) 2.6/30% (3) | BOU(A) 1.7/20% (3) |
| ★ MUN | TOT(H) 2.1/36% (2) | LEE(A) 1.5/22% (3) | BOU(H) 1.9/32% (3) | CHE(A) 1.6/20% (4) | AVL(H) 2.1/36% (3) | LIV(A) 1.4/18% (4) | BRE(H) 1.9/25% (3) | NEW(A) 1.9/27% (3) |
| ★ ARS | LEE(H) 1.9/44% (3) | NFO(A) 1.4/35% (3) | EVE(H) 2.0/46% (3) | LIV(A) 1.4/32% (4) | HUL(H) 2.3/52% (2) | NEW(A) 1.9/42% (3) | MCI(H) 1.7/34% (4) | BRE(A) 1.5/32% (3) |
| ★ CHE | BOU(H) 1.7/29% (3) | EVE(A) 1.4/20% (3) | TOT(H) 1.8/33% (2) | MUN(H) 1.6/21% (4) | SUN(A) 1.4/13% (3) | LEE(H) 1.7/27% (3) | NFO(A) 1.3/18% (3) | CRY(H) 2.0/29% (2) |
| BRE | AVL(A) 1.6/27% (3) | LIV(H) 1.7/24% (4) | HUL(A) 1.7/29% (2) | NFO(H) 1.7/28% (3) | BHA(A) 1.6/12% (4) | EVE(H) 1.9/30% (3) | MUN(A) 1.4/15% (4) | ARS(H) 1.2/22% (4) |
| FUL | IPS(A) 1.5/17% (2) | HUL(H) 1.9/31% (2) | COV(A) 1.4/24% (2) | AVL(A) 1.4/22% (3) | NEW(H) 1.9/28% (3) | MCI(A) 1.1/9% (5) | BOU(H) 1.6/25% (3) | TOT(A) 1.4/22% (3) |
| LIV | MCI(H) 1.6/22% (4) | BRE(A) 1.4/19% (3) | BHA(H) 1.9/21% (3) | ARS(H) 1.1/24% (4) | CRY(A) 1.6/25% (3) | MUN(H) 1.7/25% (4) | EVE(A) 1.5/25% (3) | SUN(H) 1.9/23% (3) |
| ★ IPS | FUL(H) 1.8/23% (2) | MCI(A) 1.1/9% (5) | NFO(H) 1.4/22% (3) | HUL(A) 1.5/23% (2) | BOU(H) 1.6/25% (3) | TOT(A) 1.3/21% (3) | AVL(H) 1.7/29% (3) | COV(A) 1.4/23% (2) |
| CRY | NFO(H) 1.4/22% (3) | BHA(A) 1.3/9% (4) | NEW(H) 1.8/28% (3) | TOT(A) 1.3/22% (3) | LIV(H) 1.4/19% (4) | COV(A) 1.3/24% (2) | HUL(H) 1.8/31% (2) | CHE(A) 1.2/14% (4) |
| BOU | CHE(A) 1.3/18% (4) | SUN(H) 1.6/20% (3) | MUN(A) 1.2/14% (4) | LEE(H) 1.5/27% (3) | IPS(A) 1.4/21% (2) | NFO(H) 1.4/26% (3) | FUL(A) 1.4/20% (3) | BHA(H) 1.6/18% (3) |
| ★ NEW | COV(A) 1.2/21% (2) | AVL(H) 1.5/27% (3) | CRY(A) 1.3/16% (3) | EVE(H) 1.4/22% (3) | FUL(A) 1.3/14% (3) | ARS(H) 0.9/15% (4) | BHA(A) 1.2/7% (4) | MUN(H) 1.3/16% (4) |
| COV | NEW(H) 1.5/29% (3) | TOT(A) 1.1/22% (3) | FUL(H) 1.4/24% (2) | SUN(H) 1.3/17% (3) | EVE(A) 1.1/18% (3) | CRY(H) 1.4/26% (2) | LEE(A) 1.0/17% (3) | IPS(H) 1.5/25% (2) |
| AVL | BRE(H) 1.3/20% (3) | NEW(A) 1.3/21% (3) | MCI(H) 1.2/15% (4) | FUL(H) 1.5/24% (2) | MUN(A) 1.0/12% (4) | SUN(H) 1.4/17% (3) | IPS(A) 1.2/18% (2) | EVE(H) 1.4/25% (3) |
| NFO | CRY(A) 1.5/25% (3) | ARS(H) 1.0/24% (4) | IPS(A) 1.5/24% (2) | BRE(A) 1.3/19% (3) | MCI(H) 1.5/21% (4) | BOU(A) 1.3/25% (3) | CHE(H) 1.7/29% (4) | HUL(A) 1.5/31% (2) |
| EVE | HUL(A) 1.4/26% (2) | CHE(H) 1.6/24% (4) | ARS(A) 0.8/13% (5) | NEW(A) 1.5/24% (3) | COV(H) 1.7/35% (2) | BRE(A) 1.2/15% (3) | LIV(H) 1.4/22% (4) | AVL(A) 1.4/25% (3) |
| HUL | EVE(H) 1.3/24% (3) | FUL(A) 1.2/16% (3) | BRE(H) 1.3/18% (3) | IPS(H) 1.5/23% (2) | ARS(A) 0.7/10% (5) | BHA(H) 1.4/14% (3) | CRY(A) 1.2/17% (3) | NFO(H) 1.2/22% (3) |
| ★ TOT | MUN(A) 1.0/13% (4) | COV(H) 1.5/34% (2) | CHE(A) 1.1/16% (4) | CRY(H) 1.5/28% (2) | LEE(A) 1.1/18% (3) | IPS(H) 1.6/26% (2) | SUN(A) 1.1/11% (3) | FUL(H) 1.5/25% (2) |
| ★ LEE | ARS(A) 0.8/15% (5) | MUN(H) 1.5/22% (4) | SUN(A) 1.3/14% (3) | BOU(A) 1.3/22% (3) | TOT(H) 1.7/35% (2) | CHE(A) 1.3/18% (4) | COV(H) 1.8/37% (2) | MCI(A) 1.2/13% (5) |
