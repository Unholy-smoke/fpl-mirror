# fpl-mirror

A daily snapshot of the Fantasy Premier League API, committed to this repository.

The FPL API is public but only ever shows you *right now* — there is no history and no way to ask what a price was last Tuesday. This repo fixes that by fetching the data every night and committing it. Two things fall out of that:

1. **Reliable access.** Some tools can read files from GitHub but can't reach the FPL API directly. This repo bridges that gap.
2. **A free time series.** Because every snapshot is a commit, the git history becomes a complete record of every price change, ownership swing and injury flag, going back to whenever you set this up. That's data you cannot get retrospectively — the API won't tell you, so the only way to have it is to start collecting.

Nothing here is authenticated. Every endpoint used is one anyone can open in a browser.

## What gets saved

Everything lands in `data/`:

| File | What's in it |
|---|---|
| `bootstrap-static.json` | Every player — price, ownership, position, availability, injury news, set-piece order — plus all 20 teams and all 38 gameweek deadlines |
| `fixtures.json` | Every fixture, kick-off time and difficulty rating |
| `event-status.json` | Whether bonus points and league tables have settled |
| `entry.json` | Your team — overall rank, squad value, money in the bank, chips used |
| `entry-history.json` | Your gameweek-by-gameweek history |
| `picks-latest.json` | Your XI, bench and captain for the current gameweek |
| `league-standings.json` | Your mini-league table, including each rival's entry ID |
| `last-updated.txt` | When the snapshot last ran successfully |

## Setting it up

No command line needed — all of this can be done on github.com.

### 1. Create the repository

New repository, name it `fpl-mirror`, set it to **Public**, and tick "Add a README file". Public matters: it's what lets tools read the raw files without a token, and there's nothing private in here.

### 2. Add the files

Use **Add file → Create new file** for each one. To create a file in a folder, just type the path with slashes — `.github/workflows/snapshot.yml` — and GitHub makes the folders for you.

You need:

- `.github/workflows/snapshot.yml`
- `config.json`
- this `README.md` (optional, but you'll thank yourself later)

### 3. Find your two ID numbers

**Entry ID** — your own team's ID. Log in to the FPL site, go to the Points tab, and look at the address bar:

```
https://fantasy.premierleague.com/entry/1234567/event/1
                                        ^^^^^^^ this is your entry ID
```

**League ID** — open your mini-league from the Leagues tab:

```
https://fantasy.premierleague.com/leagues/987654/standings/c
                                          ^^^^^^ this is your league ID
```

Put both into `config.json` as plain numbers, no quotes:

```json
{
  "entry_id": 1234567,
  "league_id": 987654
}
```

### 4. Let the workflow write to the repo

Settings → Actions → General → scroll to **Workflow permissions** → select **Read and write permissions** → Save.

Without this the fetch works but the commit is rejected, which is a confusing failure to debug. Do it before the first run.

### 5. Run it once by hand

Actions tab → **Snapshot FPL data** → **Run workflow**. It takes under a minute. Click into the run to watch the log; each fetch prints the file it wrote and how big it was.

If it went well, `data/` now has files in it and you'll see a commit from "fpl-mirror bot".

## When it runs

Every day at 02:30 UTC, plus whenever you trigger it manually. That timing is deliberate — FPL prices change around 01:30 UK time, so this catches the settled overnight state.

Two things worth knowing:

- **GitHub's scheduler is best-effort.** On a busy morning a scheduled run can be delayed by a while, occasionally skipped. Fine for daily snapshots; don't rely on it landing to the minute.
- **Scheduled workflows get switched off after 60 days without repository activity.** The daily commits normally count as activity, so this shouldn't bite — but if snapshots stop appearing, check the Actions tab for a "this workflow was disabled" banner and re-enable it.

## If a run fails

Click the failed run in the Actions tab and read the log — the step that failed is marked in red.

The usual suspects:

- **"Permission denied" on push** — step 4 above wasn't done.
- **A fetch printing `request failed`** — the FPL API was briefly unavailable, or an ID in `config.json` is wrong. The workflow keeps the previous good file rather than overwriting it with an error page, so nothing is lost. Check your IDs.
- **`picks-latest.json` missing before the season starts** — expected. Picks don't exist until a gameweek is live.

## Reading the data

Raw files are at:

```
https://raw.githubusercontent.com/<your-username>/fpl-mirror/main/data/bootstrap-static.json
```

A couple of things that will trip you up if nobody warns you: prices are in tenths, so `155` means £15.5m. Positions are numbers — 1 goalkeeper, 2 defender, 3 midfielder, 4 forward. And availability is a single letter in `status`: `a` available, `d` doubtful, `i` injured, `s` suspended, `u` unavailable.
