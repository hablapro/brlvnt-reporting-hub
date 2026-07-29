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
