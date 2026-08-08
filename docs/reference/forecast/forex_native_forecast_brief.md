
# FOREX.com Native Advertising Forecast Brief (US Hispanic & LATAM)

## Purpose

This document defines how an internal agent should build a forecast for native advertising campaigns for FOREX.com targeting U.S. Hispanic and LATAM audiences, using existing display data as the baseline and applying industry-based multipliers for native formats.[cite:52][cite:60] It includes the agent prompt, multiplier assumptions, and an example forecast table structure.

## Agent prompt

Use or adapt the following prompt for the agent that has access to FOREX.com display performance data and web analytics:

```text
Build a 3-month scenario-based forecast model for native advertising campaigns for FOREX.com targeting:
1) U.S. Hispanic audiences
2) LATAM audiences (aggregate or key countries as available)

Context:
- We DO have historical display data (CPC, CTR, CVR) by region for similar forex campaigns.
- We do NOT have direct historical native data for these segments.
- Native will run on open-web/native networks (in-feed/recommendation widgets), with content-led creatives.
- Monthly planning budgets to model initially: 35,000 USD, 40,000 USD, and 45,000 USD (can be adjusted later).

Objectives:
- Use existing display performance as the baseline.
- Apply industry-standard multipliers to estimate native CPC, CTR, and conversion rates for US Hispanic and LATAM.
- Produce Conservative, Expected, and Aggressive scenarios for each region and budget level.
- Forecast impressions, clicks, landings, registrations, funded accounts, and cost per funded account.

Data ingestion instructions:
1) From display campaigns (per region: US Hispanic, LATAM):
   - Pull: CPC_display, CTR_display, CVR_display(click→registration), CVR_display(registration→funded or best available proxy).
   - Use at least 90 days of recent data where possible, focusing on forex/CFD trading campaigns.
2) From site / analytics (optional but recommended):
   - Compare engagement metrics (bounce rate, time on page, pages per session) for traffic from content-like placements vs standard banners.

Assumption logic:
- Native vs display multipliers should be applied as follows (unless overridden by live account data):

  US Hispanic native:
  - CTR_native:
    * Conservative: 1.2 × CTR_display
    * Expected: 1.5 × CTR_display
    * Aggressive: 2.0 × CTR_display
  - CPC_native:
    * Conservative: 1.3 × CPC_display
    * Expected: 1.2 × CPC_display
    * Aggressive: 1.0 × CPC_display
  - CVR_native (click→registration):
    * Conservative: 1.0 × CVR_display
    * Expected: 1.15 × CVR_display
    * Aggressive: 1.3 × CVR_display
  - CVR_native (registration→funded):
    * Same as current display/regional funnel (no uplift unless there is evidence).

  LATAM native:
  - CTR_native:
    * Conservative: 1.2 × CTR_display
    * Expected: 1.5 × CTR_display
    * Aggressive: 2.0 × CTR_display
  - CPC_native:
    * Conservative: 1.0 × CPC_display
    * Expected: 0.9 × CPC_display
    * Aggressive: 0.7–0.8 × CPC_display
  - CVR_native (click→registration): same pattern as US Hispanic (1.0 / 1.15 / 1.3 × CVR_display).
  - CVR_native (registration→funded): use existing regional funnel without uplift.

- These multipliers reflect that native formats typically deliver higher engagement and CTR than standard display, sometimes at similar or slightly higher CPC in premium US inventory, and often at lower CPC in LATAM Spanish inventory.[cite:52][cite:57][cite:60][cite:40][cite:56]

Forecast calculations:
For each region, month, and scenario, compute:
- Clicks = Budget / CPC_native
- Landings = Clicks (or adjust by a content-read factor if available)
- Registrations = Clicks × CVR_native(click→registration)
- Funded accounts = Registrations × CVR_native(registration→funded)
- CPA funded = Budget / Funded accounts
- Impressions = Clicks / CTR_native

Output requirements:
- For each budget level (35k, 40k, 45k), and for each region (US Hispanic, LATAM), output a table with Conservative, Expected, and Aggressive scenarios.
- Include an assumptions section documenting:
  * Display metrics used as baselines.
  * Native multipliers applied.
  * Any overrides based on actual account/native data or analytics.
- Flag data quality gaps (e.g., missing funded-account tracking, unreliable regional splits).

Label this model explicitly as an assumption-based forecast to be recalibrated after 4–6 weeks of live native performance.
```

