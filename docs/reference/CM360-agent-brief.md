# CM360 Agent Brief — FOREX.com (Berelvant)

Orientation for the agent working in Campaign Manager 360 on the FOREX.com account. Reporting currency is USD, timezone America/New_York.

## The players
- **Berelvant (us):** US-based marketing execution and performance growth partner for enterprise companies in regulated, multi-market environments. We run FOREX.com's paid media, analytics, tracking, and the CM360 / Floodlight measurement layer.
- **FOREX.com (the client):** Regulated US forex and CFD broker, owned by StoneX Group (NASDAQ: SNEX), formerly GAIN Capital. CFTC/NFA regulated, 20+ years in the US, a top US FX broker by client assets. The product is online trading accounts (MT5, TradingView, web and mobile). We market account sign-ups, not e-commerce.
- **GGMI (sub-client):** Gain Global Markets Inc — FOREX.com's LATAM / Mexico business. Spanish-language, Mexico as the priority market.
- **GCG (sub-client):** GAIN Capital Group, LLC — FOREX.com's US Hispanic business. Spanish-language, targeting Hispanic traders inside the United States.

## CM360 access and scope
Connected via the CM360 MCP server (authenticated, X-API-Key).

- **Profile:** `10604084` (user `adops_berelvant`)
- **Account:** `5877` — TP - City Index - PER - DCM - UK

**Advertisers in scope — only these two:**

| Advertiser | ID | Floodlight Config ID |
|---|---|---|
| GCG US Spanish | `16576650` | `16576650` |
| GGMI - FOREX.com LATAM | `16624558` | `16624558` |

Default all CM360 operations (campaigns, placements, trafficking QA, reports, tags) to these two advertiser IDs. The profile lists other advertisers (FOREX.com LATAM `11137225`, GCG - US Hispanic `16085389`, GGMI Spanish `16576647`, plus more on later pages) — ignore them unless told otherwise. Keep GCG and GGMI separate; do not blend their reporting or conversions.

## Regions and language
| Sub-client | Market | Language | Geo targeting |
|---|---|---|---|
| **GGMI** | Mexico (priority) / LATAM | Spanish | Mexico, presence-only |
| **GCG** | United States, Hispanic | Spanish (US) | Priority states: CA, TX, FL, NY/NJ, IL, AZ |

Keep the two separate in CM360. Different entities, regions, audiences. Do not blend their reporting or their conversions.

## The funnel (what we sell)
Application start → **submitted application** → funded account → first trade. A demo-account signup sits at the top of some tracks.

## KPIs and conversion events
- **Primary KPI: submitted application**, and CPA per submitted application. Funded accounts are the downstream value and the strongest secondary signal.
- **Floodlight / conversion events to track and keep clean:** application start, submitted application, funded account. Tag both sub-clients consistently and de-duplicate against the platform pixels and GA4.
- **Standard media metrics:** spend, impressions, clicks, CTR, CPC, CPM, conversions (submitted apps), CPA, viewability (display/programmatic), GA4 sessions.
- **GCG approved targets (from the Q2 brief):** CPL (demo) under $50, cost per funded under $350, demo→funded over 10%, funded→traded over 60%.

## Channels feeding measurement
- **GGMI:** Microsoft/Bing search (read via SA360), Meta, Azerion (programmatic display), Quantcast (programmatic display).
- **GCG:** Google Ads search, Meta, Azerion, Quantcast.

## Measurement rules to respect
- **Do not sum conversions across channels.** Each platform measures a different event. The common denominator is the submitted application.
- **Meta "conversions" are mostly application starts, not submissions.** Separate StartApplication from SubmittedApplication, and judge Meta on submitted apps and GA4 sessions, not link clicks or landing-page views.
- **Platform clicks and landing-page views overstate real arrivals** (Meta in-app browser, display invalid traffic). Reconcile against GA4 sessions before trusting volume.
- **Quantcast results are mostly view-through.** Treat them as directional, not equal to click-based submissions.
- **Bing conversions are offline-imported** (live-account confirmations) and read in SA360, not in native Bing reporting.
- Current priority: close the measurement gaps so every channel reports a clean submitted-application number per region. That is the north star for the CM360 work.
