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
3. Comments 4 and 5 (June CPM, 25+ effect) are answerable from data on
   hand — draft replies for Renzo before or with the August deck.

Cycle-close bookkeeping (REPORT-INDEX, REPORTING-LOG, tracker note,
archive BUILD-STATUS) still pending.

### August 2026 GGMI — build to the NEW template

`build_deck.py` must be rebuilt to the delivered 13-slide structure
(DOCTRINE §11) before the August cycle. Do not rebuild from the 16-slide
July script shape.

### GCG July cycle — NOT STARTED (ruled: GGMI first)

Inputs already on hand: GCG client tracker transcribed
(`reports/forex/gcg/2026-07/data/sources/`), Azerion GCG July files
downloaded there too. Remember: `0426_GCG_Q2_esp_us_CTR` delivered $2,104.37
in July despite being paused now.

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
