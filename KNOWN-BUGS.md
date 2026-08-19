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
