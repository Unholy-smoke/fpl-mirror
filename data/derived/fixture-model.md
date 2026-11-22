# Fixture model v0.2 — GW12–19

**Generated** 2026-11-22 17:26 UTC from mirror `2026-11-22T17:26:00Z`.
**Observed** 11 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. With k=6 pseudo-matches, ratings are **35% prior / 65% data** for the 16 clubs on 11 matches, and **38% / 62%** for the 4 on 10. That weight shifts toward data every week.

League mean xG per team-match **1.49**; home 1.65 / away 1.32 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: BRE, EVE, LIV, MUN on 10.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW12–15, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW11 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG12–15 | CS12–15 | xG12–19 | CS12–19 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.34)* | 0.94 | **7.58** | 0.98 | 15.89 | 2.10 | +4.1 | De Cuyper, Groß |
| MUN | 1.07 *(1.21)* | 1.20 | **7.17** | 0.82 | 12.80 | 1.38 | -4.0 |  |
| ★ BOU | 1.19 *(1.28)* | 0.84 | **6.58** | 1.19 | 14.35 | 2.57 | -3.0 | Evanilson |
| ★ AVL | 0.93 *(0.91)* | 1.08 | **6.58** | 1.00 | 11.53 | 1.74 | -0.9 | N.Jackson |
| ★ MCI | 1.26 *(1.36)* | 0.84 | **6.54** | 1.09 | 14.30 | 2.47 | -0.2 | Haaland |
| LIV | 1.11 *(1.07)* | 0.87 | **6.36** | 1.12 | 13.10 | 2.52 | -1.9 |  |
| ★ NFO | 1.05 *(1.10)* | 0.94 | **6.36** | 1.02 | 13.15 | 2.10 | -9.0 | Gibbs-White |
| CRY | 0.93 *(0.95)* | 1.38 | **6.16** | 0.63 | 10.78 | 1.04 | -3.5 |  |
| ★ LEE | 1.00 *(0.99)* | 0.86 | **6.14** | 1.18 | 12.38 | 2.52 | -2.2 | Muharemović |
| ★ CHE | 0.98 *(0.90)* | 1.03 | **5.96** | 0.79 | 12.61 | 1.88 | +5.3 | Rogers |
| SUN | 1.05 *(0.97)* | 0.99 | **5.93** | 0.97 | 13.33 | 2.04 | -7.9 |  |
| ★ ARS | 1.14 *(1.08)* | 0.62 | **5.89** | 1.49 | 14.13 | 3.18 | -0.7 | Raya, Calafiori |
| ★ NEW | 0.90 *(0.81)* | 1.16 | **5.88** | 0.67 | 10.87 | 1.30 | +1.8 | Hall |
| ★ BRE | 1.07 *(1.00)* | 0.94 | **5.69** | 0.89 | 13.48 | 2.10 | +1.1 | Schade |
| EVE | 0.94 *(0.93)* | 1.02 | **5.43** | 0.85 | 10.51 | 1.64 | -1.8 |  |
| IPS | 0.86 *(0.86)* | 1.26 | **5.41** | 0.77 | 10.00 | 1.30 | +1.0 |  |
| COV | 0.75 *(0.71)* | 1.08 | **4.91** | 0.88 | 9.01 | 1.60 | +1.3 |  |
| FUL | 0.89 *(0.94)* | 1.00 | **4.81** | 0.91 | 9.20 | 1.69 | -4.3 |  |
| ★ TOT | 0.86 *(0.92)* | 0.86 | **4.65** | 1.22 | 9.11 | 2.09 | -3.1 | Kudus |
| ★ HUL | 0.73 *(0.70)* | 1.11 | **4.31** | 0.79 | 8.17 | 1.46 | +1.6 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 | GW19 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | NEW(H) 2.4/32% (3) | BOU(A) 1.4/16% (4) | NFO(A) 1.6/19% (2) | EVE(H) 2.1/31% (3) | IPS(H) 2.7/34% (2) | FUL(A) 1.7/25% (3) | TOT(A) 1.4/26% (3) | MUN(H) 2.5/26% (3) |
| MUN | BRE(H) 1.7/18% (3) | NEW(A) 1.6/17% (3) | COV(H) 1.9/31% (2) | CRY(A) 2.0/16% (2) | ARS(A) 0.9/10% (5) | NFO(H) 1.7/19% (3) | SUN(H) 1.8/19% (2) | BHA(A) 1.3/8% (4) |
| ★ BOU | FUL(A) 1.6/29% (3) | BHA(H) 1.9/24% (4) | HUL(H) 2.2/45% (2) | ARS(A) 1.0/21% (5) | COV(H) 2.1/44% (2) | TOT(A) 1.4/31% (3) | CRY(A) 2.2/28% (2) | AVL(H) 2.1/36% (3) |
| ★ AVL | IPS(A) 1.6/21% (2) | EVE(H) 1.6/26% (3) | CRY(H) 2.1/26% (2) | COV(A) 1.3/26% (2) | CHE(A) 1.3/17% (4) | LEE(H) 1.3/24% (3) | LIV(H) 1.3/21% (4) | BOU(A) 1.0/12% (4) |
| ★ MCI | ARS(A) 1.0/20% (5) | LEE(H) 1.8/33% (3) | BRE(A) 1.6/22% (4) | CHE(H) 2.1/34% (4) | HUL(H) 2.3/44% (2) | NEW(A) 1.9/28% (3) | EVE(A) 1.7/27% (3) | TOT(H) 1.8/38% (3) |
| LIV | EVE(A) 1.5/26% (3) | SUN(H) 1.8/30% (2) | CHE(A) 1.5/24% (4) | LEE(H) 1.6/32% (3) | TOT(H) 1.6/37% (3) | HUL(A) 1.6/35% (2) | AVL(A) 1.6/26% (3) | COV(H) 2.0/42% (2) |
| ★ NFO | CHE(H) 1.8/30% (4) | HUL(A) 1.5/32% (2) | BHA(H) 1.6/21% (4) | SUN(A) 1.4/20% (3) | EVE(H) 1.8/31% (3) | MUN(A) 1.7/19% (3) | NEW(A) 1.6/25% (3) | FUL(H) 1.7/33% (2) |
| CRY | HUL(H) 1.7/26% (2) | CHE(A) 1.3/11% (4) | AVL(A) 1.3/12% (3) | MUN(H) 1.8/14% (3) | SUN(A) 1.2/9% (3) | ARS(H) 1.0/12% (4) | BOU(H) 1.3/11% (3) | BRE(A) 1.2/9% (4) |
| ★ LEE | COV(H) 1.8/43% (2) | MCI(A) 1.1/17% (5) | IPS(H) 2.1/38% (2) | LIV(A) 1.2/21% (4) | FUL(H) 1.6/37% (2) | AVL(A) 1.4/27% (3) | HUL(A) 1.5/36% (2) | EVE(H) 1.7/34% (3) |
| ★ CHE | NFO(A) 1.2/17% (2) | CRY(H) 2.2/28% (2) | LIV(H) 1.4/22% (4) | MCI(A) 1.1/12% (5) | AVL(H) 1.8/28% (3) | COV(A) 1.4/28% (2) | IPS(A) 1.6/23% (2) | NEW(H) 1.9/29% (3) |
| SUN | TOT(H) 1.5/33% (3) | LIV(A) 1.2/16% (4) | NEW(A) 1.6/23% (3) | NFO(H) 1.6/25% (3) | CRY(H) 2.4/30% (2) | EVE(A) 1.4/21% (3) | MUN(A) 1.7/17% (3) | HUL(H) 1.9/38% (2) |
| ★ ARS | MCI(H) 1.6/36% (4) | BRE(A) 1.4/34% (4) | TOT(A) 1.3/42% (3) | BOU(H) 1.6/38% (3) | MUN(H) 2.3/42% (3) | CRY(A) 2.1/39% (2) | FUL(A) 1.5/40% (3) | IPS(H) 2.4/49% (2) |
| ★ NEW | BHA(A) 1.1/9% (4) | MUN(H) 1.8/19% (3) | SUN(H) 1.5/20% (2) | IPS(A) 1.5/19% (2) | BRE(A) 1.1/13% (4) | MCI(H) 1.3/14% (4) | NFO(H) 1.4/20% (3) | CHE(A) 1.2/15% (4) |
| ★ BRE | MUN(A) 1.7/19% (3) | ARS(H) 1.1/24% (4) | MCI(H) 1.5/21% (4) | FUL(A) 1.4/25% (3) | NEW(H) 2.0/33% (3) | IPS(A) 1.8/26% (2) | COV(A) 1.5/31% (2) | CRY(H) 2.4/31% (2) |
| EVE | LIV(H) 1.4/23% (4) | AVL(A) 1.3/21% (3) | FUL(H) 1.5/30% (2) | BHA(A) 1.2/12% (4) | NFO(A) 1.2/17% (2) | SUN(H) 1.5/24% (2) | MCI(H) 1.3/18% (4) | LEE(A) 1.1/19% (3) |
| IPS | AVL(H) 1.5/21% (3) | COV(A) 1.2/21% (2) | LEE(A) 1.0/12% (3) | NEW(H) 1.7/22% (3) | BHA(A) 1.1/7% (4) | BRE(H) 1.3/17% (3) | CHE(H) 1.5/20% (4) | ARS(A) 0.7/9% (5) |
| COV | LEE(A) 0.8/17% (3) | IPS(H) 1.6/29% (2) | MUN(A) 1.2/15% (3) | AVL(H) 1.3/27% (3) | BOU(A) 0.8/12% (4) | CHE(H) 1.3/25% (4) | BRE(H) 1.2/22% (3) | LIV(A) 0.9/14% (4) |
| FUL | BOU(H) 1.2/21% (3) | TOT(A) 1.0/24% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/24% (3) | LEE(A) 1.0/19% (3) | BHA(H) 1.4/19% (4) | ARS(H) 0.9/22% (4) | NFO(A) 1.1/18% (2) |
| ★ TOT | SUN(A) 1.1/23% (3) | FUL(H) 1.4/37% (2) | ARS(H) 0.9/27% (4) | HUL(A) 1.3/35% (2) | LIV(A) 1.0/21% (4) | BOU(H) 1.2/26% (3) | BHA(H) 1.3/23% (4) | MCI(A) 1.0/17% (5) |
| ★ HUL | CRY(A) 1.3/18% (2) | NFO(H) 1.1/21% (3) | BOU(A) 0.8/11% (4) | TOT(H) 1.0/29% (3) | MCI(A) 0.8/10% (5) | LIV(H) 1.1/20% (4) | LEE(H) 1.0/23% (3) | SUN(A) 1.0/15% (3) |
