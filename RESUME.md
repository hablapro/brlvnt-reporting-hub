# Resume Here

Read this first when picking the repo back up. Last updated 2026-08-27.
Delete or rewrite when the state changes.

---

## NEXT JOB: the GCG August 2026 cycle. Not started.

Before pulling any GCG data, read the three items below. The first two were found
on 2026-08-27 and will silently corrupt a GCG build the same way they
corrupted the GGMI one.

### 1. SA360 `metrics.conversions` no longer equals submitted applications

True through July 2026, false from August. On GGMI Bing three extra actions
started counting into the primary metric: `GCLID - Approved`, `GCLID - Funded`
and `App Form - Step 4`. August read 53 where only 41 were submitted
applications. **Check whether the same happened on GCG before trusting any
conversion figure.** Segment by `segments.conversion_action_name` and count
only `- Live Confirmation`. Full detail in `KNOWN-BUGS.md`.

### 2. Quantcast `endDate` is exclusive and it bit us again

August figures were pulled with `endDate: 2026-08-26`, which returns Aug 1-25,
were labelled "MTD Aug 1-26", then projected x31/26. Two compounding errors.
For an inclusive range ending day N, set `endDate` to N+1 and project on the
day count the pull actually covers.

### 3. Client-facing documents are formatted, not just converted

Build every .docx with `python3 scripts/format_doc.py <in.md> <out.docx>`,
never bare `pandoc`. Then render to PDF and look at it. See CLAUDE.md Output.

---

## GGMI September budget proposal — DELIVERED 2026-08-27

Google Doc `1NkIHJGRJAeBJJG3vI7r8MDrceWT3ibQ-wYcnQx_34eE` (update in place,
never republish to a new URL). Source markdown and `figures.json` in
`reports/forex/ggmi/2026-08/`.

Two options against the approved September plan of $205,000: **Controlled
$61,000** (recommended, -70% vs plan, -51% vs the four active August channels)
and **Deep $33,500** (-84% / -73%). Meta, TikTok and Strategic Partnerships
($80K) deferred, not cancelled. Review in the first half of October, ramp
mid-to-late October ahead of the Nov 3 midterms and Nov 5 Banxico.

Open items carried forward:

1. **Funded-account quality by source.** The proposal states in the client
   copy that we have NOT established Bing applications fund better than
   Azerion's. That data is the check that confirms or overturns the whole
   weighting. Priority ask for the October review.
2. **Who changed the SA360 conversion actions to primary, and when.**
   Question for the StoneX SA360 admin.
3. **Can FOREX.com or CM360 produce deduplicated source-level application
   counts?** If yes, channel counts become summable and the proposal gets a
   stronger headline back. If no, keep showing them per channel.
4. **Full-month August Azerion vendor report.** Current figures are projected
   from the Aug 1-17 mid-month file.

---

## Where things stand

### July 2026 GGMI cycle — DELIVERED. Canonical = the Google Slides file

Renzo restructured the built 16-slide deck into a 13-slide final and shared
it with the client: Slides `1IbiLHpMdu_EFG4zaiTv4Xu13boJKTgxLbayntrxH_o8`
("GGMI_LATAM_July_2026_Review-final"). That file is canonical; the local
PPTX is the superseded draft. The three formerly-open external-data items
(trading volume, country tab, DOOH venue mix) were resolved by removal —
Renzo cut the blocks that carried them.

Post-delivery review is DONE (2026-08-19), now a standing monthly phase
(RUNBOOK Phase 7). Read
`reports/forex/ggmi/2026-07/qa/final-deck-review-2026-08-19.md`:
full built-vs-delivered diff plus Laura Acosta's five comments. Template
and presentation rules codified in DOCTRINE §11.

Open follow-ups from Laura's comments (all on the Slides file, unresolved):

1. **Meta slide rework is the big one**: per-campaign split by objective
   (engagement: reach/impressions/CPM; conversion: CTR/sessions/
   conversions), best creatives, June CPM comparator, 25+ targeting
   before/after on reach and CPM. She said "once again" — standing rule.
2. Azerion (and every channel) slide must state the target audience.
3. Replies POSTED to all five comment threads 2026-08-19 (as Renzo,
   approved, verified by read-back). Laura's resolution/response is the
   next signal to watch. Approved drafts + backup facts:
   `reports/forex/ggmi/2026-07/output/laura-comment-replies-2026-08-19.md`.
   Key facts inside: the 25+ refinement was
   never applied — Meta's "Financial Products and Services" special ad
   category (mandatory 2025-01-21) locks age at 18-65+, verified by web
   research 2026-08-19; June-vs-July blended CPM ($1.31 → $1.89) is an
   objective-mix artifact, like-for-like traffic CPM improved
   ($1.27 → $0.94); reach fell because budget fell ($24.0K → $3.3K).
   CPM doctrine refined in §11: role depends on objective, never a
   blanket "not a KPI".

Cycle-close bookkeeping (REPORT-INDEX, REPORTING-LOG, tracker note,
archive BUILD-STATUS) still pending.

