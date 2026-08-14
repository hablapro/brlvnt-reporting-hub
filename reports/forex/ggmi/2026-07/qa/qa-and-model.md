# GGMI July 2026 — QA and Model Note

Written 2026-08-14. Phase 2 (QA) and Phase 3 (model) close-out. Data lives in
the workbooks; this note records checks and the model summary only.

## Phase 2 QA checks

| Check | Result |
|---|---|
| Cross-source reconciliation (Bing direct vs SA360) | PASS — $10,624.95 vs $10,624.94 (1¢ rounding) |
| Internal sums, all 5 channel workbooks | PASS — recorded in each workbook's Notes & QA tab |
| Client tracker reconciliation | PASS — Bing Δ$0.06, Meta Δ$0.45, Quantcast main Δ$3.20; Azerion tracker lines = vendor × 1.10 exactly (Δ<$3). Internal only. |
| Conversion source | PASS — Bing from SA360 only; Azerion vendor-reported (disclosed); Meta pixel fires excluded per ruling 2026-08-04; Quantcast n=15 not published |
| Geo compliance | Bing delivery 2.7% non-MX, **setting still PRESENCE_OR_INTEREST — breach dormant, not fixed**; Meta 100% MX verified; Quantcast 100.00% MX verified; Azerion unverifiable from vendor file ("LATAM", no country split) — disclosed |
| Conversion maturity | CLOSED — SA360 re-pulled 2026-08-14, July conversions unchanged at 20; figures final |
| Programmatic quality | Quantcast viewability 54.45% (FAIL vs 70% floor, disallow list is the lever); Azerion display 82.47% and native 77.34% PASS |
| GA4 cross-check | Diagnostic only this cycle; key-event fix landed Jul 31 (verified holding at 100% Aug 1–4); August is the first month GA4 can corroborate submitted apps |

Open disclosure items carried to the narrative: legacy Bing campaigns' zero
conversions (destination split, see build status), Meta reported
spend/delivery only, Azerion geo unverifiable, Quantcast viewability.

## Phase 3 model summary (client-facing basis)

| Channel | Spend (tracker) | Impressions | Clicks | Submitted apps | Cost per app |
|---|---|---|---|---|---|
| Bing (Search) | $10,625 | 90,394 | 4,090 | 20 | $531.25 |
| Quantcast (Display) | $39,240 | 50,483,289 | 19,188 | — | — |
| Azerion (Display) | $37,509 | 7,577,455 | 12,915 | 41* | $914.85* |
| Native (QC + Azerion) | $27,630 | 18,179,528 | 9,953 | — | — |
| Meta (Social) | $8,027 | 4,250,494 | 91,153 | — | — |
| DOOH (Perion) | $26,865 | — | — | — | — |
| **Total** | **$149,896** | 80,581,160 | 137,299 | — | — |

\* Azerion apps are vendor-reported, not CRM-validated. Total row carries no
conversion or CPA figure: each channel reports a different event from a
different system.

Model workbook: `model/GGMI-July-2026-cross-channel-model.xlsx`.
Declared figures: `figures.json` (spend basis stated inside).

Bing intra-month split (the July story): dark Jul 1–10 · Phase A legacy
Jul 11–22, $5,883, 0 apps · Phase B rebuilt MX_ Jul 22–31, $4,742, 20 apps
at $237.12.

## Decisions defaulted, for Renzo at narrative approval

1. **DOOH line included** in the spend summary (tracker structure; client
   expects $149,896 to foot). June deck had no DOOH line. Spend only, no
   delivery claims.
2. **Native reported as its own line** matching the tracker, composition
   (Quantcast NativeOnly + Azerion native) stated once, neutrally.
3. **Meta clicks** = all clicks (91,153), consistent with June's definition;
   link clicks (74,489) live in the channel workbook if the deck wants them.
