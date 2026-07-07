# Reporting Session Log

Chronological log of reporting sessions. Newest first. One block per session.

---

## 2026-07-07 (2nd session) — June 2026 GGMI: GA4 + QA/model + narrative draft — DATA COMPLETE, pending review

**Goal:** Resume the June GGMI build after connecting the GA4 MCP: pull GA4, run cross-channel QA + model, draft the narrative.

**Done:**
- **GA4 workbook** `forex/ggmi/2026-06/data/GGMI-GA4-Jan-Jun-2026-data.xlsx` — property 508849216, Mexico-only, Jan–Jun monthly (trend / channel groups / source-medium / geo QA). All pulls complete. MCP `dimensionFilter` is broken (string serialization) — workaround: country as dimension, filter locally.
- **Model** `model/GGMI-Jun-2026-cross-channel-model.xlsx` + **QA note** `qa/qa-and-model.md`. June: **$119,922 (+56% vs reconciled May), 69.9M impr, 449.8K clicks**; Bing 50 apps @ $513, Azerion 42 @ $823, Quantcast 11 VT, Meta 86 HELD. Quantcast MoM restated to +25.6% on the reconciled May $26,890 basis.
- **Narrative draft** `output/GGMI-Jun-2026-narrative-draft.md` — awaiting Renzo's framing review.

**Key findings (new):**
- **SA360 not linked to GA4**: "(unlinked SA360 account)" = 2,451 June MX sessions → Unassigned is the #1 channel (31%). One-line admin fix, queued in `recommendations/forex/ggmi/GGMI-GA4-tracking-recommendations-June-2026.md`.
- **Meta capture worsened 3x** (0.54% May → 0.19% June, alongside the new LP) — strengthens the hold on Meta's 86 conversions. Same recommendations doc.
- **H1 site trend is flat, not upward** (client expects upward): Jan 9,380 → Jun 9,236 sessions, Feb spike, May trough. June itself +61% MoM; unique visitors +26% Jan→Jun. Narrative frames June as a rebound.

**Open / next:** Renzo reviews narrative framing → build Sheet + deck (May pattern) → send Azerion email (still unsent) → GCG June not started. Repo still uncommitted.

---

## 2026-07-06 → 07-07 — June 2026 GGMI build — IN PROGRESS (paused to connect GA4 MCP)

**Goal:** Build the June 2026 GGMI (Mexico) monthly report. This session captured all MCP + vendor channel data and wrote channel workbooks + recommendation handoffs. Paused before cross-channel QA to connect the GA4 MCP.

**Done — 5 channels captured as .xlsx in `reports/forex/ggmi/2026-06/data/`** (data now stored as spreadsheets, not .md, per new convention):
- **Bing** (direct + **SA360**): SA360 is the truth source — Bing-native shows 0 conv, SA360 shows **50 submitted apps @ $513 CPA**. Spend $25,659 (+61%), account went 1→3 campaigns. Bidding is **MANUAL_CPC / blind** (conversions ExcludeFromBidding). 
- **Meta** (full 9-tab report): $25,924 (+291%), 86 pixel conv **unvalidated** (start-vs-submit + new-LP anomaly). Creative/placement/demographic cuts done — 63% of spend to 55+, FB-only (IG ~$70).
- **Quantcast**: $33,784 (+35%), 42M impr, CPM $0.81, **viewability crashed to 51%**, 11 view-through conv. Added **Site List + Disallow** tabs.
- **Azerion** (vendor XLSX, was misfiled under 2026-05, moved): $34,556 (+27%), **42 submitted applications**, CPA $823. Data gaps flagged.

**Geo compliance (GGMI = Mexico-only, hard rule):** Meta ✅ 100% MX, Quantcast ✅ 100% MX, **Bing 🔴 49% non-MX ($12,637)**, Azerion ⚠️ unverified (no geo provided).

