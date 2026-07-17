# GCG June 2026 — QA & Cross-Channel Model

Pulled 2026-07-17. Currency USD, TZ America/New_York. Comparison MoM vs May 2026. Client-facing spend basis = **client budget tracker** (standing ruling; adjustments silent in client materials).

## QA — platform vs client tracker

| Channel | Platform pull | Client tracker | Delta | Status |
|---|---|---|---|---|
| Google Ads | $22,523.79 | $22,524 | $0 | ✅ exact |
| Quantcast | $30,158.51 | $30,559 | +$400 (+1.3%) | ✅ normal adjustment |
| Meta | $34,710.97 | $30,711 | **-$4,000 (-11.5%)** | 🔴 FLAGGED — possible tracker digit swap (34,711 → 30,711); Renzo to confirm |
| Azerion | $27,092.40 (vendor raw) | $29,586 | raw + 7.5% fee + $461.67 adj | ✅ vendor files received 2026-07-17 |
| Native | no source | $3,645 | — | ⏳ pilot detail requested |
| **Total** | — | **$117,024** | — | +53.4% vs May $76,274 |

## June model (client-tracker spend; derived metrics on that basis)

| Channel | Spend | Impr | Clicks | CTR | CPM | Conversions | CPA | Viewability |
|---|---|---|---|---|---|---|---|---|
| Google Ads | 22,524 | 181,470 | 12,888 | 7.102% | — | 67 submitted apps | 336.18 | — |
| Meta | 30,711 | 3,058,402 | 74,572 (link) | 2.438% | 10.04 | 136 pixel events* | 225.82* | — |
| Quantcast | 30,559 | 37,233,620 | 2,942 | 0.008% | 0.82 | 15 (13 VT) | — | 46.9% |
| Azerion | 29,586 | pending | pending | — | — | pending | — | — |
| Native | 3,645 | pending | pending | — | — | pending | — | — |
| **Total** | **117,024** | — | — | — | — | never summed | — | — |

\* Meta = fb_pixel_custom rollup, mostly application starts (May flag stands; campaign still on CTR objective — the June conversion-objective shift did not happen).

## MoM (tracker basis)

| Channel | May | June | MoM |
|---|---|---|---|
| Google Ads | 15,201 | 22,524 | +48.2% |
| Meta | 12,243 | 30,711 | +150.8% |
| Quantcast | 22,359 | 30,559 | +36.7% |
| Azerion | 26,472 | 29,586 | +11.8% |
| Native | — | 3,645 | new pilot |
| **Total** | **76,274** | **117,024** | **+53.4%** |

## Validated findings

1. **Google conversions fell as spend scaled: 76 → 67 (-12%) on +48% spend; CPA $200 → $336 (+68%).** All 67 = "PO App Form - Step 5 - Submission Completed" (definition unchanged). TrackB remains most efficient (Platform $264, Authority $297); TrackA Trust worst ($433); Brand $379.
2. **Search growth is rank-limited, not budget-limited.** Impression share: Brand 11%, TrackA 27%, TrackB 13-24%; lost-to-rank 64-76% vs lost-to-budget 9-13%. June's extra budget bought worse auctions. Lever = ad rank (bids/QS/RSA), not more spend.
3. **Meta scaled +151% (tracker) still on the CTR objective.** Delivery healthy: LPV/click 70.6% (May 65.9%), GA4 capture ~57% of link clicks (42,747 meta/paid-social sessions) — the GGMI-style capture anomaly does NOT exist on GCG. 136 pixel events (starts rollup). CPM platform $11.35.
4. **Quantcast repeated the GGMI reach play with the same quality bill:** 37.2M impressions (+38%), 23.2M devices, CPM $0.82, but viewability 46.9% (below the 70% standard; May-era ~60s). Disallow list: 18 domains / $9,752 / 32% of June spend + recommend viewability floor. Conversions 15 (13 view-through) vs 8 in May.
5. **Client blended funnel (their dashboard):** June submitted 322 (+7% MoM; 300 May), live 306, approved 145 (45% stable), funded 41 (28%), traded 30. Q2 apps 1,033 vs Q1 1,203 (-14%) while media scaled: the start→submit step diluted (App Starts Rate 55% Jan → 4% Jun as traffic scaled).
6. **ES-audience traffic (GA4 language=es, US property):** stable ~70K sessions Jan-May, June 80,231 (+15%), users +40% MoM to 41,795. No organic-collapse story on GCG (contrast GGMI). The client-dashboard "Unique Sessions" (67,542 June) is a different scope; not reconcilable to GA4 cuts we ran — noted, not blocking.

## Open items (updated 2026-07-17)
- ✅ Azerion vendor files received: 58 apps (+35%) @ $510 tracker-basis CPA; starts 1,398→447 with completion 3.1%→13.0%; viewability 58.8%; US-only geo confirmed. See data workbook Azerion tab.
- ✅ Meta figure: Renzo ruled tracker $30,711 stands (platform $34,710.97 internal only).
- ⏳ Native pilot detail (vendor, delivery, objective) for the $3,645 line.
- Optional: GCG Budget-vs-Actual dashboard (GGMI parity) for a vs-plan QBR slide.

## GA4 Meta attribution check (2026-07-17, INTERNAL)
GA4 US property, June, `meta / paid-social` (our GCG campaign): **89 live application starts, 4 live confirmations (last-click), 5 demo confirmations**. Ruling applied: the 89 site-measured starts go in client materials as independent corroboration; the 4 last-click submitted apps stay internal ($7,678 implied CPA would misrepresent an upper-funnel channel on a traffic objective — last-click credits its closes to google/cpc and direct). Meta timing (May deck said conversion campaigns launch June; still on traffic objective) is with Renzo's performance manager internally; client materials frame the July shift forward-looking with no explanation of the slip.
