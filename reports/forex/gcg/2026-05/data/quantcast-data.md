# GCG (US) — Quantcast (Programmatic) — May 2026 Data Capture

STATUS: ✅ PULLED 2026-06-02, CORRECTED 2026-06-03 via quantcast MCP. Account 9969644 (Forex), timezone America/New_York, USD.
Date range 2026-05-01 to 2026-06-01 (endDate is EXCLUSIVE in this MCP — see note). Breakdown: Campaign Name. Normalized per `mappings/quantcast-field-mapping.md`.

## ⚠️ endDate correction
The initial pull used endDate 2026-05-31 and DROPPED May 31 (Quantcast MCP treats endDate as exclusive), understating spend by ~$800. Reconciled against the Quantcast dashboard ($22,009.23) by re-pulling with endDate 2026-06-01. Always set endDate to the first day of the next month for a full inclusive month.

## ⚠️ spend reconciliation (2026-06-08, client-confirmed)
Final reconciled campaign spend = **$22,359.00** (client/platform final for the single delivering campaign). The MCP "Budget Delivered" pull showed $22,009.23; the reconciled total is ~$350 higher. **Impressions (26,972,772), clicks (1,827), and conversions (8) are unchanged.** Derived metrics recomputed: CPM $0.82→$0.83, CPC $12.05→$12.24, CPA $2,725.56→$2,794.88.

## Delivering campaign (only GCG campaign with delivery in May)
- `Forex_GCG_spanish_conversion_campaign_us` (ID 9080386, ENABLED, goal CPA)
- `Forex_GCG_spanish_conversion_Q+campaign_us` (ID 9086987) launched 2026-05-19 — NO delivery in May.
- `0326_Forex_GCG_spanish_clicks_campaign_us` (ID 9084225) PAUSED — no delivery.

## Normalized KPIs (May 2026, corrected)
| Metric | Value | Source field |
|---|---|---|
| Spend | $22,359.00 | Reconciled campaign total (Budget Delivered MCP = $22,009.23) |
| Impressions | 26,972,772 | Impressions |
| Clicks | 1,827 | Clicks (Advanced IVT) |
| CTR | 0.007% | CTR |
| CPM (derived) | $0.83 | Spend / Impr × 1000 |
| CPC (derived) | $12.24 | Spend / Clicks |
| Device Reach | 10,184,251 | Device Reach |
| Device Frequency | 2.65 | Device Frequency |
| Conversions (Results) | 8 | Results |
| — Click-through | 1 | Click Results |
| — View-through | 7 | View Results |
| CPA (Cost Per Result) | $2,794.88 | Spend / Results (8) |
| Viewability | 60.5% | Viewability (below 70% IAB) |
| Viewable Impressions | 15,716,151 | Viewable Impressions |
| Measured Impressions | 25,995,429 | Measured Impressions |
| Revenue / ROAS | N/A | not configured |

## MoM vs April 2026 (validated $15,015.44 / 2 results)
- Spend +49% · Impressions +275% · Clicks +13% · CPM -60% · Conversions 2→8 · CPA -63%.

## Data notes / flags
- Conversions remain mostly view-through (7 of 8). VT-weighted attribution.
- CPM $0.82 and viewability 60.5% (below IAB 70%): impression scale came from cheaper, lower-viewability inventory. Inventory-quality flag.
- Q+ conversion campaign (launched May 19) had no recorded delivery in May — verify June activation.
