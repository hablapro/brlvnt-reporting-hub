# Forex — Client Instructions

## Overview
Forex is a programmatic advertising client managed through Quantcast. All reporting must be split by geo/sub-client.

## Sub-Clients

### GGMI (LATAM)
- **Geo**: Mexico
- **Market**: LATAM / Spanish-speaking
- **Quantcast Account**: Forex (ID: 9969644)
- **Campaign naming pattern**: `*GGMI*` or `*ggmi*`
- **Active campaigns (as of March 2026)**:
  - `Forex_GGMI_spanish_conversion_campaign_mx` (CPA goal, paused)
  - `0326_Forex_GGMI_spanish_clicks_campaign_mx` (CPC goal, enabled)
- **Ad set naming pattern**: `*GGMI*` or `*ggmi*`

### GCG (US)
- **Geo**: United States
- **Market**: US / Spanish-speaking
- **Quantcast Account**: Forex (ID: 9969644)
- **Campaign naming pattern**: `*GCG*` or `*gcg*`
- **Active campaigns (as of March 2026)**:
  - `Forex_GCG_spanish_conversion_campaign_us` (CPA goal, paused)
  - `0326_Forex_GCG_spanish_clicks_campaign_us` (CPC goal, enabled)
- **Ad set naming pattern**: `*GCG*` or `*gcg*`
  - GCG runs A/B ad set tests (mscl_A vs mscl_B)

## Reporting Rules

### When user requests a Forex report:
1. Ask: "Is this for GGMI (LATAM), GCG (US), or both?"
2. Always produce separate reports per sub-client — never blend GGMI and GCG into one sheet.
3. Filter Quantcast data by geo (Mexico for GGMI, United States for GCG).
4. Filter campaigns by naming pattern (GGMI or GCG in campaign name).

### Google Sheets output folder:
- Shared Drive folder ID: `1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55`
- Use `supportsAllDrives: true` when moving files to this folder.

### Naming convention:
- `Forex GGMI (LATAM) — [Month Year] [Channel] Report`
- `Forex GCG (US) — [Month Year] [Channel] Report`

## Channels

### Quantcast (Programmatic)

- Status: Active, MCP-connected
- Account ID: 9969644
- Campaign filter: `*GGMI*` for LATAM, `*GCG*` for US
- Geo filter: Mexico (GGMI), United States (GCG)

### Meta (Facebook/Instagram)

- Status: Active, MCP-connected
- Account: `FOREX.com_LATAM&US-Hispanic_Berelvant` (act_1699453997689551)
- Single account manages both GGMI and GCG campaigns
- Campaign filter: `*GGMI*` for LATAM, `*GCG*` for US
- Conversion events: `StartApplication`, `SubmittedApplication` (fb_pixel_custom)
- Attribution: Meta default (7-day click, 1-day view)
- Click metric: Use link clicks, not total clicks (Meta "clicks" includes post engagement)

### Bing Ads (via SA360)

- Status: Active, MCP-connected via SA360
- SA360 Manager ID: 6708988927 (FOREX.com LATAM)
- SA360 Account ID: 3332505241 (Forex.com LATAM Bing)
- Engine: Microsoft Bing Ads
- Sub-client: GGMI only (no GCG Bing account found)
- Active campaign: `FX_LATAM_spanish_AO_GEN_policytest_v2_brlvnt`
- Bidding: Manual CPC
- Conversion tracking: SA360 Floodlight / Bing UET
- Revenue tracking: Not configured (ROAS unavailable)
- Geo data: Not available via SA360 API for this account
- Note: Second SA360 manager (7324418878) exists but is not accessible (permission denied)

### Google Ads

- Status: TBD

## Known Data Notes

- Revenue tracking is not configured in Quantcast for this account. ROAS will show 0.
- All Quantcast conversions observed to date are view-through. Zero click-through conversions may indicate a tracking issue.
- Meta conversion events are StartApplication and SubmittedApplication (fb_pixel_custom).
- Currency: USD for both sub-clients.
- Timezone: America/New_York.
