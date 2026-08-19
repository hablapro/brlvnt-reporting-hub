# GCG July 2026 — QA & Cross-Channel Model

Pulled 2026-08-19. Currency USD, TZ America/New_York. Comparison MoM vs June
2026. Client-facing spend basis = **client budget tracker** (standing ruling;
adjustments silent in client materials). July tracker total: **$136,224**.

**FIRST LINE DISCLOSURE: Quantcast is BLOCKED this session** — the MCP cannot
connect without `QUANTCAST_MCP_API_KEY` in the launching shell (KNOWN-BUGS
2026-08-19). Blocks: Quantcast display ($29,857 tracker), the Quantcast Native
share of the $20,298 Native line, the July disallow-list refresh, and model
close. Two other client-facing gates open: July client funnel rows and
comms-since-last-report, both with Renzo.

## QA — platform vs client tracker

| Channel | Platform/vendor pull | Client tracker | Delta | Status |
|---|---|---|---|---|
| Google Search | $29,478.13 | $29,478 | $0.13 | ✅ exact |
| Google PMax (YT) | $18,174.60 | $18,175 | $0.40 | ✅ exact — NEW line, launched wk of Jul 13 |
| Meta | $6,939.50 | $6,940 | $0.50 | ✅ exact |
| Azerion (display) | $28,615.39 raw (+7.5% fee = $30,761.54, internal) | $31,477 | +$715.46 adj | ✅ normal June-pattern adjustment; tracker stands |
| Native (Azerion part) | $9,362.04 raw (+fee = $10,064.19, internal) | $20,298 | ~$10,234 gap | ⏳ HOLD — remainder expected = Quantcast Native; unverifiable until MCP access |
| Quantcast (display) | BLOCKED | $29,857 | — | 🔴 HOLD — MCP credential |
| **Total** | — | **$136,224** | — | +16.4% vs June $117,024 |

## QA checks (runbook Phase 2)

| Check | Result |
|---|---|
| Internal sums | PASS — Google campaign spend sums to Search+PMax totals and to the geo row ($47,652.73); Meta ad-level sums to campaign total ($6,939.50); Azerion ad-set rows sum to vendor totals (display and native) |
| Client tracker | PASS for Google/Meta/Azerion-display; HOLD for Native and Quantcast (above) |
| Conversion source | PASS with two flags (below) — Google = Step 5 event; Azerion = vendor-reported; Meta = pixel rollup, non-scorecard |
| Geo compliance | PASS — Google 100% US (geographic_view); Meta 100% US all 3 campaigns (country breakdown); Azerion vendor files US-filtered at source. Targeting settings: Meta ad sets US-only verified in config; Google/PMax settings not separately verified (delivery clean) |
| Conversion maturity | PASS — pulled 19 days after month close; windows matured |
| Programmatic quality | PARTIAL — Azerion display viewability 64.95% computed, BELOW the 70% floor (vendor summary claims 71.28%; discrepancy flagged, computed figure used). Azerion Native 72.68%, above floor. Quantcast viewability blocked |
| GA4 cross-check | PASS — meta/paid-social 7,902 sessions vs 11,767 GCG link clicks = 67.2% capture (June ~57%). google/cpc not comparable at property level (client-run English campaigns share the property); noted, not blocking |
| Cross-source reconciliation (Bing/SA360) | n/a — GCG has no Bing line |

## Conversion-counting flags (both material, both internal)

1. **Google `metrics.conversions` no longer equals submitted apps.** July
   Search reads 76, but 3 are offline GCLID events (2 approved, 1 funded)
   newly counted as primary. Scorecard = Step 5 only = **73**. June's 67 was
   pure Step 5, so 67 → 73 is the valid MoM. Never quote 76.
2. **PMax's 49 Step-5 conversions sit in `all_conversions` only** — the
   campaign goal config excludes Step 5 from primary (it reports 0
   conversions while driving 49 submitted apps, view-through = 1). The
   campaign is NOT optimizing to submitted applications. Goal-config fix →
   `recommendations/forex/gcg/` (account mechanics, never the deck).

## July model — PROVISIONAL (tracker spend; blocked lines dashed)

| Channel | Spend | Impr | Clicks | Submitted apps / results | CPA (tracker basis) | Viewability |
|---|---|---|---|---|---|---|
| Google Search | 29,478 | 918,059* | 9,568 | 73 (Step 5) | $403.81 | — |
| Google PMax (YT) | 18,175 | * | 14,009 | 49 (Step 5, all_conv) | $370.91 | — |
| Meta | 6,940 | 493,027 | 11,767 (link) | 284 pixel events (rollup, non-scorecard) | — | — |
| Quantcast | 29,857 | BLOCKED | — | — | — | BLOCKED |
| Azerion (display) | 31,477 | 4,769,231 | 8,892 | 80 (vendor) | $393.46 | 64.95% ⚠ below floor |
| Native (QC+Azerion) | 20,298 | 1,170,255 (Azerion part) | 816 | — (upper funnel) | — | 72.68% (Azerion part) |
| **Total** | **136,224** | — | — | **never summed** | — | — |

\* Google impressions: 918,059 is Search+PMax combined (geo view); Search
alone 125,392, PMax 792,667.

## Validated findings so far (pre-Quantcast, pre-funnel)

1. **PMax arrived and performed.** Launched week of Jul 13; $18,175 for 49
   submitted apps at $370.91 in ~18 days — at or below Search's full-month
   CPA ($403.81), on the same Step 5 event, click-based. Config caveat above.
2. **Search: spend outgrew apps again, but less.** +30.9% spend, +9.0% apps
   (67→73), CPA $336→$404. The ad-rank story from June is unchanged in
   direction: lost-to-rank 59-79% vs lost-to-budget 8-12%. Where the rank
   work landed (Trust): IS 27%→32.6%, lost-to-rank →58.7% (account best),
   CPA $433→$390.86, and Trust became the volume leader (28 apps).
3. **The Meta conversion-objective commitment is DELIVERED.**
   0726_GCG_Q3_esp_us_CONV live on OUTCOME_SALES optimizing to the
   SubmittedApplication pixel event, 44% of the (much smaller) $6,940 line.
   Meta spend fell 77% by design as Q2 CTR wound down (paused after July).
4. **Azerion display had its best application month**: 80 vendor-reported
   apps (June 58, +37.9%) at $393.46 tracker CPA (June $510, -22.8%).
   Professional Tools is the new efficiency leader ($197, 18 apps); Spanish
   Platform is the reallocation candidate ($7.3K spend, 9 apps, $812).
   Viewability below floor (64.95%) — vendor flag.
5. **Azerion Native completed its first full month**: $9,362 raw, ramped to
   ~$3.4K/week by month end, viewability 72.7% above floor, CTR 0.070% and
   falling with scale — vendor proposes optimize-to-CTR. Upper-funnel,
   delivery-reported only.
6. **ES-audience traffic gave back the paid lift**: 66,398 sessions (-17.2%)
   as Meta spend fell; slightly below the ~70K Jan-May base. Meta GA4
   capture healthy at 67.2%.

## Open before model close

1. Quantcast pull (display + native split + site list/disallow refresh) —
   needs `QUANTCAST_MCP_API_KEY` at session launch.
2. Native line reconciliation ($20,298 = Azerion ~$10.1K + QC remainder?).
3. July client funnel rows (submitted/live/approved/funded/traded) — Renzo.
4. Comms since the June report — Renzo.
5. figures.json after 1-2 resolve.
