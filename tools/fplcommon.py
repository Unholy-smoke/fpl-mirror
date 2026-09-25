"""Shared helpers for the fpl-mirror tools. Standard library only.

Every tool reads a local checkout of the mirror (default: ./data, i.e. run from the
repo root). That is how the GitHub Action runs them, and how a Claude session runs
them after `git clone https://github.com/Unholy-smoke/fpl-mirror.git`.

Conventions, shared by every tool so no prompt ever has to restate them:
  * Money in the API is in tenths (now_cost 155 = £15.5m). Tools output £m floats.
  * Every API timestamp is UTC. Anything a human reads is also given in UK local
    time with the zone named (BST/GMT) — see uk().
  * Players are keyed on element id, never web_name (web_name is duplicated).
"""
import csv, datetime as dt, json, os, sys
from zoneinfo import ZoneInfo

UK = ZoneInfo("Europe/London")
POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}


def data_dir(argv_path=None):
    d = argv_path or os.environ.get("FPL_DATA", "data")
    if not os.path.isfile(os.path.join(d, "bootstrap-static.json")):
        sys.exit(f"no bootstrap-static.json under {d!r} - run from the repo root or pass --data")
    return d


def load(d, rel):
    with open(os.path.join(d, rel), encoding="utf-8") as f:
        return json.load(f)


def parse_utc(s):
    """'2026-10-10T10:00:00Z' (or with fractional seconds) -> aware UTC datetime."""
    if s is None or s == "":
        return None
    return dt.datetime.fromisoformat(s.strip('"').replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def iso(t):
    return t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if t else ""


def uk(t, fmt="%a %d %b %H:%M"):
    """UK local time with the zone named, e.g. 'Sat 10 Oct 11:00 BST'."""
    if t is None:
        return ""
    lt = t.astimezone(UK)
    return f"{lt.strftime(fmt)} {lt.tzname()}"


def m(tenths):
    return None if tenths is None else round(tenths / 10, 1)


def selling_price(purchase, now):
    """Selling price in tenths: purchase + floor(half the rise); a fall is absorbed in full."""
    return now if now <= purchase else purchase + (now - purchase) // 2


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def write_json(path, obj):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False, sort_keys=False)
        f.write("\n")
