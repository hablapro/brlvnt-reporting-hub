# GA4 Conversion Tracking: Forex LAT (GGMI) Property Gap

**Prepared by Berelvant for StoneX / FOREX.com**
**Data period: June 2026. Pulled from the live GA4 API on July 20, 2026.**

## Summary

GA4 records key events for every paid channel on the Forex US property. On the Forex LAT property it records none. The application events themselves are firing on the LAT property; none of them are marked as key events, so the conversion layer reports zero. The fix is a configuration change in GA4 Admin, not a tagging project.

Both properties are subproperties of the same Forex Brand property, run by the same team, on the same channels. The US property captures conversions across the board while the LAT property captures a total of roughly 14 key events for the entire month. That pattern points to the LAT property configuration, not to media delivery.

## Evidence: GA4 key events by paid source, June 2026

| Paid channel | Forex US (325353267) | Forex LAT (508849216) |
|---|---|---|
| meta / paid-social | 42,747 sessions, 43,431 key events | 1,745 sessions, **0 key events** |
| bing / cpc | 15,774 sessions, 17,232 key events | 1,895 sessions, **0 key events** |
| azerion / display | 4,836 sessions, 4,996 key events | 1,363 sessions, **0 key events** |
| quantcast / display | 3,013 sessions, 3,112 key events | 904 sessions, **0 key events** |
| Whole property, all sources | key events on nearly every session | **~14 key events, all month** |

A note on reading the US column: the key event configured there is broad and fires on almost every session, so those figures are not application counts. The comparison to hold is at the property level. Key-event tracking on the US property is configured and firing. On the LAT property it records zero for every paid channel.

## What works and what does not on Forex LAT

1. GA4 pageview and session tagging: **working.** Meta alone drove 1,745 measured sessions in June.
2. GA4 key-event / conversion layer: **capturing zero paid applications on any channel.** This is the gap.

## Impact on reporting

June reporting is unaffected. Conversion figures in the June review come from SA360 offline import and vendor reporting, and GA4 serves only as the traffic and session source, which works on both properties. The gap does cost us GA4-side conversion visibility for LATAM going forward until the property is fixed.

## The live application events are already firing on Forex LAT

The event layer needs no new tagging. The live application events exist and recorded the following in June 2026 on the LAT property:

| Event | June 2026 count | Meaning |
|---|---|---|
| live_start | 4,990 | live application started |
| live_confirmation | 660 | live application confirmed |
| live_confirmation_g2 | 540 | confirmed, G2 platform |
| live_confirmation_mt5 | 117 | confirmed, MT5 |
| live_confirmation_mt4 | 4 | confirmed, MT4 |

The platform events sum to live_confirmation (540 + 117 + 4), so live_confirmation is the parent and the platform events are its breakdown.

## Requested fix

The GA4 property configuration sits with the StoneX central / WebOps team, so we are routing this request there. Two items, both in GA4 Admin:

1. Mark live_confirmation and live_start as key events on the Forex LAT property (508849216). Leave the platform-specific events (g2 / mt5 / mt4) unmarked to avoid double counting; they remain available as the platform breakdown.
2. Link the SA360 account to the Forex LAT property. In June, 2,448 of 4,990 live_start events (about 49%) carried the source "(unlinked SA360 account)", so this link materially improves attribution on the application funnel.

Berelvant will QA both changes from the reporting side as soon as they land.

## How to reproduce

GA4 API `runReport` on properties 508849216 (LAT) and 325353267 (US), date range 2026-06-01 to 2026-06-30, dimension `sessionSourceMedium`, metrics `sessions` and `keyEvents`. Both properties are subproperties of Forex Brand (313295947).
