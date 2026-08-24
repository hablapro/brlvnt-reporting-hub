# Resume Here

Read this first when picking the repo back up. Last updated 2026-08-19.
Delete or rewrite when the state changes.

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

### GCG July cycle — DECK APPROVED (Renzo gate 2026-08-24) and COMMITTED (26493ec)

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

Renzo's 12 pptx comments applied 2026-08-24 (six new standing rules in
DOCTRINE §3); deck approved and everything committed locally (26493ec,
not pushed). Open: (1) client delivery is with Renzo (once he edits a
Google Slides version, THAT becomes canonical — never re-upload over
it); (2) no report workbook was built this cycle (deck only, per Renzo's
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
