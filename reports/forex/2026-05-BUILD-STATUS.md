# May 2026 Reports — Build Status & Resume Handoff

Last updated: 2026-06-02. Plan: `/Users/rpro/.claude/plans/ok-we-need-to-jolly-fern.md`.
Beads: Reporting-Analytics-1o5 (GCG), Reporting-Analytics-2a8 (GGMI).

## ✅ COMPLETE (2026-06-02)
All deliverables built and delivered to Drive folder **May-data** (`1hWwGEgyU6HiybjSlylJIQrmJD02DK4gR`, inside "FX Report"):
- `Forex GCG (US) — May 2026 Performance Report` (Sheet, 4 tabs, formatted) — `1CTY9mk2Y9qtfR4cOT5uI8It5GOhfgIEgZmuhsUvLmJM`
- `Forex GGMI (LATAM) — May 2026 Performance Report` (Sheet, 4 tabs, formatted) — `1XsQTZ-9qxyRaLPk44GHUrgQh_WXZAu85AslcguL1vME`
- `05. GCG_US_May_2026_Performance_Review.pptx` (7 slides) — `1DFD2x24JLLlGnnYMQbLaLqHjrPcz-D4F`
- `05. GGMI_LATAM_May_2026_Performance_Review.pptx` (7 slides) — `1l57gj98f6KJTgIsc3VnyyOm7amxIkFqy`
Quantcast pulled (acct 9969644). Both beads closed. One duplicate GCG sheet (created during a create retry) was trashed with user approval.

### CORRECTION 2026-06-03 (Quantcast endDate)
Initial May Quantcast pull used endDate 2026-05-31 (MCP treats endDate as EXCLUSIVE), dropping May 31 and understating spend ~$2K. Reconciled against the platform and re-pulled with endDate 2026-06-01. Corrected May Quantcast: GCG $22,009.23 (was $21,207), GGMI $25,013.56 (was $23,826). Corrected region totals: GCG $74,077.88 (+28.9% MoM), GGMI $74,869.34 (+63.7% MoM). All artifacts updated (data, QA, both Sheets, both decks, Spend Tracker). April validated against platform ($30,020.15 exact); only May was affected. See [[reference-quantcast-mcp-enddate]].
A multi-month Spend Tracker (Mar–May, both regions) was also built and lives in the top-level "FX Report" folder: `1DmsIFkCketcWd3VXiXa7Nvz58DowS_SdWMyktezCzQg`.

### CORRECTION 2026-06-08 (GGMI Quantcast reconciled spend)
GGMI May Quantcast spend reconciled up to client-confirmed campaign total **$26,890.00** (was $25,013.56 from the MCP "Budget Delivered" pull; ~$1,876 higher). Impressions (16,481,325) and clicks (4,807) unchanged; derived metrics recomputed: CPM $1.52→$1.63, CPC $5.20→$5.59, CPA $25,013.56→$26,890.00, Quantcast MoM +67%→+79%. New GGMI May totals: client-facing (fee-inclusive Azerion) **$78,790** (was $76,914), MoM +66%→+70% (vs April fee-incl $46,298); QA modeled (raw Azerion) $76,746 (was $74,869). ALL COMPLETE 2026-06-08: quantcast-data.md, qa-and-model.md, GGMI deck (local + Drive re-upload 1l57…), GGMI Sheet (Summary + Performance), Spend Tracker (GGMI + Combined + Grand Total + chart data), Billable tab (GGMI May + Combined). GCG unaffected. Note: Billable Quantcast embedded-fee cell uses 5.5% of reported (April-tier leftover, not May 7.5%); rescaled to new spend but methodology unchanged — flagged for review. Stray formula cells E41/E44 on the Billable tab (outside the labeled tables) are pre-existing junk.

