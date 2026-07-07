# GGMI Bing (LATAM) — SA360 + Bing Audit Findings & Remediation

**Account:** FOREX.com LATAM — Bing engine 31003116 / SA360 customer 5372690580 (login 9697709980)
**Period:** June 1–30, 2026 (MoM vs May) · USD
**Prepared:** 2026-07-06, Berelvant
**Status:** Handoff artifact. This repository is reporting only and does not execute account changes. Section 6 is the action table for the execution agent (paid-media / PPC), and still requires explicit human approval before any change is made. Nothing has been changed in the account.

---

## 1. Bottom line

The account works better than the native Bing reports suggest, and worse than it should. Bing converts: June produced **50 submitted applications at a $513 blended CPA**, up from 33 at $484 in May. The Bing interface shows zero because these conversions are offline-imported and only surface in SA360.

Two problems now cost real money every day the account runs:

1. **The bidding is blind.** All three campaigns run Manual CPC with no conversion signal, so nothing adjusts bids toward the applications the account is winning.
2. **Half of spend broke the Mexico-only rule.** GGMI is a **Mexico-only account — any other country is strictly forbidden.** In June only 51% of Bing spend ($13,022) reached Mexico; **$12,637 (49%) served to non-Mexico** (Venezuela $3,456, Spain $3,349, US $1,431, Colombia $1,267, Argentina $676, Peru $359, Chile $233, + tail). This is a compliance violation, not just wasted spend. Fix: target Mexico only, exclude everything else. (Meta and Quantcast were verified 100% Mexico; Bing is the only channel in breach.)

Both are fixable this week. Neither requires new budget.

---

## 2. Why Bing looks broken but isn't

Bing-direct and SA360 agree on every delivery metric and disagree on the one that matters:

| Metric | Bing-direct API | SA360 | Verdict |
|---|---|---|---|
| Spend | $25,658.61 | $25,658.61 | match |
| Impressions | 466,582 | 466,582 | match |
| Clicks | 21,480 | 21,480 | match |
| **Conversions** | **0** | **50** | SA360 is the truth |

The GGMI conversion goals are offline-import goals (uploaded from the CRM, not fired by a pixel). Bing's native reporting does not show them against the campaigns, so any audit built only on the Bing API reads "0 conversions" and misjudges the account. Every conclusion below uses SA360.

June performance, by campaign:

| Campaign | Spend | Conversions | CPA |
|---|---|---|---|
| AO_GEN_policytest_v2 | $13,508 | 27 | $500 |
| MX_BrandGeneric | $8,154 | 9 | $906 |
| MX_PlatformIntercept | $3,996 | 14 | $285 |
| **Total** | **$25,659** | **50** | **$513** |

---

## 3. The core problem: measurement without steering

The account measures conversions but never feeds them back into bidding. Three settings confirm it:

- **Bid strategy:** all three campaigns are `MANUAL_CPC` with `enhancedCpcEnabled = false`. No automated layer of any kind.
- **Conversion goals:** the GGMI offline goals are Active and recording, but every one carries `ExcludeFromBidding = true`. That flag tells every Bing automated strategy to ignore them.
- **SA360 side:** the only portfolio bid strategy in the account is a leftover `test-SEARCH-…` Target CPA with zero spend, attached to nothing.

So bids sit at whatever a person set or imported from Google, and nothing moves them when an application comes in. The 50 conversions are a scoreboard, not a steering wheel. This is why the blended CPC doubled to $1.19 in June without anything pulling it back.

**To close the loop:** unlock the signal (turn off `ExcludeFromBidding`), then switch to a conversion-based strategy. An SA360 portfolio Target CPA is the cleaner route than a native Bing strategy, because SA360 already holds the conversions and sidesteps the offline-import lag. Pool all three campaigns into one strategy: 50 conversions a month supports Smart Bidding at the account level, but only AO clears the volume threshold on its own.

---

## 4. Mexico-only violation: half of Bing spend ran outside Mexico

GGMI is a **Mexico-only account. Delivery to any other country is strictly forbidden** (client compliance rule). Renzo set the Mexico campaign to presence-only on June 3 and excluded Venezuela and Brazil, which helped — Mexico rose from 18% of clicks in May to 40% in June and is now the top market. But the country-by-country exclusion approach is the wrong model: only **51% of June spend ($13,022) reached Mexico; 49% ($12,637) served non-Mexico.**

| Country | June spend | Share | Status |
|---|---|---|---|
| 🇲🇽 Mexico (only allowed geo) | $13,022 | 50.7% | compliant |
| 🇻🇪 Venezuela | $3,456 | 13.5% | forbidden — excluded Jun 3 but still serving |
| 🇪🇸 Spain | $3,349 | 13.1% | forbidden |
| 🇺🇸 United States | $1,431 | 5.6% | forbidden |
| 🇨🇴 Colombia | $1,267 | 4.9% | forbidden |
| 🇦🇷 Argentina · 🇵🇪 Peru · 🇨🇱 Chile · tail | $2,134 | 8.3% | forbidden |

