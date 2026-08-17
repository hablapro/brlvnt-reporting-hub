# July 2026 Report — Build Status & Resume Handoff (GGMI)

Cycle opened 2026-08-04. Approach this cycle: pull channel by channel, QA each channel's data before moving to the next, model and narrate after all channels are in. Reporting only; no account mutations from this repository.

**PHASE 5 BUILD CLOSED 2026-08-17.** Narrative approved by Renzo 2026-08-17; deck (14 slides, housestyle) and formatted report built; all four gates pass (verify_numbers, protection_scan 0 BLOCK, render QA 14/14 all slides inspected, doctrine walk). **One item before Phase 6 delivery: July client-funnel rows (slide 2) — Renzo supplies; then re-run gates on the updated deck and upload to the FX Report Drive folder.** Deliverables: `reports/forex/ggmi/2026-07/output/GGMI_LATAM_July_2026_Performance_Review.pptx` + `GGMI-July-2026-Performance-Report.xlsx`.

**PHASE 3 MODEL CLOSED 2026-08-14.** All 5 GGMI channels pulled + QA'd; tracker received and reconciled; `reports/forex/ggmi/2026-07/figures.json` and `model/GGMI-July-2026-cross-channel-model.xlsx` complete; QA note at `qa/qa-and-model.md`. Client-facing basis: tracker (Total Working Media $149,896 incl. DOOH $26,865 and Native $27,630 lines, both new vs June). Next: Phase 4 narrative → Renzo approval → deck build. Meta ruling confirmed 2026-08-14: spend/delivery only. Google Ads row below is GCG-cycle scope, not GGMI (ruling 2026-08-14: GGMI first, GCG after).

Kickoff reading done per `PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md` §9: the two standing questions are (1) what does the client already hold, (2) how is the agency scored. Agency scorecard = low-cost primary conversions; downstream funnel framed as the client's journey, neutral. Protection scan required before any deliverable ships.

## Channel status

| Channel | Data pulled | QA | Model | Notes |
|---|---|---|---|---|
| **Bing / SA360** | ✅ 2026-08-04 | ✅ all reconciliations PASS | — | `reports/forex/ggmi/2026-07/data/GGMI-Bing-July-2026-data.xlsx` |
| **Meta** | ✅ 2026-08-04 | ✅ all reconciliations PASS (spot-checked live by main session) | — | `reports/forex/ggmi/2026-07/data/GGMI-Meta-July-2026-data.xlsx` |
| **Quantcast** | ✅ 2026-08-04 | ✅ all reconciliations PASS (spend + geo independently re-verified by main session) | — | `reports/forex/ggmi/2026-07/data/GGMI-Quantcast-July-2026-data.xlsx` |
| **Azerion** | ✅ 2026-08-14 | ✅ 13/13 reconciliations PASS | ✅ | `GGMI-Azerion-July-2026-data.xlsx`. July EOM xlsx arrived by email 2026-08-04 (Gmail msg `19fce71106bf7329`, thread "Azerion \| Forex \| 7/16/26 \| July \| mid month Reporting"); download blocked on `gws auth login` reauth. Add 7.5% tech fee (internal only). Vendor call summary claims US display ~80 apps @ ~$350 — that is GCG, keep out of GGMI. |
| Google Ads | — | — | — | |
| **GA4 / client funnel** | ✅ 2026-08-04 | ✅ all reconciliations PASS/disclosed | — | `reports/forex/ggmi/2026-07/data/GGMI-GA4-July-2026-data.xlsx`. Traffic/geo/diagnostic only — NOT a conversion source this cycle. |

---

## ✅ BING (GGMI LATAM) — pulled 2026-08-04

**File:** `reports/forex/ggmi/2026-07/data/GGMI-Bing-July-2026-data.xlsx` — 10 tabs (Campaigns, Phases, Daily Trend, Geo Compliance, Funnel, Keywords, Conversion Goals, Config Audit, Search Queries, Notes & QA).
**Actions:** `recommendations/forex/ggmi/GGMI-Bing-August-2026-actions.md` — 12 items, P0/P1/P2, all approval-gated.

