# GGMI Bing July 2026 workbook builder

Rebuilds `reports/forex/ggmi/2026-07/data/GGMI-Bing-July-2026-data.xlsx` (10 tabs).

Run from the repo root: `python3 tools/forex-july-2026-ggmi-bing/build_bing_workbook.py`

**Caveat:** figures are embedded literals captured from the 2026-08-04 pull, not a
live re-query — this reproduces the workbook, it does not refresh the data. The
keyword and search-query tabs read two MCP result files from that session's
scratchpad (paths at the top of the script); if those are gone, re-pull:

- `bing_ads_keyword_performance` acct 31003116, 2026-07-01 to 2026-07-31
- `bing_ads_search_term_report` acct 31003116, 2026-07-25 to 2026-08-04, **no campaign filter**
  (the `campaign_ids` param is silently ignored — see `KNOWN-BUGS.md`)

Conversions come from SA360 (customer 5372690580 / login 9697709980), never from
the Bing API, which reads zero for GGMI's offline-imported goals.