## Industry rationale for multipliers

- Native formats (in-feed, recommendation widgets, sponsored content) make up a large and growing share of digital display spend because they consistently outperform banners on CTR and engagement.[cite:52][cite:60] 
- Benchmarks suggest native ads often achieve significantly higher click-through rates than standard banners, while landing-page conversion rates for high-intent campaigns tend to fall in mid-single to high-single digits, with strong programs going higher.[cite:60]
- Open-web native pricing varies by network and vertical, but typical CPC ranges of roughly 0.10–2.00 USD and CPM ranges of roughly 3–7+ USD are commonly quoted, with finance and premium audiences at the higher end.[cite:57][cite:60]
- Spanish CPCs in many Latin American markets tend to be lower than in Spain or the U.S. due to competition and pricing differences, with U.S. Hispanic inventory priced more like premium U.S. placements.[cite:40]
- Native is particularly suited to finance because it allows educational content and longer-form explanations, which can pre-qualify users and improve lead quality, though the final funding decision is still driven by funnel and product rather than the ad format alone.[cite:59][cite:62]

These points justify:
- CTR multipliers greater than 1.0 for native vs display.
- Slightly higher or similar CPC for US Hispanic native vs display, and lower CPC for LATAM native.
- Modest positive adjustments (0–30%) to click→registration conversion rates for well-localized, content-led native traffic, while keeping registration→funded conversion unchanged unless proven otherwise.[cite:52][cite:57][cite:60][cite:62]

## Example forecast structure (illustrative)

The following example assumes that the agent has already computed native CPC, CTR, and CVRs from display baselines and multipliers. Numbers here are placeholders for structure only and should be replaced by the agent with real inputs and computed outputs.

### Example: US Hispanic native, July (budget 40,000 USD)

| Scenario      | CPC_native (USD) | CTR_native | Clicks | Impressions | Registrations | Funded accounts | CPA funded (USD) |
|--------------|-----------------:|-----------:|-------:|------------:|--------------:|----------------:|-----------------:|
| Conservative | 2.40             | 1.20 × CTR_display | 16,667 | 16,667 / (1.20 × CTR_display) | 16,667 × (1.0 × CVR_display_c2r) | Reg × CVR_display_r2f | 40,000 ÷ Funded |
| Expected     | 2.20             | 1.50 × CTR_display | 18,182 | 18,182 / (1.50 × CTR_display) | 18,182 × (1.15 × CVR_display_c2r) | Reg × CVR_display_r2f | 40,000 ÷ Funded |
| Aggressive   | 2.00             | 2.00 × CTR_display | 20,000 | 20,000 / (2.00 × CTR_display) | 20,000 × (1.30 × CVR_display_c2r) | Reg × CVR_display_r2f | 40,000 ÷ Funded |

Where:
- `CTR_display`, `CVR_display_c2r`, and `CVR_display_r2f` are already known from display and are region-specific.
- The agent should resolve the formulas and output actual numeric values once baselines are loaded.

### Example: LATAM native, August (budget 45,000 USD)

| Scenario      | CPC_native (USD) | CTR_native | Clicks | Impressions | Registrations | Funded accounts | CPA funded (USD) |
|--------------|-----------------:|-----------:|-------:|------------:|--------------:|----------------:|-----------------:|
| Conservative | 1.00 × CPC_display | 1.20 × CTR_display | 45,000 ÷ (1.00 × CPC_display) | Clicks / (1.20 × CTR_display) | Clicks × (1.0 × CVR_display_c2r) | Reg × CVR_display_r2f | 45,000 ÷ Funded |
| Expected     | 0.90 × CPC_display | 1.50 × CTR_display | 45,000 ÷ (0.90 × CPC_display) | Clicks / (1.50 × CTR_display) | Clicks × (1.15 × CVR_display_c2r) | Reg × CVR_display_r2f | 45,000 ÷ Funded |
| Aggressive   | 0.75 × CPC_display | 2.00 × CTR_display | 45,000 ÷ (0.75 × CPC_display) | Clicks / (2.00 × CTR_display) | Clicks × (1.30 × CVR_display_c2r) | Reg × CVR_display_r2f | 45,000 ÷ Funded |

This structure ensures every forecasted value is a transparent function of known display baselines and clearly documented native multipliers.
