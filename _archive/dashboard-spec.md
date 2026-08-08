# Dashboard Spec

## Purpose
This document defines the standard dashboard structure for the Marketing Intelligence Hub.

Dashboards should:
- answer business questions quickly
- prioritize decision-driving KPIs
- make trends obvious
- separate overview from diagnostics
- support both client-facing and operator-facing reporting

***

## Dashboard Design Principles

- Put the most important KPIs first.
- Keep the first screen skimmable in under 30 seconds.
- Show trends before granular diagnostics.
- Use comparisons: prior period, target, benchmark, or both.
- Avoid clutter and vanity metrics.
- Match the dashboard to the audience.
- Use filters for deeper exploration without overwhelming the top view.

***

## Standard Dashboard Types

### 1) Executive Overview Dashboard
**Audience:** executives, clients, senior leadership  
**Goal:** show business impact and top-level performance

#### Required Sections
1. KPI scorecards
2. Period-over-period trend charts
3. Channel or campaign contribution view
4. Executive narrative summary
5. Risks / opportunities / action items

#### KPI Scorecards
Include:
- Spend
- Conversions
- CPA / CPL
- Revenue
- ROAS
- Reach
- Frequency when relevant

#### Recommended Charts
- Spend trend
- Conversion trend
- Revenue or ROAS trend
- Channel contribution bar chart
- Campaign leaderboard

***

### 2) Monthly Client Report Dashboard
**Audience:** clients, account managers, strategists  
**Goal:** show monthly performance, context, highlights, and next actions

#### Required Tabs or Sections
1. Summary
2. Performance Trends
3. Campaign Breakdown
4. Audience / Placement / Creative Breakdown
5. Recommendations / Next Steps

#### Summary Tab Must Include
- Top KPI cards
- Executive Summary
- Campaign Analysis
- Campaign Highlights
- Suggested Optimizations
- Next Steps

#### KPI Cards
Default:
- Spend
- Impressions
- Clicks
- CTR
- Conversions
- CPA
- Revenue or ROAS
- Reach / Frequency for display and programmatic

***

### 3) Channel Dashboard
**Audience:** media buyers, channel owners, analysts  
**Goal:** go beyond summary and diagnose what is driving results

#### Required Sections
1. KPI overview
2. Trend diagnostics
3. Dimension breakdowns
4. Optimization opportunities
5. Notes / caveats

#### Dimension Breakdowns
Use as relevant:
- Campaign
- Ad set / ad group
- Ad / creative
- Audience
- Device
- Geography
- Placement
- Publisher
- Format

***

### 4) Programmatic Dashboard
**Audience:** programmatic traders, strategists, clients  
**Goal:** combine performance, quality, and inventory diagnostics

#### Required KPI Blocks
- Spend
- Impressions
- Reach
- Frequency
- CTR
- Conversions
- CPA
- ROAS if available
- Viewability Rate
- Video Completion Rate if video is included

#### Required Diagnostics
- Placement / publisher table
- Inventory quality view
- Viewability trend
- Frequency distribution if available
- Audience segment performance
- Creative / format performance
- Pacing or delivery status

***

## Standard Layout Hierarchy

### Row 1: KPI Cards
Purpose:
- communicate top-line results instantly
- compare against prior period and/or target

Each KPI card should include:
- KPI name
- current value
- comparison value
- delta %
- mini trend sparkline if possible

### Row 2: Trend Charts
Purpose:
- show changes over time
- reveal pacing, spikes, and softening performance

Recommended charts:
- line charts for trends
- small multiples for channel comparison
- stacked bars only when composition matters

### Row 3: Breakdown Tables and Rankings
Purpose:
- identify the drivers behind the top-line metrics

Recommended tables:
- top campaigns
- top audiences
- top placements
- top creatives
- device/geography splits

### Row 4: Narrative / Actions
Purpose:
- turn the dashboard into a decision tool

Include:
- what happened
- why it happened
- what to do next

***

## Filter Standards

All dashboards should support these filters where relevant:
- Date range
- Channel
- Account
- Campaign
- Creative
- Audience
- Device
- Geography
- Placement / publisher
- Objective / funnel stage

Rules:
- Keep default filters obvious
- Use the same date logic across pages
- Do not hide critical caveats inside obscure filters

***

## Comparison Standards

Every major KPI should support at least one comparison:
- vs previous period
- vs target
- vs benchmark
- vs same month last year when useful

Display comparisons consistently:
- absolute delta
- percentage delta
- direction indicator

***

## Chart Selection Rules

### Use line charts for:
- spend over time
- conversion trends
- ROAS trends
- viewability trends

