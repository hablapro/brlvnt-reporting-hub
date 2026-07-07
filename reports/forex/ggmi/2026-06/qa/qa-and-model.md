# GGMI (Mexico) — June 2026 — QA Note + Modeled KPI Tables

Period: 2026-06-01 to 2026-06-30. Currency USD. Timezone America/New_York. Comparison: MoM vs May 2026 (Quantcast May on the reconciled $26,890 basis). ROAS excluded (no revenue tracking on any channel). Modeled workbook: `../model/GGMI-Jun-2026-cross-channel-model.xlsx`. GA4 workbook: `../data/GGMI-GA4-Jan-Jun-2026-data.xlsx`.

## QA / Data Quality

| Check | Result |
|---|---|
| Bing source | Spend/impr/clicks from bing-ads MCP direct (acct 31003116); conversions from SA360 (customerId 5372690580 / loginCustomerId 9697709980). Bing-native UI shows 0 conversions; SA360 is the conversion source of truth. |
| Bing conversions | PASS — 50 submitted applications (SA360 Primary) at $513 CPA, +52% vs May's 33. |
| Bing geo | FAIL — Mexico-only rule violated: 51% MX ($13,022) vs 49% non-MX ($12,637; Venezuela, Spain, US, LATAM ex-MX). Remediation doc on file. |
| Meta conversions | HOLD — 86 fb_pixel_custom conversions unvalidated (starts vs submit ambiguity + new-LP anomaly). GA4 check below strengthens the hold. |
| Meta geo | PASS — 100% Mexico. |
| Quantcast spend | June = MCP Budget Delivered $33,784.20, single delivering campaign (Q+ conversion). May basis reconciled to $26,890 (client-confirmed 2026-06-08), so June MoM = +25.6%, not the +35% shown against the raw MCP May figure. |
| Quantcast quality | Viewability 51.3%, below the IAB 70% floor and down from 67.2% in May. Disallow list of 49 sites ($10,734, 32% of spend) delivered per standing process. 11 conversions are view-through only. |
| Azerion | Spend $34,555.83 reconciles to ad-set sum. 42 submitted applications at $823 CPA. Geo unverified; upper funnel held pending vendor reply (email drafted, not sent). Viewability 68.5%. |
| GA4 pull | PASS — property 508849216, Mexico-only, Jan-Jun by month. All three pulls complete (trend 840/840, channel 2,940/2,940, source/medium 4,995/4,995 rows). API-side country filter failed to serialize through the MCP; pulled with country as a dimension and filtered locally, which yields identical metric values. |
| Cross-channel conversion definitions comparable? | NO — four different events; never sum conversions or blend CPA. |

## GA4 reconciliation (new this month)

Platform clicks vs GA4 Mexico sessions, June:

| Channel | Platform clicks (MX where known) | GA4 MX sessions | Verdict |
|---|---|---|---|
| Bing | 8,693 MX (21,480 total) | 663 tagged + up to 2,451 sitting in "(unlinked SA360 account)" | TRACKING GAP — SA360 account is not linked to GA4 property 508849216, so paid-search sessions land as Unassigned (31% of June MX sessions). Fix in GA4 Admin. |
| Meta | 407,136 link clicks, 249,972 claimed LPVs | 786 | ANOMALY, PLATFORM-SIDE — Meta's LPs are tagged and receiving GA4 sessions (landing-page check, `ga4-deep-dive.md`), so this is not a missing tag. Meta's claimed 250K LPVs are 5x the entire property's June traffic (all countries); the inflation sits in cheap in-app inventory where GA4 never fires. Capture fell 0.54% (May) → 0.19% (June) as spend quadrupled. 86 conversions stay held. |
| Quantcast | 11,284 | 270 | Expected range for display (IVT, in-app inventory). |
| Azerion | 9,910 | 61 azerion/display + 294 tradingview/display | Expected range. tradingview/display attributed to Azerion pending vendor site breakdown. |

### GA4 site trend (client expects an upward trend; the data does not show one)
Sessions: Jan 9,380 → Feb 22,229 → Mar 12,614 → Apr 7,577 → May 5,751 → Jun 9,236. June is a real recovery (+61% MoM) and unique visitors grew Jan→Jun (+26%, 4,651 → 5,838), but H1 sessions are flat Jan-to-Jun with a Feb spike and a May trough. Frame June as a rebound, not H1 as growth.

## Modeled cross-channel summary (June 2026)

| Channel | Spend | Impressions | Clicks | CTR | CPM | CPC | Primary conversions | CPA |
|---|---|---|---|---|---|---|---|---|
| Bing | 25,658.61 | 466,582 | 21,480 | 4.60% | — | 1.19 | 50 submitted apps (SA360 Primary) | 513.17 |
| Meta | 25,923.71 | 19,780,693 | 407,136 | 2.06% | 1.31 | — | 86 pixel conv (UNVALIDATED, hold) | 301.44* |
| Quantcast | 33,784.20 | 41,964,872 | 11,284 | 0.0269% | 0.81 | 2.99 | 11 view-through (soft) | 3,071.29 |
| Azerion | 34,555.83 | 7,679,074 | 9,910 | 0.129% | 4.50 | — | 42 submitted apps (vendor-defined) | 822.76 |
| **Total** | **119,922.35** | **69,891,221** | **449,810** | — | — | — | see definitions note | — |

\* Apparent CPA on unvalidated events; do not publish.

## MoM totals
Total spend May $76,745.78 (reconciled basis) → June $119,922.35 = **+56%**. Drivers: Meta +291% ($6,626 → $25,924), Bing +61%, Azerion +27%, Quantcast +26% (reconciled basis). Azerion in this table is raw vendor spend; internal billing adds the 7.5% tech fee, client deliverables and this model do not.

## Key findings (validated)

1. **Bing remains the efficiency leader and scaled cleanly on conversions:** 50 submitted applications at $513 CPA (+52% conversions on +61% spend). The geo violation is the asterisk: 49% of June spend served outside Mexico, so MX-only efficiency is better than the blended CPA suggests and remediation is fix #1.
2. **Azerion held its CPA through a budget increase:** 42 applications at $823 (+13% CPA on +27% spend), 440 Step-1 starts. Certification blocked on vendor geo data.
3. **Meta's 86 conversions stay out of the client narrative.** The landing-page check killed the missing-tag theory: Meta sessions register on tagged forex.com LPs. What remains is platform-side inflation (250K claimed LPVs vs ~54K sessions on the whole property, all countries) from cheap in-app inventory, worsening as spend quadrupled (capture 0.54% → 0.19%). Sharpest flag: 67 of the 86 conversions come from one retargeting campaign with 126 LPVs, a 53% conversion rate no application funnel produces. Full analysis in `ga4-deep-dive.md`.
4. **Quantcast bought cheap reach at a steep quality cost:** CPM $0.81 (-47%) and 42M impressions, but viewability fell to 51.3% and all 11 conversions are view-through. The 49-site disallow list addresses the worst third of spend; a campaign-level viewability floor is the structural fix.
5. **The site itself is not growing in H1.** June rebounded off the May low, and unique visitors are up 26% Jan→Jun, but sessions are flat Jan-to-Jun. Two tracking fixes would materially improve attribution before July reporting: link SA360 to GA4 (recovers the 31% Unassigned bucket) and resolve the Meta LP tagging question.

## Attribution note (carry into Data Notes tab)
Bing = submitted applications via SA360 Primary. Meta = pixel custom events, unvalidated and held. Azerion = vendor-defined submitted applications. Quantcast = view-through Results. Spend and impressions are summable; conversions and CPA are per channel only.
