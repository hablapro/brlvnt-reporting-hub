# GGMI Bing (LATAM) — Quick Audit

**Account:** FOREX.com LATAM — Bing 31003116 / SA360 customer 5372690580 (login 9697709980)
**Date:** 2026-07-13 · USD · Mexico-only mandate
**Scope:** Quick audit (live config + July MTD), emphasis on geo compliance, conversion tracking, wasted spend.
**Status:** Reporting only. No account changes made. Extends the July 6 remediation doc (`recommendations/forex/ggmi/GGMI-Bing-SA360-remediation-June-2026.md`).

---

## Bottom line

The account is **live again** — 5 Berelvant-built campaigns Active, 155 legacy campaigns paused. Two of the three highest-priority fixes from the July 6 remediation are **still not applied**, and both cost efficiency and carry compliance risk every day the account runs:

1. **Bidding is still blind.** The GGMI offline conversion goals are Active and recording, but every one still carries `ExcludeFromBidding = true`. Campaigns run Enhanced CPC with no conversion signal to steer on. Remediation row 3 ("unlock the signal") was not applied.
2. **Mexico-only compliance is STILL IN BREACH — 51.6% of spend served outside Mexico.** SA360 user-location (last 30 days) shows **$11,892 of $23,051 (51.6%) delivered non-Mexico**, essentially unchanged from June's 49%. The breach is almost entirely the two campaigns *named* `MX_GEN` — see the geo section below. This is a live compliance violation, not just wasted spend.

**Correction to the July 6 read and my first-pass hypothesis:** the leak is NOT in the `AO` campaigns. `policytest_v2` (the biggest spender, $10,459) is **100% Mexico** and correctly targeted. The violators are `BrandGeneric` (6.9% MX) and `PlatformIntercept` (2.3% MX).

July spend is near-zero so far (**$883 over Jul 1–13**, vs ~$25.7K in June), so July is too thin to grade performance. This audit grades live configuration.

---

## Live state (2026-07-13)

- **Campaigns:** 160 total — **5 Active, 155 Paused.** Active set (all Enhanced CPC per Bing API; SA360 reports MANUAL_CPC — reconcile):

| Campaign | Daily budget | Jul 1–13 spend | Clicks | CTR | Conv (SA360) |
|---|---|---|---|---|---|
| FX_LATAM_spanish_AO_GEN_policytest_v2_brlvnt | $1,120.22 | $415.18 | 247 | 9.97% | 0 |
| FX_LATAM_spanish_MX_GEN_BrandGeneric_brlvnt | $670 | $241.49 | 220 | 10.76% | 0 |
| FX_LATAM_spanish_MX_GEN_PlatformIntercept_brlvnt | $330 | $177.08 | 141 | 2.36% | 0 |
| FX_LATAM_spanish_AO_GEN_TradingView_brlvnt | $148 | $43.47 | 15 | 4.16% | 0 |
| FX_LATAM_spanish_AO_Brand_brlvnt | $100 | $6.11 | 2 | 28.57% | 0 |
| **Total** | **$2,468/day** | **$883.33** | **625** | **5.76%** | **0** |

- Budgeted daily spend ($2,468) vs actual (~$68/day) → campaigns are throttled or only recently re-enabled. **68% of budgeted daily spend sits in one campaign (policytest_v2, $1,120/day).**
- **0 conversions in July is not a real zero** — GGMI conversions are offline-imported and read only through SA360; June recorded 50. At ~$500 CPA, $883 of July spend implies ~1–2 conversions expected, so thin volume also explains it.

---

## Post-relaunch settings check (campaigns relaunched Sat 2026-07-11)

The 30-day geo breach below is **pre-relaunch** and does not reflect Saturday's settings. Checking current config + delivery since relaunch (Jul 11–13):

**Root-cause setting — still wrong on all 5 campaigns.** Every active campaign has `positiveGeoTargetType = PRESENCE_OR_INTEREST` (serves people physically in Mexico OR merely "interested in" Mexico). For a Mexico-only mandate this must be **`PRESENCE`** (physically in Mexico). `negativeGeoTargetType = PRESENCE` is already correct. Location criteria are just `+Mexico (2484)` with scattered, inconsistent single-country negatives (policytest excludes Brazil/Colombia/Venezuela; BrandGeneric + PlatformIntercept exclude only Colombia; the two AO campaigns have no negatives). PlatformIntercept has **no Venezuela negative** and is bleeding to Venezuela.

