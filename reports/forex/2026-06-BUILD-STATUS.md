# June 2026 Report — Build Status & Resume Handoff (GGMI)

Last updated: 2026-07-16 (3rd session). Scope: **GGMI (LATAM/Mexico) only.** GCG June not started.
Reporting only — no account mutations from this repo. Recommendations go to `recommendations/`.

## ✅ DELIVERABLES BUILT & IN DRIVE 2026-07-16 (GGMI June COMPLETE pending Renzo's deck edit/send)

Renzo approved narrative v2 framing as-is (2026-07-16) and scoped this session to GGMI only. Built and uploaded to **06. June-data** (`1x1jeGRsh0AgYsB8hVLaW1O1FGPf6OF2Y`, FX Report shared drive):
- **Google Sheet** `Forex GGMI (LATAM) — June 2026 Performance Report` — `1P3SIZEXgGsG289lz-33MOefgLRepgdkslaQN4sE09xE` (4 tabs Summary/Performance/Diagnostics/Data Notes, styling per dashboard-spec; converted from the formatted xlsx, verified populated). Local xlsx: `reports/forex/ggmi/2026-06/output/GGMI-June-2026-Performance-Report.xlsx` (Drive copy of raw xlsx: `1HzJGXJYR9KCILiH09nx3f9JSnTQnwXLM`).
- **Deck (working draft)** — Google Slides `1iNeaobJVJLF_Dr3NU2W6Wutsvh55xqJhRFGOL-P_mug` + source PPTX `1yxhTuN7OxLffoAWQz9mZcT67puzJPxWu` (local: `report-client-decks/06. GGMI_LATAM_June_2026_Performance_Review.pptx`). **12 slides mirroring the FINAL May client deck structure** (per-channel Performance + Read/Recommendations pairs, exec summary x2, cross-channel close) **+ new Site Traffic (GA4) slide**. Meta conversions shown as "Held"; Bing geo framed as efficiency lever per approved narrative. Renzo reviews/edits the Slides and sends.
- **Spend Tracker** (`1DmsIF…`) extended to June: GGMI June column + MoM (Jun) (+56.3% raw basis), chart-source June rows (charts auto-extended), GCG June = "—" pending. **Billable tab**: GGMI June section added (Azerion fee $2,591.69 → billable $37,147.52; Quantcast embedded 7.5% = $2,357.04 — May's 5.5%-leftover methodology bug NOT repeated; GGMI June billable total $122,514.04).
- **Spend basis (REVISED 2026-07-16, Renzo ruling): June client materials match the CLIENT TRACKER.** Azerion June = **$35,026** (vendor raw $34,555.83 + $470.17 adjustment), Quantcast $33,784 (matched already), June total = **$120,392.52 (+52.8% vs May reported $78,790)**, Azerion CPA $833.95 (+5.3% vs May $791.95), Azerion MoM +19.5%. Ad-set spends scaled pro-rata (×1.0136) so the table reconciles to $35,026. **No adjustment/basis commentary anywhere in the deck or Sheet** (Data Notes scrubbed; verified programmatically). Adjustment detail internal only: this file, tracker note (B9), Billable tab. Deck+Sheet rebuilt and Drive files updated IN PLACE (same IDs/links).
- Build scripts committed to the repo this time: `tools/forex-june-2026/` (May's /tmp scripts were lost on reboot).
- gws CLI needed reauth this session (`gws auth login`, done by Renzo). Drive-connector base64 upload of xlsx produced an EMPTY converted Sheet (trashed: `1qKJmAwzd0LW7Gi…`) — use `gws drive files create --upload` + `files copy` with target Google mimeType instead; shared drive requires `supportsAllDrives:true`.
- REPORT-INDEX.md + report-index.html updated with June links. Bead Reporting-Analytics-22f.

## ▶ RESUME HERE (what's left)

**1. Renzo: review/edit the June Slides working draft, then send to client** (visual check of the PPTX→Slides conversion included).
**2. GCG June report** — not started (pull → QA → model → narrative → deliverables; then fill the tracker's GCG June column + Billable June combined totals).
**3. Azerion vendor reply** still pending (geo certification, funnel/site/format/creative breakdowns) — email sent 2026-07-07. GA4 tracking fixes still with execution (`recommendations/forex/ggmi/GGMI-GA4-tracking-recommendations-June-2026.md`): SA360→GA4 link (expect July paid-search restatement ~4x, flag it), Meta placement audit before reinstating conversions.
**4. July report carry-overs:** client questions A–D in `recommendations/forex/ggmi/GGMI-July-2026-action-checklist.md`; Quantcast disallow refresh each report.

**Added 2026-07-07 (client funnel file):** client sent `sources/GGMI Jan to June 2026 summary report.xlsx` (funnel App Starts→Traded = trusted; impressions/clicks/sessions = distrusted; Total Cost column = Renzo's media numbers). Normalized to `data/GGMI-client-funnel-Jan-Jun-2026-data.xlsx` (Funnel / Cost per Stage / Reconciliation / Notes). Headlines: submitted fell 1,080→655 (-39%) while spend rose 70x; funnel tracks the organic base (≥86% of submissions non-attributed); June start→submit collapsed 23.9%→14.9%; cost/funded $27 (Jan) → $6,020 (Jun) — blended, apples-to-oranges caveat below.
Corrections after Renzo review: (1) funnel is **all-LATAM by design** (reverse solicitation legal for organic; paid restricted to MX) → paid-vs-funnel CPA comparisons are apples-to-oranges, and the Bing non-MX spend is a **compliance exposure** (active solicitation outside licensed market), elevated in the July checklist. (2) Client says 'Total CTR' = cost per traded; **math contradicts it twice** (their sheet does P&L = CTR − cost exactly; they already have a CPT column at $203-$825) — formula requested, all P&L reads SUSPENDED. (3) Their embedded cost basis decoded from CPS/CPA/CPF/CPT ($10.9-25.2K/mo) matches real spend in no month — their cost feed is broken; stored ratios discarded. Client questions A-C added to the July checklist.

**Added 2026-07-07 (budget planning):** Google Doc (client-facing draft) created: `https://docs.google.com/document/d/1dB_RqzWkEWSCqjWhYu9VLHMEbLHtkEdoj2uswDfqWwY` — full rationale incl. conservative forecast (Q4 floor ≈253 apps, FY27 floor ≈812) + roadmap discovery questions. Committed locally as `134ecc7`.
 client asked for Q4 FY26 (Jul-Sep) recommendation + FY2027 proposal off the tracker (FY Oct-Sep, $1.044M budget, $320,575/30.7% spent, $723,425 remaining — underspend is client-side timing). Deliverables in `2026-06/output/`: `GGMI-Q4-FY2027-budget-recommendation.xlsx` (Summary/Q4 Plan/FY2027/Assumptions) + `.md` draft. Recommendation: **Q4 = $420K quality-gated ramp** (Jul 95 / Aug 135 / Sep 190; Sep pilots Native $15K + Apple Search Ads $5K; NOT the full $723K — June proved quality breaks at $120K), FY26 finishes ~71%. **FY27 = $1.2M base + $300K gated flex**; dual-objective (acquisition CPA channels vs awareness stack judged on reach + branded-search growth); all unfunded tracker rows funded or scoped (Native, TikTok, ASA, Affiliates/Partnerships — the last needs compliance scoping first; DOOH stays client-led). Aligned to client onboarding roadmap: lower $100 min deposit + stablecoin (fixes Approve→Fund), Persona KYC (start→submit), WhatsApp Jan launch (click-to-WhatsApp via Meta = Q2 flex). Tracker anomaly: DOOH $26,454 excluded from their own totals (client question D).

**Added 2026-07-07 (internal accountability):**
- **Agency post-mortem (INTERNAL ONLY):** `reports/forex/ggmi/GGMI-H1-2026-agency-postmortem.md` — geo enforcement failure ($45-55K est. out-of-market search YTD), Meta scaled into junk inventory (capture 15.7% Feb → 0.19% Jun), measurement hygiene gaps, no quality floors, no whole-picture owner. Plus process changes (launch checklist, standing QA page, scale gates).
- **July action checklist (execution handoff):** `recommendations/forex/ggmi/GGMI-July-2026-action-checklist.md` — 6 stop-the-bleed items this week (MX whitelist, SA360-GA4 link, Meta placement audit + exclusions, Quantcast floor, Azerion hold), 3 Renzo decisions (July budget hold at ~May level, Meta conv reporting stays off, SEO workstream), 4 pre-July-report items.

## ✅ DONE 2026-07-07 (2nd session) — GA4 + QA/model + narrative

- **GA4 workbook** `data/GGMI-GA4-Jan-Jun-2026-data.xlsx` (6 tabs: Summary, Trend, Channel Groups, Source-Medium, Geo QA, Notes). Property 508849216, Mexico-only, Jan–Jun by month. All pulls complete (840/840, 2,940/2,940, 4,995/4,995 rows). MCP dimensionFilter param broken (serialization) — pulled with country as dimension, filtered locally.
- **Model workbook** `model/GGMI-Jun-2026-cross-channel-model.xlsx` (June Model / MoM & Trend / GA4 Reconciliation / Data Notes). June totals: **$119,922 spend (+56% vs reconciled May $76,746), 69.9M impressions, 449.8K clicks**. Conversions never summed (4 definitions).
- **QA note** `qa/qa-and-model.md` — May-format QA table + GA4 reconciliation + 5 validated findings.
- **Narrative draft** `output/GGMI-Jun-2026-narrative-draft.md` — pending Renzo review.
- **New recommendations** `recommendations/forex/ggmi/GGMI-GA4-tracking-recommendations-June-2026.md`:
  1. **Link SA360 → GA4 property 508849216** — "(unlinked SA360 account)" = 2,451 June MX sessions; Unassigned is the #1 channel (31%).
  2. **Verify Meta new-LP GA4 tagging** — capture 0.54% (May, known in-app loss) → 0.19% (June); explains conversion-validation hold.
- **GA4 key numbers (MX):** Jun 9,236 sessions (+61% MoM), 5,838 unique visitors (+125% MoM, +26% vs Jan), 18.6% of property traffic. June paid sources: bing/cpc 663, meta 786, quantcast 270, azerion 61 + tradingview 294.

## ✅ DONE — June GGMI data captured (5 channels), all as .xlsx in `reports/forex/ggmi/2026-06/data/`

| Channel | File | June headline |
|---|---|---|
| Bing (direct) | `GGMI-Bing-Apr-Jun-2026-data.xlsx` | $25,659 spend (+61% MoM), 3 campaigns (was 1), CPC $0.53→$1.19, CTR→4.6%. Bing-native shows 0 conv. |
| Bing (SA360 = truth) | `GGMI-Bing-SA360-June-2026-data.xlsx` | **50 submitted apps @ $513 CPA** (SA360 sees offline conv). Geo: only 51% Mexico. Bidding MANUAL_CPC/blind. |
| Meta | `GGMI-Meta-Apr-Jun-2026-data.xlsx` (9 tabs) | $25,924 (+291%), 86 pixel conv (unvalidated: starts vs submit + new-LP anomaly). 63% spend to 55+. FB-only. |
| Quantcast | `GGMI-Quantcast-Apr-Jun-2026-data.xlsx` | $33,784 (+35%), 42M impr, CPM $0.81, **viewability 51%** (below IAB 70%), 11 view-through conv. + Site List + Disallow tabs. |
| Azerion | `GGMI-Azerion-Apr-Jun-2026-data.xlsx` + `sources/Azerion...June...xlsx` | $34,556 (+27%), **42 submitted applications** (Result=submitted app), CPA $823, viewability 68.5%. |

Currency USD. Comparison basis MoM vs May (some Apr→Jun trend). ROAS N/A across channels (no revenue tracked).

## 🔴 GEO COMPLIANCE — GGMI is MEXICO-ONLY (hard client rule; any non-MX = violation)
- **Meta = compliant** (100% MX). **Quantcast = compliant** (100% MX).
- **Bing = VIOLATION**: only 51% Mexico ($13,022); **49% ($12,637) non-MX** (Venezuela $3,456, Spain $3,349, US $1,431, Colombia, Argentina, Peru, Chile...). Fix = whitelist Mexico only, presence-only. In the Bing remediation doc.
- **Azerion = unverified** (no geo provided; requested). Cannot certify until country breakdown arrives.

## 📋 Recommendations / handoffs written (`recommendations/forex/ggmi/`)
- `GGMI-Bing-SA360-remediation-June-2026.md` — 8 fixes; #1 = Mexico-only geo ($12,637), then conversion-based bidding (currently blind MANUAL_CPC), rebalance by CPA.
- `GGMI-Meta-recommendations-June-2026.md` — validate conversions, age targeting (kill 55+/65+ skew), exclude AN/reels_overlay, complete objective shift, don't cut TradingView.
- `GGMI-Quantcast-disallow-list-June-2026.md` + `GGMI-Quantcast-disallow-June-2026.txt` — 49 sites / $10,734 (32%) to block; recommend campaign-level viewability floor.
- `GGMI-Azerion-data-request-June-2026.md` + `GGMI-Azerion-email-June-2026.md` — email drafted (NOT yet sent): fix overlapping weeks, funnel as data, add geo/site/format/creative breakdowns.

## Audits (artifacts, this session)
- Bing-direct scorecard: https://claude.ai/code/artifact/588ff91e-4893-475b-9019-4f977f5ca9b5 (superseded by SA360 view — showed 0 conv, wrongly flagged TradingView).
- SA360 scorecard (accurate): https://claude.ai/code/artifact/bbe43f77-318d-4485-8fb0-2e794e9dd2fb

## Key IDs / conventions
- Bing acct 31003116. SA360 GGMI customerId 5372690580 / loginCustomerId 9697709980 (query client not manager). Meta act_1699453997689551 (GGMI campaigns only). Quantcast acct 9969644 (endDate EXCLUSIVE → use 1st of next month). GA4 GGMI property 508849216. Azerion = vendor XLSX.
- Data stored as .xlsx workbooks (not .md). Every programmatic report includes a Domain/App site list + disallow list. Reporting only — recs to `/recommendations/`. Never name competitors in vendor/client comms.
- Conventions in `reports/README.md`; standing rules in project memory.
