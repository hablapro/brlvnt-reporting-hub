# GGMI (LATAM) — Quantcast (Programmatic) — May 2026 Data Capture

STATUS: ✅ PULLED 2026-06-02, CORRECTED 2026-06-03 via quantcast MCP. Account 9969644 (Forex), timezone America/New_York, USD.
Date range 2026-05-01 to 2026-06-01 (endDate is EXCLUSIVE in this MCP — see note). Breakdown: Campaign Name. Normalized per `mappings/quantcast-field-mapping.md`.

## ⚠️ endDate correction
The initial pull used endDate 2026-05-31 and DROPPED May 31 (Quantcast MCP treats endDate as exclusive), understating spend by ~$1,188. Reconciled against the Quantcast dashboard ($25,013.56) by re-pulling with endDate 2026-06-01. Always set endDate to the first day of the next month for a full inclusive month.

## ⚠️ spend reconciliation (2026-06-08, client-confirmed)
Final reconciled campaign spend = **$26,890.00** (client/platform final for the single delivering campaign). The MCP "Budget Delivered" pull showed $25,013.56; the reconciled total is ~$1,876 higher. **Impressions (16,481,325) and clicks (4,807) are unchanged.** Derived metrics recomputed on the reconciled spend: CPM $1.52→$1.63, CPC $5.20→$5.59, CPA $25,013.56→$26,890.00. Conversions = 1.

## Delivering campaign (only GGMI campaign with delivery in May)
- `Forex_GGMI_spanish_conversion_campaign_mx` (ID 9083134, ENABLED, goal CPA)
- `Forex_GGMI_spanish_conversion_Q+campaign_mx` (ID 9086988) launched 2026-05-19 — NO delivery in May.
- `0326_Forex_GGMI_spanish_clicks_campaign_mx` (ID 9084224) PAUSED · `OLD NOT USE ..._MX` (ID 9080387) PAUSED — no delivery.

## Normalized KPIs (May 2026, corrected)
| Metric | Value | Source field |
|---|---|---|
| Spend | $26,890.00 | Reconciled campaign total (Budget Delivered MCP = $25,013.56) |
| Impressions | 16,481,325 | Impressions |
| Clicks | 4,807 | Clicks (Advanced IVT) |
| CTR | 0.029% | CTR |
| CPM (derived) | $1.63 | Spend / Impr × 1000 |
| CPC (derived) | $5.59 | Spend / Clicks |
| Device Reach | 6,316,851 | Device Reach |
| Device Frequency | 2.61 | Device Frequency |
| Conversions (Results) | 1 | Results |
| — Click-through | 1 | Click Results |
| — View-through | 0 | View Results |
| CPA (Cost Per Result) | $26,890.00 | Spend / Results (1) |
| Viewability | 67.1% | Viewability (below 70% IAB) |
| Viewable Impressions | 10,385,715 | Viewable Impressions |
| Measured Impressions | 15,466,603 | Measured Impressions |
| Revenue / ROAS | N/A | not configured |

## MoM vs April 2026 (validated $15,004.71 / 0 results)
- Spend +79% · Impressions +135% · Clicks +43% · CPM -24% · CPC +26% · Conversions 0→1 · Viewability 66.2%→67.1% (+0.9pp).

## Data notes / flags
- First recorded Quantcast conversion for GGMI (1, click-through) after the April pixel fix — directional only.
- Viewability 67.1% still below IAB 70% standard.
- Q+ conversion campaign (launched May 19) had no recorded delivery in May — verify June activation.
