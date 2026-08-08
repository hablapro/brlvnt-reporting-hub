# GGMI Bing (LATAM) — Recommended Actions, August 2026

**Account:** Bing 31003116 (FOREX.com LATAM) · SA360 customer 5372690580 / login 9697709980 · USD · Mexico-only mandate
**Basis:** July 2026 data pull + live config audit, both 2026-08-04. Evidence: `reports/forex/ggmi/2026-07/data/GGMI-Bing-July-2026-data.xlsx` (tabs: Config Audit, Geo Compliance, Search Queries, Funnel).
**Status:** RECOMMENDATIONS ONLY. This repository executes no account changes. Every item below requires explicit per-batch approval by Renzo before the paid-media/PPC agent touches the account. Floodlight/conversion changes additionally require verification before and after.

Supersedes the open rows of `GGMI-Bing-SA360-remediation-June-2026.md` (Jul 6) and the quick-win list in `reports/forex/ggmi/2026-07/qa/BING-quick-audit-2026-07-13.md` (Jul 13). Items 1 and 2 have now been carried for three consecutive cycles.

---

## P0 — compliance and measurement, do these first

### 1. Set `positiveGeoTargetType = PRESENCE` on all 9 enabled campaigns
**Why:** every enabled campaign still serves "presence OR interest", meaning Bing shows ads to people merely *interested in* Mexico. This is the root cause of the 49% (June) and 51.6% (trailing-30-day, July 13) non-Mexico delivery. July looked clean at 2.7% only because volume was low and the three leaking legacy campaigns were paused on Jul 22. **The breach is dormant, not fixed, and returns as volume scales.**
**Scope:** campaigns 627650448, 627650449, 627650450, 627650451, 627650452, 627650453, 627650454, 627650455, 627650601.
**Also:** Venezuela is still not excluded despite being the largest single source of forbidden delivery in both June and July. Once presence-only is set, country negatives become unnecessary — fix the setting rather than chasing 69 countries with exclusions.
**Housekeeping in the same batch:** remove the redundant Mexico City (20703) positive target, which is nested inside Mexico (2484); and identify geo target `9450400` on MX_GEN_Competitor, which did not resolve in the `geo_target_constant` lookup.
**Verification:** re-run `user_location_view` (targeting_location = false) 7 days after the change and confirm non-Mexico spend is ~0%.

### 2. Set `ExcludeFromBidding = false` on the 7 GGMI conversion goals
**Why:** third consecutive cycle carrying this. Goals `40059107 / 40059122 / 40059144 / 40059152 / 40059170 / 40059184 / 40059257` are all Active and now all `RecordingConversions`, so the data is flowing — but every one is excluded from bidding, so no bid strategy can use it. The account is measuring correctly and bidding blind. July's $140.71 cost per submitted application was achieved with zero conversion feedback.
**Sequence:** do this *before* any move to automated bidding, and let it accumulate signal for 2–3 weeks first.
**Note:** the primary-KPI import concern from Jul 13 is now resolved — both live-confirmation (submitted application) goals report `RecordingConversions`.

### 3. Change ad rotation from `OptimizeForClicks` to conversion-oriented
**Why:** the account is optimising rotation for clicks while being scored on submitted applications. Cheap to change, and pointless to leave once item 2 unlocks the signal.

---

## P1 — waste and relevance

### 4. Add negative keywords for low-intent TradingView and MetaTrader modifiers
**Why:** 16.3% of covered search-query spend ($458.08 of $2,812.87, Jul 25 – Aug 4) went to queries with no commercial intent for a broker. The largest slice is navigational traffic looking for TradingView the product: `tradingview.com` ($164.71), `tradingview iniciar sesión` + `iniciar sesión gratis` ($93.72), `tradingview página oficial` ($16.01).
**Do NOT cut the TradingView theme** — it produced 17 of July's 20 submitted applications. Negative the modifiers, keep the core terms. This is the "fix relevance, don't cut" path already agreed in June.
**Suggested negatives (phrase):** `gratis`, `descargar`, `download`, `iniciar sesión`, `página oficial`, `tradingview.com`, `paper trading`, `curso`, `manual`, `pdf`, `que es`, `cómo operar`, `simulador`, `prueba gratis`.
**Campaign-specific:** MX_GEN_MT5 is the worst proportionally (~20% of its covered spend on download/manual intent) and needs `mp5` as a negative — `mp5 x7 descargar` is an audio-player query. Also add competitor negatives found live: `xm broker`, `exness`, `oanda`, `etoro`, `webull`, `forex factory`.
**Check first:** the account already has 11 shared negative lists including Countries (31), General (389), Educational (228), Competitor (594), Irrelevant (45). Verify which lists are attached to the 9 new campaigns before adding anything — the Jul 13 audit found the Countries list had only 2 associations. It is likely the new campaigns inherited none of them.

