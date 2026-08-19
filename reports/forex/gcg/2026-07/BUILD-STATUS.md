# July 2026 Report — Build Status & Resume Handoff (GCG (US Hispanic))

Cycle opened: 2026-08-19. Reporting only; no account mutations from this repo.

Kickoff per `docs/RUNBOOK.md` phase 0. The two standing questions, answered
before any pull:

1. **What does the client already hold for July 2026?**
   - Client budget tracker page: ON HAND, transcribed to
     `data/sources/GCG-client-tracker-July-2026.xlsx`. July working media
     $136,224: Google Search $29,478 · Quantcast $29,857 · Azerion $31,477
     · Native $20,298 · YT (PMax) $18,175 · Meta $6,940. CTV/DOOH/TikTok/
     affiliates $0. Spend basis = tracker (standing ruling).
   - Client funnel / BvA dashboard for July: NOT on hand — asked of Renzo
     2026-08-19 (June had submitted/live/approved/funded/traded rows).
   - Comms since the June report: asked of Renzo 2026-08-19; assumed none
     until answered.
2. **How is the agency scored this month?** Submitted applications and cost
   per submitted application (standing). Google Ads event
   "PO App Form - Step 5 - Submission Completed"; Azerion = vendor-reported
   applications. Verify the Google event name is unchanged at pull time.

**New this month vs June:** YT (PMax) line at $18,175 (was $0) — locate in
Google Ads account 4781995752 and report separately from Search. Native
scaled $3,645 → $20,298 (Azerion Native vendor file on hand). Meta fell
$30,711 → $6,940; `0426_GCG_Q2_esp_us_CTR` delivered $2,104.37 in July
despite being paused now — reconcile the rest.

## Channel status

| Channel | Data pulled | QA | In model | Notes |
|---|---|---|---|---|
| Google Ads (Search) | ✅ 2026-08-19 | ✅ tracker exact | provisional | 73 submitted (Step 5); metrics.conversions=76 incl. 3 GCLID — never quote 76 |
| Google Ads (PMax/YT) | ✅ 2026-08-19 | ✅ tracker exact | provisional | 49 submitted in all_conv only; goal-config fix → recommendations |
| Meta | ✅ 2026-08-19 | ✅ tracker exact | provisional | CONV objective DELIVERED (June commitment); Q2 CTR paused after July |
| Quantcast (display) | ✅ 2026-08-19 | ✅ tracker exact (0.01%) | provisional | $29,854.75; viewability 49.26% (June 46.9%, improving, still below 70% floor) |
| Quantcast (Native) | ✅ 2026-08-19 | ✅ see Native row | provisional | $10,002.73, new campaign (created 2026-07-02), first delivery month; viewability 57.98%, below floor |
| Azerion (display) | ✅ vendor file | ✅ June-pattern adj | provisional | 80 apps, $393.46 tracker CPA; viewability 64.95% computed BELOW floor (vendor claims 71.28% — discrepancy flagged) |
| Native (Azerion + Quantcast) | ✅ vendor file + MCP | ✅ resolved (1.1% delta) | provisional | Azerion raw $9,362 + fee $10,064 (internal) + QC $10,003 = $20,067 vs tracker $20,298 — HOLD cleared |
| GA4 / client funnel | ✅ GA4; funnel pending Renzo | ✅ capture 67.2% | provisional | ES sessions 66,398 (-17.2%); funnel rows when client dashboard arrives |

Bing/SA360: not a GCG channel (GGMI only). Geo check: GCG is US — check
delivery, not just settings, on every channel.

## Carry-overs from last month (June deck, "Recommended next steps (July)")

1. Meta shift to conversion objective, judged on submitted apps — VERIFY
   whether it happened (June deck promised it after a May slip).
2. Search ad-rank program (bids, QS, RSA refresh) on TrackB before budget —
   check July impression share / lost-to-rank for movement.
3. Quantcast: 18-site blocklist delivered covering 32% of June spend +
   viewability-floor recommendation — **verified NOT applied**: all 18
   domains still delivered in July ($11,087 combined). July display
   viewability 49.26% vs 46.9% June (+2.4pts, still below the 70% floor).
   Refreshed 35-domain list issued for July
   (`recommendations/forex/gcg/GCG-Quantcast-disallow-July-2026.md`).
4. Azerion: concentrate on Trusted Broker + Broker 1, format shift
   728x90 → 300x600, viewability above standard; Native pilot detail —
   Native vendor file now on hand.
5. Start-to-submit funnel step on the joint roadmap (client-owned; status
   from Renzo).

Also standing from June QA: Meta tracker $30,711 ruling (platform figure
internal); client "Unique Sessions" scope differs from GA4 (noted, not
blocking). Laura's presentation rules (DOCTRINE §11) apply to GCG:
state the target per channel, no naked stats, MoM on every KPI, Meta split
per campaign by objective.

## Open items before this month can ship

1. July client funnel rows (submitted/live/approved/funded/traded) — Renzo.
2. Comms-since-last-report check — Renzo.
3. Meta objective-shift status and Meta $6,940 composition — platform pull
   + Renzo's performance manager context if needed.

## Gate status
| Gate | Run | Result |
|---|---|---|
| QA reconciliations | — | |
| Tracker reconciliation | — | |
| `scripts/verify_numbers.py` | — | |
| `scripts/protection_scan.py` | — | |
| Render QA (slide count + visual) | — | |
