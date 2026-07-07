# GGMI Meta (LATAM) — June 2026 Findings & Recommendations

**Account:** Meta act_1699453997689551 — GGMI (LATAM) campaigns only
**Period:** June 1–30, 2026 (MoM vs May) · USD · attribution 7d-click / 1d-view
**Prepared:** 2026-07-07, Berelvant
**Status:** Handoff artifact. This repository is reporting only and does not execute account changes. Section 5 is the action table for the execution agent (Meta paid), and still requires explicit human approval before any change. Nothing has been changed in the account.

---

## 1. Bottom line

Meta scaled about 4x in June ($6,626 to $25,924) and delivery is cheap and strong: CPM $1.31, link CPC near $0.06, landing-page views up 289% to 249,972. The team also started fixing the funnel, launching a conversion-objective campaign on a new landing page alongside the Q2 traffic campaign.

Two things block the account from turning that cheap traffic into applications:

1. **The traffic objective buys the wrong people.** 63% of June spend reached age 55+, and 32% reached 65+. These clicks are cheap, which is exactly why a traffic objective favors them, but they rarely open a funded trading account. This is the main reason 250,000 landing-page views produced almost no applications.
2. **Placement and creative spread is lopsided.** Facebook took 99.7% of spend and Instagram got $70. Two creatives carried 96% of the prospecting budget. Cheap junk inventory (reels overlay, Audience Network) absorbed real money at low intent.

None of this needs more budget. It needs the objective, audiences, placements, and creative set tightened, and it needs the conversions validated before anyone trusts the June numbers.

---

## 2. What the June cuts show

**Creative (ad level).** Two ads are the entire prospecting engine: `edu_trust_q2` ($15,932, 66% of the traffic campaign) and `demo_trust_q2` ($7,210). `demo_trust` converts better per dollar, carrying 11 of the campaign's 19 pixel conversions on roughly half `edu_trust`'s spend. In the new conversion campaign, one retargeting reel, `TradingView_exe_q2_reel`, drove 60 of 67 pixel conversions on $967. `TradingView_direct_q2_reel` spent on 606 clicks and returned zero.

**Placements.** Facebook Feed is the efficient core: 65% of spend, CPM $1.23, 64% of clicks reaching a landing-page view. Facebook Stories has the best CTR at 6.40%, worth its higher CPM. Reels overlay burned 2.6M impressions at a 0.76% CTR. Audience Network and rewarded video (about $673 combined) ran a 35% landing-page-view rate and low intent. Instagram is untested at $70 of $24K.

**Demographics.** 82% of spend reached age 45+, 63% reached 55+, and 32% reached 65+. For a forex and CFD account product, that skew is inverted from the audience most likely to fund an account.

---

## 3. Do not trust the conversion count yet

Meta reports GGMI conversions rising from 4 in May to 86 in June. Treat this as unvalidated:

- **Start vs submit.** May's "4" aligned to application starts, with zero submitted. June's 86 is likely starts too, not 86 submitted applications.
- **New-LP anomaly.** The conversion campaign shows 67 conversions on 126 landing-page views, and its top reel shows 60 on 91. That rate is implausible for real submissions, so the pixel or the landing-page setup needs a check.

Validate June Meta conversions against SA360 (if Meta is imported), GA4 Forex LAT property 508849216, and the CRM submitted-application count before reporting any submitted-app figure or CPA to the client. This is the same lens that corrected Bing.

---

## 4. Do not cut, keep

`demo_trust_q2` and the `TradingView_exe` retargeting reel are the closest thing to a working conversion path Meta has produced. Hold them, and scale the reel once its conversions validate. Facebook Feed and Facebook Stories are the placements to protect.

---

## 5. Recommendations (approval required before any change)

These are account mutations for the Meta execution agent. Approve the batch before anything runs. Each row lists a rollback.

| # | Priority | Entity | Current | Proposed change | Reason | $ at stake | Rollback |
|---|---|---|---|---|---|---|---|
| 1 | HIGH | Conversion tracking (validation) | 86 pixel events, definition unconfirmed | Validate start-vs-submit and the new-LP pixel vs SA360 / GA4 508849216 / CRM before reporting | Blocks trustworthy reporting and conversion bidding | gates all optimization | n/a (measurement) |
| 2 | HIGH | Age targeting, Q2 CTR campaign | 63% of spend to 55+, 32% to 65+ | Set an age ceiling or bid down 55+; concentrate 25–54 | Older clicks are cheap but do not fund accounts | ~$15,076/mo reallocated | Restore open age range |
| 3 | HIGH | Campaign objective | Primary spend on OUTCOME_TRAFFIC | Complete the shift to conversion objective on the validated landing page | Traffic objective buys LP views, not applications | reframes ~$24K/mo | Revert to traffic campaign |
| 4 | MED | Placements — Audience Network + rewarded video | Included, ~$673/mo, 35% LPV rate | Exclude both | Low intent, low LP-view rate | ~$673/mo | Re-include |
| 5 | MED | Placement — Facebook reels_overlay | 2.6M impr at 0.76% CTR, $1,653/mo | Cap or exclude | Cheap, low-engagement inventory | ~$1,653/mo | Re-enable |
| 6 | MED | Instagram placements | ~$70 of $24K | Test IG Feed, Reels, Stories with a controlled budget | Untested channel for a Mexican consumer audience | opportunity | Pause IG |
| 7 | MED | Creative — `TradingView_exe_q2_reel` | $967, 60 conv (unvalidated) | Scale after conversions validate | Best June conversion signal | scale opportunity | Hold budget |
| 8 | MED | Creative — `TradingView_direct_q2_reel` | 606 clicks, 0 conv | Pause | No conversion return | ~$43/mo | Re-enable |

---

## 6. Sequence

1. **First — validate conversions** (row 1). Everything else depends on knowing what the 86 represents.
2. **Then — fix who and what** (rows 2, 4, 5): age targeting and placement exclusions stop the low-intent spend right away.
3. **Then — fix the objective** (row 3): move budget to the conversion objective on the validated landing page.
4. **Ongoing — creative** (rows 6, 7, 8): test Instagram, scale the winning reel once validated, cut the zero-conversion reel.

---

## 7. Sources

- meta-ads MCP, account act_1699453997689551, GGMI campaigns only. Campaign, ad, placement (publisher_platform x platform_position), and age/gender cuts pulled 2026-07-06 for June, with April and May for trend.
- Data workbook: `reports/forex/ggmi/2026-06/data/GGMI-Meta-Apr-Jun-2026-data.xlsx` (Summary, Trend, Campaigns, Creative, Placements, Demographics, Funnel, Conversion QA, Notes).
- Conversion metric: `offsite_conversion.fb_pixel_custom` (unvalidated). ROAS N/A (no revenue tracking).
- Caveat: the conversion campaign and Followers campaign launched mid-to-late June, so their figures reflect a partial month.
