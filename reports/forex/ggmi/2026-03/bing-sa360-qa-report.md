# QA Report: Forex GGMI (LATAM) -- Bing Ads via SA360
# Account ID: 3332505241
# Period: 2026-03-01 to 2026-03-31
# Report Date: 2026-04-03
# Source: SA360 MCP (Search Ads 360 API)

---

## Summary

| Field               | Value                                |
|---------------------|--------------------------------------|
| sources_checked     | SA360 (Bing engine account 3332505241) |
| extraction_status   | Partial -- campaign/ad group/keyword/device extracted; geo and conversions detail failed |
| date_ranges         | 2026-03-01 to 2026-03-31            |
| freshness_status    | PASS -- March is fully closed (today is April 3); 3-day lag is sufficient for Bing/SA360 finalization |
| schema_issues       | See below                            |
| qa_issues           | See below                            |
| tables_ready        | Campaign, Ad Group, Keyword, Device (with caveats) |
| blockers            | None critical -- data is usable with documented caveats |

---

## QA Checks

### 1. Date Coverage and Completeness

**Result: PASS**

- Full calendar month requested (2026-03-01 to 2026-03-31).
- Data returned for 1 active campaign across 12 enabled ad groups.
- 49 REMOVED campaigns returned with zero metrics -- expected behavior, not an issue.
- No day-level data was reviewed. If daily granularity is needed downstream, a separate pull should confirm no missing dates.

### 2. Data Freshness

**Result: PASS**

- Today is 2026-04-03. March 2026 ended 3 days ago.
- Bing Ads data in SA360 typically finalizes within 24-48 hours of close.
- 3-day lag provides adequate confidence that March data is fully closed.

### 3. Totals Reconciliation

**Result: WARNING**

Campaign-level totals vs. dimension-level sums:

| Metric      | Campaign Total | Ad Group Sum | Device Sum   | Keyword Sum  |
|-------------|---------------|--------------|--------------|--------------|
| Spend       | $15,939.28    | $15,706.48   | $15,706.48   | $15,674.97   |
| Impressions | 249,963       | --           | 249,958      | 249,586      |
| Clicks      | 29,569        | --           | 29,904       | 29,848       |
| Conversions | 4             | --           | 3            | 3            |

Discrepancies found:

| Issue | Severity | Detail |
|-------|----------|--------|
| Spend gap: campaign vs ad group/device | WARNING | $232.80 delta (1.5%). Likely caused by removed ad groups or SA360 engine-level adjustments not attributed to active ad groups. |
| Spend gap: device vs keyword | INFORMATIONAL | $31.51 delta (0.2%). Minor rounding or keywords not captured in top-N pull. |
| Click mismatch: campaign (29,569) vs device (29,904) | WARNING | Device sum is 335 clicks HIGHER than campaign total. This is anomalous -- dimension sums should not exceed the parent. Possible SA360 cross-device deduplication at campaign level, or a reporting lag artifact. |
| Conversion mismatch: campaign (4) vs device/keyword (3) | WARNING | 1 missing conversion at dimension level. The 4th conversion (Brand_Mexico_LATAM_EXA, 1 conv) may not appear in the device or keyword breakdowns if it was attributed via a different conversion action or lag. |
| Impression gap: campaign vs keyword | INFORMATIONAL | 377 impressions (0.15%) not accounted for in keyword-level data. Minor; likely long-tail keywords outside the pull. |

**Recommendation**: The spend delta of 1.5% between campaign and ad group totals is within acceptable tolerance for SA360 reporting. The click overcounting at device level (335 extra) should be noted in the final report. Use campaign-level totals as the authoritative row for the reporting model; use dimension breakdowns for distribution analysis only.

### 4. Structural / Schema Issues

**Result: WARNING**