**Delivery since relaunch (Jul 11–13, user-location): 23% non-Mexico — down from 51.6%, not zero.**

| Campaign | MX $ | non-MX $ | MX % | Status |
|---|---|---|---|---|
| policytest_v2 | $377.80 | $0.00 | 100% | clean |
| BrandGeneric | $232.47 | $0.00 | 100% | clean (fixed Sat) |
| PlatformIntercept | $0.00 | $173.56 | **0%** | **still all Venezuela** (5,656 impr VE vs 102 MX, 0 MX clicks) |
| TradingView | $29.28 | $14.19 | 67% | leaking (VE/AR/NI/CL/CO/PE) |
| AO_Brand | $0.00 | $3.35 | 0% | 1 US click |
| **Total** | **$639.55** | **$191.10** | **77%** | |

Non-MX this window: Venezuela $168.85, US $8.39, Nicaragua $6.73, Argentina $3.81, Peru $1.42, tail. **The Saturday fix worked for BrandGeneric and policytest; PlatformIntercept, TradingView, and AO_Brand still leak.** Fix: set `positiveGeoTargetType = PRESENCE` on all 5 (top priority PlatformIntercept). With presence-only on, country-by-country negatives are unnecessary.

**Confirmation — Jul 12–13 only (excludes all of Saturday, pure post-relaunch): 19% non-Mexico.** Same pattern, no pre-change ambiguity: policytest 100% MX, BrandGeneric 100% MX, **PlatformIntercept 0% MX** ($0 / 0 clicks / 83 impr to Mexico vs 57 clicks / 2,690 impr / $63 to Venezuela), TradingView 78% MX, AO_Brand 1 US click. Non-MX trend: **51.6% (30d, pre-relaunch) → 23% (Jul 11–13) → 19% (Jul 12–13).** The residual is not lag — PlatformIntercept is structurally serving Venezuela under the Presence-or-Interest setting.

## Geo compliance — user-location, last 30 days (SA360, PRE-RELAUNCH)

Source: `user_location_view` (physical location of the user, `targeting_location = false`), customer 5372690580, last 30 days. This is the "where the user actually was" view, not targeting settings.

**$11,892 of $23,051 (51.6%) served outside Mexico** — 69 countries. Top forbidden destinations: Spain $3,347 (14.5%), Venezuela $2,845 (12.3%), United States $1,418 (6.2%), Colombia $1,208 (5.2%), Argentina $648, Peru $347, Dominican Rep. $346, Chile $229, Ecuador $194. The tail includes non-Spanish markets (Canada, UK, Germany, Italy, India, Japan) — clear untargeted spillover.

**The breach is campaign-specific.** The two `MX_GEN`-named campaigns are the violators; the `AO` campaigns are compliant:

| Campaign | Total 30d | Mexico $ | **MX %** | non-MX $ | Conv | CPA |
|---|---|---|---|---|---|---|
| policytest_v2 (AO) | $10,459 | $10,459 | **100.0%** | $0 | 15 | $697 |
| BrandGeneric (MX_GEN) | $8,385 | $581 | **6.9%** | $7,805 | 9 | $932 |
| PlatformIntercept (MX_GEN) | $4,170 | $97 | **2.3%** | $4,072 | 14 | $298 |
| TradingView (AO) | $35 | $23 | 66.9% | $12 | 0 | n/a |
| AO_Brand | $3 | $0 | 0.0% | $3 | 0 | n/a |
| **Total** | **$23,051** | **$11,160** | **48.4%** | **$11,892** | **38** | — |

`BrandGeneric` + `PlatformIntercept` account for **$11,877 — 99.9% of all forbidden spend.** `policytest_v2` proves correct Mexico presence-only targeting is already configured on one campaign; copy those exact location settings to the other two. Do not chase the 69 countries with exclusions one at a time.

Note: PlatformIntercept shows the best CPA ($298), but 98% of its traffic is non-Mexico — that CPA is largely earned on forbidden delivery and will change once restricted to Mexico. Conversions ARE recording (38 in 30d), so the account is measuring; it just isn't geo-compliant or bid-steering.

## Findings by area

