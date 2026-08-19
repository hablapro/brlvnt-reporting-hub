# Monthly Reporting Runbook

The end-to-end process for one entity for one month. Run it twice each cycle,
once for GGMI and once for GCG. Same seven phases, same gates, different
channel mix.

Phases run in order. A phase does not start until the one before it closes,
and each closes on a named check rather than a feeling that it is done.

**Timing.** Start the first working day after month close. Both entities
usually take four to six working days end to end, and the pacing item is
almost always the Azerion vendor file or the client tracker, not the analysis.

---

## Phase 0: Kickoff

Nothing gets pulled until these are answered. About a third of the June 2026
cycle was rework, and the retrospective traced nearly all of it to building
from the best data on hand instead of asking what the client already holds.

Scaffold the month:

```bash
./scripts/new_month.sh ggmi 2026-08      # or: gcg
```

That creates `reports/forex/<entity>/<YYYY-MM>/` with `data/sources/`, `qa/`,
`model/`, `output/`, plus stubs for `figures.json`, the QA note and
`BUILD-STATUS.md`.

### The two standing questions

Ask Renzo both, in one message, and write the answers into `BUILD-STATUS.md`.

1. **What does the client already hold for this month?** Budget tracker pages
   for both entities, any client funnel or BvA dashboard, and any comms sent
   since the last report on a sensitive topic. Every client-facing number is
   checked against these, so a number written before they arrive is a number
   you will rewrite.
2. **How is the agency scored this month?** The primary conversion event and
   the cost per it. The standing answer is submitted applications and cost per
   submitted application; downstream steps belong to the client's journey.
   Confirm it rather than assume it, because the conversion goals have been
   renamed mid-cycle before.

### Kickoff inputs

| Input | Source | Blocks |
|---|---|---|
| Client budget tracker page | Renzo | Every client-facing spend figure |
| Client funnel / BvA dashboard | Renzo | The outcome rows. Funnel rows only; their spend rows are broken. |
| Azerion vendor XLSX | Vendor email | The Azerion section, both entities |
| Client comms since last report | Renzo | Any sensitive-topic framing |
| Prior `BUILD-STATUS.md` | This repo | Carry-overs and commitments |
| Prior deck | `report-client-decks/` | Every promise made to the client |

Read the prior month's `BUILD-STATUS.md` and the prior deck's recommendations
before pulling anything. A commitment made in last month's deck is either
delivered this month, re-sequenced with a stated reason, or asked about live
on the call.

**Closes when:** both questions are answered in `BUILD-STATUS.md`, and the
carry-over list is written.

---

## Phase 1: Pull

One channel at a time. QA each channel before starting the next, so a broken
pull surfaces while you still remember what you did.

### Sources of truth

| Channel | Entity | Source | Account |
|---|---|---|---|
| Bing | GGMI | `bing-ads` MCP for spend, impressions, clicks, keywords, config | `31003116` |
| Bing conversions | GGMI | **`sa360` MCP only** | customer `5372690580`, login `9697709980` |
| Google Ads | GCG | `google-ads` MCP | `4781995752` |
| Meta | both | `meta-ads` MCP, one shared account, split by campaign name | `act_1699453997689551` |
| Quantcast | both | `quantcast` MCP | `9969644` |
| Azerion | both | Vendor XLSX into `data/sources/` | no API |
| GA4 | GGMI | `google-analytics` MCP | property `508849216` |
| GA4 | GCG | `google-analytics` MCP | property `325353267` |
| Organic | GGMI | `gsc` MCP | forex.com property |

**GGMI conversions come from SA360, never from the Bing API.** They are
offline-imported, so the Bing API reads zero and reports a real month as a
dead one. This has caused a wrong read more than once.

### Output

One `.xlsx` workbook per channel in `data/`, named
`<ENTITY>-<Channel>-<Month>-<Year>-data.xlsx`. Each records its source and
account ID, the period, channel totals with MoM, the relevant breakdowns, and
a Notes and QA tab. Raw vendor files go in `data/sources/` untouched.

Data belongs in workbooks, not markdown. Markdown is for narrative and QA
notes.

### Every month, without being asked

- **Programmatic site list and disallow refresh.** Pull the Domain/App
  breakdown with Budget Delivered for Quantcast and any programmatic channel.
  Add Site List and Disallow Candidates tabs to the workbook, write a
  refreshed disallow list to `recommendations/<client>/<sub-client>/` as a
  `.txt` block list plus a summary. Flag sites under 35% viewability with few
  or no results. Inventory rotates, so a stale list is worth little.