| Issue | Severity | Detail |
|-------|----------|--------|
| Conversions API failure | WARNING | PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE error when querying conversion actions. This means we have aggregate conversion counts but no breakdown by conversion type (e.g., lead vs. application). |
| Geo data gap | WARNING | SA360 returned only geo target ID 2484 with zero metrics. This is likely a default/fallback geo target, not actual geo performance data. Bing geo reporting through SA360 may require a different query approach or direct Bing Ads API pull. |
| ROAS = $0.00 | INFORMATIONAL | Revenue is not configured for this account in SA360/Bing. Consistent with the Quantcast note in forex.md that revenue tracking is absent. ROAS should be excluded or shown as N/A in dashboards. |
| Currency | PASS | All values appear in USD. No micros-to-dollars confusion detected (spend values are in standard dollar format with two decimal places). |
| Null fields | PASS | No unexpected nulls reported in the core metrics (spend, impressions, clicks, conversions). |

### 5. Anomaly Flags

| Issue | Severity | Detail |
|-------|----------|--------|
| Extremely high CTR on "trading online" keyword | CRITICAL | 15.8% CTR (16,700 clicks / 106K impressions) on a phrase match keyword is abnormally high for non-brand search. Possible causes: (a) Bing broad/phrase matching to near-exact brand queries, (b) ad serving in low-competition LATAM auctions, (c) invalid click activity. Recommend: pull search terms report for this keyword to validate traffic quality. |
| Mobile CTR 15.02% vs Desktop 3.05% | WARNING | 5x CTR gap between mobile and desktop is unusual. Mobile drives 81.8% of spend but 0 conversions. Desktop drives 18% of spend but 3 of 4 conversions. This may indicate mobile click fraud or extremely poor mobile landing page experience. |
| 4 total conversions on $15,939 spend = $3,985 CPA | INFORMATIONAL | Very high CPA. Not a data quality issue per se, but worth flagging for the analysis agent. This is a performance concern, not a QA concern. |
| "plataforma metatrader" CTR: 13.2% | WARNING | 8,300 clicks on 63K impressions for a phrase match keyword is high. Same pattern as "trading online" -- warrants search terms validation. |
| Brand keywords converting at low CPA | INFORMATIONAL | "forex" exact ($36.65 CPA) and "forex.com" exact ($19.71 CPA) are the only converting keywords. All non-brand spend ($15,846) produced 0 conversions. Not a data issue, but reinforces need for search terms audit. |

### 6. Known Limitations (Documented)

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| No conversion-type breakdown | Cannot distinguish lead types or funnel stages | Flag in report; request SA360 conversion configuration review |
| No geo performance data | Cannot validate Mexico-only targeting | Verify targeting in Bing Ads UI or pull directly from Bing Ads API |
| No search terms data in this pull | Cannot validate keyword match quality | Separate SA360 search terms pull recommended before final report |
| No daily granularity validated | Cannot confirm even delivery across March | Pull daily data if pacing analysis is needed |
| Device click sum exceeds campaign total | Minor inconsistency in click attribution | Use campaign total as authoritative; note in report |

---

## Verdict

**DATA IS FIT FOR REPORTING -- WITH CAVEATS**

The core metrics (spend, impressions, clicks, conversions) at the campaign level are complete and fresh. The data can proceed to the modeling step under these conditions:

1. Use campaign-level totals ($15,939.28 spend, 249,963 impressions, 29,569 clicks, 4 conversions) as the authoritative figures for the Bing Ads channel row in the reporting model.
2. Use ad group, keyword, and device breakdowns for distribution analysis only. Document that dimension-level sums do not perfectly reconcile with campaign totals.
3. Exclude ROAS from the Bing channel (revenue not tracked).
4. Note the geo data gap -- we cannot confirm Mexico-only delivery from this data alone.
5. Flag the high non-brand CTRs (trading online, plataforma metatrader) for search terms validation before the analysis agent draws traffic quality conclusions.
6. The conversions API error means we report aggregate conversions (4) without type breakdown.

### Issues by Severity

- **CRITICAL (1)**: Abnormally high CTR on non-brand phrase match keywords -- needs search terms validation
- **WARNING (5)**: Spend reconciliation gap, click overcounting at device level, conversion mismatch, mobile vs desktop CTR disparity, geo data gap
- **INFORMATIONAL (4)**: Minor impression/spend rounding gaps, ROAS not tracked, high CPA, brand-only conversions
