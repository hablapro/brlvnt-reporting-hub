# GCG (US) — May 2026 — QA Note + Modeled KPI Tables

Period: 2026-05-01 to 2026-05-31. Currency USD. Timezone America/New_York. Comparison: MoM vs April 2026. ROAS excluded (no revenue tracking on any channel).

## QA / Data Quality

| Check | Result |
|---|---|
| Google Ads spend reconciles to campaign sum | PASS ($4,560.21+$3,040.24+$5,320.19+$2,280.13 = $15,200.77) |
| Google Ads conversions single-action, evenly distributed | PASS (76 = App Step 5; tracking fixed, April week-5 anomaly resolved) |
| Meta conversions = aggregated fb_pixel_custom app events | NOTE (StartApplication + SubmittedApplication mixed by API; not directly equal to GAds completed-app definition) |
| Azerion spend reconciles to ad-set sum | PASS (~$4.1k × 6 ad sets ≈ $24,625) |
| Quantcast spend = reconciled campaign total, single delivering campaign | PASS ($22,359.00, Forex_GCG_spanish_conversion_campaign_us; client-confirmed 2026-06-08. MCP Budget Delivered showed $22,009.23; reconciled up ~$350, impressions/clicks/conversions unchanged, CPM/CPC/CPA recomputed) |
| Cross-channel conversion definitions comparable? | NO — see attribution note. Do not sum into one CPA/ROAS. |

### Attribution note (carry into Data Notes tab)
Each channel measures a different conversion event: Google Ads = completed application (Step 5, last-click); Meta = pixel app events (7d-click/1d-view); Azerion = Step 1 + completed application (DSP); Quantcast = Results, predominantly view-through (7 of 8). These are NOT the same action and must not be summed into a single funnel total. Spend and impressions are summable; conversions/CPA are reported per channel.

## Modeled cross-channel summary (May 2026)

| Channel | Spend | Impressions | Clicks | CTR | CPM | Primary conversions | CPA | MoM CPA |
|---|---|---|---|---|---|---|---|---|
| Google Ads | 15,200.77 | 126,851 | 9,953 | 7.85% | — | 76 completed apps | 200.01 | -84% |
| Meta | 12,242.61 | 2,316,020 | 40,790 | 1.76% | 5.29 | 109 app events | 112.32 | -33% |
| Azerion | 24,625.27 | 4,104,212 | 42,274 | 1.03% | 6.00 | 43 apps / 1,398 Step 1 | 572.68 / 17.61 | +187% / -43% |
| Quantcast | 22,359.00 | 26,972,772 | 1,827 | 0.0068% | 0.83 | 8 results (7 VT) | 2,794.88 | -63% |
| **Total** | **74,427.65** | **33,519,855** | **94,844** | — | — | see note | — | — |

## MoM totals
- Total spend April = $57,488 (GAds 15,120 + Meta 12,167 + Azerion 15,186 + Quantcast 15,015) → May $74,428 = **+29.5%**, driven by Azerion (+62%) and Quantcast (+49%). [Quantcast May corrected 2026-06-03: $21,207 → $22,009 after endDate fix. Corrected 2026-06-08: Quantcast May $22,009 → $22,359 (reconciled campaign total; impressions/clicks/conversions held, CPM/CPC/CPA recomputed).] Note: this modeled table uses raw Azerion ($24,625.27); client deliverables use fee-inclusive Azerion ($26,472.17), so the client-facing May total is $76,274.55.

## Key findings (validated)
1. **Measurement turned a corner.** Google Ads conversion tracking is fixed (76 completed apps, evenly distributed, single action). May is the first clean measured month for the channel; CPA $200 now sits between Meta ($112) and Azerion ($573 app).
2. **Meta is the efficiency leader** — best month, 109 conversions at $112 CPA, CPM -45%, on healthy 65.9% LPV/click. Scale `0426_GCG`.
3. **Azerion scaled hard but app conversion worsened** — Step 1 +184% at an efficient $17.61, yet completed apps fell 76→43 and app CPA rose to $573. Step 1 → application drop-off is the optimization target.
4. **Quantcast scaled impressions +275% on a CPM crash to $0.82**, but viewability fell to 60.5% (below IAB 70%) and conversions remain view-through and minimal. Inventory-quality flag.
5. **Google Ads non-brand is now rank-limited (67-81% lost IS to rank), not budget-limited;** Brand is budget-throttled (60% lost to budget) at a respectable $285 CPA — candidate for budget increase.