**Sources:** bing-ads MCP acct 31003116 (spend/impressions/clicks/keywords/goal config) + sa360 MCP customer 5372690580 / login 9697709980 (conversions, geo, funnel steps, daily). Conversions MUST come from SA360 — GGMI conversions are offline-imported and read 0 in the Bing API.

**Primary KPI (settled 2026-08-04, Renzo):** the goals named *Live Confirmation* fire on the post-submission confirmation / ThankYou page, so a Live Confirmation **is** a submitted application. Confirmed from the account's own URL-based goals — `FX ES Step 1–4` map to `/en/step/1`…`/en/step/4` (form pages) and the confirmation goals map to `/en/step/ThankYou`. June's "submitted applications" wording is correct and carries forward unchanged. Downstream steps are separate goals (`GCLID - Approved / Funded / Traded`) and stay out of the agency scorecard.

**Headline numbers:** $10,624.94 spend · 90,394 impressions · 4,090 clicks · 4.52% CTR · $2.60 avg CPC · **20 submitted applications** · $531.25 blended cost per submitted app.

**July is two accounts in one month — do not report it as one.**
- Jul 1–10: **dark**, zero delivery (carry-over from the June pause; relaunched Sat Jul 11).
- Jul 11–22: **Phase A, legacy campaigns.** $5,882.57 spend, **0 submitted apps.**
- Jul 22–31: **Phase B, rebuilt Mexico-only `MX_` structure.** $4,742.37 spend, **20 submitted apps at $237.12 each** ($140.71 across the two campaigns that actually converted) vs June's $513.17.

Only `MX_GEN_Tradingview` (18) and `MX_GEN_Upper_funnel` (2) converted, both new.

**Three findings that change the story:**

1. **Mexico-only breach is closed.** Non-Mexico delivery = $285.01 of $10,624.94 = **2.7%**, against 49% in June and 51.6% at the Jul 13 audit. All 6 new `MX_` campaigns delivered **100% Mexico**. All residual leakage sits in three legacy campaigns paused Jul 22 (PlatformIntercept $244.67 — 96% of the leak, almost all Venezuela; AO_GEN_TradingView $34.23; AO_Brand $6.11).

2. **The legacy campaigns broke at Step 2 → Step 3, and it is not import lag.** They produced **207 application starts** (policytest_v2 104, PlatformIntercept 81, BrandGeneric 22) and **zero Step 3, zero Step 4, zero submitted applications.** Steps 1 and 2 imported normally for those same campaigns, and the new campaigns' Step 3/4/live imported fine over a *shorter* window — so a pipeline delivering Step 2 but never Step 3 across three campaigns over 11 days is a funnel failure. `MX_GEN_Tradingview` by contrast carries 134 starts → 74 → 16 → 16 → 16 submitted (**13.4% start-to-submitted**). This matches the GCG Q2 post-mortem conclusion: the loss is in start→submit, not top-of-funnel volume. Highest-value item for the client conversation.

3. **Primary-KPI import is fixed; the bidding signal is still off.** Both submitted-application goals (40059184, 40059257) now read `RecordingConversions` — they were `NoRecentConversions` at the Jul 13 audit, so that flag is resolved. But all 7 GGMI goals still carry `ExcludeFromBidding = TRUE` and every campaign runs MANUAL_CPC. **Third consecutive month** this item has been carried (June report, Jul 6 remediation row 3, Jul 13 audit item 1). July's $140.71 cost per submitted app was earned with no conversion feedback at all.

**Reconciliations — all PASS:** Bing-direct $10,624.95 vs SA360 $10,624.94 (1¢, BrandGeneric rounding) · keyword spend = campaign spend · geo spend (MX $10,339.93 + non-MX $285.01) = total · daily spend and clicks = SA360 totals · ad-group conv (17+1+2) = campaign conv (18+2) = 20 · conversion-action detail (16+2 G2 live + 2 MT5 live) = 20.

### 🔴 Open items before the Bing section can ship