### CORRECTION 2026-06-08 (GCG Quantcast reconciled spend)
GCG May Quantcast spend reconciled up to client-confirmed campaign total **$22,359.00** (was $22,009.23 from the MCP "Budget Delivered" pull; ~$350 higher). Impressions (26,972,772), clicks (1,827), conversions (8) unchanged; derived metrics recomputed: CPM $0.82→$0.83, CPC $12.05→$12.24, CPA $2,725.56→$2,794.88, Quantcast MoM +47%→+49%. GCG Azerion confirmed at $26,472 (fee-inclusive) — no change. New GCG May totals: client-facing (fee-inclusive Azerion) **$76,274.55** (was $75,924.78), MoM +30.2%→+30.8% (vs April fee-incl $58,323); QA modeled (raw Azerion) $74,427.65 (was $74,077.88). New Combined Grand Total: reported $155,065 / billable $155,064.66 (two-month $259,685.72). ALL COMPLETE 2026-06-08: gcg/quantcast-data.md, gcg/qa-and-model.md, GCG deck (local + Drive re-upload 1DFD…), GCG Sheet (Summary + Performance), Spend Tracker (GCG + Combined + Grand Total + chart data), Billable tab (GCG May + Combined). GGMI unaffected. Same Billable Quantcast embedded-fee note applies (GCG cell uses 7.5% of reported; rescaled, methodology unchanged).
### FINAL CLIENT DECKS 2026-06-10
Renzo finalized and sent the May decks to the client as **Google Slides** (his own edits, including the Meta reframe we reviewed). These supersede the Berelvant PPTX working drafts (`report-client-decks/05.*`, Drive `1l57…`/`1DFD…`).
- GGMI final: https://docs.google.com/presentation/d/1npxoxCCbytXSRAjgliG7Ybv8UUS_OQwsUd4uzAaJd4o/edit
- GCG final: https://docs.google.com/presentation/d/1Dj7Gh8KJxnYH_8jPskpfSS9iEsDUjw7F1KW0iRjmXys/edit
REPORT-INDEX.md and report-index.html updated to point to these. PENDING (needs gws reauth): read the final Slides and reconcile internal data/QA (esp. Meta GCG 109→submitted-app framing, GGMI Bing/Meta) to match what the client received.

Open blockers flagged in reports: SA360 access (resolve via customerId/loginCustomerId convention), GGMI Mexico LP/app funnel, Azerion Step1->app drop-off, Bing offline-conversion tracking pending.

## Deliverables (per sub-client): 1 Google Sheet + 1 PPTX deck
- Sheets: `Forex GCG (US) — May 2026 Performance Report`, `Forex GGMI (LATAM) — May 2026 Performance Report`
- Decks: `report-client-decks/05. GCG_US_May_2026_Performance_Review.pptx`, `05. GGMI_LATAM_May_2026_Performance_Review.pptx`
- Upload BOTH to Drive folders `1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55` AND `1hWwGEgyU6HiybjSlylJIQrmJD02DK4gR` (supportsAllDrives:true)
- Comparison basis: MoM vs April 2026. Currency USD. Timezone America/New_York. ROAS excluded (no revenue tracking).
- Format: Google Sheets Styling Standard in `dashboards/dashboard-spec.md`; deck mirrors April layout in `report-client-decks/04.*`.

## DATA STATUS
All pulled data is saved as `reports/forex/<sub>/2026-05/data/<channel>-data.md`. Raw vendor files (Azerion XLSX) are in `.../2026-05/data/sources/`. Folder convention: `reports/README.md`. Session log: `reports/REPORTING-LOG.md`.

| Channel | GCG | GGMI | Source |
|---|---|---|---|
| Google Ads | ✅ google-ads-data.md | n/a | google-ads MCP, acct 4781995752 |
| Meta | ✅ meta-data.md | ✅ meta-data.md | meta-ads MCP, act_1699453997689551 |
| Bing | n/a | ✅ bing-data.md | **bing-ads MCP direct, acct 31003116** (SA360 BLOCKED) |
| Azerion | ✅ azerion-data.md | ✅ azerion-data.md | xlsx in azerions-data/may/ |
| Quantcast | ✅ quantcast-data.md | ✅ quantcast-data.md | **quantcast MCP, acct 9969644 (PULLED 2026-06-02)** |

