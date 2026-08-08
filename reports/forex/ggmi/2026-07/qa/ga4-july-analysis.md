# GGMI — GA4 July 2026 Analysis
Property 508849216 (Forex LAT). Pulled 2026-08-04. Companion workbook: `../data/GGMI-GA4-July-2026-data.xlsx`.
GA4's role this cycle: traffic, engagement, geo, and diagnostic evidence for the tracking gap. **Not a conversion source** — see hard constraint below.

## Headline
37,574 sessions in July, down 24.9% vs June's 50,055. The drop is almost entirely one bucket: Unassigned sessions collapsed from 19,540 to 3,845 (-80.3%, -15,695 sessions) — 126% of the entire net decline. Excluding Unassigned, sessions were up 10.5% (30,515 → 33,729). The topline "traffic fell a quarter" read is wrong; strip out the bucket that moved and traffic grew.

## The key-event gap: still open for the month, but fixed on the last day
This is the most important finding. Daily `eventName x keyEvents` pulls show:
- **live_start** and **live_confirmation** both read exactly **zero** key events on every single day from July 1 through July 30, despite firing normally (58-141/day for live_start, 12-36/day for live_confirmation).
- **July 31 is the first day either counts at all**, and even then only a partial-day fraction (58 of 74 live_start events, 14 of 17 live_confirmation events) — consistent with the designation change taking effect mid-day.
- **Confirmed persistent:** August 1-4 shows 100% capture (282/282 live_start, 67/67 live_confirmation). This was a real, sticking config change, not a one-day blip.
- Total usable key events for the entire month: **86** (58 live_start + 14 live_confirmation + 14 first_open), almost all generated in the final hours of July. Of the ~82 attributable to a channel, only **7 (8.5%) trace to Bing** (6 bing/cpc + 1 unlinked-SA360); Quantcast, Azerion, and Meta show 0-1 each for the whole month.

**Reconcile this against the June/UTM handover:** the fix StoneX shipped is real (verification matrix, `GA4-conversion-tracking-gap-2026-06.md`, closed 2026-07-28-08-03pm receipt test). It just landed on the very last day of the window this report covers. Frame it as "fixed, but too late to help July's numbers" — not as a reopened or unresolved item, and not as evidence the fix didn't work.

## Venezuela anomaly — resolved in volume, not in configuration
14,552 sessions (June) → 1,382 (July), -90.5%. Mexico fell a normal 9,236 → 7,310 (-20.9%) over the same period, so this isn't a general MX-property decline. July's remaining Venezuela traffic is organic/direct-led (591 organic of 1,382 total in a partial capture), a reversal from June's paid-search-led pattern.

This matches the Bing channel report exactly: Venezuela-heavy legacy campaigns paused July 22; all 6 new Mexico-only campaigns delivered 100% Mexico. **The GA4 drop is the downstream effect of Bing's pause, not a fix to the geo bug.** Per the Bing report, all 9 enabled campaigns still carry `positiveGeoTargetType = PRESENCE_OR_INTEREST` and Venezuela is still not on the location-negative list. Do not tell the client the compliance issue is resolved — it's dormant and returns if Bing scales delivery again without fixing targeting first.

## Unassigned bucket: 3,845 sessions, size and composition
Down from 19,540 in June. Composition:
| Source | Sessions | % of Unassigned |
|---|---|---|
| (unlinked SA360 account) — Bing | 1,307 | 34.0% |
| (not set) | 867 | 22.5% |
| (not set) / inappuser | 809 | 21.0% |
| Quantcast / native | 713 | 18.5% |
| Azerion / native | 107 | 2.8% |
| Long tail | 42 | 1.1% |

**Bing's share of Unassigned: 34.0%.** But the collapse itself is not evidence the SA360→GA4 link happened — both the tagged `bing / cpc` row (1,895→527, -72.2%) and the unlinked-SA360 bucket (17,794→1,307, -92.7%) fell together. If the link had gone live, sessions would have moved OUT of Unassigned INTO tagged bing/cpc, growing that row, not falling with it. This tracks Bing's own July delivery collapse (dark Jul 1-10, relaunch Jul 11), not a fix.

**New finding, not previously quantified:** Quantcast and Azerion NATIVE (CM360 tracking-ad) traffic (820 sessions combined, 21.3% of Unassigned) lands in Unassigned rather than the Display channel that the same vendors' display-format buys get. This is a distinct GA4 channel-grouping gap from the casing-duplicate issue already on file, and worth a line item in the next tracking remediation pass.

## UTM attribution damage, quantified for July
**Vendor casing split** (display/native, Azerion + Quantcast): 5,817 sessions split 76.8% capitalized-scheme / 23.1% lowercase-scheme / 0.07% malformed. Matches the 14-day 1,116:630 ratio the July 28 platform audit found, persisting at full-month scale — each variant is a separate GA4 row, so summing both is required to see true vendor volume.

**Meta medium fragmentation** (new quantification): three medium spellings live simultaneously — `meta/paid-social` (462), `Meta/social` (127), `Meta/paidsocial` (71), 660 sessions total. `Meta/social` reads as organic to GA4's channel-grouping rules and lands in **Organic Social, not Paid Social** — understating Paid Social and overstating Organic Social by 127 sessions (19.2% of Meta-platform traffic). This corroborates from the session side what the July 28 UTM audit flagged as an unaudited ad-level gap on Meta.

## Reconciliation results
- Key-event daily figures for live_start (2,720) and live_confirmation (682) sum exactly to their month totals — full daily coverage, no truncation on those two events.
- first_open's daily breakdown (7) undercounts its month total (14) — a date x eventName query hit the API's 1,000-row cap on a 1,095-combination result; the month-level total (14) is authoritative and used throughout.
- Source/medium x eventName channel attribution reconciles 82 of the month's 86 key events; the 4-event gap is disclosed as immaterial (long-tail rows past the API's row cap on a 1,447-combination query), not investigated further given the bounded-effort policy.
- Channel-group totals match source/medium crosstab totals for both July (37,574) and June (50,055).

## Open questions / not resolved this pull
1. **Whether the SA360→GA4 link has actually been completed** — cannot be confirmed from session data alone this cycle, since Bing's own volume collapse confounds the read. Re-check once Bing's delivery normalizes (August+) — if the link is live, tagged `bing/cpc` sessions should then clearly exceed the unlinked bucket at comparable volume.
2. **Mexico-only landing-page cut** — not derived. The GA4 MCP's `dimensionFilter` is confirmed broken again this session (a `country=Mexico` filter returned all 128 countries unfiltered). Worked around for country-level cuts by pulling unfiltered and filtering locally; a landing-page x country cross at that scale wasn't worth the pull for one data point under the bounded-effort policy. Mexico's channel-level mix (23.2% paid by channel) is the closest proxy delivered this cycle.
3. **Quantcast/Azerion native → Unassigned channel-grouping gap** — newly surfaced, not yet sized against a fix path. Route to the UTM remediation backlog alongside the casing fix.

## Hard constraint honored
No GA4 number is used anywhere in this workbook as a GGMI conversion, CPA, or funnel figure. The Key Events tab is explicitly labeled diagnostic and carries the reconciliation math above so it can't be lifted into a performance claim by mistake.
