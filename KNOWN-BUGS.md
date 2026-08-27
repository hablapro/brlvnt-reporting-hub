# Known Bugs & Environment Workarounds

Consult this before browser/render work. Do not re-diagnose a recorded bug.

## PowerPoint AppleScript PDF export serves a stale cached copy
**Seen:** 2026-07-21, rendering GGMI/GCG June rev1 decks for QA.
**Symptom:** exporting a `.pptx` to PDF via `osascript` returns the *previous* version — an N-slide deck exports N−1 pages when a slide was just added, because PowerPoint reopens an already-open/cached document.
**Workaround:**
1. Copy the saved `.pptx` to a **fresh, uniquely-named** temp file (e.g. `~/tmp-deck-render/g.pptx`), not a name reused this session.
2. `osascript -e 'tell application "Microsoft PowerPoint" to quit'` then `sleep 3` — but note the quit itself can throw a `-50` parameter error if a doc is mid-close; if so, skip the quit and just use a fresh filename + `delay 4-5` before `save`.
3. In the AppleScript: `activate`, `delay 2`, `open`, `delay 5`, then `save … as save as PDF`.
4. Verify with `pdfinfo <pdf> | grep Pages` before trusting the render.
Temp render copies live in `~/tmp-deck-render/` and are deleted after QA.
**Do not** conclude a slide "didn't save" from a short PDF — check the source file's slide count with python-pptx first (`len(Presentation(path).slides)`); the file is almost always correct and the PDF is stale.

## gws CLI token expires mid-session (invalid_grant / reauth_related invalid_rapt)
**Seen:** 2026-07-20/21, multiple times in one session.
**Symptom:** `gws drive …` returns a 401 `invalid_grant: reauth related error`. A parser that does `d.get('comments', [])` will silently report **0 results** instead of surfacing the auth error.
**Workaround:** Renzo runs `gws auth login` (suggest `! gws auth login` in the prompt). Always detect `if 'error' in response` before treating an empty list as real data — an auth error must not masquerade as "no comments / no files".

## Word AppleScript "save as PDF" silently redirects to the app sandbox container
**Seen:** 2026-07-28, exporting the GA4 gap docx to PDF for render QA.
**Symptom:** `save as theDoc file name <posix path> file format format PDF` throws `-1708 ("doesn't understand the save as message")` when the target is `/private/tmp/...` (scratchpad). Targeting `(path to documents folder as text)` exits 0 but the PDF is NOT in `~/Documents` — it lands in `~/Library/Containers/com.microsoft.Word/Data/Documents/`.
**Workaround:**
1. Save with `file name ((path to documents folder as text) & "name.pdf")`.
2. Fetch the result from `~/Library/Containers/com.microsoft.Word/Data/Documents/name.pdf` and copy it where needed.
3. Same fresh-uniquely-named-copy rule as the PowerPoint bug applies before opening.

## bing-ads MCP `bing_ads_list_ads` returns 400 NullRequest (tool broken)
**Seen:** 2026-08-04, auditing GGMI Bing July RSA creative depth (ad group 1306221121842778).
**Symptom:** every call fails with `400 {"OperationErrors":[{"Code":100,"ErrorCode":"NullRequest","Details":"Invalid JSON at line 0 position N. Path: $.ReturnAdditionalFields","Message":"The request message is null."}]}`. Fails identically with and without the `ad_types` parameter (position shifts 105 → 90, so the malformed field is server-side in the MCP's request serialization, not caused by our input).
**Impact:** RSA headline/description asset counts cannot be pulled via MCP. The June finding "brand RSAs at 4 headlines / 2 descriptions, below the Bing 8+/3+ standard" therefore remains UNVERIFIED on the current campaigns.
**Workaround:** none via MCP. Either read creative depth in the Bing UI, or use `bing_ads_bulk_download` (untested for this purpose). Do not re-attempt `list_ads` expecting it to work.
**Related:** `bing_ads_search_term_report` silently ignores the `campaign_ids` filter and, when given a start date on which only some campaigns delivered, can return only that single day. Verify covered spend against campaign totals before trusting its output; re-run without the campaign filter if coverage looks thin.

## verify_numbers / protection_scan: numeric xlsx cells are invisible (found 2026-08-17)

`scripts/protection_scan.py::text_from` only yields `isinstance(cell.value, str)`
cells from .xlsx, so a workbook whose figures are numeric cells bypasses BOTH
gates' number and vocabulary checks entirely (verify_numbers reported all 23
approved figures MISSING against a numerically-populated report).
Workaround: client-facing report workbooks write figures as formatted strings
("$10,625"), which is also the right presentation form. Fixing the extractor to
yield numeric cells needs a ruling before touching the gate script.