### Conversion Tracking (25% weight) — FAIL
- **BCT (bidding signal): FAIL.** GGMI offline goals `40059107 / 40059122 / 40059144 / 40059152 / 40059170 / 40059184 / 40059257` are Active but all `ExcludeFromBidding = true`. No automated strategy can use them. This is remediation row 3, still open.
- **BCT07 (offline import freshness): WARNING.** The primary submitted-app goals — "G2 Raw Live Confirmation" (40059184) and "MT5 Live Confirmation" (40059257) — show `TrackingStatus = NoRecentConversions`. Sitewide/step goals show `RecordingConversions`. Confirm the live-account-confirmation import is still uploading; the primary KPI is the one showing stale.
- **BCT01/03: partial.** Global UET tags active (5060495, 247020089, 247020090); account-specific FOREX.com EN/UK tags (146001063, 146001059) are **Inactive** — fine for offline-import goals, but the URL-based goals attached to them are dead.
- **Clutter:** ~40 legacy conversion goals (CIMA EN/ES step goals, US/UK demo goals) mostly Paused/TagInactive. Recommend archiving to de-risk accidental bidding inclusion.

### Wasted Spend (20% weight) — FAIL (geo breach confirmed)
- **BWS06 (geo — Mexico-only): FAIL — live breach.** SA360 user-location (last 30 days) confirms **51.6% non-Mexico ($11,892 of $23,051)**, across 69 countries. Detail in the geo section below. Immediate fix required.
- **BWS02 (negatives): PASS.** 11 shared negative lists, well-built: Countries (31), General (389), Educational (228), Competitor (594), Irrelevant (45), plus brand/non-brand separators. Note Countries list has only 2 associations — verify it is attached to the active campaigns.

### Account Structure (15% weight) — WARNING
- **155 paused legacy campaigns** vs 5 active. Naming is inconsistent across eras (`FX_LATAM_MA_MEX_EN_GEN_HI_*` legacy vs `FX_LATAM_spanish_*_brlvnt` current). Archive stale campaigns for clean segmentation.
- **Budget concentration:** policytest_v2 at $1,120/day is 45% of total daily budget in the account's lowest-QS, highest-geo-risk campaign.

### Keywords (15% weight) — WARNING
- **3 keywords QS < 4 with >100 impressions:** `plataforma trading` (QS3, BrandGeneric), `tradingview free` (QS3, policytest_v2), `mt5` (QS3, policytest_v2). Review ad relevance / landing page; per the remediation, TradingView theme converts well so fix relevance, don't cut.

### Ads (15% weight) — WARNING (carried from June)
- Not re-pulled in this quick pass. June finding: brand RSAs at 4 headlines / 2 descriptions, below the Bing standard (8+ / 3+). Verify on the live brlvnt campaigns.

### Settings (10% weight) — WARNING
- Enhanced CPC is enabled but has no conversion signal (see BCT). Device/schedule/audience-network settings not reviewed in this quick pass.

---

## Quick wins (priority order)

1. **Unlock the bidding signal** — set `ExcludeFromBidding = false` on the 7 GGMI offline goals (remediation row 3). Nothing steers until this is done.
2. **Stop the geo breach now (HIGHEST priority)** — `BrandGeneric` (6.9% MX) and `PlatformIntercept` (2.3% MX) are delivering ~$11,877/30d outside Mexico. Copy the Mexico presence-only location settings from `policytest_v2` (100% MX) onto both. Whitelist Mexico, don't exclude 69 countries one at a time. ~$11.9K/mo of forbidden spend at stake.
3. **Verify the primary-KPI import** — live-account-confirmation goals show `NoRecentConversions`; confirm the offline upload is current.
4. **Right-size policytest_v2 budget** — $1,120/day into the lowest-QS, highest-geo-risk campaign; cap until geo + QS are addressed.
5. **Archive legacy clutter** — 155 paused campaigns and ~40 dead conversion goals.

These extend the July 6 remediation table (rows 1, 3, 4, 6, 8 still relevant). Execution and any account mutation remain with the paid-media/PPC agent under explicit approval; this repository does not change the account.

---

## Sources
- bing-ads MCP, account 31003116: account info, campaigns (160), conversion goals, UET tags, shared negative lists, account diagnostics (2026-07-13).
- sa360 MCP, customer 5372690580 / login 9697709980: active-campaign performance and geo, Jul 1–13.
- Prior: `recommendations/forex/ggmi/GGMI-Bing-SA360-remediation-June-2026.md` (Jul 6), `reports/forex/ggmi/2026-06/data/GGMI-Bing-SA360-June-2026-data.xlsx`.
- **Caveat:** July MTD spend ($883) is too thin to grade performance; this is a configuration audit. Bing-native "0 conversions" reflects offline-import reporting, not true zero.
