# GGMI (LATAM) — May 2026 — QA Note + Modeled KPI Tables

Period: 2026-05-01 to 2026-05-31. Currency USD. Timezone America/New_York. Comparison: MoM vs April 2026. ROAS excluded (no revenue tracking on any channel).

## QA / Data Quality

| Check | Result |
|---|---|
| Bing source | Spend/impr/clicks pulled bing-ads MCP direct (acct 31003116) AND reconciled to SA360 (customerId 5372690580 / loginCustomerId 9697709980) — match exactly. SA360 confirmed working (earlier "blocked" was wrong); SA360 is the source for Bing conversions. |
| Bing keyword spend reconciles to campaign total | PASS (~$15,969 vs $15,972, rounding) |
| Bing conversions | PASS — submitted applications (Primary conversion = live-account confirmation goal, KPI) = 33 (May 1-31) at $484 CPA via SA360. Full funnel fires (all_conversions May 4-Jun 2: 558→66→24→17→26 funded, +3 MT5). Earlier '0/gap' was a reading error: metrics.conversions (Primary only) vs all_conversions, plus -1777 synced goal copies. |
| Meta conversions = aggregated fb_pixel_custom app events | PASS (4 app events) — funnel failure, not a tracking gap |
| Azerion spend reconciles to ad-set sum | PASS (~$27,258 across 7 ad sets) |
| Quantcast spend = reconciled campaign total, single delivering campaign | PASS ($26,890.00, Forex_GGMI_spanish_conversion_campaign_mx; client-confirmed 2026-06-08. MCP Budget Delivered showed $25,013.56; reconciled up ~$1,876, impressions/clicks unchanged, CPM/CPC/CPA recomputed) |
| Cross-channel conversion definitions comparable? | NO — different events per channel; do not sum CPA. |

### Attribution note (carry into Data Notes tab)
Bing submitted applications (KPI) = 33 via SA360 (Primary conversion = live-account confirmation goal; tracking works, full funnel fires). Meta = pixel app events. Azerion = Step 1 + completed application. Quantcast = Results (1 click-through). Spend and impressions are summable; conversions/CPA are per channel.

## Modeled cross-channel summary (May 2026)

| Channel | Spend | Impressions | Clicks | CTR | CPM | CPC | Primary conversions | CPA |
|---|---|---|---|---|---|---|---|---|
| Bing | 15,972.00 | 368,704 | 29,944 | 8.12% | — | 0.53 | 33 submitted apps (SA360 Primary) | 484.00 |
| Meta | 6,626.06 | 6,838,850 | 128,231 | 1.875% | 0.97 | — | 4 app events | 1,656.52 |
| Azerion | 27,257.72 | 6,057,272 | 6,301 | 0.10% | 4.50 | — | 37 apps / 225 Step 1 | 736.70 / 121.15 |
| Quantcast | 26,890.00 | 16,481,325 | 4,807 | 0.0292% | 1.63 | 5.59 | 1 result (CT) | 26,890.00 |
| **Total** | **76,745.78** | **29,746,151** | **169,283** | — | — | — | see note | — |

## MoM totals
- Total spend April = $45,736 (Bing 15,289 + Meta 5,227 + Azerion 10,215 + Quantcast 15,005) → May $76,746 = **+68%**, driven by Azerion (+167%) and Quantcast (+79%). [Corrected 2026-06-02: April mis-added as $35,736. Corrected 2026-06-03: Quantcast May $23,826 → $25,014 after endDate fix. Corrected 2026-06-08: Quantcast May $25,014 → $26,890 (reconciled campaign total; impressions/clicks held, CPM/CPC/CPA recomputed).] Note: this modeled table uses raw Azerion ($27,257.72); client deliverables use fee-inclusive Azerion ($29,302.05), so the client-facing May total is $78,790.

## Key findings (validated)
1. **Media delivery is strong and cheap across all four channels;** the constraint is the Mexico landing-page/application funnel, not media. Meta produced 64,264 LPV but only 4 applications (0.006% of LPV).
2. **Bing and Azerion both convert at scale.** Bing = 33 submitted applications at $484 CPA (most efficient GGMI converter, via SA360). Azerion = 37 applications (up 95% MoM, $736.70 CPA, +37%) on +167% budget; Experience + TradeForex lead.
3. **Bing tracking works (audit-confirmed); it is GGMI's most efficient converter** at 33 submitted applications / $484 CPA. Efficient brand capture ("plataforma metatrader" QS10 $0.31 CPC); new TradingView theme (~24% of spend, $2.34-$4.99 CPC) unproven, dragged CTR down (11.66%→8.12%), CPC up ($0.46→$0.53). The earlier 'gap' was a reading error (resolution note on file).
4. **Quantcast recorded its first conversion** (1, click-through) after the April pixel fix — directional confirmation only; viewability 67.1% still below IAB 70%.
5. **SA360 works** (customerId/loginCustomerId convention); pull conversions with metrics.all_conversions (full funnel) and metrics.conversions (Primary/KPI), ignoring the -1777 synced copies. GCG Google Ads 76 = all "Step 5 Submission Completed" (clean). Meta (Start 108/Submit 1 GCG; 4/0 GGMI) HELD pending same-lens verification.