**RESOLVED 2026-08-25 (Renzo ruling).** `text_from` now yields numeric cells
rendered the way the audience reads them: `$` prefix when the cell's number
format is currency, percent cells scaled up (0.198 stored → "19.8%"), plain
numbers as-is; booleans and dates still skipped. Verified against the GGMI
July workbook (formerly all-MISSING, now 0 MISSING / 0 UNSOURCED) and the GCG
July deck (unchanged: 5 accepted MISSING, 0 BLOCK / 0 WARN). The
formatted-strings workaround is no longer required but remains fine.

## PowerPoint clobbers rebuilt output files it has open (found 2026-08-17)
**Symptom:** a deck rebuilt by `build_deck.py` reverts to older content with a fresh mtime. If the output `.pptx` is open in PowerPoint while the build script overwrites it, PowerPoint's auto-save/save writes its stale in-memory copy back over the new file.
**Workaround:** never keep the output file open during a build cycle; review from a copy or a PDF render. After any handoff, verify the binary's actual text (python-pptx) rather than trusting mtime. The build script is the source of truth; a clobber is fixed by re-running it.

## Quantcast MCP: key must be in the launching shell (2026-08-19)

The quantcast server in `.mcp.json` sends `X-API-Key: ${QUANTCAST_MCP_API_KEY}`,
expanded from the environment at session start. There is no `.env` auto-load
(`.env.example` documents the name only, value intentionally absent). If the
variable is not set in the shell that launched Claude Code, the server fails
DCR with HTTP 405 and every Quantcast pull is blocked for the session.
Fix: set the variable before launch (part of the pending MCP secret handover),
then restart the session. Do not paste the key into chat or commit it.

**RESOLVED 2026-08-19 (same day).** The quantcast server now lives in the
user-level Claude config (`~/.claude.json`, key stored there, never in the
repo) and was removed from the project `.mcp.json` (backup
`.mcp.json.bak-20260819-143515`). Verified: `quantcast_accounts` and a
July 2026 `quantcast_metrics_report` on account 9969644 both returned data,
GGMI display matched the July model exactly. No shell variable needed at
launch any more. Metric names are the display names from
`quantcast_available_metrics` ("Impressions", "Clicks (Advanced IVT)",
"Budget Delivered", "Viewability"); lowercase "clicks" returns
INVALID_ARGUMENT.

## verify_numbers.py: negative approved figures can never match deck prose (found 2026-08-20)

`_NUM` in `scripts/verify_numbers.py` does not capture a leading minus sign,
so every number it extracts from a deliverable is unsigned. A figure declared
in `figures.json` as a negative MoM percentage (e.g. `-77.4`) can therefore
never register as found, even when the deck states the fact in the
doctrine-mandated natural phrasing ("down 77.4%", "fell 22.8%") — `close(-77.4,
77.4)` is `False` by construction, regardless of how the copy is worded.
Confirmed on the GCG July 2026 build: `mom.meta_spend_pct` (-77.40),
`mom.quantcast_spend_pct` (-2.30) and `mom.azerion_cpa_pct` (-22.80) all sat
MISSING against a deck that stated all three figures in prose. Positive MoM
figures with the same content (e.g. `mom.google_search_spend_pct` at 30.9)
matched fine once written as plain digits.
**Workaround:** treat MISSING findings on figures.json entries with a negative
value as expected/non-blocking once you have manually confirmed the fact
appears in the deck in natural (unsigned, "fell/declined/down") phrasing per
`docs/DOCTRINE.md` §3 — do not force a literal minus sign into client copy to
satisfy the gate. Record the confirmation in the build's QA note. Fixing the
regex needs a ruling before touching the gate script, same class of change as
the xlsx numeric-cell bug below.

## Quantcast MCP: `quantcast_metrics_report` `filters` parameter returns empty results (found 2026-08-19)

**Seen:** GCG July Quantcast pull, account 9969644. Every call using the
`filters` array (e.g. `[{"breakdown": "Campaign Name", "values": [...]}]`),
including a single exact-match value on a breakdown present in the unfiltered
data, returned `{"accountMetricsReport": []}` — no error, just empty. Tried
with one and two breakdowns, one and two filter values; all empty. This is a
different symptom from the already-documented `quantcast_campaigns` /
`quantcast_accounts` object-shaped-filter rejection (that one throws a
validation error; this one silently returns nothing).
**Workaround:** do not use `filters` on `quantcast_metrics_report`. Pull the
account unfiltered (scoped only by breakdowns/metrics/date range) and filter
client-side on the "Campaign Name" (or other) breakdown value. Every pull
this session reconciled to the cent doing it this way.
**Related:** a `Campaign Name` × `Domain/App` breakdown on the whole account
exceeded the sync call's token limit (auto-saved to a file, fine) and on the
identical retry the MCP session itself returned `"MCP server \"quantcast\"
session expired"` twice in a row, while an unrelated small call
(`quantcast_accounts`) succeeded in between. Do not burn retries on the same
oversized sync call a third time — switch to `quantcast_async_report`
(`action: "request"` → poll → `action: "download"`, ~20s), which completed
cleanly and returned a gzipped CSV.