1. ~~Geo setting not verified.~~ **VERIFIED 2026-08-04 — STILL WRONG.** All 9 enabled campaigns carry `positiveGeoTargetType = PRESENCE_OR_INTEREST`. July's 2.7% non-Mexico is a low-volume artifact plus the Jul 22 pausing of the leaking legacy campaigns, **not** a fix. Venezuela — the largest leak in both June and July — is still not excluded; the only negatives are Canada, Guatemala and the US. **The breach is DORMANT, not closed, and returns as volume scales. Do not tell the client the geo issue is resolved.** Fix = P0 item 1 in the recommendations file.
2. ~~Conversion maturity.~~ **CLOSED 2026-08-14.** SA360 re-pulled live: July conversions unchanged at exactly 20 (Tradingview 18, Upper_funnel 2), campaign spend reconciles to $10,624.94 to the cent. Ten additional days of the 90-day window added zero conversions, so 20 / $531.25 blended / $237.12 Phase B are final for the deck.
3. ~~Legacy zero-conversion anomaly.~~ **FOCUSED LOOK DONE 2026-08-14.** (a) Still zero after 10 more days of maturity — drop-off confirmed, not lag. (b) SA360 `ad_group_ad.final_urls` shows a clean destination split: policytest_v2 sent 1,515 of its 1,796 July clicks (84%) to `forex.com/es/about-us/overview/` (corporate About Us page); BrandGeneric and PlatformIntercept used the legacy `/lp/plataforma-de-verdad/` and `/lp/broker-de-confianza/` pages; **all 20 submitted applications came from campaigns landing on `/es/`** (homepage). Client-facing characterization: neutral — legacy campaigns' application starts came from non-product landing destinations and none progressed past Step 2, vs 13.4% start-to-submitted on the rebuilt campaigns landing on `/es/`. Do not claim a proven single cause (LP effect and keyword-intent effect are confounded); recommendation is to standardize on the converting destination and review the legacy-LP → application handoff.
4. ~~Client tracker not reconciled.~~ **RECEIVED + RECONCILED 2026-08-14.** Renzo supplied both entity tracker pages (tracker last-update 08/06/2026); transcribed verbatim to `reports/forex/<entity>/2026-07/data/sources/<ENTITY>-client-tracker-July-2026.xlsx`. **Client-facing GGMI spend basis:** Bing $10,625 · Quantcast $39,240 · Azerion $37,509 · Native $27,630 · Meta $8,027 · DOOH $26,865 · Total Working Media $149,896. Reconciliation vs platform: Bing $10,624.94 PASS (Δ$0.06) · Meta $8,027.45 PASS (Δ$0.45) · Quantcast **tracker line = main campaign only** ($39,240 vs $39,236.80, Δ$3.20 PASS) — the NativeOnly campaign ($10,003.47) sits inside the tracker's separate "Native" $27,630 line, presumably with Azerion native ($17,626.53 residual, confirm when vendor file lands). Azerion $37,509 unreconciled until vendor xlsx is downloaded. DOOH (Perion, $26,865) is on the tracker but outside our pulled channel scope — decide its deck treatment against June precedent at model time. Per standing ruling, deltas recalculate silently; none reach client artifacts.
5. ~~KPI wording.~~ **RESOLVED 2026-08-04** — Live Confirmation = submitted application, confirmed against the account's URL-based step goals. June wording stands; no restatement and no footnote needed.
6. Housekeeping only: 155 paused legacy campaigns, ~40 dead conversion goals still in the account.


### Campaign assessment (config audit + search queries, 2026-08-04)

**Verdict: the structure is right and the settings are wrong.** The July rebuild fixed the thing that mattered strategically — a Mexico-named, theme-segmented account where the winning theme is isolated and measurable — while leaving every underlying misconfiguration from June in place.

