# Resume Here

Read this first when picking the repo back up. Last updated 2026-08-18
(session close). Delete or rewrite when the state changes.

---

## Where things stand

### July 2026 GGMI cycle — DECK FINAL, AWAITING PHASE 6

The deck (`reports/forex/ggmi/2026-07/output/GGMI_LATAM_July_2026_Performance_Review.pptx`,
16 slides) and report workbook are built, gate-clean, and reflect every Renzo
ruling through 2026-08-17. Built entirely by
`tools/forex-ggmi-july-2026/build_deck.py` — **the script is the source of
truth; never hand-edit the pptx, and never keep it open in PowerPoint during
a rebuild** (it clobbers the output; see KNOWN-BUGS).

Open items, all waiting on external data (slot in, re-run gates, deliver):

1. **July trading volume** (slide 2 row shows a dash) — Renzo asking client.
2. **Country-tab period** — client says July-only but the tab foots to 2026
   YTD (5,724 submitted vs July's 653); Renzo asking. Mexico absolute counts
   go in once answered (rates-only bullet meanwhile). Draft client note:
   `output/client-note-country-data-july.md`.
3. **DOOH venue mix** (airport/roadside/mall table has dash placeholders) —
   Renzo fills when vendor data arrives.

Phase 6 on Renzo's word: upload deck + report to FX Report Drive folder
(`1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55`, shared drive), verify by reading back,
then close the cycle (REPORT-INDEX, REPORTING-LOG, tracker note, archive
BUILD-STATUS).

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