## SA360 GGMI Bing: `metrics.conversions` stopped equalling submitted apps in August 2026 (found 2026-08-27)

**Seen:** customer `5372690580` (FOREX.com LATAM Bing), login `9697709980`,
Aug 1-26 2026. Summing `metrics.conversions` at campaign level returned 53.
The SA360 UI Summary > Goals card for the same window showed 29 + 12 = 41.
Segmenting by `segments.conversion_action_name` explains the gap: three
additional conversion actions are now counting into the primary `conversions`
metric.

| Conversion action | Category | Aug 1-26 |
|---|---|---|
| G2 Raw Spread - Live Confirmation | SUBMIT_LEAD_FORM | 29 |
| MT5 Raw Spread - Live Confirmation | SUBMIT_LEAD_FORM | 12 |
| GCLID - Approved | IMPORTED_LEAD | 7 |
| GCLID - Funded | IMPORTED_LEAD | 1 |
| G2 / MT5 Raw Spread - App Form - Step 4 | PAGE_VIEW | 4 |

Only the two Live Confirmation actions are submitted applications. Approved
and Funded are downstream funnel stages (the client's journey, not the agency
scorecard) and Step 4 is a page view. Taking `metrics.conversions` at face
value inflates August submitted apps by 29% (53 vs 41) and understates cost
per submitted app by $86 ($293 vs $379).

May, June and July 2026 are clean: every non-zero `metrics.conversions` row in
those months is a Live Confirmation action, which is why the standing rule
("SA360 `metrics.conversions` already IS submitted apps", memory
`reference_forex_submitted_app_goals`) held through the July cycle. The rule
is now false for GGMI Bing from August 2026 onward.

**Workaround:** never sum bare `metrics.conversions` for GGMI Bing. Segment by
`segments.conversion_action_name` and count only the `- Live Confirmation`
actions:

```
SELECT segments.month, segments.conversion_action_name, metrics.conversions
FROM customer
WHERE segments.date BETWEEN '<start>' AND '<end>' AND metrics.conversions > 0
```

Cross-check the total against the SA360 UI Summary > Goals card before it goes
into `figures.json`. Note the UI column is labelled "All conv." but the Goals
card lists actions individually, so read the per-action rows, not a total.
Demo Confirmation is Secondary and is correctly excluded from
`metrics.conversions`; do not add it back.

**Still open:** who changed the Approved / Funded / Step 4 actions to primary,
and when in August. Needs a question to StoneX/SA360 admin before the August
cycle closes. Reporting-only repo, so do not change the goal config here.

## Quantcast MCP: exclusive `endDate` silently shortened a month-to-date pull, then the projection compounded it (found 2026-08-27)

**Seen:** GGMI August 2026 spend-reduction model, account 9969644. The
Quantcast run rates in `reports/forex/ggmi/2026-08/figures.json` were pulled
with `endDate: "2026-08-26"` and recorded as "MTD Aug 1-26". `endDate` is
EXCLUSIVE, so that call returns Aug 1-25. The figures were then projected to a
31-day month by multiplying x31/26, dividing 25 days of delivery by 26. Two
compounding errors in one number.
**Proof:** the recorded `quantcast.nativeonly_mtd` of 7979.18 reproduces to the
cent on an `endDate: "2026-08-26"` pull, and returns 8342.75 on the correct
`endDate: "2026-08-27"`. The gap is one day of that campaign's delivery.
**Effect:** the GGMI main Quantcast line read 29,634 instead of 31,387, about
5.6% low, and channel pacing against the approved budget read 85% instead of
90%.
**Workaround:** for an inclusive range ending on day N, set `endDate` to day
N+1, and project using the same day count the pull actually covers. This is the
already-documented exclusive-endDate behaviour (memory
`reference_quantcast_mcp_enddate`); the rule existed and was not applied, so
verify the day count independently rather than trusting the label on a stored
figure. Cheapest check: pull the same campaign at `endDate` N and N+1 and
confirm the difference is one plausible day of spend.
