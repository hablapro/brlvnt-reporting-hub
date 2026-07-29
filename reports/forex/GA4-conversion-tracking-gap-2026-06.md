# GA4 Conversion Tracking Gap — GGMI vs GCG (June 2026)
**Internal evidence note. Berelvant. Not client-facing as-is.**
Pulled 2026-07-20 from the live GA4 API. Purpose: one page that proves the GGMI conversion-measurement problem sits in the GA4 property configuration, not in media, by comparing it directly to the GCG property that works.

## The finding in one sentence
On the Forex US property GA4 records conversions for every paid channel; on the Forex LAT property (GGMI) it records zero, so GGMI's application events are not firing into GA4.

## The evidence — GA4 key events by source, June 2026, paid channels

| Paid channel | GCG · Forex US (325353267) | GGMI · Forex LAT (508849216) |
|---|---|---|
| meta / paid-social | 42,747 sessions → 43,431 key events | 1,745 sessions → **0 key events** |
| bing / cpc | 15,774 → 17,232 | 1,895 → **0** |
| azerion / display | 4,836 → 4,996 | 1,363 → **0** |
| quantcast / display | 3,013 → 3,112 | 904 → **0** |
| Whole property, all sources | key events on nearly every session | **~14 key events, all month** |

Same brand, same agency, same channels, two subproperties of the one Forex Brand property. The US property captures conversions across every channel. The LAT property captures none.

## The one caveat to hold (do not overclaim)
On the US property key events run about equal to sessions on nearly every row (Meta: 42,747 sessions vs 43,431 key events). A very broad event is marked as a key event there, so it fires on almost every visit. The 43,431 is not 43,000 applications. State the point at the property level, not the volume level:

- **Forex US:** key-event tracking is configured and firing. The clean application count our QA isolated was **89 Meta application starts** in June.
- **Forex LAT (GGMI):** key-event tracking records **0** for Meta and every other paid channel.

## Sentence you can stand behind
"On the US property GA4 captures conversions for every channel. On the LAT property it captures none. The GGMI application events are not firing into GA4, which is why we source GGMI conversions from SA360 and the vendors instead."

## What works vs what does not (GGMI / Forex LAT)
1. GA4 pageview and session tag: **working.** Meta drove 1,745 measured sessions in June.
2. GA4 key-event / conversion layer: **not capturing paid applications for any channel.** This is the gap.
3. Meta's own platform pixel: **firing but unreliable** (86 reported, 67 of them from one retargeting campaign with 126 landing-page views). Separate issue.

## Why the June reporting still stands
The June deck uses no GA4 number for any conversion. Bing conversions come from SA360 offline import, Azerion from the vendor, Meta is held, Quantcast is view-through. GA4 was only the traffic and session source, and that layer works. No reported number is wrong because of this gap.

## Ownership
The GA4 property configuration and the on-site application key events are client-owned (StoneX central / WebOps). Berelvant does not own this tracking setup. This has been an open item across multiple months.

## Fix path (client-owned)
1. Configure and mark the application-start and submit events as key events on the Forex LAT property.
2. Link the SA360 account to the Forex LAT property (also recovers the ~31% Unassigned bucket, about 2,451 June Mexico sessions).

## How to reproduce
GA4 API `runReport`, property 508849216 (LAT) and 325353267 (US), 2026-06-01 to 2026-06-30, dimension `sessionSourceMedium`, metrics `sessions` and `keyEvents`. Both properties are subproperties of Forex Brand (313295947).

## UPDATE 2026-07-28 — the events DO fire; the gap is key-event designation
Event-level pull (dimension `eventName`, June 2026) shows the live-application events firing on the LAT property. The earlier claim "application events are not firing into GA4" is wrong at the event layer; they fire but none are marked as key events, so the `keyEvents` metric reads ~0. This makes the fix a config toggle in GA4 Admin, not a tagging/dev ticket.

The live application event family on LAT, June 2026:

