# Quantcast → Shared KPI Field Mapping

## Purpose
Maps Quantcast MCP metric and breakdown names to the shared KPI dictionary.
Used by the data-modeling agent to normalize Quantcast data into the reporting model.

***

## Metric Mapping

### Core Reporting Metrics (use in all reports)

| Quantcast Metric | Shared KPI | Notes |
|---|---|---|
| Budget Delivered | Spend | Primary spend metric. Do not use "Total Budget Delivered" unless non-billable delivery is intentionally included. |
| Impressions | Impressions | Direct map. |
| Clicks (Advanced IVT) | Clicks | Use Advanced IVT as the default click metric (Quantcast's filtered version). Preserve "Clicks (General IVT)" as a diagnostic if needed. |
| CTR | CTR | Formula: Clicks (Advanced IVT) / Impressions. Direct map. |
| CPM | CPM | Formula: Budget Delivered / Impressions * 1000. Direct map. |
| Device Reach | Reach | Quantcast reports device-level reach, not person-level. Document this distinction. |
| Device Frequency | Frequency | Impressions per device. Direct map. |
| Household Reach | Reach (Household) | Preserve as a separate metric. Do not blend with Device Reach. |
| Household Frequency | Frequency (Household) | Preserve as a separate metric. |
| Results | Conversions | Sum of Click Results + View Results. Specify attribution type in Data Notes. |
| Click Results | Conversions (Click-through) | Preserve as a breakdown of total conversions. |
| View Results | Conversions (View-through) | Preserve as a breakdown of total conversions. |
| Cost Per Result | CPA | Formula: Budget Delivered / Results. Direct map. |
| Revenue | Revenue | Direct map. |
| ROAS | ROAS | Formula: Revenue / Budget Delivered. Direct map. |
| Viewability | Viewability Rate | Formula: Viewable Impressions / Measured Impressions. Direct map. |
| Viewable Impressions | Viewable Impressions | Supporting metric for Viewability Rate. |
| Measured Impressions | Measured Impressions | Supporting metric for Viewability Rate. |

### Video Metrics (include when video campaigns are present)

| Quantcast Metric | Shared KPI | Notes |
|---|---|---|
| 100% Completion Rate | Video Completion Rate | Direct map. This is the primary VCR metric. |
| 25% Completion Rate | Video 25% Rate | Diagnostic only. |
| 50% Completion Rate | Video 50% Rate | Diagnostic only. |
| 75% Completion Rate | Video 75% Rate | Diagnostic only. |
| Completed Views | Completed Video Views | Supporting metric for VCR. |
| CPCV | Cost Per Completed View | Formula: Budget Delivered (Video) / Completed Views. |
| Completed Views (Audible & Visible) | Completed Views (A&V) | Quality-filtered version. Preserve separately. |
| 100% Completion Rate (Audible & Visible) | VCR (Audible & Visible) | Quality-filtered version. Preserve separately. |

### Audio Metrics (include when audio campaigns are present)

| Quantcast Metric | Shared KPI | Notes |
|---|---|---|
| 100% Listen Through Rate | Audio Completion Rate | Direct map. |
| Completed Listens | Completed Audio Listens | Supporting metric. |
| CPCL | Cost Per Completed Listen | Formula: Budget Delivered (Audio) / Completed Listens. |

### Fee Metrics (operational, not client-facing)

| Quantcast Metric | Shared KPI | Notes |
|---|---|---|
| Ad External Fees | External Fees | Third-party vendor fees. Operational only. |
| Ad Agency Fees | Agency Fees | Agency margin. Operational only. |
| Survey Spend | Survey Spend | Brand Lift Live cost. Operational only. |

### Third-Party Metrics (use for verification, not primary reporting)

| Quantcast Metric | Shared KPI | Notes |
|---|---|---|
| Third Party Impressions | 3P Impressions | Use for discrepancy analysis only. |
| Third Party Clicks | 3P Clicks | Use for discrepancy analysis only. |
| Third Party Results | 3P Conversions | Use for discrepancy analysis only. |
| Third Party Viewability | 3P Viewability | Use for discrepancy analysis only. |
| Third Party Revenue | 3P Revenue | Use for discrepancy analysis only. |
| Impression Variance | Impression Variance | QC vs 3P discrepancy %. Diagnostic. |
| Attribution Ratio | Attribution Ratio | QC vs 3P conversion ratio. Diagnostic. |

### Estimated Metrics (exclude from primary reporting)

QC Estimated metrics (QC Estimated Budget Delivered, QC Estimated CPM, etc.) are Quantcast's modeled estimates. Do not use as primary reporting metrics. Include only when explicitly requested for directional analysis.

***

## Breakdown Mapping

### Hierarchy (Level breakdowns)

| Quantcast Breakdown | Report Dimension | Notes |
|---|---|---|
| Account Name / ID | Account | Top level. |
| Campaign Name / ID | Campaign | Primary grouping for performance tables. |
| Ad Set Name / ID | Ad Set | Secondary grouping. |
| Creative Name / ID | Creative | Granular creative-level analysis. |

### Time Breakdowns

| Quantcast Breakdown | Report Dimension | Notes |
|---|---|---|
| Day | Date (Daily) | Use for trend charts and pacing. |
| Week | Date (Weekly) | Use for weekly summaries. |
| Month | Date (Monthly) | Use for MoM comparisons. |

### Demographic Breakdowns

| Quantcast Breakdown | Report Dimension | Notes |
|---|---|---|
| Age | Age Range | Diagnostic. |
| Gender | Gender | Diagnostic. |
| Income | Household Income | Diagnostic. |
| Education | Education Level | Diagnostic. |
| Ethnicity | Ethnicity | Diagnostic. Use with care in reporting. |
| Household Children | Has Children | Diagnostic. |

### Geographic Breakdowns

| Quantcast Breakdown | Report Dimension | Notes |
|---|---|---|
| Country/Territory | Country | Use for geo performance tables. |
| Region | State/Region | Diagnostic. |
| Metro Area | DMA / Metro | Diagnostic. |
| City | City | Granular only when relevant. |
| Postal Code | Zip Code | Granular only when relevant. |

### Delivery Breakdowns

| Quantcast Breakdown | Report Dimension | Notes |
|---|---|---|
| Device Type | Device | Mobile, Desktop, Tablet, CTV. |
| Channel | Ad Channel | Display, Native, Video, CTV, Audio. |
| Domain/App | Publisher / Placement | Critical for inventory quality analysis. |
| Exchange | SSP / Exchange | Supply-path diagnostics. |
| Environment | Environment | Browser vs In-App. |
| Targeting Type | Targeting Type | Prospecting vs Retargeting. |
| Deal ID / Deal Name | Deal | PMP/PG diagnostics. |

***

## Default Metric Set for Monthly Quantcast Report

### Summary Tab
Spend, Impressions, Clicks, CTR, CPM, Device Reach, Device Frequency, Results, Cost Per Result, Revenue, ROAS, Viewability

### Performance Tab
Breakdowns: Campaign Name, Ad Set Name
Metrics: Spend, Impressions, Clicks, CTR, CPM, Device Reach, Device Frequency, Results, Cost Per Result, Revenue, ROAS

### Diagnostics Tab
Breakdowns: Domain/App, Exchange, Device Type, Channel, Targeting Type
Metrics: Impressions, Spend, Viewability, Viewable Impressions, Device Frequency, Results, Cost Per Result
Video (if applicable): 100% Completion Rate, Completed Views, CPCV
