# Reporting Session Log

Chronological log of reporting sessions. Newest first. One block per session.

---

## 2026-08-28, FOREX.com September budget revisions complete

**Goal:** Apply Mateus's evidence-first framework and revise the GCG and GGMI September Recommended Spend and Minimum Spend proposals.

**Delivered:** `reports/forex/September_Budget_Evidence_Base.md`, `reports/forex/gcg/2026-08/GCG-September-budget-proposal-MATEUS-REVISION.md`, and `reports/forex/ggmi/2026-08/GGMI-September-budget-proposal-MATEUS-REVISION.md`.

**Authority ruling:** the Aug 27 Renzo-final proposals in `reports/forex/_final-delivered/2026-09/` are the pre-feedback baselines. August draft and backup files are working history.

**Final decision:** GCG retains an authorization ceiling of up to $110,000, commits $105,000 at launch, holds $5,000 behind established-line performance gates, and carries a $55,000 Minimum plan. GGMI carries a $90,000 Recommended plan and a $60,000 Minimum plan. No new or returning September initiatives receive spend.

**Hard condition:** GGMI Azerion remains at $0 until written Mexico delivery controls and a minimum 95% Mexico delivery standard are confirmed by September 3. If the condition is not met, neither GGMI scenario remains authorized as designed and the allocation returns for a revised decision.

**Decision structure:** every retained or tested line has a role, evidence and confidence statement, hypothesis, media action, KPI, numeric threshold, evaluation window, meet and miss rule, low-volume rule, and stated operating condition. Agency, shared, and client or system responsibilities are separated without assigning blame.

**QA:** evidence-base structure passed; proposal arithmetic and scenario assertions passed; protection scan returned 0 blocking findings and 0 warnings; Markdown whitespace and client-language scans passed; independent reporting-strategist review passed correctness, traceability, decision usability, and client-risk checks. No live media or tracking changes were made. Bead `Reporting-Analytics-7u7` closed.

## 2026-08-04 → 08-08 — Repo restructured for Performance Lead handover — COMPLETE, 4 decisions pending

**Goal:** Make the repo cloneable and runnable by an incoming Performance Lead with minimal guidance. Not a reporting cycle; a handover build.

**Diagnosis:** the process was already mature but undiscoverable. Doctrine lived in `PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md` and scattered build statuses, the README still described a generic "marketing intelligence hub", and the two checks the doctrine calls mandatory were run by eye.

**Delivered (commit `2b1e90e`):**
- **`docs/`** — RUNBOOK (7 phases per entity, each closing on a named check), DOCTRINE (what may go in a client artifact + why each rule exists), SETUP (all 8 MCP servers, every skill by phase, a 10-minute verification pass), HANDOVER (risks, access, manual steps, carry-overs), DESIGN-SYSTEM (promoted from the unused `.skill`).
- **`lib/housestyle.py`** — one design system replacing ~1,400 lines of forked builder + the separate restyle pass. `Deck.verify()` refuses to save on slide-count drift (the wrong-footer bug that shipped twice). Verified against a real PowerPoint render; 3 contrast/overlap bugs fixed from what the render showed.
- **`scripts/protection_scan.py`** — the doctrine's "verify programmatically" requirement. Reproduces known history independently: Mar–May decks BLOCK, both June finals pass.
- **`scripts/verify_numbers.py`** + per-month `figures.json` — deliverables vs approved figures, both directions, so a stale number surviving a month-fork is caught. Negative-tested. Worked example: `reports/forex/ggmi/2026-06/figures.json` (PASSES against the June GGMI final).
- **`scripts/new_month.sh`** + `templates/month/` — idempotent scaffold.
- **Config** — `.mcp.json` 3 → the 8 servers actually used, secrets as `${VAR}`; `.env.example`; `requirements.txt`; rewritten `.gitignore`.

**Retired to `_archive/`** (reasons in `_archive/README.md`): 10 project-local agents in a wrong-cased `.claude/AGENTS/` that Claude Code never discovered, an identical `.codex` copy, the unregistered JS deck generator, 2 generic templates. Deleted: empty `download.html`, a text dump of the May GCG deck.

**New finding:** `"$124 vendor-basis"` on slide 14 of the GCG June final is forbidden vocabulary that survived two manual protection passes. June is closed and the canonical Slides stay as presented, so it is logged as a July carry-over, not retro-fixed. It is the evidence for running gate 2 before every delivery.

