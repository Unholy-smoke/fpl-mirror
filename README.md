# fpl-mirror

Snapshots of the public Fantasy Premier League API, committed to git eight times a day, plus a few
files derived from them. It exists for two reasons:

1. **Reachability.** Claude's cloud sessions can read `raw.githubusercontent.com` and `git clone` this
   repo, but can't reach the FPL API.
2. **History.** The FPL API only ever shows *now*. Every snapshot here is a commit, so git history
   is the time series: prices, ownership, flags and deadlines, as they were.

No login is used. Every endpoint is public. Ben's private squad state (bank, selling prices, pending
transfers) is **not** here. It lives in the Claude project, read from the FPL site in Ben's own
browser session.

## Schedule

`.github/workflows/snapshot.yml` runs at `01:11 03:47 07:11 09:52 13:11 15:53 18:49 21:30` UTC (GitHub cron is UTC
only), plus on demand (Actions → *Snapshot FPL data* → *Run workflow*, or the dispatch API). GitHub's
scheduler is best-effort and often runs one to three hours late. Design nothing around a slot landing on time.

## What's in `data/`

| File | What it is |
|---|---|
| `events.json` | **Start here** (~16 KB). Current/next gameweek, `next_deadline_utc`, every gameweek's deadline and status, chip windows |
| `fetch-status.json` | `run_at`, `failed_this_run`, and per-file `last_success`. **Judge freshness by `last_success` on the keys you need** |
| `bootstrap-static.json` | Every player, team and gameweek (~2.5 MB; filter it, never read it whole) |
| `fixtures.json` | Every fixture, kick-off (UTC) and FDR |
| `event-status.json` | Whether bonus and league tables have settled |
| `entry.json`, `entry-history.json` | Ben's entry and per-gameweek history |
| `picks-latest.json` | Ben's picks for the **current gameweek, i.e. the last one whose deadline has passed**. Not the upcoming one, and nothing in the file says so |
| `league-standings.json` | The mini-league table and every entry id |
| `rivals/gw<N>-entry<ID>.json` | Every league member's picks for gameweek N (frozen once N stops being current) |
| `rivals/history-entry<ID>.json` | Every member's per-gameweek history and chips |
| `transfers/entry<ID>.json` | Every member's transfer log, with purchase (`element_in_cost`) and sale prices |
| `live/gw<N>.json` | Per-player stats for the current and previous gameweek |
| `elements/<id>.json` | Element summaries for a watchlist (Tuesdays, or on demand) |
| `history/prices.csv` | Every observed price change, stamped at the fetch that saw it |
| `history/ownership/<date>.csv` | One ownership/price snapshot per day |
| `history/progress/<date>.csv` | FPL's own price predictor (`price_change_percent`, projections) for every player at every fetch |
| `derived/deadlines.csv` | Every deadline in UTC and UK local, first fixture, and the "deadline = first kick-off − 90 min" check |
| `derived/deadline-changes.csv` | Append-only: every time a deadline moved, and when it was seen |
| `derived/league-state.json` | All nine managers at the last deadline: bank, **free transfers**, chips held, squad with **selling prices** |
| `derived/fpl-proj-scores.csv` | How well FPL's predictor (progress, proj_0/1/2) called each night's price changes |

**Traps:** prices are in tenths (`155` = £15.5m); positions are 1 GK / 2 DEF / 3 MID / 4 FWD; every
timestamp is **UTC** (convert before telling a human); key players on `id`, never `web_name`
(names are duplicated). Ids are stable within a season in practice, but new players are appended, so be
wary of an id remembered from weeks ago.

## Tools (`tools/`, Python standard library only, run from the repo root)

| Script | Does |
|---|---|
| `deadlines.py` | Deadline table, drift log, 90-minute invariant. Prints the next deadline in UK time |
| `league_state.py` | Free transfers, bank, chips and selling prices for all nine managers |
| `price_scores.py fpl` | Scores FPL's predictor against actual changes |
| `price_scores.py calls FILES` | Scores Claude's own price calls (CSV files kept in the project) |
| `health.py` | Freshness and completeness check: one OK/WARN/FAIL line per check |
| `fixture-model.py [START END] [--squad squad.json]` | Pairwise fixture model v0.2 (a tie-breaker, never a lead) |
| `fixture-matrix.py` | FDR matrix |

The first three run inside the workflow on every snapshot (step 5c) and write `data/derived/`. A failure
there is logged and never blocks the snapshot.

## Maintenance

- Workflow and tool changes are made in `C:\Users\ben\Cowork\FPL\mirror-repo\` (the authoritative copy)
  and uploaded here by Ben via *Add file → Upload files*. After an upload, run the workflow once by hand
  and check the log for `!!` lines.
- Scheduled workflows are disabled after 60 days without repo activity. The snapshot commits count, but
  if snapshots stop, check the Actions tab for a "disabled" banner.