### 5. Move informational queries out of MX_GEN_Forex
**Why:** MX_GEN_Forex is paying exact-match bids for `que es forex`, `que es el forex trading`, `forex que es y como operar`. Those are upper-funnel queries sitting on a $20 exact bid.
**Action:** negative them in MX_GEN_Forex and let MX_GEN_Upper_funnel capture them at its lower bids.

### 6. Fix the ad group language setting
**Why:** MX_GEN_Tradingview's ad groups are set to `Language: English`; MX_GEN_Forex's are unset. These are Spanish-language campaigns targeting Mexico. Neither is Spanish, and the two disagree with each other.
**Action:** set all ad groups to Spanish. **Audit the other 7 campaigns** — only 2 of 9 were checked in this pull.

### 7. Review the CPC bid spread
**Why:** MX_GEN_Forex bids $20 exact / $15 phrase; MX_GEN_Tradingview bids $8 / $7. Forex spent $1,671.85 for zero submitted applications in July (2 in August); Tradingview delivered 18 at less than half the bid. The bid hierarchy is inverted relative to the results.
**Action:** bring Forex bids down toward Tradingview's level and reallocate the headroom, pending item 2 giving the account a real signal to bid on.

### 8. Address the QS 3 keywords on the MetaTrader theme
**Why:** four keywords carry Quality Score 3 with meaningful impressions — `mt4` and `metatrader 4` (PlatformIntercept), `mt5` (PlatformIntercept and policytest_v2). The MT theme has scored badly since June. Note that `metatrader` phrase carries QS 10 at 146 clicks, so the *intent* is healthy; it is the model-number keywords whose ad and landing relevance is weak.
**Action:** ad copy and landing relevance work on the MT model-number keywords, not bid cuts.

---

## P2 — investigate before it reaches client material

### 9. Explain the legacy funnel collapse
**Why:** the three legacy campaigns generated **207 application starts** (Step 1) in July and **zero Step 3, Step 4 or submitted applications**. policytest_v2 alone spent $4,039.90 at 100% Mexico with a 7.19% CTR, produced 104 starts, and submitted nothing — after 27 submitted applications in June. Steps 1 and 2 imported normally for those campaigns and the new campaigns' Step 3/4/submitted imported fine over a shorter window, so this reads as a genuine funnel break rather than import lag.
**Why it matters:** this is the single highest-value finding for the client conversation and it corroborates the GCG Q2 post-mortem ("fix the start→submit funnel"). It must be explained before it is characterised in a deck.
**Suggested checks:** landing page / application URL served by those campaigns vs the new ones; whether a form step or redirect broke between Jul 11 and Jul 22; whether the destination differed by campaign.

### 10. Verify RSA creative depth manually
**Why:** `bing_ads_list_ads` is broken (400 NullRequest, server-side — see `KNOWN-BUGS.md`), so June's finding of 4 headlines / 2 descriptions against Bing's 8+/3+ standard could not be re-checked. Do this in the Bing UI or via bulk download.

### 11. Reconcile the bid-strategy discrepancy
**Why:** Bing reports Enhanced CPC (`InheritFromParent → EnhancedCpc`); SA360 reports `MANUAL_CPC`. This disagreement has persisted since June and means one of the two reporting surfaces is misleading.

### 12. Archive legacy clutter
155 paused legacy campaigns and ~40 dead conversion goals. No performance impact; reduces the risk of an accidental re-enable and cleans segmentation.

---

## Do NOT do

- **Do not raise budgets to chase volume.** Roughly $140,800/month is already configured across the enabled campaigns against $4,742 of actual Phase B spend. The account is delivery-constrained, not budget-constrained.
- **Do not cut the TradingView theme.** It is the only theme producing submitted applications.
- **Do not move to automated bidding before item 2 has accumulated signal.**