**🔴 Four decisions pending from Renzo before the Lead can start:**
1. **Push.** 39 commits are local-only. `hablapro/brlvnt-reporting-hub` is a personal-namespace remote holding StoneX vendor data and delivered decks. Is that still the right home, and push or not? (Suggestion: move to a private `Berelvant/` repo first.)
2. **The 3 MCP secrets** handed over out of band: `QUANTCAST_MCP_API_KEY`, `GA_MCP_AUTHORIZATION`, `CM360_MCP_API_KEY`.
3. **Access grants** — `docs/HANDOVER.md` §2. Lead time on: FX Report shared drive, Reported Spend Tracker (confirm the internal Billable tab may be shared), canonical Slides, Azerion vendor email distribution.
4. **Confirm 2 doctrine points inferred from the retrospective, not ruled on directly:** (a) agency scorecard = submitted applications + cost per submitted app, downstream neutral; (b) client-facing spend = client budget tracker, recalculated silently, reconciliation internal-only. Both are written into `docs/DOCTRINE.md` as standing rules.

**Also open, lower priority:** repo lives in `/Users/rpro/AI-BRLVNT/`, which is neither the vault nor `dev/<category>/<project>/` per the deliverables rule; the June builders still carry the pre-library palette (new months should import `lib/housestyle.py`).

**Not touched:** `tools/forex-july-2026-*`. A parallel session was building there and committed `e02d4f1` (GGMI July Bing/Meta/Quantcast/GA4 pulls) on 08-08. **The July cycle is further along than `reports/forex/2026-07-BUILD-STATUS.md` showed on 08-04 — read it fresh, do not trust the summary in `docs/HANDOVER.md` §6.**

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

***

## Session 2026-07-16/17 — GGMI June finalized + Q3 FY2026 QBR built, deck APPROVED TO SEND

**Delivered (all in Drive `06. June-data`, 1x1jeGRsh0AgYsB8hVLaW1O1FGPf6OF2Y, shared drive):**
- Google Sheet `Forex GGMI (LATAM) — June 2026 Performance Report` (`1P3SIZ…`, 4 tabs, formatted, numbers verified vs model).
- Deck: Google Slides `1iNea…` = **CANONICAL, 19 slides, approved to send 2026-07-17**. QBR-first order: title → blended Summary (Jan–Jun KPI table w/ MoM) → Q3 spend/apps/vs-plan → Renzo's 2 market-volatility slides (his calc, reviewed + fixed in place) → site traffic + SEO slides with line charts → June channel detail → close. Raw PPTX in Drive (`1yxhT…`) + local `report-client-decks/06.*` are exports of the Slides.
- Spend Tracker + Billable extended to June (GGMI); GCG June column pending.
- Key rulings this session: (1) client-facing spend MUST match the client budget tracker, adjustments recalculated silently (June Azerion $35,026, total $120,393, +53%); (2) Slides file is canonical once Renzo edits it — never re-upload a built PPTX over it; edit via `gws slides presentations batchUpdate` replaceAllText (gws supports ALL Google APIs, not just the 5 in --help).

**Resume next session:** GCG June 2026 report, bead `Reporting-Analytics-7v6` (full pull → QA → model → narrative → deliverables; get the GCG client-tracker figures from Renzo first). Then: Azerion vendor reply pending, SA360→GA4 link (July restatement ~4x, flag it), July client questions A–D.

***

## Session 2026-07-17 (cont.) — GCG June built end-to-end; both decks protection-hardened; SESSION CLOSE

**GCG June (bead Reporting-Analytics-7v6, CLOSED):** full cycle in one session — platform pulls (Google exact-to-tracker; Meta $34,711 platform vs $30,711 tracker, Renzo ruled tracker stands; Quantcast 46.9% viewability + 18-site disallow; GA4 ES-audience healthy), Azerion vendor files integrated same-day (58 apps +35% @ $510; starts-quality fix 3.1%→13.0%; US-only geo), narrative approved, 15-slide QBR-first deck + 4-tab Sheet delivered to `06. June-data`, tracker GCG June column + Native row + billable section done. Native framed as intentional small pilot, **full read promised for July (mandatory)**.

**Protection passes (both decks):** agency KPI doctrine established (submitted apps at low cost/submitted = our scorecard; downstream = client journey, neutral framing); cost-per-submitted-app added to both decks (GCG $350-420 band; GGMI ~$650); self-indicting language reframed (scale-ups = diagnostics that produced the map); GGMI geo aligned to the client-communicated $8,612 (Bing Ads review deck) — SA360 $12,637 internal only; Meta GA4 check: 89 starts client-facing, 4 last-click conv internal-only.

**State at close:** GGMI 19-slide Slides = canonical, send-ready. GCG 15-slide Slides + Sheet awaiting Renzo review (safe to rebuild until he edits; then batchUpdate only). Retrospective written: `PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md` (repo root) — read it at next cycle start; Section 9 is the July kickoff checklist.
