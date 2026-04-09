# KPI Dictionary

## Purpose
This file defines the shared KPI language for the Marketing Intelligence Hub.

Use these definitions across:
- dashboards
- channel analysis
- executive summaries
- monthly reports
- optimization recommendations

If a platform-specific metric differs from the shared definition:
1. Preserve the source-platform metric
2. Document the difference
3. Do not silently remap it

***

## Global Rules

- Always label the reporting window clearly: daily, weekly, MTD, monthly, QTD, or custom.
- Always define attribution assumptions when reporting conversions, revenue, CPA, or ROAS.
- Always distinguish between source-platform metrics and normalized reporting metrics.
- Use the same currency across the report.
- For cross-channel views, only compare metrics that are truly comparable.

***

## KPI Categories

### 1) Delivery KPIs

#### Spend
**Definition:** Total media cost incurred during the reporting period.  
**Formula:** Sum of media spend.  
**Use when:** Measuring budget pacing, efficiency, and scale.  
**Notes:** Must use a consistent currency.

#### Impressions
**Definition:** Total number of ad impressions served.  
**Formula:** Sum of impressions.  
**Use when:** Measuring delivery volume and exposure.  
**Notes:** High impressions alone do not indicate effectiveness.

#### Reach
**Definition:** Estimated number of unique users exposed to the campaign.  
**Formula:** Platform-defined unique reach.  
**Use when:** Measuring breadth of audience delivery.  
**Notes:** Not always perfectly comparable across channels.

#### Frequency
**Definition:** Average number of times each reached user saw an ad.  
**Formula:** Impressions / Reach  
**Use when:** Monitoring saturation, overexposure, and pacing quality.  
**Notes:** Especially important for display and programmatic.

***

### 2) Engagement KPIs

#### Clicks
**Definition:** Total number of ad clicks during the reporting period.  
**Formula:** Sum of clicks.  
**Use when:** Measuring traffic generation and engagement.

#### CTR
**Definition:** Click-through rate.  
**Formula:** Clicks / Impressions  
**Use when:** Measuring engagement efficiency.  
**Notes:** Should always be interpreted alongside channel type, audience, and creative format.

#### CPC
**Definition:** Cost per click.  
**Formula:** Spend / Clicks  
**Use when:** Measuring traffic acquisition efficiency.

#### Landing Page View Rate
**Definition:** Percentage of clicks that result in a landing page load or equivalent validated session.  
**Formula:** Landing Page Views / Clicks  
**Use when:** Diagnosing post-click friction.  
**Notes:** Availability depends on platform and analytics integration.

***

### 3) Conversion KPIs

#### Conversions
**Definition:** Number of desired actions completed during the reporting period.  
**Formula:** Sum of attributed conversion events.  
**Use when:** Measuring outcome volume.  
**Notes:** Must specify conversion event and attribution source.

#### Conversion Rate
**Definition:** Rate at which clicks or visits become conversions.  
**Formula:** Conversions / Clicks or Conversions / Sessions  
**Use when:** Measuring traffic quality and landing page effectiveness.  
**Notes:** Always specify denominator.

#### CPA
**Definition:** Cost per acquisition or cost per conversion.  
**Formula:** Spend / Conversions  
**Use when:** Measuring outcome efficiency.  
**Notes:** Must reflect the same conversion definition used in the report.

#### CPL
**Definition:** Cost per lead.  
**Formula:** Spend / Leads  
**Use when:** Lead generation reporting only.  
**Notes:** Do not use interchangeably with CPA unless the conversion is a lead.

***

### 4) Revenue KPIs

#### Revenue
**Definition:** Total attributed revenue generated during the reporting period.  
**Formula:** Sum of attributed revenue.  
**Use when:** Measuring business impact.  
**Notes:** Must identify attribution source and window.

#### ROAS
**Definition:** Return on ad spend.  
**Formula:** Revenue / Spend  
**Use when:** Measuring revenue efficiency.  
**Notes:** Only meaningful when revenue attribution is reliable.

#### MER
**Definition:** Marketing efficiency ratio.  
**Formula:** Total Revenue / Total Marketing Spend  
**Use when:** High-level blended efficiency analysis.  
**Notes:** Use only when full-funnel or blended-spend logic is intentionally applied.

***

### 5) Quality KPIs

#### Viewability Rate
**Definition:** Percentage of measurable impressions that were viewable.  
**Formula:** Viewable Impressions / Measurable Impressions  
**Use when:** Evaluating display/programmatic inventory quality.  
**Notes:** Critical for programmatic and video display analysis.

