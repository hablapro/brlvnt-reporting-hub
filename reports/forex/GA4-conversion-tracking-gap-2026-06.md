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
