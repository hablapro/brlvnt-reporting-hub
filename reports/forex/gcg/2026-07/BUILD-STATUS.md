# July 2026 Report — Build Status & Resume Handoff (GCG (US Hispanic))

Cycle opened: 2026-08-19. Reporting only; no account mutations from this repo.

Kickoff per `docs/RUNBOOK.md` phase 0. The two standing questions, answered
before any pull:

1. **What does the client already hold for July 2026?**
   - Client budget tracker page: ON HAND, transcribed to
     `data/sources/GCG-client-tracker-July-2026.xlsx`. July working media
     $136,224: Google Search $29,478 · Quantcast $29,857 · Azerion $31,477
     · Native $20,298 · YT (PMax) $18,175 · Meta $6,940. CTV/DOOH/TikTok/
     affiliates $0. Spend basis = tracker (standing ruling).
   - Client funnel / BvA dashboard for July: NOT on hand — asked of Renzo
     2026-08-19 (June had submitted/live/approved/funded/traded rows).
   - Comms since the June report: asked of Renzo 2026-08-19; assumed none
     until answered.
2. **How is the agency scored this month?** Submitted applications and cost
   per submitted application (standing). Google Ads event
   "PO App Form - Step 5 - Submission Completed"; Azerion = vendor-reported
   applications. Verify the Google event name is unchanged at pull time.

**New this month vs June:** YT (PMax) line at $18,175 (was $0) — locate in
Google Ads account 4781995752 and report separately from Search. Native
scaled $3,645 → $20,298 (Azerion Native vendor file on hand). Meta fell
$30,711 → $6,940; `0426_GCG_Q2_esp_us_CTR` delivered $2,104.37 in July
despite being paused now — reconcile the rest.

## Channel status

| Channel | Data pulled | QA | In model | Notes |
|---|---|---|---|---|
| Google Ads (Search) | ✅ 2026-08-19 | ✅ tracker exact | ✅ 2026-08-19 | 73 submitted (Step 5); metrics.conversions=76 incl. 3 GCLID — never quote 76 |
| Google Ads (PMax/YT) | ✅ 2026-08-19 | ✅ tracker exact | ✅ 2026-08-19 | 49 submitted in all_conv only; goal-config fix → recommendations |
| Meta | ✅ 2026-08-19 | ✅ tracker exact | ✅ 2026-08-19 | CONV objective DELIVERED (June commitment); Q2 CTR paused after July |
| Quantcast (display) | ✅ 2026-08-19 | ✅ tracker exact (0.01%) | ✅ 2026-08-19 | $29,854.75; viewability 49.26% (June 46.9%, improving, still below 70% floor) |
| Quantcast (Native) | ✅ 2026-08-19 | ✅ see Native row | ✅ 2026-08-19 | $10,002.73, new campaign (created 2026-07-02), first delivery month; viewability 57.98%, below floor |
| Azerion (display) | ✅ vendor file | ✅ June-pattern adj | ✅ 2026-08-19 | 80 apps, $393.46 tracker CPA; viewability 64.95% computed BELOW floor (vendor claims 71.28% — discrepancy flagged) |
| Native (Azerion + Quantcast) | ✅ vendor file + MCP | ✅ resolved (1.1% delta) | ✅ 2026-08-19 | Azerion raw $9,362 + fee $10,064 (internal) + QC $10,003 = $20,067 vs tracker $20,298 — HOLD cleared |
| GA4 / client funnel | ✅ GA4 2026-08-19; funnel export 2026-08-21 | ✅ capture 67.2%; funnel scope verified (Website es Forex.com US Spanish) | ✅ 2026-08-21 (both) | ES sessions 66,398 (-17.2%); funnel: submitted 404 (+24.3%), sessions 39,446 (-41.6%), app-start rate 7.5% (June 3.8%); two session counts are different scopes, never shown together |

## Phase 3 (Model) — CLOSED 2026-08-19

