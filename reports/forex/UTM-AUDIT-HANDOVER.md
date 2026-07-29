# UTM Parameters Audit — Project Handover
**Written 2026-07-28. Source session: GA4 conversion-gap investigation (GGMI). Read this first, then `GA4-conversion-tracking-gap-2026-06.md` (verification matrix at bottom).**

## Project goal
Audit UTM parameters across all live Forex channels (GGMI LATAM + GCG US Hispanic) and drive correct implementation: full parameter set, consistent casing, campaign-level attribution in GA4, no untagged leakage.

## What is already VERIFIED (do not re-derive; evidence + repro steps in the gap file)
1. **Ingestion pipeline works end to end.** Live test 2026-07-28: seeded click `utm_source=azerion&utm_medium=display&utm_campaign=brlvnt_qa_test_20260728` on forex.com/es/ passed the Cloudflare challenge, GA4 received the full URL, and the session appeared in the LAT property (508849216) ~4h later with all three parameters intact. The site does NOT strip UTMs. This also proves the seeded-campaign receipt test as a reusable QA method.
2. **Quantcast + Azerion display clicks (CM360-served) carry ONLY `utm_source` + `utm_medium`.** No `utm_campaign`, `utm_content`, `utm_term` on any of the 248 CM360 ads checked. Root cause of campaign showing `(referral)`/`(not set)` in GA4 for both vendors.
3. **Casing is fragmented and both variants are live.** CM360 display ads: lowercase (`azerion`, `quantcast`). CM360 native ads (launched Jun 25, campaign 36170375, type AD_SERVING_TRACKING): capitalized (`Azerion`, `Quantcast`) with `utm_medium=native`. GA4 splits each vendor into 2+ rows; on Jul 28 capitalized `Quantcast / display` outweighed lowercase 15:1 in daily sessions.
4. **CM360 landing-page library is a landmine.** Advertiser 16624558 has: "Default" = `https://www.forex.com/es/?utm_source=quantcast&utm_medium=display` (hardcoded quantcast, any ad falling back to it credits Quantcast) and "GGMI_es_default" = `https://www.forex.com/es/` (no UTMs at all).
5. **Untagged leakage exists:** `s0.2mdn.net / referral` (Google's CM360 creative CDN as referrer) took 34 sessions on Jul 28 alone = ad clicks arriving with no UTMs. Also one malformed source `quantcast,mp-dtom` (comma-joined macro).
6. **Cloudflare challenges ad-click URLs** (curl gets 403 `cf-mitigated: challenge`; a real Chrome session passed via interstitial, `__cf_chl_tk` redirect visible in GA4 referrer). Did not block a passing browser's UTMs. Open question below on attrition.
7. **GA4 LAT key-event config** (context, owned by the sister workstream): only `first_open` is designated; `live_confirmation`/`live_start` fire but are unmarked. Fix is with StoneX WebOps; docx for Roshni ready at `reports/forex/GA4 Conversion Tracking - Forex LAT Property Gap - June 2026.docx` (Renzo reviewing).

## Channel-by-channel starting state (June + Jul-28 GA4 observations, LAT unless noted)
| Channel | Source/medium seen in GA4 | Campaign in GA4 | Status |
|---|---|---|---|
| Quantcast display | `quantcast / display` + `Quantcast / display` | (referral)/(not set) | Broken: no campaign, case split |
| Quantcast native | `Quantcast / native` | (referral)/(not set) | Broken: same |
| Azerion display | `azerion / display` + `Azerion / display` | (referral)/(not set) | Broken: same |
| Azerion native | `Azerion / native` | (referral)/(not set) | Broken: same |
| Bing paid (SA360) | `bing / cpc` | Real names (`FX_LATAM_…_brlvnt`) | Campaign OK; big chunk sits in `(unlinked SA360 account)` bucket until SA360→GA4 link (client-owned) |
| Google paid (GCG) | `google / cpc` | Real names (`GCG_US_…`) | Campaign OK; NOTE: GCG US campaigns appear on the LAT property (cross-property tagging on /es/ pages) — audit item |
| Meta | `meta / paid-social` AND `Meta / social` | not audited | Two schemes live in June — needs dedicated audit |
| Email (SFMC) | `et / email` | Real names | Looks OK, verify template |
| Push | `LATAM_NA_PN / Push` | LATAM_Marketing | Capital-P medium — normalize |
| TradingView widget | `tradingview / display` | `openaccountbutton` etc. | Partnership tag, not paid media; leave but document |

## Not yet audited (the actual to-do)
- Meta ad-level URL parameters (both GGMI and GCG accounts) — meta-ads MCP: `get_ad_creatives` exposes URL tags.
- Bing/SA360 final-URL suffixes (bing-ads / sa360 MCPs) — campaigns resolve, but confirm the template and `utm_content` depth.
- GCG-side CM360 advertiser 16576650 (only GGMI 16624558 was checked).
- Native pilot (GCG) tagging.
- Email/push templates (client-owned, SFMC).
- A written UTM taxonomy/standard to hand every vendor (utm-governance skill has the framework).

## Fix backlog (by owner)
1. **Berelvant, CM360 (mutation-gated — show mutation table, wait for explicit yes):** add `utm_campaign={campaign}` + `utm_content={adset/creative}` to all vendor click-through URLs; normalize all sources/mediums to lowercase; fix or retire the hardcoded-quantcast "Default" landing page; investigate the s0.2mdn.net untagged path (likely backup-image/rich-media exits without suffix).
2. **StoneX WebOps (via Roshni doc, in flight):** key-event designation + SA360→GA4 link; review Cloudflare challenge on paid landing paths.
3. **Open diagnostic:** Azerion page_view gap (June: 1,366 session_start vs ~130 page_view; Quantcast 903 vs 573). Candidates: challenge attrition, consent mode, instant bounce. Test: fresh browser profile, click test, do NOT touch consent banner, watch which GA4 events fire.

## Proven test protocol (reuse for every fix)
1. Seed a click with a unique `utm_campaign=brlvnt_qa_<what>_<yyyymmdd>` on the target URL.
2. Watch the GA4 collect hit in the browser network log (`dl=` carries the URL; 503 responses can still ingest).
3. ~4h later (intraday lag proven ~4h, allow up to 24): `runReport` on the property, dims `[sessionCampaignName, sessionSourceMedium]`, today/today, find the seeded row.

## Key IDs and access
- GA4: LAT/GGMI `508849216`, US/GCG `325353267`, brand umbrella `313295947`. Web stream measurement ID (LAT): `G-XPZTRCXSST`.
- CM360: profile `10604084`, account `5877`; advertisers GGMI `16624558`, GCG `16576650`. Display/native campaign seen: `35506122` (display), `36170375` (native tracking ads).
- SA360 / Bing / Meta / Quantcast: MCPs configured in `.mcp.json`; SA360 customer IDs in memory `reference_sa360_query_ids`.

## Tooling gotchas (cost hours today; do not rediscover)
- GA4 MCP `dimensionFilter` is broken (serializes to string) — pull unfiltered with high limit, filter locally in python; large results auto-save to a file path given in the error.
- GA4 realtime API has NO campaign dimensions — receipts must use standard reports.
- `getConversionEvents` (MCP) does NOT return the key-event flag — use `eventName × keyEvents` metric instead.
- Quantcast MCP `quantcast_creatives` without accountId returns other clients' accounts — CM360 is the click-URL authority for this buy anyway.
- curl to forex.com gets Cloudflare 403 — use the Chrome extension for live tests.
- Word/PowerPoint AppleScript quirks: see repo `KNOWN-BUGS.md`.

## Doctrine that binds this project
- Mutations (CM360 URL edits) only behind an explicit per-batch approval table. Reporting-only posture otherwise.
- Client-facing materials: no vendor blame, no competitor names, spend matches client tracker.
- Skills to load when executing: `utm-governance`, `cm360-trafficking-qa`; `stop-slop` for any written deliverable.
