# Fixture model v0.2 — GW11–18

**Generated** 2026-11-07 18:00 UTC from mirror `2026-11-07T17:59:49Z`.
**Observed** 10 gameweek(s) — [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. With k=6 pseudo-matches, ratings are **38% prior / 62% data** for the 8 clubs on 10 matches, and **40% / 60%** for the 12 on 9. That weight shifts toward data every week.

League mean xG per team-match **1.44**; home 1.60 / away 1.28 at an assumed home advantage of ×1.25.

> **Read this as a first iteration, not an oracle.** The prior mapping and home advantage are assumptions to be
> refit around GW10. Ratings are mostly prior right now *by design* — that is what stops one bad afternoon
> becoming a permanent verdict. Fewest matches: AVL, BOU, BRE, BHA, CHE, CRY, IPS, LIV, MCI, MUN, NFO, SUN on 9.

## Next 8 gameweeks

**xG / CS** = expected goals created and expected clean sheets over GW11–14, **summed** not averaged. **Att** is opponent-adjusted, with the *(raw)* unadjusted per-game figure beside it — the gap between them is how flattering the fixtures have been. **Def** is the xG a club concedes relative to average, so *lower is better*. Both are centred on 1.00. **G−xG** is finishing over/underperformance so far — not in the model, shown to see whether it is worth adding. ★ = Ben owns a player, per picks-latest.json = GW10 squad, the last FINISHED gameweek; it may not be the current squad. Pass --squad for the live one.

| Club | Att *(raw)* | Def | xG11–14 | CS11–14 | xG11–18 | CS11–18 | G−xG | Owned |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | 1.28 *(1.36)* | 0.96 | **7.09** | 1.06 | 14.88 | 2.21 | +6.4 | De Cuyper, Groß |
| ★ BOU | 1.15 *(1.22)* | 0.80 | **6.96** | 1.40 | 13.10 | 2.76 | -1.8 | Evanilson |
| LIV | 1.10 *(1.02)* | 0.83 | **6.65** | 1.17 | 12.93 | 2.64 | -2.2 |  |
| ★ MCI | 1.29 *(1.43)* | 0.89 | **6.54** | 1.09 | 14.51 | 2.38 | +1.4 | Haaland |
| ★ CHE | 1.07 *(1.04)* | 0.95 | **6.52** | 1.14 | 12.73 | 2.20 | +5.5 | Rogers |
| ★ AVL | 0.90 *(0.84)* | 1.09 | **6.36** | 0.98 | 11.16 | 1.89 | -0.9 | N.Jackson |
| ★ ARS | 1.16 *(1.11)* | 0.59 | **6.22** | 1.61 | 13.35 | 3.35 | -1.0 | Raya, Calafiori |
| ★ BRE | 1.12 *(1.11)* | 0.96 | **6.15** | 0.96 | 13.10 | 2.12 | +1.7 | Schade |
| MUN | 1.03 *(1.11)* | 1.13 | **6.03** | 0.89 | 11.85 | 1.65 | -4.4 |  |
| SUN | 1.09 *(1.03)* | 1.06 | **5.96** | 0.93 | 12.98 | 1.85 | -6.3 |  |
| ★ NFO | 1.05 *(1.15)* | 0.92 | **5.77** | 1.04 | 12.09 | 2.07 | -8.9 | Gibbs-White |
| ★ LEE | 0.95 *(0.93)* | 0.91 | **5.73** | 1.14 | 10.97 | 2.32 | -3.5 | Muharemović |
| EVE | 0.96 *(0.96)* | 1.04 | **5.38** | 0.90 | 10.69 | 1.60 | -1.8 |  |
| TOT | 0.85 *(0.87)* | 0.90 | **5.00** | 1.16 | 9.48 | 2.21 | -2.5 |  |
| COV | 0.74 *(0.67)* | 1.07 | **4.97** | 0.97 | 9.26 | 1.85 | +0.4 |  |
| CRY | 0.86 *(0.86)* | 1.35 | **4.94** | 0.73 | 9.57 | 1.26 | -2.2 |  |
| IPS | 0.90 *(0.95)* | 1.23 | **4.91** | 0.82 | 10.51 | 1.52 | +1.7 |  |
| ★ NEW | 0.86 *(0.79)* | 1.21 | **4.88** | 0.64 | 9.77 | 1.26 | +1.6 | Hall, Barnes |
| FUL | 0.92 *(1.01)* | 1.02 | **4.53** | 0.81 | 9.30 | 1.66 | -4.5 |  |
| ★ HUL | 0.72 *(0.66)* | 1.11 | **4.12** | 0.74 | 7.95 | 1.61 | +1.5 | Tzolakis, Egan |

## The same fixtures, priced

Expected goals **for** the club, and its clean-sheet probability, fixture by fixture. FDR in brackets for comparison — note where they disagree.

| Club | GW11 | GW12 | GW13 | GW14 | GW15 | GW16 | GW17 | GW18 |
|---|---|---|---|---|---|---|---|---|
| ★ BHA | HUL(A) 1.8/33% (2) | NEW(H) 2.5/35% (3) | BOU(A) 1.3/17% (4) | NFO(A) 1.5/20% (2) | EVE(H) 2.1/31% (3) | IPS(H) 2.5/33% (2) | FUL(A) 1.7/24% (3) | TOT(A) 1.5/27% (3) |
| ★ BOU | NFO(H) 1.7/34% (3) | FUL(A) 1.5/31% (3) | BHA(H) 1.8/27% (4) | HUL(H) 2.0/48% (2) | ARS(A) 0.9/22% (5) | COV(H) 2.0/47% (2) | TOT(A) 1.3/34% (3) | CRY(A) 2.0/33% (2) |
| LIV | MUN(H) 2.0/34% (3) | EVE(A) 1.5/28% (3) | SUN(H) 1.9/31% (2) | CHE(A) 1.3/24% (4) | LEE(H) 1.6/37% (3) | TOT(H) 1.6/41% (3) | HUL(A) 1.6/39% (2) | AVL(A) 1.5/31% (3) |
| ★ MCI | FUL(H) 2.1/35% (2) | ARS(A) 1.0/19% (5) | LEE(H) 1.9/34% (3) | BRE(A) 1.6/20% (4) | CHE(H) 2.0/30% (4) | HUL(H) 2.3/44% (2) | NEW(A) 2.0/30% (3) | EVE(A) 1.7/26% (3) |
| ★ CHE | LEE(H) 1.5/32% (3) | NFO(A) 1.3/20% (2) | CRY(H) 2.3/35% (2) | LIV(H) 1.4/26% (4) | MCI(A) 1.2/14% (5) | AVL(H) 1.9/34% (3) | COV(A) 1.5/33% (2) | IPS(A) 1.7/26% (2) |
| ★ AVL | SUN(H) 1.5/22% (2) | IPS(A) 1.4/21% (2) | EVE(H) 1.5/26% (3) | CRY(H) 1.9/30% (2) | COV(A) 1.2/28% (2) | CHE(A) 1.1/15% (4) | LEE(H) 1.3/26% (3) | LIV(H) 1.2/21% (4) |
| ★ ARS | NEW(A) 1.8/44% (3) | MCI(H) 1.6/38% (4) | BRE(A) 1.4/35% (4) | TOT(A) 1.3/45% (3) | BOU(H) 1.5/42% (3) | MUN(H) 2.1/46% (3) | CRY(A) 2.0/44% (2) | FUL(A) 1.5/42% (3) |
| ★ BRE | EVE(H) 1.9/31% (3) | MUN(A) 1.6/21% (3) | ARS(H) 1.1/24% (4) | MCI(H) 1.6/20% (4) | FUL(A) 1.5/24% (3) | NEW(H) 2.2/35% (3) | IPS(A) 1.8/25% (2) | COV(A) 1.5/32% (2) |
| MUN | LIV(A) 1.1/14% (4) | BRE(H) 1.6/20% (3) | NEW(A) 1.6/21% (3) | COV(H) 1.8/34% (2) | CRY(A) 1.8/21% (2) | ARS(A) 0.8/12% (5) | NFO(H) 1.5/22% (3) | SUN(H) 1.7/21% (2) |
| SUN | AVL(A) 1.5/22% (3) | TOT(H) 1.6/32% (3) | LIV(A) 1.2/16% (4) | NEW(A) 1.7/23% (3) | NFO(H) 1.6/24% (3) | CRY(H) 2.4/31% (2) | EVE(A) 1.5/20% (3) | MUN(A) 1.6/18% (3) |
| ★ NFO | BOU(A) 1.1/19% (4) | CHE(H) 1.6/29% (4) | HUL(A) 1.5/35% (2) | BHA(H) 1.6/22% (4) | SUN(A) 1.4/20% (3) | EVE(H) 1.8/32% (3) | MUN(A) 1.5/22% (3) | NEW(A) 1.6/28% (3) |
| ★ LEE | CHE(A) 1.2/21% (4) | COV(H) 1.6/43% (2) | MCI(A) 1.1/15% (5) | IPS(H) 1.9/35% (2) | LIV(A) 1.0/20% (4) | FUL(H) 1.6/34% (2) | AVL(A) 1.3/27% (3) | HUL(A) 1.3/35% (2) |
| EVE | BRE(A) 1.2/15% (4) | LIV(H) 1.3/23% (4) | AVL(A) 1.3/22% (3) | FUL(H) 1.6/29% (2) | BHA(A) 1.2/12% (4) | NFO(A) 1.1/17% (2) | SUN(H) 1.6/23% (2) | MCI(H) 1.4/18% (4) |
| TOT | IPS(H) 1.7/35% (2) | SUN(A) 1.1/21% (3) | FUL(H) 1.4/34% (2) | ARS(H) 0.8/26% (4) | HUL(A) 1.2/36% (2) | LIV(A) 0.9/20% (4) | BOU(H) 1.1/27% (3) | BHA(H) 1.3/23% (4) |
| COV | CRY(H) 1.6/31% (2) | LEE(A) 0.9/20% (3) | IPS(H) 1.4/29% (2) | MUN(A) 1.1/17% (3) | AVL(H) 1.3/29% (3) | BOU(A) 0.8/14% (4) | CHE(H) 1.1/23% (4) | BRE(H) 1.1/21% (3) |
| CRY | COV(A) 1.2/20% (2) | HUL(H) 1.5/29% (2) | CHE(A) 1.0/10% (4) | AVL(A) 1.2/14% (3) | MUN(H) 1.6/17% (3) | SUN(A) 1.2/9% (3) | ARS(H) 0.8/13% (4) | BOU(H) 1.1/14% (3) |
| IPS | TOT(A) 1.0/19% (3) | AVL(H) 1.6/24% (3) | COV(A) 1.2/23% (2) | LEE(A) 1.0/15% (3) | NEW(H) 1.7/26% (3) | BHA(A) 1.1/8% (4) | BRE(H) 1.4/17% (3) | CHE(H) 1.4/19% (4) |
| ★ NEW | ARS(H) 0.8/17% (4) | BHA(A) 1.1/8% (4) | MUN(H) 1.6/20% (3) | SUN(H) 1.5/18% (2) | IPS(A) 1.4/18% (2) | BRE(A) 1.1/11% (4) | MCI(H) 1.2/14% (4) | NFO(H) 1.3/20% (3) |
| FUL | MCI(A) 1.0/12% (5) | BOU(H) 1.2/22% (3) | TOT(A) 1.1/25% (3) | EVE(A) 1.2/21% (3) | BRE(H) 1.4/23% (3) | LEE(A) 1.1/21% (3) | BHA(H) 1.4/19% (4) | ARS(H) 0.9/22% (4) |
| ★ HUL | BHA(H) 1.1/16% (4) | CRY(A) 1.2/22% (2) | NFO(H) 1.1/23% (3) | BOU(A) 0.7/13% (4) | TOT(H) 1.0/30% (3) | MCI(A) 0.8/10% (5) | LIV(H) 0.9/21% (4) | LEE(H) 1.0/26% (3) |
