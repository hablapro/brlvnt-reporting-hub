# GCG July 2026 — QA & Cross-Channel Model

Pulled 2026-08-19. Currency USD, TZ America/New_York. Comparison MoM vs June
2026. Client-facing spend basis = **client budget tracker** (standing ruling;
adjustments silent in client materials). July tracker total: **$136,224**.

**FIRST LINE DISCLOSURE: Quantcast pull completed 2026-08-19**, resolving last
week's BLOCKED state. One new tool issue hit and worked around (see Quantcast
section below): the `quantcast_metrics_report` `filters` parameter returned
empty results on every attempt (not the previously-documented
`quantcast_campaigns`/`quantcast_accounts` object-filter bug) — worked around
by pulling the account unfiltered and filtering client-side on Campaign Name,
consistent with the GGMI July pull's approach. The Domain/App breakdown also
hit the sync token limit and then an MCP session expiry on retry; recovered
via `quantcast_async_report`. Two client-facing gates remain open: July client
funnel rows and comms-since-last-report, both with Renzo.

## QA — platform vs client tracker

| Channel | Platform/vendor pull | Client tracker | Delta | Status |
|---|---|---|---|---|
| Google Search | $29,478.13 | $29,478 | $0.13 | ✅ exact |
| Google PMax (YT) | $18,174.60 | $18,175 | $0.40 | ✅ exact — NEW line, launched wk of Jul 13 |
| Meta | $6,939.50 | $6,940 | $0.50 | ✅ exact |
| Azerion (display) | $28,615.39 raw (+7.5% fee = $30,761.54, internal) | $31,477 | +$715.46 adj | ✅ normal June-pattern adjustment; tracker stands |
| Native (Azerion + Quantcast) | $9,362.04 (Azerion raw) + $10,002.73 (QC) = $19,364.77; with Azerion fee: $10,064.19 + $10,002.73 = $20,066.92 | $20,298 | $231.08 (1.1%), fee-inclusive basis | ✅ resolved — HOLD cleared. Composition: QC Native + fee-inclusive Azerion Native reconciles the tracker to within 1.1%, the same order of adjustment as the Azerion display line |
| Quantcast (display) | $29,854.75 | $29,857 | $2.25 (0.01%) | ✅ exact |
| **Total** | — | **$136,224** | — | +16.4% vs June $117,024 |

## QA checks (runbook Phase 2)

| Check | Result |
|---|---|
| Internal sums | PASS — Google campaign spend sums to Search+PMax totals and to the geo row ($47,652.73); Meta ad-level sums to campaign total ($6,939.50); Azerion ad-set rows sum to vendor totals (display and native) |
| Client tracker | PASS for Google/Meta/Azerion-display/Quantcast-display; PASS (1.1% delta) for Native once Quantcast is in the mix |
| Conversion source | PASS with two flags (below) — Google = Step 5 event; Azerion = vendor-reported; Meta = pixel rollup, non-scorecard; Quantcast Results = platform-attributed, internal only |
| Geo compliance | PASS — Google 100% US (geographic_view); Meta 100% US all 3 campaigns (country breakdown); Azerion vendor files US-filtered at source; Quantcast 100% US across both campaigns (52-state Region breakdown, zero non-US rows, delivery checked not just targeting). Targeting settings: Meta ad sets US-only verified in config; Google/PMax/Quantcast settings not separately verified (delivery clean) |
| Conversion maturity | PASS — pulled 19 days after month close; windows matured |
| Programmatic quality | PARTIAL — Azerion display viewability 64.95% computed, BELOW the 70% floor (vendor summary claims 71.28%; discrepancy flagged, computed figure used). Azerion Native 72.68%, above floor. Quantcast display 49.26% (June 46.9%, improving, still below floor) and Quantcast Native 57.98% (no June comparator, below floor) — both FAIL vs the 70% floor |
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
| Quantcast (display) | 29,857 | 22,486,572 | 2,574 | 15 (platform, internal only) | — | 49.26% ⚠ below floor |
| Azerion (display) | 31,477 | 4,769,231 | 8,892 | 80 (vendor) | $393.46 | 64.95% ⚠ below floor |
| Native (QC+Azerion) | 20,298 | 1,170,255 (Azerion) + 9,411,481 (QC) | 816 (Azerion) + 1,660 (QC) | 10 (QC, platform, internal only) | — | 72.68% (Azerion) / 57.98% (QC) ⚠ both below floor |
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

## Quantcast — July 2026 (pulled 2026-08-19)

Source: `quantcast_metrics_report` + `quantcast_async_report`, account 9969644,
2026-07-01–2026-08-01, America/New_York. Workbook:
`reports/forex/gcg/2026-07/data/GCG-Quantcast-July-2026-data.xlsx`.

1. **Two live campaigns, tracker-tight.** Display `Forex_GCG_spanish_conversion_Q+campaign_us`
   $29,854.75 (tracker $29,857, delta 0.01%). Native
   `Forex_GCG_spanish_conversion_Q+campaign_NativeOnly_US_ES` $10,002.73 — a
   brand-new campaign, created 2026-07-02, first delivery month. Two other
   GCG campaigns (old-naming, paused) had $0 July spend.
2. **Native line reconciliation resolved.** QC Native $10,002.73 + Azerion
   Native (fee-inclusive, internal) $10,064.19 = $20,066.92 vs the $20,298
   tracker line — 1.1% delta, the same class of normal adjustment as the
   Azerion display line. Clears last week's HOLD.
3. **Geo: 100% US, PASS.** Every dollar across 52 states/territories in the
   Region breakdown; zero non-US rows on either campaign.
4. **Viewability improving but still below floor.** Display 49.26% (June
   46.9%, +2.4pts) — second straight month of improvement, still 20.7pts
   under the 70% IAB floor. Native 57.98% — no June comparator (new
   campaign), also below floor.
5. **The June disallow list was not applied.** All 18 domains flagged in
   June's list (`recommendations/forex/gcg/GCG-Quantcast-disallow-June-2026.txt`)
   still received July spend — $11,087 combined. yahoo.com, June's single
   largest flag at $2,270, grew to $2,359. Refreshed list: 35 domains,
   $13,456 (34% of spend), same criteria as June (spend ≥$100, viewability
   <40%) — `recommendations/forex/gcg/GCG-Quantcast-disallow-July-2026.md`
   and `.txt`.
6. **Tool issues, both worked around, no data gap.** The `metrics_report`
   `filters` parameter returned empty results on every breakdown this
   session (new finding, not the previously-documented `quantcast_campaigns`
   object-filter bug) — worked around with unfiltered pulls filtered
   client-side on Campaign Name; every total ties to the cent against the
   account-level campaign summary. The Domain/App breakdown exceeded the
   sync call's token limit and then hit an MCP session expiry on retry;
   recovered via `quantcast_async_report` (CSV export), which ties to the
   account total within $2.68 — expected two-decimal rounding across 10,586
   CSV rows, not a data issue.

## Open before model close

1. July client funnel rows (submitted/live/approved/funded/traded) — Renzo.
2. Comms since the June report — Renzo.
3. figures.json once 1-2 resolve. Quantcast, Azerion, Google, and Meta are
   all tracker-reconciled and ready to feed the model.