**Recommendations written (`recommendations/forex/ggmi/`):** Bing/SA360 remediation (8 fixes, Mexico-only geo #1), Meta recs, Quantcast disallow list (49 sites/$10,734 + .txt), Azerion data-request + **email draft (not yet sent)**. Two audit scorecard artifacts (Bing-direct, SA360).

**New conventions established this session** (in `reports/README.md` + project memory): data as .xlsx not .md; reporting-only (no execution, recs to `/recommendations/`); every programmatic report ships a Domain/App site list + disallow list; GGMI Mexico-only geo check every report; never name competitors in vendor/client comms.

**BLOCKED / resume:** GA4 MCP not connected this session. User is connecting it and restarting. **On resume:** pull GA4 (property 508849216, Mexico-only, Jan–Jun monthly: sessions/totalUsers/activeUsers/pageviews; by channel grouping; by source/medium) → then cross-channel QA + model. Full detail in `reports/forex/2026-06-BUILD-STATUS.md`.

---

## 2026-06-08 → 06-15 — May reconciliation, final decks, GCG Q2 post-mortem — COMPLETE

**Quantcast May spend reconciled (client-confirmed), both regions:**
- GGMI $25,014 → **$26,890**; GCG $22,009 → **$22,359**. Held impressions/clicks/conversions, recomputed CPM/CPC/CPA. New region totals: GGMI **$78,790**, GCG **$76,275**; Combined grand total $155,065. Pushed through both Sheets, both decks, Spend Tracker, Billable tab, and repo data/QA/BUILD-STATUS.

**Slide-by-slide deck review (data integrity):**
- Bing (GGMI): the 33 are live-account confirmations from newly-live offline tracking (submit step ~23); client keeps **33 submitted / $484**, geo omitted; added tracking-history wording, removed internal SA360/Primary jargon. SA360 confirmed monthly: Mar Primary 0, Apr 180 (Step-1), May 33 (Live Confirmation) — Primary action was reassigned, so MoM isn't like-for-like.
- Meta: GGMI **0 submitted / 4 starts**, GA4 **~695 real sessions** vs 64,264 Meta LPV (in-app browser loss). GCG **1 submitted / ~108 starts** on a traffic/CTR objective (LANDING_PAGE_VIEWS optimization) — the 109 was starts, not conversions.
- Azerion (GGMI): reconciled to 7 ad sets ($29,302 / 37); deck had shown 6.

**Final client decks = Google Slides (Renzo's edits), canonical, superseding the PPTX drafts:**
- GGMI `1npxoxCCbytXSRAjgliG7Ybv8UUS_OQwsUd4uzAaJd4o`, GCG `1Dj7Gh8KJxnYH_8jPskpfSS9iEsDUjw7F1KW0iRjmXys`. Updated REPORT-INDEX.md, report-index.html, BUILD-STATUS, project memory.

**New artifacts:**
- `reports/report-index.html` — searchable master-index dashboard (region filters, copy-link buttons).
- `reports/forex/gcg/GCG-Q2-2026-post-mortem.md` — GCG-only Q2 post-mortem for Q4 planning (what happened / wrong / learned / well / Q4 recs).
- `context/CM360-agent-brief.md` — onboarding brief for the CM360 agent (who's who, regions, KPIs, measurement rules, CM360 access). Confirmed entity names: **GGMI = Gain Global Markets Inc**, **GCG = GAIN Capital Group, LLC**. CM360 access added by user: profile `10604084` (adops_berelvant), account `5877`, in-scope advertisers GCG US Spanish `16576650` + GGMI FOREX.com LATAM `16624558` (floodlight config IDs match).

**Open / next:** optional GGMI post-mortem (needs GGMI brief); quantified GCG scorecard needs demo/funded numbers; GGMI Bing geo re-pull (reminder ~Jun 10) to confirm presence-only fix; **repo still uncommitted**.

---

## 2026-06-02 — Forex May 2026 reports (GGMI + GCG) — IN PROGRESS

**Goal:** Build May 2026 Performance Reviews for both Forex sub-clients — Google Sheet + PPTX deck each, MoM vs April, delivered to Drive folders `1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55` and `1hWwGEgyU6HiybjSlylJIQrmJD02DK4gR`.

**Done this session (data acquisition):**
- GCG: Google Ads, Meta, Azerion — pulled, normalized, saved to `forex/gcg/2026-05/data/`.
- GGMI: Bing (direct), Meta, Azerion — pulled, normalized, saved to `forex/ggmi/2026-05/data/`.
- Reorganized repo: established `data/` + `data/sources/` + `qa/` + `model/` + `output/` per monthly report; added `reports/README.md` convention and this log. Moved Azerion XLSX into each report's `data/sources/`.
- Beads: Reporting-Analytics-1o5 (GCG), Reporting-Analytics-2a8 (GGMI) — in_progress.

**Key findings:**
- GCG Google Ads conversion tracking is FIXED (76 conv, $200 CPA vs April week-5 anomaly $1,260).
- Bing SA360 access fully blocked (PERMISSION_DENIED) — rerouted to direct Bing Ads MCP (acct 31003116). GGMI offline conversion goals now Active/RecordingConversions.
- GGMI Meta funnel still broken (64K LPV → 4 conv) — Mexico landing-page funnel is the constraint.

**Blocked / pending:**
- Quantcast (both sub-clients): MCP not connected this session. User is connecting the `quantcast` MCP and reloading. Placeholders + pull instructions in each `data/quantcast-data.md`.

**Resume next session:** read `forex/2026-05-BUILD-STATUS.md`, pull Quantcast, then QA → model → build 2 Sheets + 2 decks → upload to both Drive folders → close beads.