| Event | LAT count | US count | Meaning |
|---|---|---|---|
| `live_start` | 4,990 | 47,212 | live application started |
| `live_confirmation` | 660 | 9,558 | live application confirmed (parent event) |
| `live_confirmation_g2` | 540 | 250 | confirmed on G2 platform |
| `live_confirmation_mt5` | 117 | 119 | confirmed on MT5 |
| `live_confirmation_mt4` | 4 | 36 | confirmed on MT4 |

- On LAT the platform-suffixed events sum to the parent (540+117+4=661 ≈ 660): mark ONLY `live_confirmation` (+ `live_start`) as key events, use the suffixed ones for platform splits, else you double count.
- On US the parent (9,558) far exceeds the suffix sum (405); US has app streams (`screen_view` present) likely firing the parent without suffix. LAT is web-only.
- `live_start` by source on LAT: **2,448 of 4,990 (~49%) attributed to "(unlinked SA360 account)"** — the SA360 link fix recovers this directly. Direct 1,042, google/organic 603, tradingview/display 265, bing/cpc 169, Meta/social 70.
- `live_confirmation` by source on LAT: direct 205, google/organic 155, inappuser 108, tradingview 57, unlinked SA360 40, bing/cpc 7, Meta/social 8, quantcast/azerion 0. HOLD INTERNALLY: GA4 last-non-direct-click will show far fewer paid live apps than SA360 offline / vendor view-through. Pre-frame that difference before the client sees GA4 conversion numbers, or it reads as a discrepancy in our reporting.
- Demo equivalents exist (`demo_confirmation`, `_g2`, `_mt5`, `_mt4`) if demo accounts are ever wanted as key events.

## VERIFICATION MATRIX 2026-07-28 (systematic pass, pre-client certainty)
**VERIFIED (reproducible evidence):**
1. LAT key-event config = `first_open` ONLY (app event). Jan–Jun keyEvents: 0/1/0/5/23/14, all first_open. Web application events were NEVER designated. (Data API: eventName × keyEvents.)
2. US key-event list exact: session_start (the inflator), live_start, live_confirmation(+g2/mt5/mt4), demo_confirmation(+g2/mt5/mt4), first_open, lead_generation, view_search_results. LAT target = this list minus session_start, parent events only.
3. Vendor clicks DO carry UTMs: CM360 creative assignments — QC display `/es/about-us/overview/?utm_source=quantcast&utm_medium=display`, AZ display `/es/?utm_source=azerion&utm_medium=display`, AZ native `utm_source=Azerion&utm_medium=native` (capitalized → the GA4 case-split rows). NO utm_campaign on any = root cause of campaign-level blindness ("(referral)"/"(not set)").
4. Site does NOT strip UTMs: live browser test 2026-07-28 ~16:12 ET, GA4 collect hit `dl=` carried full UTMs incl. seeded `utm_campaign=brlvnt_qa_test_20260728` (tid G-XPZTRCXSST).
5. Cloudflare challenge intercepts ad-click URLs: normal Chrome session got interstitial (GA4 `dr=` shows `__cf_chl_tk` redirect); curl gets 403 `cf-mitigated: challenge`; June vendor landing pages show `__cf_chl_*` tokens.
**OPEN (do NOT assert to client until closed):**
A. **CLOSED-CONFIRMED 2026-07-28 8:03pm ET.** Receipt query on LAT returned the row `brlvnt_qa_test_20260728 | azerion / display | 1 session`. End-to-end ingestion PROVEN: click URL → Cloudflare challenge → landing page → GA4 collect → property, with source/medium/campaign all intact. The 503 on the collect POST was transient (hit retried/ingested). The core client story stands with zero open contradictions; Roshni docx cleared to send.
B. Azerion page_view gap: 1,366 session_start vs ~130 page_view (quantcast 903 vs 573). Candidate causes: challenge attrition, consent-mode blocking page_view, instant bounce. Test: fresh profile/incognito click, do NOT touch consent banner, watch which GA4 events fire.
C. GA4 rendering campaign as "(referral)" vs "(not set)": cosmetic labeling question only; missing utm_campaign is proven either way.