**Working:**
- TradingView theme is the engine. `MX_GEN_Tradingview` → `Exact` ad group → keyword `tradingview` produced 17 of July's 20 submitted applications and carries 13.4% of its application starts through to submission.
- Both primary conversion goals are importing again (`RecordingConversions`), so the account is measurable for the first time since the June gap.
- August 1–4 corroborates July rather than contradicting it: 6 submitted applications on $1,458.99 = **$243 each**, against July Phase B's $237. MT5 and Forex have now started converting too (2 each), which softens the July "Forex spent $1,672 for nothing" concern.
- `Network: OwnedAndOperatedOnly` — Bing search only, no syndicated partners. Correct quality choice.
- SA360 tracking parameters (`dsadgroup` / `dsadgroupid`) present on the ad groups checked.

**Missing / broken (full evidence in the Config Audit tab):**
| Item | Found | Verdict |
|---|---|---|
| `positiveGeoTargetType` | `PRESENCE_OR_INTEREST` on all 9 | **breach dormant, not fixed** |
| Location negatives | Canada, Guatemala, US only — **no Venezuela** | incomplete |
| Location positives | Mexico + Mexico City (nested, redundant); Competitor has unresolved ID 9450400 | sloppy |
| Conversion goals | all 7 still `ExcludeFromBidding = TRUE` | **3rd cycle carried** |
| Ad rotation | `OptimizeForClicks` | wrong objective |
| Ad group language | English on Tradingview, unset on Forex — neither Spanish | wrong; 7 of 9 unchecked |
| Bid strategy | Bing says eCPC, SA360 says MANUAL_CPC | unreconciled since June |
| CPC bids | Forex $20/$15 vs Tradingview $8/$7 | inverted vs results |
| RSA creative depth | **could not pull** — `list_ads` broken | unverified since June |

**Waste:** 16.3% of covered search-query spend ($458.08 of $2,812.87, Jul 25–Aug 4) went to non-commercial queries. The bulk is navigational TradingView traffic — `tradingview.com` ($164.71), `tradingview iniciar sesión` ($93.72), `página oficial` ($16.01) — people looking for TradingView the product, not a broker. MX_GEN_MT5 is worst proportionally (~20%), including `mp5 x7 descargar` (an audio-player query) and `xm broker descargar` (a competitor).

**Budget headroom is not the constraint:** ~$140,800/month configured across the enabled campaigns against $4,742 of actual Phase B spend. The account is delivery-constrained. Raising budgets will not raise volume.

**Tool failures this pull (per doctrine, disclosed):**
- `bing_ads_list_ads` — 400 NullRequest, server-side, failed twice, bounded effort exhausted. RSA depth unverified. Recorded in `KNOWN-BUGS.md`.
- `bing_ads_search_term_report` — silently ignores `campaign_ids`, and a start date on which only some campaigns delivered returned a single day ($160.61). Re-pulled without the filter to get usable coverage. Also recorded.


---

## ✅ META (GGMI LATAM) — pulled 2026-08-04 by `meta-july` subagent

**File:** `reports/forex/ggmi/2026-07/data/GGMI-Meta-July-2026-data.xlsx` — 8 tabs (Summary, Campaigns, Ad Sets, Creatives, Geo, Placements, MoM, Notes & QA).
**Build script:** `tools/forex-july-2026-ggmi-meta/build_meta_workbook.py`

**Attribution (the shared-account trap):** `act_1699453997689551` carries both GGMI and GCG. Split by campaign name prefix, cross-checked against ad-set geo (all GGMI ad sets MX-only, all GCG US-only). No ambiguous campaigns. **Verified live by the main session:** 4 GGMI campaigns sum to exactly $8,027.45 / 4,250,494 impr / 91,153 clicks; 3 GCG campaigns total $6,939.50.

**Headline (July):** $8,027.45 spend · 4,250,494 impr · 74,489 link clicks · 45,818 LPV · **117 SubmittedApplication pixel fires** · $39.67 cost per result blended, $36.63 / $41.22 on the two conversion campaigns.

**MoM vs June:** spend −69.0%, impressions −78.5%, link clicks −81.7%, LPV −81.7%, pixel conversions **+36.0%** (117 vs 86). Spend fell hard while conversions rose — an objective-mix effect, not a pullback. Not fully apples-to-apples because the objective mix itself changed.