### Use bar charts for:
- campaign ranking
- audience ranking
- placement ranking
- channel contribution

### Use tables for:
- detailed diagnostics
- sortable dimension analysis
- top and bottom performers

### Avoid
- too many pie charts
- 3D charts
- over-stacked visuals
- decorative widgets with no decision value

***

## Dashboard Audience Rules

### Executives / Clients
Show:
- outcomes
- trends
- risks
- actions
Hide or de-emphasize:
- overly granular diagnostics unless they explain a business issue

### Media Buyers / Analysts
Show:
- outcome and efficiency metrics
- delivery diagnostics
- audience / placement / creative details
- optimization clues

***

## Mandatory Notes

Every dashboard should clearly state:
- reporting period
- data freshness
- attribution basis
- currency
- source systems
- known data limitations if present

***

## QA Checklist

Before any dashboard is considered complete, verify:
- KPI definitions match the shared KPI dictionary
- totals reconcile to source data
- date filters work correctly
- comparisons use the correct prior period
- labels are readable
- charts answer a real business question
- no redundant widgets remain
- narrative blocks align with the data shown

***

## Default Programmatic Summary View

Use this default order for a monthly programmatic Summary tab:
1. KPI cards
2. Spend + conversion trend
3. Reach / frequency / viewability snapshot
4. Campaign highlights
5. Inventory or placement quality note
6. Suggested optimizations
7. Next steps

## Output Constraint
Design all dashboards for implementation in Google Sheets first.

***

## Google Sheets Styling Standard

All Google Sheets reports must be formatted using these rules. Apply formatting via the Sheets `batchUpdate` API after writing data.

### Brand Colors

| Name | RGB | Use |
|------|-----|-----|
| Dark Navy | (26, 42, 58) | Title bars, section headers (text or background) |
| Medium Blue | (59, 89, 152) | Table header rows |
| Light Gray | (243, 243, 243) | Alternating row backgrounds |
| White | (255, 255, 255) | Default background |
| Accent Green | (39, 174, 96) | Positive indicators, improvements |
| Accent Red | (231, 76, 60) | Negative indicators, risks |

### Title Bar
- Merge across all used columns in row 1
- Dark Navy background, white text
- Font: Arial, 16pt, bold
- Row height: 50px
- Center-aligned vertically

### Metadata Section (report header fields)
- Light Gray background on all metadata rows
- Column A: bold labels
- Column B: regular weight values
- Column A width: 180px, Column B width: 350px

### Table Headers (KPI tables, performance tables, device tables)
- Medium Blue background, white text
- Font: Arial, 10–11pt, bold
- Freeze header row on Performance and Diagnostics tabs

### Data Rows
- Alternating White / Light Gray backgrounds
- Label columns (A): bold
- Numeric columns: right-aligned
- Font: Arial, 10pt

### Total Rows
- Bold all cells
- Light Gray background
- Top border (solid, dark gray)

### Section Headers (Executive Summary, Campaign Highlights, Optimizations, Next Steps, etc.)
- Font: Arial, 12–13pt, bold
- Text color: Dark Navy
- No background fill
- Merge across all used columns

### Narrative Text (executive summary paragraphs, bullet points, observations)
- Merge across all used columns so text wraps properly
- Wrap text enabled
- Font: Arial, 10pt, regular weight

### Column Widths by Content Type

| Content | Width |
|---------|-------|
| Labels / Field names | 180px |
| Values / Descriptions | 350px |
| Campaign names | 320px |
| Ad set names | 200px |
| Numeric metrics | 100px |
| Long text (Data Notes value column) | 500px |

### Tab-Level Settings

| Tab | Freeze | Gridlines | Hide unused columns |
|-----|--------|-----------|-------------------|
| Summary | Row 1 | Hidden | Yes |
| Performance | Row 1 | Visible | Yes (beyond last data column) |
| Diagnostics | None | Visible | Yes (beyond last data column) |
| Data Notes | None | Hidden | Yes |

### Data Formatting
- **Percentages**: `X.XXX%` for CTR, `XX.XX%` for viewability
- **Currency**: Raw decimal numbers (2 places), not pre-formatted strings
- **Integers**: Impressions, clicks, results, reach — no decimal places
- **Missing values**: Use `—` (em dash) for cost-per-result when results = 0
- **No emojis** in any output

### Global Defaults
- Default font: Arial, 10pt across all tabs
- Hide all columns beyond the last data column on every tab
- Set spreadsheet timezone to match the account timezone
- No decorative elements, 3D charts, or empty widgets

