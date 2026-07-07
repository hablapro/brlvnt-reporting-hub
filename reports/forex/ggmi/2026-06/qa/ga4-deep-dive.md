# GGMI — GA4 Deep Dive — What Is Actually Happening (Jan-Jun 2026, Mexico)

Date: 2026-07-07. Property 508849216 (Forex LAT). Companion to `qa-and-model.md`; source workbook `../data/GGMI-GA4-Jan-Jun-2026-data.xlsx`. Supplemental pulls this session: hostName by month, June landing pages by source (top 5,000 of 5,889 rows; tail rows are 1-2 session slivers).

## The H1 "trend" is three separate stories, not one decline

MX sessions: Jan 9,380 → Feb 22,229 → Mar 12,614 → Apr 7,577 → May 5,751 → Jun 9,236.

**1. The Feb spike was a one-off paid-social burst tagged `an / paid_social`.**
13,323 sessions in Feb, 2,596 in Mar, then dead (Apr-Jun: 1, 0, 1). It is not any current Berelvant channel (Berelvant Meta tags `meta / paid-social`, which starts Mar). Remove it and the early baseline is flat: Jan 9,380 → Feb ~8,906 → Mar ~10,018. Any client conversation about "the trend since February" is really a conversation about a burst campaign that stopped.

**2. The Apr-May trough is mostly an organic search decline plus a paid-search pullback.**
`google / organic` fell 4,634 (Jan) → 1,124 (May), -76%, and only stabilized in June (1,218). Tagged `bing / cpc` fell from 1,321 (Mar) to 164 (May) while spend was flat, because sessions started leaking into the unlinked-SA360 bucket (below). Direct declined slowly (3,093 → 2,811).

**3. The June rebound is entirely the paid scale-up.**
June +3,485 sessions vs May decomposes to: unlinked SA360 +2,102, meta +537, bing/cpc +499, quantcast +147, tradingview +127. Organic contributed +94. Paid media bought the rebound; the organic base is still at its low.

## "(unlinked SA360 account)" is Bing paid search. Confirmed by landing pages.

Its June MX landing pages are exactly the Bing campaign LPs: `/es/lp/forex-brand-trust-live` 1,579 · `/es/lp/tradingview` 417 · `/es/lp/plataforma-de-verdad` 129 · `/es/trading-platforms/metatrader-5-platform` 94. Timeline (Apr 89 → May 349 → Jun 2,451) matches the SA360 conversion rollout and the 1→3 campaign expansion.

**True June paid-search visibility = 663 tagged + 2,451 unlinked = 3,114 sessions, 34% of all MX sessions** — paid search is GA4's largest June channel once reattributed, which matches Bing's 8,693 MX clicks far better (36% capture vs the 7.6% the tagged number implies). The GA4 Admin link fix reclassifies this from link date forward.

## Meta: the LPs are tagged. The gap is platform-side. (Revises the earlier hypothesis.)

- Meta's June MX sessions land on tracked forex.com pages: `/es` 250, `/es/lp/forex-brand-trust-live` 223, `/es/lp/tradingview-forex` 145 (the "Meta / social" tagging variant), `/es/about-us/overview` 30. GA4 registers them, so the "new LP missing the GA4 tag" theory is out.
- The property records hostnames www/application/account/webtrader/apply.forex.com only. **The whole property, all countries, saw ~54K sessions in June. Meta claims 249,972 Mexico landing-page views** — 5x the entire site's measured traffic. Those LPVs cannot be real loads of tagged pages.
- Best-supported explanation: Meta's LPV event counts in-app browser loads on cheap inventory ($1.31 CPM, FB-only, 63% of spend to 55+) where the GA4 tag never executes; a real but much smaller share of humans continues into a measurable session. May ran 0.54% click→session capture; June's 0.19% says June's marginal inventory was worse, bought at 4x the spend.
- The conversion red flag sharpens: per the Meta workbook's Conversion QA tab, **67 of the 86 pixel conversions come from one retargeting campaign with 126 LPVs** (0726_GGMI_Q3_newlp_CONV). A 53% LPV→conversion rate on a pixel custom event is not a believable application metric. Hold stands.
- Validation question for the account team is now: what exactly fires `fb_pixel_custom`, on which URL, and why does the retargeting campaign convert half its LPVs?

## What this means for the client narrative

1. Frame June as a paid-driven rebound (true and demonstrable channel by channel).
2. The organic decline (-74% Jan→May, stabilizing in June) is the structural site story and worth an SEO/GEO look; it is not a media problem.
3. Do not present the Feb peak as a baseline; it was a burst that ended in early March.
4. After the SA360-GA4 link, July channel reporting will show paid search roughly 4x larger than June's tagged view; note the restatement in advance.

## Property-wide view (Mexico filter removed) — answers "we spent $320K YTD and traffic is flat"

Property totals, all countries: Jan 43,458 → Feb 53,683 → **Mar 69,634 → Apr 67,170** → May 50,360 → Jun 49,675. Traffic is not flat; it surged with the spend and settled 14% above January.