- **Geo check.** GGMI is Mexico-only and GCG is US. Check delivery, not just
  the targeting setting. A campaign set to presence-or-interest still leaks.
- **Tool failures get disclosed.** Two retries maximum, then stop and record
  it in `KNOWN-BUGS.md` and in the build status. A degraded tool that quietly
  falls back is worse than one that fails loudly.

**Closes when:** every in-scope channel has a workbook, and each one
reconciles internally (sub-tables sum to the channel total).

---

## Phase 2: QA

Write into `qa/qa-and-model.md`. QA precedes modeling, and modeling precedes
any commentary.

| Check | Passes when |
|---|---|
| Cross-source reconciliation | Bing-direct spend equals SA360 spend within rounding |
| Internal sums | Keyword, ad-group and geo spend each sum to the campaign total |
| Client tracker | Every client-facing spend figure matches the tracker |
| Conversion source | Each channel's conversion comes from its declared source of truth |
| Geo compliance | Delivery is in-market, and the targeting setting is verified separately |
| Conversion maturity | Recent clicks against the conversion window; a late-month pull under-reports |
| Programmatic quality | Viewability against the 70% IAB floor, view-through flagged as directional |
| GA4 cross-check | Platform clicks against GA4 sessions, gaps explained rather than averaged |

Two failure modes that have both cost a cycle:

- **A number that is correct on the platform and wrong for the client.** SA360
  reported $12,637 of non-Mexico spend, correctly, but the client had been
  given $8,612 from Bing's own UI. Client-facing figures match what the client
  holds; the platform figure stays internal.
- **An empty result that is really an auth error.** A parser doing
  `d.get('comments', [])` reports zero results on a 401. Check for an error key
  before treating an empty list as data.

**Closes when:** every check has a PASS, a FAIL with remediation, or an
explicit HOLD, and the tracker reconciliation is done.

---

## Phase 3: Model

Build the cross-channel model in `model/` as a workbook, and put the summary
table in the QA note.

Rules that hold every month:

- **Spend and impressions sum. Conversions and CPA do not.** Each channel
  reports a different event from a different system. The Total row carries a
  dash in the conversion and CPA cells, with the footnote explaining why.
- **Never blend the entities.** GGMI and GCG stay separate everywhere.
- Preserve the source-platform metric when it differs from the shared
  definition, document the difference, and do not silently remap it. The
  definitions live in `mappings/kpi-dictionary.md`.
- Judge Meta against its own objective. A traffic objective buying landing
  page views is not a conversion campaign that underperformed.

Then declare the figures. Fill `figures.json` with every client-facing number
and its source, and write `spend_basis` stating where spend came from. This is
what phase 5 checks against, and the worked example is
`reports/forex/ggmi/2026-06/figures.json`.

**Closes when:** the model workbook exists, the summary table is in the QA
note, and `figures.json` is complete with a declared spend basis.

---

## Phase 4: Narrative

Draft into `output/<ENTITY>-<Mon>-<Year>-narrative-draft.md`. Load `stop-slop`
before writing, and `dataviz` before specifying any chart.

Structure: what happened, why it happened, what to do next. Facts,
interpretation and recommendation stay separated. Every recommendation ties to
a validated number.

The voice and framing rules are in `docs/DOCTRINE.md`. Read them before
drafting rather than after, because the protection scan in phase 5 rejects
copy that ignores them and rewriting a slide is slower than writing it right.

**One approval gate.** Renzo reviews the narrative before any deck is built.
For a quarter-close cycle, get the slide order approved as a numbered list at
the same time. Prose hides order, and a deck built in the wrong order gets
rebuilt whole.

**Closes when:** Renzo approves the narrative, and the slide order for a
quarter-close.

---

## Phase 5: Build and gate

### Build

Deliverables are a formatted `.xlsx` performance report and a `.pptx` deck,
both built from the model, never hand-keyed.

Build scripts import `lib/housestyle.py`, which owns the palette, the fonts and
every component. Do not redefine a colour in a build script. `docs/DESIGN-SYSTEM.md`
is the human-readable spec, and `python3 lib/housestyle.py` renders a deck
exercising every component if you need to see one.

Copy last month's builder for the same entity into `tools/forex-<entity>-<month>/`
and edit the numbers and copy. Declare `n_slides` up front; `Deck.verify()`
refuses to save when the real slide count drifts from the footer denominator,
which is the check that catches a bug that shipped twice.

### Gates, all four

