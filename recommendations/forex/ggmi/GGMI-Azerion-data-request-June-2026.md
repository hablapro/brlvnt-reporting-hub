# Azerion — GGMI (LATAM) June 2026 Report: Data Requests & Fixes

**To:** Azerion account team (via the client/account lead)
**From:** Berelvant (FOREX.com / GGMI Mexico)
**Re:** June 2026 GGMI report — gaps and corrections needed
**Date:** 2026-07-07
**Send-ready version:** `GGMI-Azerion-email-June-2026.md`

Thanks for the June report. The delivery numbers reconcile (spend $34,555.83 = 7,679,074 impressions at the $4.50 CPM; the seven ad sets and the weekly rows both total correctly). Items below before we finalize.

## Correction (please fix and re-send)

1. **Weekly trend has overlapping weeks.** The Performance tab lists both **"Jun 22-28" and "Jun 23-29"** (a 6-day overlap), plus a standalone "June-30th." Please re-issue clean, non-overlapping weekly buckets that partition the month.

## The gap: the funnel steps are narrative, not data

2. **Provide the full funnel as data.** Results = 42 is the submitted-application count (the instructed conversion) — that's clear. The issue is that the rest of the funnel the exec summary cites (**Step1 225 → 440**, site lands) appears only in prose, not in any table. Please provide the **full funnel as data**, per ad set and per week: Impressions → Clicks → Site lands → Step1 → Step2 → Submitted applications. This is the main item.

## Breakdowns the report is missing (please add)

3. **Geo by country.** As a reminder, **GGMI targets Mexico only.** Include the country breakdown with delivery so Mexico-only is visible in the report.
4. **Site / Domain (Domain/App)** — site-level delivery with spend and viewability, so we can review inventory quality and set up a site block list.
5. **Channel / format** — the summary mentions a newly launched **Native** tactic, but there is no Display vs Native split. Please break out performance by format.
6. **Creative** — creative-level performance for optimization.
7. **Step / site-level viewability** — June came in at 68.5% (down from 71.6% in May); include viewability at the step and site level so we can see where it drops.

---

## For the internal file (not part of the vendor message)

- Raw vendor file: `reports/forex/ggmi/2026-06/data/sources/Azerion Forex GGMI (LATAM) — June 1st-June 30th.xlsx` (was placed under the 2026-05 folder; moved to 2026-06).
- Normalized: `reports/forex/ggmi/2026-06/data/GGMI-Azerion-Apr-Jun-2026-data.xlsx` (Summary & Trend, Ad Sets, Device, Data Gaps).
- **Status:** reporting only. Results = 42 is the submitted-application count (Azerion was instructed that the submitted application is the conversion; DSPs label it generically as "Result"). Treat 42 as submitted applications. The outstanding item is getting the upper funnel (site lands, Step1, Step2) as data, not a definition.
- **CPM note (internal):** the flat $4.50 CPM is a contracted rate (spend = impressions × $4.50/1000), not measured delivered CPM. No action needed from the vendor; noted so the model treats it as a rate, not a market cost. Client-facing spend adds the 7.5% tech fee per internal billing convention.
- **Geo compliance (internal):** GGMI is Mexico-only across all channels. Meta and Quantcast were verified 100% Mexico for June; Bing was in breach (49% non-MX). Azerion geo is unverified until the country breakdown arrives, so Azerion cannot be certified compliant for June yet.
- **June GGMI Azerion, as reported:** Spend $34,556 (+27% MoM), Impr 7.68M, Clicks 9,910 (+57%), **42 submitted applications** (+13.5% MoM vs 37), CPA $823 (+12%), Viewability 68.5% (-3.1pp). Best ad set: Global Market ($407 CPA, 10 results). Weakest: Spanish Platform ($1,391 CPA, 3) and Commodities ($4,072, 0 results) — reallocation candidates for the execution agent, not a vendor question (all ad sets share one tracking setup).