#### Video Completion Rate
**Definition:** Percentage of video impressions that completed playback.  
**Formula:** Completed Views / Video Starts  
**Use when:** Evaluating video engagement quality.  
**Notes:** Especially useful for upper-funnel video campaigns.

#### Invalid Traffic Rate
**Definition:** Share of traffic or impressions identified as invalid or fraudulent.  
**Formula:** Invalid Traffic / Total Traffic or Impressions  
**Use when:** Diagnosing inventory risk and traffic quality.  
**Notes:** Depends on platform and verification vendor.

#### Bounce Rate
**Definition:** Percentage of sessions that leave without meaningful engagement.  
**Formula:** Platform-defined bounce logic  
**Use when:** Diagnosing post-click traffic quality.  
**Notes:** Use analytics-source definitions consistently.

***

### 6) Search-Specific KPIs

#### Impression Share
**Definition:** Percentage of eligible impressions actually received.  
**Formula:** Impressions / Eligible Impressions  
**Use when:** Measuring search demand capture and competitive coverage.

#### Top Impression Share
**Definition:** Percentage of impressions served in top positions.  
**Formula:** Platform-defined  
**Use when:** Measuring visibility quality in paid search.

#### Search Lost IS (Budget)
**Definition:** Impression share lost due to budget constraints.  
**Use when:** Diagnosing underdelivery caused by budget caps.

#### Search Lost IS (Rank)
**Definition:** Impression share lost due to ad rank limitations.  
**Use when:** Diagnosing underdelivery caused by bid or quality issues.

***

### 7) Meta-Specific Diagnostic KPIs

#### CPM
**Definition:** Cost per 1,000 impressions.  
**Formula:** Spend / Impressions * 1000  
**Use when:** Measuring delivery cost efficiency.

#### Hook Rate
**Definition:** Early-stage creative engagement indicator, usually based on 3-second views or equivalent early attention signal.  
**Use when:** Diagnosing creative stopping power.  
**Notes:** Definition may vary by reporting stack.

#### Thumbstop / Attention Metric
**Definition:** A proxy metric for whether creative captured initial attention.  
**Use when:** Creative analysis on social/video-heavy campaigns.  
**Notes:** Use only if clearly defined in your data model.

***

### 8) Programmatic-Specific KPIs

#### eCPM
**Definition:** Effective cost per 1,000 impressions.  
**Formula:** Spend / Impressions * 1000  
**Use when:** Measuring display buying efficiency.

#### Completion Rate
**Definition:** See Video Completion Rate.  
**Use when:** Video programmatic reporting.

#### Fill Rate
**Definition:** Percentage of ad requests filled with an impression.  
**Use when:** Publisher or ad-serving diagnostics.  
**Notes:** Only include when relevant to the supply setup.

#### Win Rate
**Definition:** Share of bid requests won.  
**Formula:** Auctions Won / Bid Requests  
**Use when:** Diagnosing bidding competitiveness in programmatic buying.

***

## Comparison Rules

### Safe Cross-Channel Comparison
Use for:
- Spend
- Impressions
- Clicks
- CTR
- Conversions
- CPA
- Revenue
- ROAS

### Compare With Caution
Use with definitions clearly labeled:
- Reach
- Frequency
- Conversion Rate
- Viewability
- Video Completion Rate

### Do Not Blend Casually
Do not blend without explicit notes:
- Attribution-window-based conversion metrics from different platforms
- Platform-estimated reach across multiple walled gardens
- Platform-native engagement metrics with different definitions
- Assisted revenue and click-through revenue unless defined consistently

***

## Reporting Labels

Every KPI shown in a dashboard or monthly report should have:
- Display name
- Definition
- Formula
- Source system
- Reporting window
- Comparison basis: MoM, WoW, QoQ, YoY, target, or benchmark
- Owner or analyst note when appropriate

***

## Mandatory Narrative Questions

For each major KPI block, analysis should answer:
1. What happened?
2. Why did it happen?
3. Does it matter?
4. What action should be taken?

***

## Default Priority by Dashboard Type

### Executive Dashboard
Prioritize:
- Spend
- Conversions
- CPA / CPL
- Revenue
- ROAS
- Reach
- Trend vs prior period

### Channel Dashboard
Prioritize:
- Core delivery
- Efficiency
- Outcome
- Diagnostic quality metrics

### Programmatic Dashboard
Prioritize:
- Spend
- Impressions
- Reach
- Frequency
- CTR
- Conversions
- CPA
- Viewability
- Completion Rate
- Placement / inventory quality

### Search Dashboard
Prioritize:
- Spend
- Clicks
- CTR
- CPC
- Conversions
- CPA
- ROAS
- Impression Share