Model workbook `model/GCG-July-2026-cross-channel-model.xlsx` (Cross-
Channel Model + MoM vs June tabs) and `figures.json` (56 figures, spend
basis, history, MoM deltas) built via
`tools/forex-gcg-july-2026-model/build_model.py`. Final summary table and
MoM table in `qa/qa-and-model.md`. `verify_numbers.py` run against the
model xlsx: 29 MISSING, expected and non-blocking — the xlsx reader only
scans string cells and the model stores figures numerically, same as the
GGMI July model (confirmed 38 MISSING there too, same cause). This is a
Phase 5 gate on the built deck/report, not the Phase 3 model. Funnel rows
and comms-since-June remain open with Renzo; both block Phase 4
(narrative), neither blocked the model.

Bing/SA360: not a GCG channel (GGMI only). Geo check: GCG is US — check
delivery, not just settings, on every channel.

## Carry-overs from last month (June deck, "Recommended next steps (July)")

1. Meta shift to conversion objective, judged on submitted apps — VERIFY
   whether it happened (June deck promised it after a May slip).
2. Search ad-rank program (bids, QS, RSA refresh) on TrackB before budget —
   check July impression share / lost-to-rank for movement.
3. Quantcast: 18-site blocklist delivered covering 32% of June spend +
   viewability-floor recommendation — **verified NOT applied**: all 18
   domains still delivered in July ($11,087 combined). July display
   viewability 49.26% vs 46.9% June (+2.4pts, still below the 70% floor).
   Refreshed 35-domain list issued for July
   (`recommendations/forex/gcg/GCG-Quantcast-disallow-July-2026.md`).
4. Azerion: concentrate on Trusted Broker + Broker 1, format shift
   728x90 → 300x600, viewability above standard; Native pilot detail —
   Native vendor file now on hand.
5. Start-to-submit funnel step on the joint roadmap (client-owned; status
   from Renzo).

Also standing from June QA: Meta tracker $30,711 ruling (platform figure
internal); client "Unique Sessions" scope differs from GA4 (noted, not
blocking). Laura's presentation rules (DOCTRINE §11) apply to GCG:
state the target per channel, no naked stats, MoM on every KPI, Meta split
per campaign by objective.

## Open items before this month can ship

1. ~~July client funnel rows (submitted/live/approved/funded/traded) — Renzo.~~
   RESOLVED 2026-08-21: correctly-scoped export received, added as deck
   slide 12, `figures.json` extended, gates re-run clean.
2. Comms-since-last-report check — Renzo.

Item 3 (Meta objective-shift status and $6,940 composition) resolved in
Phase 1-3: conversion objective (OUTCOME_SALES) DELIVERED, 44% of Meta
spend; traffic-line/conversion-line split documented in figures.json and
the model's MoM tab.

## Phase 4 (Narrative) — CLOSED 2026-08-20

Draft: `output/GCG-Jul-2026-narrative-draft.md`, stop-slop'd, built to the June
GCG narrative's shape with DECISION lines added per DOCTRINE §11. Answers all
five of June's "Recommended next steps" explicitly (see narrative's closing
section): Meta shift DONE; ad-rank program PARTIAL (Trust proven, Authority/
Platform not yet reached); Quantcast blocklist NOT APPLIED, refreshed;
Azerion concentration PARTIAL (Professional Tools is the new leader, format
shift unverifiable this month, vendor file lacks the format cut); funnel step
OPEN, client-owned. Pending Renzo's approval per the one-approval-gate rule
(runbook Phase 4) before this counts as fully closed.

## Phase 5 (Build) — deck built 2026-08-20, three of four gates PASS

Build script `tools/forex-gcg-july-2026-deck/build_deck.py`, 12 slides, to the
delivered GGMI July 13-slide template. Output:
`output/GCG_US_July_2026_Performance_Review.pptx`.

