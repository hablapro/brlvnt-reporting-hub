# GGMI (LATAM) — Bing Ads — May 2026 Data Capture

- Source: **bing-ads MCP (direct)**, account 31003116 "FOREX.com LATAM" (B001LWA8), USD.
- NOTE: SA360 path is BLOCKED this month — account 3332505241 returns USER_PERMISSION_DENIED and no longer appears under SA360 manager 6708988927. Pulled directly from Bing Ads instead (source of truth). This is a degradation of the April "Bing SA360 auth" blocker.
- Period: 2026-05-01 to 2026-05-31.

## Channel totals (May vs April)
| Metric | May 2026 | April 2026 | MoM |
|---|---|---|---|
| Spend | $15,972 | $15,289 | +4.5% |
| Impressions | 368,704 | — (Mar 249,963) | — |
| Clicks | 29,944 | 33,393 | -10.3% |
| CTR | 8.12% | 11.66% | -3.54pp |
| Avg CPC | $0.53 | $0.46 | +15% |
| Conversions | 0 reported | N/A (blocked) | — |
| Campaign status | Budget paused | — | budget-limited |

- Single campaign: `FX_LATAM_spanish_AO_GEN_policytest_v2_brlvnt` (Manual CPC). "Budget paused" = hit budget cap (budget-limited).

## Ad group / keyword breakdown (May) — diversified vs April
| Ad group | Spend | ~Share | Top keyword (QS) |
|---|---|---|---|
| Brand_Discovery_EXA | $6,884 | 43% | "trading online" 12.29% CTR $0.60 (QS8); "plataforma forex" (QS10) |
| Brand_Platform_MT_EXA | $4,635 | 29% | "plataforma metatrader" 181,640 impr, 8.12% CTR, $0.31 CPC (QS10) |
| TV_Catch_Phrase | $2,526 | 16% | "tradingview" 2.56% CTR, $2.34 CPC (QS8) |
| TV_Core_Exact | $1,353 | 8% | "tradingview signals" $4.99 CPC (QS7) |
| Brand_Mexico_LATAM_EXA | $359 | 2% | "forex mexico"; "forex.com" 41.67% CTR (QS10) |
| Brand_Trading_EXA | $211 | 1% | "forex" exact 12.44% CTR |
- Keyword spend reconciles to ~$15,969 vs $15,972 campaign total (rounding; PASS).

## Conversion tracking status (improving but not yet reporting)
- Campaign-level Conversions = 0. BUT the account now has **Active, "RecordingConversions"** GGMI offline-conversion goals (created ~late-period): "GGMI - FOREX.com LATAM ES" Sitewide, G2 Raw Spread App Form Step 1/2, MT5 App Form Step 1, Demo Confirmation, Live Confirmation. Conversion infrastructure is being built; campaign metrics not yet populated (offline goals are ExcludeFromBidding, attribution lag, or zero qualifying conversions in May).
- ROAS unavailable (revenue not tracked).

## Read
- Efficient brand/brand-adjacent demand capture: "plataforma metatrader" (QS10, $0.31 CPC) and "trading online" (12.29% CTR) drive volume cheaply.
- **New in May: a TradingView keyword theme** (TV_* ad groups, ~24% of spend) at much higher CPCs ($2.34–$4.99) and lower CTR — an unproven, costlier expansion with no measured conversions yet.
- CTR fell (11.66%→8.12%) and CPC rose ($0.46→$0.53), partly from the higher-cost TradingView terms diluting the cheap brand mix.
- Conversion measurement remains the core gap; offline goals going Active is the path to finally attributing Bing performance.