### August 2026 GGMI — build to the NEW template

`build_deck.py` must be rebuilt to the delivered 13-slide structure
(DOCTRINE §11) before the August cycle. Do not rebuild from the 16-slide
July script shape.

### GCG July cycle — CLOSED: 14-slide deck APPROVED and COMMITTED (final 1a2ba39)

Phases 0-5 complete as of 2026-08-24. State of record:
`reports/forex/gcg/2026-07/BUILD-STATUS.md` and `qa/qa-and-model.md`.

- All six channels pulled, workbook'd, tracker-reconciled ($136,224).
  Quantcast MCP unblocked 2026-08-19 (user-level config; KNOWN-BUGS).
- Model + figures.json final (tracker basis; 73 Search / 49 PMax apps,
  never 76). Client funnel received 2026-08-21 (US-Spanish scope verified;
  the whole-site export was rejected) and built in as slide 12.
- Deck: `output/GCG_US_July_2026_Performance_Review.pptx`, 13 slides to
  the delivered-GGMI §11 template, through nine review rounds: Laura's
  five rules applied, Meta paused/flagged status (StoneX owns resolution,
  no forward Meta commitments), client-proofing, humanizer, viewability
  demotion, §8 internal-content sweep (June-disallow-list status is
  INTERNAL, Renzo handles with Jean Paul), plain-language rewrite for
  non-specialist readers (Dina/Raman). Gates clean: protection_scan
  0 BLOCK; verify_numbers 5 accepted MISSING (documented in
  BUILD-STATUS) / 0 UNSOURCED; render QA on every slide.
- Internal evidence for the Jean Paul conversation:
  `recommendations/forex/gcg/GCG-Quantcast-disallow-list-July-2026.md`
  (marked Internal; 35-domain July list + June-list status).

Renzo's 12 pptx comments applied 2026-08-24 (six standing rules in
DOCTRINE §3); blended June-format opener added as slide 2 (deck 14
slides, §11 opener rule now per-entity) and downstream story reframed
(approvals +5.9% grew with volume; funding 19.8% is the watch item,
FOREX.com's process). Final deck approved by Renzo 2026-08-24 and
committed locally (26493ec, 3de9f3d; not pushed). Open item (1) CLOSED 2026-08-25: GCG July deck DELIVERED to client by Maria via ClickUp (client-shared space 90171157891) and email (Renzo confirmed 2026-08-25). If a Google Slides version appears with Renzo/Maria edits, THAT becomes canonical — never re-upload over it. Remaining open: (2) no report workbook was built this cycle (deck only, per Renzo's
request) — build one only if asked; (3) comms-since-June never answered
(narrative assumed none); (4) cycle-close bookkeeping (REPORT-INDEX /
REPORTING-LOG) pending for BOTH July cycles. Read DOCTRINE §3/§8/§11
before touching any deck; the comment-round rulings are binding.

## Rulings made this cycle (all in docs/DOCTRINE.md + auto-memory — READ THEM)

- **Permanent reporting rule** (§1): each channel on its own partner signal;
  channel/source/decision-basis table; methodology note stated ONCE; no
  blending across attribution systems — the June combined Bing+Azerion
  metric is RETIRED. Terminology: "partner-attributed".
- **Deck scope** (§8): account mechanics (targeting/bidding/settings/conversion
  config) never in client decks — recommendations file + Renzo only.
- **Tone** (§3): calm/level headlines, "came in at" not "fell"/"biggest";
  headline earns its place or the slide runs without one; no viewability as
  headline/priority (vanity metric — data point only).
- **No assumptions**: source labels never exceed verified facts (Bing =
  SA360-reported source of record, NOT "CRM-validated"); Bing bidding lives
  at the SA360 layer (native ExcludeFromBidding flags are expected).
- Bing Jul 1–10 = planned rebuild (Ruben), never "dark/down". Meta 25+
  restricted by Meta financial-vertical policy. Meta paid paused,
  StoneX-owned. Quantcast June blocklist was executed (internal fact).

## Ops handoff to Ruben (via Renzo)

`recommendations/forex/ggmi/GGMI-Bing-August-2026-actions.md`: geo setting
still PRESENCE_OR_INTEREST + no Venezuela exclusion (P0, dormant risk),
SA360 conversion-based bid strategy (all 8 campaigns MANUAL_CPC, verified
2026-08-17), landing destinations, query negatives.

## Supporting artifacts this session

- Partner-level detail (internal, unmasked):
  `reports/forex/ggmi/2026-07/output/GGMI-July-2026-partner-detail.md`
- QA + rulings record: `reports/forex/ggmi/2026-07/qa/qa-and-model.md`
- Figures: `reports/forex/ggmi/2026-07/figures.json` (regenerate via
  `tools/forex-july-2026-ggmi-model/build_model.py`)
- Build status: `reports/forex/2026-07-BUILD-STATUS.md`

## Prior handover thread (2026-08-08)

Still pending Renzo: push destination decision, MCP secret handover, access
grants, doctrine confirmations. 60+ commits are local-only.