## QUANTCAST — the only remaining pull (do this after MCP reload)
- Quantcast MCP URL: `https://quantcast-mcp.principal-e85.workers.dev/mcp` (type http).
- Account ID 9969644. Filter campaigns `*GCG*` (US) and `*GGMI*` (MX); geo United States / Mexico.
- Normalize via `mappings/quantcast-field-mapping.md`: Budget Delivered→Spend, Clicks (Advanced IVT)→Clicks, Results→Conversions (note VT vs CT), Device Reach/Frequency, Viewability. Revenue not configured → ROAS N/A.
- April Quantcast for MoM: GCG = $15,015 / 7.2M impr / 1,622 clicks / CPM $2.08 / 2 VT conv / $7,508 CPA. GGMI = $15,005 / 7.0M impr / 3,369 clicks / CPM $2.14 / 0 conv / 66.2% viewability / CPC $4.46.
- After pulling, write `reports/forex/<sub>/2026-05/quantcast-data.md`, then assemble Sheets + decks.

## KEY MAY FINDINGS (validated)
### GCG (US)
- **Google Ads**: $15,200.77 / 126,851 impr / 9,953 clicks / 7.85% CTR / 76 conv / **$200.01 CPA**. CONVERSION TRACKING FIXED (all 76 = "PO App Form Step 5 Submission Completed", evenly distributed across all 5 weeks; April's 12 were all in week 5). TrackB Authority+Platform = 52 conv ($121–169 CPA); TrackA Trust laggard ($332 CPA); Brand budget-limited (60% lost to budget, $285 CPA). Non-brand now RANK-limited not budget-limited. Mobile converts (56/76).
- **Meta**: $12,242.61 / 2.32M impr / 40,790 link clicks / CPM $5.29 / 109 conv / $112.32 CPA. Best Meta month, CPM -45%, conv +49%, CPA -33% MoM. LPV/click 65.9%. Scale 0426_GCG.
- **Azerion**: $24,625 / 4.1M impr / 42,274 clicks / 1.03% CTR / 1,398 Step1 ($17.61) / 43 apps ($572.68). Spend +62%, Step1 +184%, but apps 76→43 and app CPA worsened — Step1→application drop-off increased.
- April GCG cross-channel ref (from deck 04): GAds $15,120/12 conv; Meta $12,167/73/$166.68; Quantcast $15,015/2; Azerion $15,186/76/$199.82.

### GGMI (LATAM)
- **Bing**: $15,972 / 368,704 impr / 29,944 clicks / 8.12% CTR / $0.53 CPC / 0 conv reported (budget paused). SA360 path PERMISSION_DENIED — used Bing Ads MCP directly. New TradingView keyword theme (~24% spend, $2.34–4.99 CPC). GGMI offline conversion goals now Active/"RecordingConversions" (tracking being built). CTR down vs April 11.66%, CPC up vs $0.46.
- **Meta**: $6,626 / 6.84M impr / 128,231 link clicks / CPM $0.97 / 64,264 LPV / **only 4 conv** / $1,656 CPA. Funnel broken at post-LPV (Mexico landing page). Top-funnel cheap & strong; media not the constraint.
- **Azerion**: $27,258 / 6.06M impr / 6,301 clicks / 0.10% CTR / 225 Step1 ($121) / 37 apps ($736.70). Apps 19→37 MoM on +167% budget. Viewability 71.6%. LATAM journey drop-off less severe than US.
- April GGMI cross-channel ref (from deck 04): Bing $15,289/11.66% CTR; Meta $5,227/1 conv; Quantcast $15,005/0; Azerion $10,215/19/$538.

## CROSS-CHANNEL THEMES FOR NARRATIVE
- GCG: measurement turned a corner — Google Ads now tracking; all three measured channels (GAds $200, Meta $112, Azerion $573 app / $17 Step1) comparable. Azerion Step1→app drop-off + GCG site funnel is the optimization target.
- GGMI: media delivery is strong and cheap across Bing/Meta/Azerion; the constraint is the Mexico landing-page/app funnel (Meta 4 conv on 64K LPV) and Bing conversion measurement (SA360 auth + offline goals just activated). Azerion is the only GGMI channel converting at scale (37 apps).

## REMAINING BUILD STEPS
1. Pull Quantcast (both subs) → quantcast-data.md.
2. Write QA note + modeled KPI tables per sub-client (reuse March QA format).
3. Build 2 Google Sheets (tabs: Summary, Performance, Diagnostics, Data Notes) with full formatting.
4. Build 2 PPTX decks (mirror April 04.* structure; run stop-slop on prose).
5. Upload Sheets + decks to both Drive folders; close beads; flag blockers (SA360 auth, GGMI Mexico funnel, Azerion drop-off).