| Gate | Run | Result |
|---|---|---|
| QA reconciliations | 2026-08-19 | PASS — see qa/qa-and-model.md |
| Tracker reconciliation | 2026-08-19 | PASS, all six channels within normal adjustment range |
| Phase 3 model + figures.json | 2026-08-19 | CLOSED — see Phase 3 section above |
| `scripts/verify_numbers.py` | 2026-08-20 (deck pptx) | 4 MISSING, 0 UNSOURCED. All 4 accepted/documented: `azerion.viewability_vendor_claim` deliberately excluded (vendor's own conflicting viewability claim, judged internal-QA-only, computed figure used instead — flagged to Renzo for a ruling); `mom.meta_spend_pct`, `mom.quantcast_spend_pct`, `mom.azerion_cpa_pct` are all negative-valued figures.json entries that ARE stated in the deck in natural phrasing ("down 77.4%", "down 2.3%", "fell 22.8%") — the gate script's number regex does not capture minus signs so a negative approved figure can never match unsigned deck prose; new tool limitation, recorded in `KNOWN-BUGS.md`. Two figures.json figures added at build time (`quantcast.june_disallow_spend_still_delivered`, `quantcast.july_disallow_refresh_spend`) to clear the $10,000 currency-floor UNSOURCED check on the disallow-list disclosure, sourced from qa-and-model.md |
| `scripts/protection_scan.py` | 2026-08-20 (deck pptx) | PASS — 0 BLOCK, 0 WARN |
| Render QA (slide count + visual) | 2026-08-20 | PARTIAL. Slide count confirmed programmatically (12/12, `Deck.verify()` and python-pptx both agree) and no shape exceeds the slide's bounding box. **The visual look (PowerPoint AppleScript PDF export per KNOWN-BUGS.md) could not complete in this session** — PowerPoint did not respond to AppleScript automation (hung/no GUI session in this subagent), one retry made per the bounded-effort rule, then stopped and disclosed rather than retried further. A human or a session with a working GUI needs to open the pptx and eyeball every slide before delivery, particularly the four dense tables (Search keywords, Meta creatives x2, Azerion audience ranking, Azerion Native creatives) for row-height/footer overflow |
| Doctrine walk (`docs/DOCTRINE.md`) | 2026-08-20 | PASS with two disclosed gaps: (1) "creative previews earn slides" (§11) — the Meta and Azerion Native creative slides are data tables with verdicts, not actual creative image previews; no creative asset images were available in this month's data pull. (2) the vendor-viewability-claim exclusion above |

**Not delivered.** This pptx is a draft for Renzo's gate, per the dispatch
brief. Not uploaded, not committed as final, GGMI files untouched.

## Render-QA round (2026-08-20) — 5 findings, all fixed

Team-lead rendered and inspected all 12 slides. Findings and fixes: (1) FAIL,
slides 9/10 table/card overlap clipping the status column — narrowed both
tables and added a proper gap before the card; (2) cover title em dash —
replaced with the middot separator used elsewhere in the deck; (3) Azerion
weekly table missing its Jul 29-31 row (spend gap vs the headline) — added
the row back, now reconciles to the month; (4) Meta conversion-campaign
sessions (Laura checklist #3) — GA4 can't isolate sessions to the conversion
campaign alone this month, disclosed on-slide rather than omitted, checklist
score for #3 downgraded to partial; (5) slide 6 status-column text wrap —
rebalanced column widths. Re-ran both gates after fixing: same 4
accepted MISSING (0 UNSOURCED), `protection_scan.py` PASS 0/0.

## Client funnel added (2026-08-21) — deck now 13 slides

Correctly-scoped funnel export arrived (`data/sources/GCG-client-funnel-Jan-Jul-2026.xlsx`,
filter "Website es Forex.com US Spanish", verified against the whole-site
file that was rejected earlier). Added as new slide 12 (`CLIENT FUNNEL ·
JULY VIEW`), positioned after the GA4 site-traffic slide and before the
cross-channel closer (now slide 13) — a judgment call on placement since the
delivered GGMI 13-slide template carries no funnel content to copy
positionally (it was cut there); flagged for Renzo/team-lead to correct if a
different slot was intended. `figures.json` extended with 30 `funnel.*`
figures (July, Q1, Q2) plus 10 June comparator values in `history`, sourced
from the SAME export for both periods per the no-restatement-commentary
rule — the stale June-deck snapshot (322/306/145/41/30) is not referenced
anywhere. The closer's fourth blocker (previously "Measurement to close,"
promising the funnel "next cycle") is rewritten to "Downstream to watch"
since the gap it described no longer exists. Narrative draft's funnel
section, Data Quality item 5, Recommended Next Steps item 5, and June
Commitment 5 all rewritten from "pending" to delivered.

Re-ran both gates: `verify_numbers.py` — same 4 previously-accepted MISSING
(0 UNSOURCED; all 30 new funnel figures matched cleanly, no new findings).
`protection_scan.py` — PASS, 0 BLOCK, 0 WARN. Shape-bounds check — 13/13
slides, 0 overflow. Render QA not re-attempted in this session (no working
GUI); team-lead re-rendering per their own message.

## Viewability demoted (2026-08-24) — DOCTRINE §11 standing ruling

Renzo ruling, 2026-08-17, GGMI cycle (mis-pointed to at first, now in
DOCTRINE.md §11 explicitly): viewability is a vanity metric. Data-point
mentions only, no headlines, no KPI tiles, no 70% floor language anywhere
in a client deck. Applied to slides 7, 8, 10, 13: killed viewability
KPI tiles on 7 and 8 (replaced with sourced delivery figures already in
figures.json — Native impressions/clicks on 7, Avg CPC on 8); slide 7's
headline and card rewritten number-first with viewability reduced to one
data-point sentence and no floor reference; slide 10's creative table
restructured to Spend/Clicks/CTR (viewability column removed) — the
SCALE ranking was recomputed on CTR alone, not just relabeled, since two
creatives (City_view_MHTN, Phone_closeup) swap places when viewability
drops out of the basis; slide 13's Priority blocker had an indirect floor
reference ("the same floor has been proposed") caught on the grep sweep
and reworded. `mom.quantcast_viewability_pts` (2.36) joined the
accepted-MISSING set on `verify_numbers.py` since the deleted delta
sentence was its only occurrence in the deck.

## §8 sweep — June-list-not-applied content ruled internal (2026-08-24)

Renzo ruling (DOCTRINE §8 class): the June Quantcast disallow list's
never-applied status — $11,086.71 still delivered on the 18 flagged
domains, yahoo.com $2,270→$2,359 — is an internal accountability matter
Renzo handles directly with Jean Paul, not client-deck material. Removed
entirely from slide 7's "The site list" card and slide 13's HIGH blocker;
both now carry neutral forward framing only ("send the refreshed list to
Quantcast ahead of August," no dollar figure, no "never applied," no
"second cycle," no yahoo.com callout). `figures.json` figures
`quantcast.june_disallow_spend_still_delivered` and
`quantcast.july_disallow_refresh_spend` removed (they existed solely to
source the deleted text); the underlying evidence stays fully documented
in `qa/qa-and-model.md` and
`recommendations/forex/gcg/GCG-Quantcast-disallow-list-July-2026.md`,
which now opens with an explicit internal/not-client-facing marker.

Full 13-slide §8 sweep run fresh (not assuming earlier rounds got this
dimension right): only slides 7 and 13 held genuine violations; all other
11 slides re-read clean — see the session report to team-lead for the
per-slide reasoning.

Gates re-run: `verify_numbers.py` — 5 accepted MISSING (unchanged from
the viewability round; the two figure removals matched the two text
removals exactly, so nothing new went MISSING or UNSOURCED).
`protection_scan.py` — PASS, 0 BLOCK, 0 WARN. Shape-bounds — 13/13, 0
overflow. Also caught and fixed one unrelated typo in slide 8's weekly
table footnote during this pass ("the month's month total" → "the
month's client-facing total").