Non-Mexico total: **$12,637, or 49% of June Bing spend** — a compliance violation, not just wasted spend. The fix is to **whitelist Mexico and exclude everything else**, presence-only, rather than blocking countries one at a time. Meta and Quantcast were verified 100% Mexico; Bing is the only channel in breach. Azerion geo is unverified (requested).

---

## 5. What not to do

A Bing-direct audit flags the TradingView keyword theme as pure waste: high CPC, low CTR, zero conversions. SA360 shows the opposite. The TradingView ad groups (TV_Catch, TV_Core) drove about 19 of the AO campaign's 27 conversions at a $241–285 CPA, better than the $513 account average. **Keep TradingView.** The fix there is to localize its English ads, not to cut it.

---

## 6. Remediation plan (approval required before any change)

The account is currently Paused, so confirm the intended on/off state first. These are account mutations. Approve the batch before Berelvant executes any of them; each row can be rolled back.

| # | Priority | Entity | Current | Proposed change | Reason | $ at stake | Rollback |
|---|---|---|---|---|---|---|---|
| 1 | HIGH | Location targeting — MEXICO ONLY | Only 51% of spend reached Mexico; 49% served to non-MX (Venezuela $3,456, Spain $3,349, US $1,431, Colombia $1,267, Argentina $676, Peru $359, Chile $233, + tail) | Set targeting to **Mexico only, presence-only**, and exclude every other country. GGMI is a Mexico-only account (compliance rule) — do not allow any non-MX delivery. Excluding countries one-by-one is the wrong approach; whitelist Mexico. | **Compliance violation** + wasted spend | **$12,637/mo** | Restore prior geo (not advised) |
| 3 | HIGH | Conversion goals (GGMI offline: 40059107 / 40059122 / 40059144 / 40059152 / 40059170 / 40059257) | `ExcludeFromBidding = true` | Set to `false` | Bidding has no signal without this | unlocks #4 | Reset to true |
| 4 | HIGH | Bid strategy — all 3 campaigns | Manual CPC, eCPC off | SA360 portfolio Target CPA ~$500, pooled across all 3 | Bids never optimize to outcomes | ~$4–6K/mo efficiency | Revert to Manual CPC with prior bids |
| 5 | MED | Budget split across the 3 campaigns | Even-ish | Shift toward PlatformIntercept ($285 CPA), trim BrandGeneric ($906 CPA) | 3x CPA gap between campaigns | reallocates ~$8,154/mo | Restore prior budgets |
| 6 | MED | Brand ad groups (RSAs) | 4 headlines / 2 descriptions | Build to 8+ headlines / 3+ descriptions | Below Bing RSA standard; caps Ad Strength and QS | CTR / QS lift | Revert ads |
| 7 | MED | TradingView ad groups | English RSAs served to a Spanish audience | Replace with Spanish variants | Language mismatch on the best-converting theme | conversion-rate lift | Re-enable English ads |
| 8 | MED | "forex mexico" keyword | Matching currency-quote queries (tipo de cambio, dólar hoy, banxico, usd mxn) | Add as negatives; attach the General and Educational shared lists | Informational, non-trading intent | ~$130+/mo | Remove negatives |

---

## 7. Sequence for this week

1. **Today — stop the bleed.** Rows 1, 2, 8. Geo exclusions and negatives reclaim wasted spend the moment they apply.
2. **Today — unlock the signal.** Row 3. Turn off `ExcludeFromBidding` so conversions can reach a bid strategy. Confirm conversions keep recording for 24–48 hours.
3. **Day 2–3 — hand Bing a steering wheel.** Row 4. Once the signal flows, move all three campaigns to the pooled SA360 Target CPA.
4. **This week — creative and mix.** Rows 5, 6, 7. Rebalance budget by CPA, fatten the brand RSAs, localize the TradingView ads.

---

## 8. Sources and reconciliation

- **Bing-direct:** bing-ads MCP, account 31003116 (campaigns, keywords, search terms, UET tags, negative lists, budgets, diagnostics).
- **SA360:** sa360 MCP, customer 5372690580 / login 9697709980 (campaign conversions, user-location geo, ad-level conversions, bid strategy).
- **Conversion read:** `metrics.conversions` (Primary/KPI = submitted applications). `metrics.all_conversions` is inflated by sitewide events and `-1777…` synced copies and is not used here.
- **Reconciliation:** SA360 and Bing-direct match to the cent on spend, and exactly on impressions and clicks. They diverge only on conversions, which is the reason this account must be audited through SA360.
- **Data workbooks:** `data/GGMI-Bing-Apr-Jun-2026-data.xlsx` (trend + keywords), `data/GGMI-Bing-SA360-June-2026-data.xlsx` (conversions, geo, ad-level, bidding status).
- **Scorecards:** Bing-direct audit and SA360 audit (artifact links in the session).
- **Caveat:** the 3-campaign structure launched around June 18, so June reflects about 12–13 days of the current setup. Treat the month as directional.