```bash
# 1. Numbers agree with the approved set, both directions
python3 scripts/verify_numbers.py reports/forex/<entity>/<month>/figures.json \
  path/to/deck.pptx path/to/report.xlsx

# 2. Protection scan: forbidden vocabulary, statements against interest
python3 scripts/protection_scan.py path/to/deck.pptx path/to/report.xlsx
```

3. **Render QA.** Convert to PDF and look at every slide. Check the page count
   against the source before trusting the render; PowerPoint serves a stale
   cached PDF, and the workaround is in `KNOWN-BUGS.md`. Watch for table
   overflow into the footer and text past card edges.
4. **The protection scan's human half.** The script catches vocabulary and
   phrasing. It cannot tell you a slide promises something you have not
   delivered, or that a number the client can cross-check disagrees with
   theirs. Walk `docs/DOCTRINE.md` section by section.

A BLOCK is a stop. If a flagged word is genuinely required, get it ruled on
and add the exception to the doctrine, not quietly to the script.

**Closes when:** all four gates pass, and any failure is disclosed on the first
line of the handoff rather than buried.

---

## Phase 6: Deliver

Upload to the month's Drive folder under **FX Report**
(`1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55`). Use `supportsAllDrives: true`; it is a
shared drive.

**Once Renzo edits the Google Slides file, that file is canonical.** Never
re-upload a built PPTX over it. Later edits go through
`gws slides batchUpdate` replaceAllText, longest strings first so `2 / 17`
does not match inside `12 / 17`, and verify `occurrencesChanged` on every
call. Keep the local and Drive PPTX as exports of the Slides, not as the
source.

Verify uploads by reading the content back. The Drive connector's base64
upload has silently produced an empty Sheet, and it was caught only because
someone checked.

Then close the cycle:

- Update the Reported Spend Tracker and the Billable tab.
- Update `reports/REPORT-INDEX.md` and `reports/report-index.html`.
- Append a session block to `reports/REPORTING-LOG.md`.
- Archive or delete the month's `BUILD-STATUS.md` once shipped.
- Move delivered recommendations out of the queue, or note the outcome.
- Commit. Do not push without approval.

**Closes when:** the client has the deliverable, the index and log are current,
and the repo is committed.

---

## Phase 7: Post-delivery review (standing, every month — Renzo ruling 2026-08-19)

After Renzo delivers and the client has had the deck, review what actually
shipped. The delivered Slides file is the template baseline for the next
month, not the built PPTX.

1. **Diff the canonical Slides against the built deck.** Pull the Slides
   JSON (`gws slides presentations get --params '{"presentationId":"..."}'`)
   and compare slide-by-slide: what Renzo cut, merged, added, reworded.
2. **Pull client comments.** Drive comments API
   (`gws drive comments list --params '{"fileId":"...","fields":"comments(id,content,anchor,author(displayName),createdTime,resolved,quotedFileContent(value),replies(content,author(displayName)))"}'`).
   The `anchor.page` field maps each comment to a slide objectId.
3. **Write the review** to `reports/forex/<entity>/<month>/qa/final-deck-review-<date>.md`:
   the structural diff, each comment with the standing rule it implies, and
   the follow-ups.
4. **Codify same day.** Template-structure changes go into DOCTRINE §11 and
   the deck build script; client presentation asks become doctrine rules.
   A client comment that recurs ("once again") means the rule was missed
   the first time; find the original ask.
5. **Answer or route the comments.** Answerable-from-data questions get
   drafted replies for Renzo; build-affecting ones go into the next
   cycle's kickoff carry-overs.

**Closes when:** the review doc exists, doctrine and the build template
reflect the deltas, and every client comment is either answered or carried
into the next kickoff.

First instance: `reports/forex/ggmi/2026-07/qa/final-deck-review-2026-08-19.md`.

---

## Quick reference

```bash
./scripts/new_month.sh ggmi 2026-08                      # phase 0
python3 lib/housestyle.py                                # library check
python3 scripts/verify_numbers.py <figures.json> <file>  # phase 5 gate 1
python3 scripts/protection_scan.py <file>                # phase 5 gate 2
```

| Phase | Closes on |
|---|---|
| 0 Kickoff | Two questions answered, carry-overs listed |
| 1 Pull | Every channel has a reconciling workbook |
| 2 QA | Every check resolved, tracker reconciled |
| 3 Model | Model built, `figures.json` complete |
| 4 Narrative | Renzo approves narrative and slide order |
| 5 Build | Four gates pass |
| 6 Deliver | Client has it, index and log current, committed |
| 7 Post-delivery review | Deck diff + client comments codified, replies routed |
