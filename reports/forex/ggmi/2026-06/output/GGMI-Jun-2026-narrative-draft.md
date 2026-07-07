# GGMI (Mexico) — June 2026 Performance Narrative — DRAFT for deck build (v2)

Internal draft, pending Renzo review before any client formatting. Facts from `../model/GGMI-Jun-2026-cross-channel-model.xlsx`, `../qa/qa-and-model.md`, and `../qa/ga4-deep-dive.md` (GA4 + GSC deep dive, 2026-07-07). Client-facing rules applied: no vendor or competitor names in commentary, Meta conversions held, raw Azerion spend. v2 adds the GSC-confirmed organic findings, the resolved February traffic spike, and the Meta inventory-quality evidence.

## Executive summary

June was GGMI's biggest media month of 2026: $119,922 invested across four channels, up 56% from May, delivering 69.9M impressions and 449.8K clicks. Application volume followed the spend. Search produced 50 submitted applications at $513 each (up from 33 in May), and programmatic display added 42 at $823, holding efficiency through a 27% budget increase.

Site traffic recovered with the spend: 9,236 Mexico sessions (+61% vs May) and 5,838 unique visitors (+125%). The recovery is real but bought. Media drove essentially all of the June gain while organic search sat at its low.

Three findings shape the July plan. First, search delivery outside Mexico (49% of June search spend) remains the top efficiency lever; remediation is defined and partially applied. Second, organic search has fallen 75% since January, confirmed independently in Search Console, for identifiable SEO reasons; no media budget fixes this, and it is why total site traffic feels flat while investment grows. Third, paid social click quality degraded sharply as that channel scaled; its conversion reporting stays on hold until the placement audit completes.

## Channel detail

### Search (Bing) — $25,659, 50 submitted applications, $513 CPA
- Spend +61% MoM across 3 campaigns (was 1); conversions +52%, so efficiency held through the scale-up ($484 → $513 CPA).
- CPC rose $0.53 → $1.19 with the shift into new campaign themes; CTR 4.6%.
- Geo: 51% of June spend served Mexico. The remaining 49% ($12,637) served out-of-market users, and site analytics show the scale of it: out-of-market paid visitors outnumbered Mexican paid visitors on the site for most of H1. The June 3 exclusion is already working; completing the Mexico presence-only restriction is optimization #1 and should improve effective MX CPA immediately.

### Meta — $25,924, awareness-to-traffic engine with a quality problem
- Spend +291% MoM, 19.8M impressions, 407K link clicks, 250K platform-reported landing-page views. 100% Mexico.
- Click quality is the June issue. This account's own February flight converted platform clicks into measured site visits at 15.7%; June's campaigns ran at 0.19%, roughly $33 per real visit versus $0.55 in February. Same pixel, same site, same market. The difference is the inventory the June campaigns bought (heavy in-app placements at $1.31 CPM, 63% of spend to 55+). A placement-level audit is the highest-value Meta action for July.
- Conversion reporting for June stays withheld: 67 of the 86 platform-reported conversions come from one retargeting campaign with 126 landing-page views, which is not a credible application rate. Delivery metrics (reach, clicks, CPM) are unaffected.
- Optimization queue: placement audit and exclusions first, then rebalance the 55+ age skew and complete the objective shift.

### Programmatic — Quantcast line — $33,784, 11 view-through conversions
- Deliberate scale month: 42M impressions (+155%), CPM $0.81 (-47%), device reach 18.2M.
- The cost of cheap reach: viewability fell to 51% (May 67%), below the 70% standard. We delivered a 49-site blocklist covering $10,734 (32%) of June spend and recommend a campaign-level viewability floor.
- All 11 June conversions are view-through; treat as directional support, not proven response.

### Programmatic — Azerion line — $34,556, 42 submitted applications, $823 CPA
- Spend +27%, applications +14%, CPA +12% ($737 → $823): efficiency roughly held at higher volume. 440 application starts (Step 1), viewability 68.5%.
- Country-level delivery confirmation and funnel/site/format breakdowns requested from the vendor (email sent 2026-07-07); certification of Mexico-only delivery is pending their reply.

## Site traffic (GA4, Mexico) — the honest read

| | Jan | Feb | Mar | Apr | May | Jun |
|---|---|---|---|---|---|---|
| Sessions | 9,380 | 22,229 | 12,614 | 7,577 | 5,751 | 9,236 |
| Unique visitors | 4,651 | 14,172 | 6,554 | 3,366 | 2,592 | 5,838 |

The half-year is not one trend. It is three separate events, each now verified:

1. **February's peak was a single paid social flight**, not organic growth: one campaign delivered 13,323 sessions that month at exceptional click quality, then ended in early March. February is not a valid baseline for any month-over-month story.
2. **The March–May slide is an organic search decline, confirmed in Search Console.** Mexico organic clicks fell from 4,811 in January to 1,210 in June (-75%), and GA4 shows the same numbers independently, so this is real ranking loss, not a tracking artifact. Two causes are visible: dated news and analysis content that lost 87-99% of its clicks as it aged out with nothing replacing it, and mid-funnel commercial pages sliding in rank (demo account from position 12 to 23, trading academy 14 to 24) while brand rankings actually improved (homepage now position 2.5). The decline spans every country the Spanish site serves, so it is a site-level content issue.
3. **June's rebound was bought by media**: of the +3,485 sessions vs May, paid search contributed +2,601, paid social +537, display +274. Organic added +94.

Unique visitors up 26% January to June is the legitimate bright spot. The message for the client: media is doing its job and June proves it can move traffic; the organic foundation needs its own workstream, and until it recovers, total site traffic will track media spend rather than compound on top of it.

## Data quality and measurement

1. **Paid-search attribution is undercounted in site analytics.** The search platform's account link to GA4 is missing, so 2,451 June sessions (27% of all MX sessions) sit unattributed. One admin-level fix, queued for immediate action. Heads-up: once linked, July reporting will show paid search roughly 4x larger than June's attributed view; we will flag the restatement.
2. **Paid social measurement is validated; the platform's counts are the issue.** Landing pages are confirmed tagged and tracking. The platform's reported landing-page views exceed what any measurement system records on the site by an order of magnitude, and the February-vs-June capture comparison isolates the cause to inventory quality, not tracking. Conversions stay out of reporting until the placement audit and pixel-event review complete.
3. **Conversion definitions differ by channel** (search = submitted applications; display lines = vendor-defined applications and view-through results). We never sum them or blend CPA.

## Recommended next steps (July)
1. Complete the Mexico presence-only restriction on search (top efficiency lever, $12.6K/month at stake; June 3 exclusion already showing effect).
2. Link the search account in GA4 (recovers the 27% unattributed bucket) and run the Meta placement-level audit plus pixel-event review before reinstating conversion reporting.
3. Open a dedicated SEO workstream for the Spanish site: refresh the news/analysis publishing cadence and diagnose the mid-funnel ranking slide. This is the structural fix for "traffic feels flat while spend grows."
4. Apply the programmatic blocklist and set a viewability floor on the low-viewability line.
5. Hold budget mix pending the measurement fixes and the placement audit; revisit channel allocation with clean July attribution.