**Where the paid sessions went (H1, GA4 paid-attributed):**
| Destination | H1 paid sessions | What it was |
|---|---|---|
| Venezuela | 69,192 | Bing geo leak. VE clicks were cheap, so the budget bought VE sessions at scale — Venezuela became the property's #1 country from March (May: 22,131 total sessions vs Mexico's 5,751). Excluded from Bing June 3; June's remaining 13.6K attributed sessions are partly last-click attribution carry-over (actual June VE spend $3.5K). |
| United States | ~26,363 | Meta paid-social, concentrated Mar (8,255) and Apr (15,380) — consistent with GCG (US Hispanic) flights landing on this shared property. Confirm against GCG flight dates. |
| Mexico | ~11,904 | The GGMI target market. Paid search 6,955 + Meta 2,209 + display 2,740. Smallest share of the three because MX budget is majority display (view-based, ~2–4% click→session by design) and Meta in-app capture is poor. |
| Mexico Feb burst | 15,929 | `an / paid_social`, Feb–early Mar only. Origin unconfirmed — worth asking what ran in February under "an" tagging. |

**The other half of the answer: organic collapsed property-wide.** Organic Search fell 25,673 → 9,243 sessions/month Jan→Jun, **-64% across every country** (google/organic alone: 24,287 → 8,394). That is ~16K monthly sessions lost — the paid surge silently replaced them, which is why the topline looks "flat" while spend rises. Timing of the drop (Feb–Apr) should be checked against index coverage, /es page inventory, and algorithm updates. This is the single most important structural finding in the account and is invisible in any single-channel media report.

**Net framing:** the $320K YTD bought a real traffic engine (paid sessions 4.0K → 26.9K/month, 6.6x). Its output went mostly to the wrong countries until the June 3 geo fix, Mexico's share of it is structurally low because of the display-heavy mix, and the organic base eroded underneath. All three are fixable or already in remediation; none of them means the spend "did nothing."

## Independent confirmation (GSC + platform pulls, 2026-07-07)

**GSC confirms the organic collapse — it is rankings/content, not a GA4 tracking issue.** Property `https://www.forex.com/es/`:
- Mexico organic clicks Jan 4,811 → Jun 1,210 (-74.8%), matching GA4's google/organic MX 4,634 → 1,218 almost exactly. Two independent measurement systems agree.
- Daily clicks fell ~800-1,050 (Jan) → ~170-370 (Jun); daily impressions roughly halved. Every country declined -46% to -77% (MX -75%, ESP -65%, USA -77%, COL -57%, ARG -63%, VEN -75%).
- Two failure modes in the page data:
  1. **Content decay:** the biggest losers are dated news/analysis pages — forex-market-hours (-1,477 clicks/mo), the "pronóstico 2026" USD/MXN and EUR/USD articles (-99%), S&P 500 explainer (-87%). January's organic base leaned on articles that aged out and were not replaced.
  2. **Commercial pages lost rank:** /demo-account position 12→23, /trading-academy 14→24, /simulated-trading 16→21, /trading-platforms/tradingview -89% clicks. Meanwhile the homepage improved to position 2.5 and "forex trading" ranks #1.6 — brand queries are fine; mid-funnel pages are the casualty.
- SEO/GEO scope: refresh the news/analysis publishing cadence (Spanish market content) + diagnose the mid-funnel ranking slide (internal linking, content freshness, competitor displacement).

**Bing Jan-Mar confirms the paid ramp and the Venezuela machine.** Account 31003116 ran `FX_LATAM_spanish_AO_GEN_policytest_v2_brlvnt` (now paused): $30,763, 45,965 clicks, $0.67 CPC, 10.3% CTR, Jan-Mar. Timing and cheap CPC match GA4's paid-search sessions ramping Feb (3.5K) → Mar (14.9K), overwhelmingly Venezuela. Bing YTD spend ≈ $87.9K (Jan-Mar $31.0K + Apr $15.3K + May $16.0K + Jun $25.7K).

**The February burst mystery is SOLVED — it was our own Meta flight.** Campaign `GGMI_Q2_esp_mx_020426`: Feb $7,276.58 / 84,961 clicks; early Mar $1,058.72 / 9,595 clicks. Its UTMs were `an / paid_social`; tagging changed to `meta / paid-social` when the 0326 campaigns launched in March. Click→session capture by flight:
| Flight | Clicks | GA4 MX sessions | Capture |
|---|---|---|---|
| Feb `GGMI_Q2_esp_mx_020426` | 84,961 | 13,323 | 15.7% |
| Mar `0326_GGMI_Q2_esp_mx_CTR` | 22,911 | 468 | 2.0% |
| Jun (all GGMI Meta) | 407,136 | 786 | 0.19% |
The February campaign delivered sessions at ~$0.55 each; June's delivered at ~$33 each. This is the strongest evidence yet that June's Meta clicks are qualitatively different inventory (in-app junk), not a normal in-app measurement discount — and it retires the "in-app loss is the baseline" framing entirely. Also confirmed: GCG's `0326_GCG_Q2_esp_us_CTR` runs in the same Meta ad account and lands on this property (Mar $5,946 / 11,267 clicks → 8,255 US sessions, 73% capture — with GCG's US audience, capture is fine, further isolating GGMI's June inventory quality as the problem).

## Corrections applied to earlier June docs
`qa-and-model.md` (Meta reconciliation row + finding 3), `GGMI-GA4-tracking-recommendations-June-2026.md` (fix 2 causes), and the narrative draft's data-quality wording updated: cause shifted from "missing GA4 tag" to platform-side LPV inflation + conversion concentration in the 126-LPV retargeting campaign.
