# Marketing Intelligence Hub

## Purpose
This repository powers a multi-agent marketing intelligence system for:
- Pulling paid media performance data
- Validating and normalizing source data
- Building dashboards
- Producing campaign analysis and client-ready reporting

Primary channels:
- Meta
- Google Ads
- Bing Ads
- SA360 (cross-engine search)
- Programmatic / Display

## Data Source Rule
Primary source data comes from MCP tools, not manual exports.

Current MCP sources include:
- SA360 (configured in `.mcp.json`)
- Google Ads
- Meta
- Google Analytics
- Google Search Console
- Quantcast (field mapping in `mappings/quantcast-field-mapping.md`)

Use MCP tools first for data retrieval whenever available.
Use Google Sheets as the reporting, modeling, dashboard, and monthly-report output layer.
Do not assume raw CSV exports are the default input if an MCP source exists.


## Core Rule
Always use a shared reporting model before generating dashboards or analysis.

Do not:
- Build dashboards directly from messy raw exports when modeled data exists
- Write strategic commentary before QA is complete
- Allow one channel specialist to redefine global KPI logic

## Workflow Order
1. Clarify the request
2. Pull source data
3. Run QA
4. Normalize/model data
5. Run channel analysis
6. Build dashboard outputs
7. Generate narrative reporting
8. Flag blockers before final delivery

## Shared KPI Set
Use standardized definitions when possible for:
- Spend
- Impressions
- Clicks
- CTR
- CPC
- CPM
- Conversions
- CPA
- CPL
- Revenue
- ROAS
- Reach
- Frequency
- Viewability
- Video completion rate

If a platform metric differs from the shared definition:
- preserve the source metric
- document the difference
- do not silently remap it

## Reporting Rules
- Separate facts, interpretations, and recommendations
- Surface anomalies and data quality issues explicitly
- Keep dashboards decision-oriented
- Keep executive summaries concise and client-friendly
- Tie every recommendation to validated performance data

## Agent Routing
Use specialist agents for:
- orchestration
- data ingestion and QA
- data modeling
- dashboard building
- Meta analysis
- Google Ads analysis
- Bing Ads analysis
- SA360 analysis
- Programmatic analysis
- narrative reporting

If a request is cross-channel, the orchestrator must assemble the final output.

## Repo Conventions
- Reuse shared metric definitions
- Avoid duplicated transformation logic
- Prefer mapping tables over hardcoded assumptions
- Document taxonomy and KPI changes
- Keep prompts modular and easy to audit

## Output Format Rule
This project is Google Sheets-first.

All dashboard planning, KPI mapping, monthly report structure, and reporting templates should be designed for implementation in Google Sheets.

Preferred deliverables:
- Google Sheets tab structures
- sheet-ready tables
- formulas compatible with Google Sheets
- export-friendly layouts for PDF sharing
- optional Looker Studio connections using Google Sheets as a source

Do not default to Excel unless explicitly requested.
If spreadsheet files are generated locally, structure them so they can be uploaded to Google Sheets without redesign.