**The June open question is answered: the conversion-objective switch happened.** July spend by objective: `OUTCOME_SALES` 56.8% ($4,561.62, 2 campaigns / 3 ad sets, all three explicitly promoting the `SubmittedApplication` custom event), `LINK_CLICKS` 41.6% ($3,341.99), `OUTCOME_ENGAGEMENT` 1.5% ($123.84). Objectives confirmed live.

**Mexico compliance: clean.** 100% of GGMI spend, impressions and clicks in MX across all 4 campaigns, same as June. (Only anomaly: 2 clicks with country "unknown", $0 spend.) Unlike Bing, this is genuinely clean — geo targeting is MX-only at ad-set level, not merely clean-looking at the delivery level.

**Client asks from the June deck — one done, one not:**
- ✅ **Instagram tested.** Placements: Facebook 89.2%, Instagram 10.2% (up from June's 0.3%), Audience Network 0.25%, Threads 0.3%, Messenger <0.1%.
- ❌ **Age 25+ refinement NOT implemented.** All 5 GGMI ad sets still target 18–65 with Advantage+ Audience on. On the CTR campaign (like-for-like vs June): 55+ = 60.1% of spend (June 62.8%), 65+ = 29.2% (June 32.0%). Essentially flat. Laura asked for this in the June review; it did not happen.

**Reconciliations — all PASS:** campaign spend = account total exactly; ad-set spend = campaign totals (all 5); ad-level spend = ad-set totals (all 34 ads); placement and age/gender breakdowns reconcile within $0.02 (rounding).

### 🔴 RENZO RULING 2026-08-04 — META IS A SPEND/DELIVERY REPORT ONLY

**Ruling:** pixel verification is not actionable right now and Meta is down until further notice. July Meta reporting is **what was spent and delivered** — nothing forward-looking, no receipt test, no optimisation roadmap.
*(Interpreting "Meta is down until further notice" as the Meta channel being off going forward, so forward-looking fixes are moot. Correct me if it means the pixel/tracking specifically.)*

**Consequences for the July deck:**
- Report Meta on **spend, impressions, reach, frequency, clicks, CTR, CPC, CPM, LPV, placements, geo**. These are all platform-native, fully reconciled, and safe.
- The **117 SubmittedApplication pixel fires stay labelled as Meta-reported and unvalidated.** With no receipt test possible, they cannot be certified. The event name is inferred from `promoted_object.custom_event_str`, and nothing is cross-checked against GA4 or the client funnel.
- **Do NOT publish a Meta cost-per-submitted-application figure, and do NOT compare Meta to Bing on cost per app.** Bing's 20 are offline-imported and CRM-validated; Meta's 117 are unvalidated client-side pixel fires. Putting $39.67 beside $237 implies Meta is 6x more efficient than Bing, which the data cannot support — the gap is at least partly measurement. This caveat is now permanent for July rather than something a receipt test will resolve.
- The agency scorecard for July therefore rests on **Bing's 20 validated submitted applications**. Meta contributes spend, reach and traffic to the story, not scorecard conversions.
- Drop the previously-recommended Meta pixel receipt test from this cycle's plan. The GA4 LAT key-event gap remains open and client-owned, tracked in the GA4 workstream.

### Open items — Meta
1. ~~Age 25+ not implemented~~ — moot for forward action under the ruling above (channel is down), but **still a factual finding for the July deck**: the client asked in June and it was not implemented. Report it neutrally if the deck covers Meta targeting.
2. ~~Pixel event unverified~~ — **CLOSED as not actionable** per the ruling. Consequence carried above: no Meta cost-per-app figure, no cross-channel comparison.
3. **Reach cannot be de-duplicated** across the 4 campaigns via this MCP. Dominant-campaign figure used (2,251,346), matching the June convention; naive sum 2,573,778 disclosed as an upper bound only. Do not sum reach.
4. **Fatigue watch:** `Retargeting_newlps` ad set has the highest frequency of any GGMI ad set (3.76) on the smallest reach (49,815). `TradingView_exe_q2_reel` is 71% of that ad set's spend. Note the cross-channel echo — TradingView creative on Meta, TradingView keywords carrying Bing.
5. **`RTDOOH_WC_q3`** (World Cup retargeting) is new, one month of data. Do not scale on it yet.
6. **For the GCG July cycle:** `0426_GCG_Q2_esp_us_CTR` delivered $2,104.37 in July despite now being paused — it was live into July. Confirmed live. Don't miss it when GCG is pulled.


---

## ✅ QUANTCAST (GGMI LATAM) — pulled 2026-08-04 by `quantcast-july` subagent

**File:** `reports/forex/ggmi/2026-07/data/GGMI-Quantcast-July-2026-data.xlsx` — 8 tabs (Summary, Campaigns & Ad Sets, Creatives, Geo (Mexico Compliance), Sites (Domain-App), Disallow List, MoM, Notes & QA).
*(Pull was blocked mid-session by a genuine Quantcast 503 platform outage; API verified recovered from the main session and the subagent resumed. No data lost.)*

**Headline (July):** $49,240.27 spend (+45.8% MoM) · 66,659,496 impressions (+58.9%) · 24,255 clicks (+114.9%) · CTR 0.0364% · CPM $0.7387 (−8.8%) · device reach 23,056,195 · **viewability 54.45%** (+3.15pts, still 15.5pts under the IAB 70% floor) · 15 results (5 click-through + 10 view — first click-throughs of the year).

**⚠️ THE QUANTCAST ACCOUNT IS SHARED GGMI+GCG — same trap as Meta.** Account 9969644 "Forex" carries four campaigns, two per entity:
| Campaign | Entity | Spend | Country |
|---|---|---|---|
| `Forex_GGMI_spanish_conversion_Q+campaign_mx` | GGMI | $39,236.80 | Mexico only |
| `Forex_GGMI_spanish_conversion_Q+campaign_NativeOnly_mx` | GGMI | $10,003.47 | Mexico only |
| `Forex_GCG_spanish_conversion_Q+campaign_us` | GCG | $29,854.75 | US only |
| `Forex_GCG_spanish_conversion_Q+campaign_NativeOnly_US_ES` | GCG | $10,002.73 | US only |

An unscoped account-level pull returns ~$89K and shows ~$40K of United States delivery, which would read as a catastrophic geo breach. It is not — it is GCG. **Any Quantcast pull for either entity must be scoped by campaign.** For the GCG July cycle: GCG Quantcast is $39,857.48 across those two campaigns.

**Mexico compliance: PASS, 100.00%** — independently re-verified by the main session via a Campaign × Country/Territory breakdown; both GGMI campaigns return Mexico rows only, zero non-Mexico spend or impressions. Note this is the **first explicit Quantcast geo confirmation** — June's QA recorded only Bing (FAIL) and Meta (PASS), so Quantcast's "clean" status had been assumed rather than evidenced. Given what Bing turned out to be, that distinction matters.

**⚠️ TIMEZONE SENSITIVITY — $232.36 swing.** `quantcast_metrics_report` results depend on the `timezone` parameter. Passing `America/New_York` (the account's own timezone) gives GGMI $49,240.27; omitting it defaults to UTC and gives $49,472.63. **$49,240.27 on America/New_York is the correct basis.** Always pass the account timezone explicitly, and state the basis when reconciling to the client tracker.

**Disallow list: 66 sites, $16,281.30 = 33.1% of GGMI spend** (June: 49 sites / 32% — consistent scale). Two tiers:
- **Tier 1 — low viewability** (<30%, spend ≥$10): 58 sites, $11,263.52.
- **Tier 2 — audience mismatch** regardless of viewability: 8 sites, $5,017.78 — poki.com, biblegateway.com, fandom.com, chunkbase.com, aternos.org, garticphone.com, dalechatea.me, lacuerda.net.
- **Repeat offender, lead with this one: `tvazteca.com`** — spend *grew* $1,346.25 → $3,451.61 while viewability stayed ~9.6%, two cycles running. If the client actions only one exclusion, it is this.
- Others of note: heraldodemexico.com.mx $1,575.53 @ 11.9%, weather.com $1,112.53 @ 10.8%, ebay.com $481.07 @ 2.9%, duolingo.com $322.45 @ 12.5%.
- Site tab covers the top 100 domains by spend (88.4% of total); 6,109 domains delivered overall, full list parsed and on hand if the client wants exhaustive transparency.

**Reconciliations — all PASS to the cent:** account summary = 31-day daily breakdown = 36-row geo breakdown = 2 delivering campaigns = 108 creatives = 6,109 domains. 31 full days confirmed present, so the exclusive-`endDate` handling was correct.

### Open items — Quantcast
1. **`Forex_GGMI_spanish_conversion_campaign_mx` (9083134) is ENABLED with $0 July spend.** Check with the account team whether that is intentional.
2. **No client tracker for July Quantcast yet.** $49,240.27 is the platform figure (already includes the 7.5% Berelvant tech fee — do not add it again).
3. **n=15 results is too low for a CPA claim.** Keep Quantcast framed as awareness/reach in client materials, not conversion, per the standing note. Cost per result computes to ~$3,283 ($49,240.27/15); the subagent reported $3,333.69, likely a platform-computed variant on a different spend basis. Immaterial at this n, but reconcile before any figure is published.
4. **Viewability 54.45% is still 15.5pts under the IAB 70% floor** even after +3.15pts MoM. The disallow list is the lever.
5. MCP gotcha, same class as the `quantcast_accounts` `organizationId` bug: **`quantcast_campaigns` also rejects an object-shaped `accountId` filter.** Pull unfiltered and filter client-side. Also note metric names are display-form ("Budget Delivered", "Clicks (Advanced IVT)"), not snake_case — `spend` throws `INVALID_ARGUMENT`.

---

## ✅ GA4 (GGMI LATAM) — pulled 2026-08-04 by `ga4-july` subagent

**File:** `reports/forex/ggmi/2026-07/data/GGMI-GA4-July-2026-data.xlsx` — 9 tabs (Summary, Channels, Source-Medium, Geo, Landing Pages, Key Events (diagnostic), Unassigned, MoM, Notes & QA).
**Analysis note:** `reports/forex/ggmi/2026-07/qa/ga4-july-analysis.md`.
**Property:** 508849216 (Forex LAT). **Role this cycle: traffic/engagement/geo + tracking-gap diagnostic evidence only. NOT a conversion source — do not compute a GA4 CPA, conversion rate, or funnel number for GGMI.**

**Headline:** 37,574 sessions, down 24.9% vs June's 50,055 — but Unassigned alone collapsed 19,540 → 3,845 (-80.3%, -15,695 sessions), 126% of the entire net decline. Excluding Unassigned, sessions were actually **up 10.5%** (30,515 → 33,729). The "-25%" topline is a channel-mix artifact of Bing's own July delivery collapse (dark Jul 1-10, relaunch Jul 11), not a traffic decline.

**The key-event gap: closed, but on the last day of the month.** Daily `eventName x keyEvents` pulls prove `live_start`/`live_confirmation` read **zero key events every single day July 1-30** despite firing normally (58-141/day), and only start counting on **July 31** (partial-day: 58/74 and 14/17 that day). **Confirmed sticking:** Aug 1-4 shows 100% capture (282/282, 67/67). Total usable July key events = 86, virtually all from July 31; of the ~82 attributable to a channel, only 7 (8.5%) trace to Bing, 0-1 each to Quantcast/Azerion/Meta. **Reconcile against the June/UTM handover: the StoneX fix is real and landed as promised — it just missed nearly the entire reporting month.** Frame as "fixed, too late to help July," not as reopened or still-broken.

**✅ KEY-EVENT FIX INDEPENDENTLY RE-VERIFIED by the main session (2026-08-04), property 508849216, unfiltered `eventName x eventCount x keyEvents` pulls:**
| Window | `live_start` | `live_confirmation` | Capture |
|---|---|---|---|
| Jul 1–30 | 2,646 events → **0 key events** | 665 events → **0 key events** | **0%** — gap fully open, all 30 days |
| Jul 31 (derived) | 74 events → 58 key events | 17 events → 14 key events | ~78–82% — mid-day activation |
| **Aug 1–4** | **283 → 283** | **67 → 67** | **exactly 100%** |

The fix activated **mid-day July 31** and is holding cleanly. The subagent's July key-event figures (58 + 14 + 14 `first_open` = 86) are confirmed exact. Platform-suffixed detail events (`live_confirmation_g2` / `_mt5` / `_mt4`) remain 0 key events, which is correct — the parent `live_confirmation` carries the count, so marking them too would double-count. Only `first_open` was designated before Jul 31, exactly as the June diagnosis found.

**Bottom line for the client conversation:** StoneX did deliver the fix, it works, and it arrived with ~1 day of the reporting month left. July must still be reported on offline/platform data; **August is the first month GA4 can corroborate submitted applications**, which is also the first opportunity to reconcile Bing's offline-imported count against a GA4 figure.

**Venezuela: resolved in volume, not configuration.** 14,552 (June) → 1,382 (July) sessions, -90.5%, now organic/direct-led rather than paid-led. This tracks Bing's Jul 22 pause of the Venezuela-heavy legacy campaigns exactly — **it is not a fix to the underlying geo bug**, which the Bing report already flags as dormant (`positiveGeoTargetType = PRESENCE_OR_INTEREST` on all 9 enabled campaigns, Venezuela still not on the location-negative list). Do not tell the client this is resolved; it returns if Bing scales delivery again without a real targeting fix.

**Unassigned composition (3,845 sessions):** Bing/SA360 unlinked = 34.0% (known issue, unchanged root cause). **New finding:** Quantcast + Azerion NATIVE tracking-ad traffic (820 sessions, 21.3%) lands in Unassigned rather than Display — a distinct channel-grouping gap from the casing issue already on file, not previously quantified.

**UTM damage quantified for July:** vendor display/native casing split 76.8% capitalized / 23.1% lowercase (5,817 sessions, matches the 14-day audit ratio at full-month scale). **New finding:** Meta has a THIRD medium spelling live (`meta/paid-social`, `Meta/social`, `Meta/paidsocial`, 660 sessions) — `Meta/social` (127 sessions, 19.2% of Meta traffic) is misclassified into Organic Social instead of Paid Social by GA4's own channel-grouping rules.

**Reconciliations — PASS/disclosed:** live_start and live_confirmation daily sums match month totals exactly (no truncation). first_open's daily breakdown (7) undercounts its month total (14) — disclosed, API 1,000-row cap on a 1,095-combination query; month total (14) used throughout. Channel-attribution of key events reconciles 82 of 86 (4-event gap disclosed, immaterial, same row-cap cause on a 1,447-combination query). Channel-group totals match source/medium crosstab totals both months.

### 🔴 Open items — GA4
1. **Whether SA360→GA4 link actually happened is still unconfirmed.** Bing's own July volume collapse confounds the read (both bing/cpc and the unlinked bucket fell together, which is what you'd expect from delivery collapse, not from linking). Re-check once Bing's delivery normalizes.
2. **Mexico-only landing-page cut not derived** — GA4 MCP's `dimensionFilter` confirmed broken again this session (returns unfiltered results). Country-level Mexico cuts are reliable (pulled unfiltered, filtered locally); Mexico's channel-level paid share (23.2%) is the closest proxy delivered this cycle.
3. **Quantcast/Azerion native → Unassigned gap** needs a line in the next UTM/tracking remediation pass — newly surfaced, not yet actioned.
4. Tool gotchas hit again, consistent with `UTM-AUDIT-HANDOVER.md`: broken `dimensionFilter`; large multi-dimension pulls overflow to scratch files and were parsed with Python rather than paged; `getConversionEvents` still doesn't expose the key-event flag.
