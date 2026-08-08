#!/usr/bin/env python3
"""Verify every client-facing figure in a deliverable against the approved set.

Roughly a third of the June 2026 cycle was rework, and the retrospective's
one-line root cause was: numbers were written from the best data on hand
instead of from what the client already holds. The fix is a per-month
figures.json that states the approved client-facing figures once, and this
script, which proves the deliverable agrees with it in both directions.

    python3 scripts/verify_numbers.py <figures.json> <deliverable> [...]

Two checks:
  MISSING  an approved figure does not appear in the deliverable.
  UNSOURCED a currency amount over the threshold appears in the deliverable
            but is not in the approved set. This is the stale-fork detector:
            last month's number surviving into this month's deck.

Exits 1 on either. Formatting is normalised, so $35,026 / 35026 / $35,026.00
all match, and 19.78M matches 19,780,693 within tolerance.

figures.json shape (see templates/month/figures.json):

    {
      "entity": "GGMI (LATAM)", "month": "2026-07",
      "spend_basis": "client budget tracker, received 2026-08-05",
      "figures": {
        "bing.spend": 10624.94,
        "bing.submitted_apps": 20,
        "total.spend": 120393
      },
      "allow": [2026, 31, 90],
      "notes": "total.spend is the tracker figure, not the platform sum."
    }

`allow` is for numbers that legitimately appear and are not figures: years,
slide counts, day counts. `history` is for prior-period and QBR figures
carried for comparison; declare their origin in `history_source`. Keep both
short and justify additions in `notes`.

Limits, so nobody over-trusts a PASS:
  - UNSOURCED only inspects currency amounts over the floor. A wrong
    conversion count, CTR or CPA is not caught unless it is also declared and
    goes MISSING.
  - Small integers (a conversion count of 33) often appear legitimately
    elsewhere in the deck, so MISSING is weak for them. Read the QA note.
  - It proves the deliverable agrees with figures.json. It cannot prove
    figures.json agrees with the client's tracker. That is a human step, and
    `spend_basis` is where you record having done it.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from protection_scan import text_from            # noqa: E402  (shared reader)

# Currency amounts below this are footnote noise (a $2.60 CPC), not the
# figures a tracker reconciliation is about. Override per month with
# "currency_floor" in figures.json.
#
# Calibration: set this to the level a client actually cross-checks. On the
# June GGMI QBR deck a $1,000 floor returns 48 UNSOURCED, because a
# quarter-close deck legitimately carries prior-month and campaign-level
# figures. At $10,000 it returns the headline set. Start high, declare the
# headline figures, then lower the floor as the declaration gets complete.
# A month whose every client-facing number is declared can run at 1000.
CURRENCY_FLOOR = 10000.0
# Relative tolerance. Covers "19.78M" against 19,780,693 and rounding to the
# dollar, without letting a genuinely different number slide through.
TOLERANCE = 0.001

_NUM = re.compile(r'\$?\s?(\d[\d,]*\.?\d*)\s?([KMB])?', re.I)
_MULT = {'k': 1e3, 'm': 1e6, 'b': 1e9}


def numbers_in(text):
    """Yield (value, is_currency, raw) for every number-looking token."""
    for m in _NUM.finditer(text):
        raw = m.group(0).strip()
        try:
            val = float(m.group(1).replace(',', ''))
        except ValueError:
            continue
        if m.group(2):
            val *= _MULT[m.group(2).lower()]
        yield val, raw.startswith('$'), raw


def close(a, b):
    if a == b:
        return True
    scale = max(abs(a), abs(b), 1.0)
    return abs(a - b) / scale <= TOLERANCE


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2

    spec = json.loads(Path(argv[0]).read_text())
    approved = [float(v) for v in spec.get('figures', {}).values()]
    allow = [float(v) for v in spec.get('allow', [])]
    # Prior-period and QBR-history figures. Same effect as `allow`, kept
    # separate so a reader can tell "this month's figure, sourced" from
    # "last quarter's figure, carried for comparison". A quarter-close deck
    # is mostly history and would otherwise read as 27 stale numbers.
    history = [float(v) for v in spec.get('history', [])]
    known = approved + allow + history
    label = {float(v): k for k, v in spec.get('figures', {}).items()}
    floor = float(spec.get('currency_floor', CURRENCY_FLOOR))

    print(f'figures.json: {spec.get("entity")} {spec.get("month")} — '
          f'{len(approved)} approved figure(s), currency floor ${floor:,.0f}')
    if spec.get('spend_basis'):
        print(f'spend basis:  {spec["spend_basis"]}')
    else:
        print('spend basis:  !! not declared. Client-facing spend must state '
              'its source (docs/DOCTRINE.md).')

    failures = 0
    for arg in argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f'\n!! not found: {path}')
            failures += 1
            continue

        seen = []       # (value, is_currency, raw, locator)
        for loc, chunk in text_from(path):
            for val, is_cur, raw in numbers_in(chunk):
                seen.append((val, is_cur, raw, loc))

        missing = [(v, label[v]) for v in approved
                   if not any(close(v, s[0]) for s in seen)]
        unsourced = {}
        for val, is_cur, raw, loc in seen:
            if not is_cur or val < floor:
                continue
            if any(close(val, k) for k in known):
                continue
            unsourced.setdefault(val, (raw, loc))

        print(f'\n=== {path.name} — {len(missing)} MISSING, '
              f'{len(unsourced)} UNSOURCED')
        for val, name in missing:
            print(f'  [MISSING]   {name} = {val:,.2f} is approved but does '
                  f'not appear in the file')
        for val, (raw, loc) in sorted(unsourced.items(), reverse=True):
            print(f'  [UNSOURCED] {raw} at {loc} — not in figures.json. '
                  f'Either add it with its source, or it is a stale number.')
        failures += len(missing) + len(unsourced)

    print(f'\n{"FAIL" if failures else "PASS"}: {failures} finding(s).')
    if failures:
        print('Do not ship. Every client-facing figure traces to a source the '
              'client already holds, or it does not go in the deck.')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
