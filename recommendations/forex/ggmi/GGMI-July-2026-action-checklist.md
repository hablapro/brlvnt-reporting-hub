# GGMI — July 2026 Action Checklist (Execution Handoff)

Written 2026-07-07 from the H1 post-mortem (`reports/forex/ggmi/GGMI-H1-2026-agency-postmortem.md`). This repo is reporting-only: items marked EXEC are account mutations for the execution agent, per-batch approval required before each. Items marked RENZO need an owner decision. Verification column = how we confirm it actually happened.

## This week (stop the bleed)

| # | Action | Owner | Detail | Verification |
|---|--------|-------|--------|--------------|
| 1 | Mexico presence-only whitelist on ALL Bing campaigns | EXEC | Replace reactive country exclusions with a Mexico-only location target, "people in" (presence), not "presence or interest". Applies to all 3 active campaigns. Ref: `GGMI-Bing-SA360-remediation-June-2026.md` fix #1. **Elevated to compliance: reverse solicitation permits organic non-MX clients, but PAID delivery outside Mexico = active solicitation outside the licensed market. Regulatory exposure, not just inefficiency. Fix quietly and immediately; keep the history out of client-facing decks.** | SA360 geo report shows ≥95% MX spend within 7 days of change |
| 2 | Link SA360 account to GA4 property 508849216 | EXEC (admin) | GA4 Admin → Product links → Search Ads 360 → GGMI account (customerId 5372690580 / manager 9697709980). Ref: `GGMI-GA4-tracking-recommendations-June-2026.md` fix #1. | "(unlinked SA360 account)" sessions stop accruing from link date; Paid Search channel group picks them up |
| 3 | Meta placement-level audit | EXEC (read-only) | Pull June insights broken down by publisher_platform + placement; compare LPVs per placement vs GA4 sessions. Benchmark: this account's Feb flight captured at 15.7%; June ran 0.19%. Ref: `GGMI-GA4-tracking-recommendations-June-2026.md` fix #2. | Audit doc identifying which placements carry the junk clicks |
| 4 | Meta placement exclusions from the audit | EXEC | Expected outcome: exclude Audience Network and low-quality in-app placements; revisit 55+ delivery (63% of June spend). Mutation batch sized from item 3's findings. | Capture rate (GA4 sessions / link clicks) recovers toward ≥2% within the first week |
| 5 | Quantcast: apply 49-site disallow + set viewability floor ≥70% as campaign setting | RENZO → vendor | Send `GGMI-Quantcast-disallow-June-2026.txt` (already prepared) and request the floor as a persistent campaign-level setting, not a one-time cleanup. | Vendor confirmation; July viewability ≥70% |
| 6 | Azerion: hold scale until geo confirmation | RENZO | Email sent 2026-07-07. No budget increase until country breakdown certifies Mexico-only delivery. | Vendor reply on file |

## Decisions (Renzo)

| # | Decision | Recommendation |
|---|----------|----------------|
| 7 | July budget level | **Per-channel verification gates, not a blanket hold** (revised 2026-07-07 after Renzo review). Bing: keep June level (~$25K), 100% MX post-whitelist; the fix is a setting and verifies in days. Watch CPA and impression share for 2 weeks; if MX inventory can't absorb it, let campaigns underspend rather than loosen geo. Meta: pull back to ~$8-10K until the placement audit lands and capture recovers ≥2%, then re-scale toward the Feb playbook (gate: days, not weeks). Quantcast: ~May level ($25K) until the ≥70% viewability floor is confirmed as a campaign setting; June's increment is what bought sub-floor inventory. Azerion: flat ($34.5K max) until geo certifies. July starts ~$95K and re-scales channel by channel as each gate clears. |
| 8 | Meta conversion reporting | Stays out of all reporting until item 3 completes and the `fb_pixel_custom` trigger is documented. Fast first step: split the 86 by event name — the account fires both `StartApplication` and `SubmittedApplication` under fb_pixel_custom (see `clients/forex.md`). If most are StartApplication, the finding shifts from "not credible" to "starts misread as submits," which changes the client story. |
| 9 | SEO workstream | Open as its own track (outside monthly media report): refresh Spanish news/analysis cadence, diagnose mid-funnel rank loss (/demo-account 12→23, /trading-academy 14→24). GSC-confirmed, -75% MX organic Jan→Jun. |

## Client questions (from the funnel file, `data/GGMI-client-funnel-Jan-Jun-2026-data.xlsx`)

| # | Question | Why |
|---|----------|-----|
| A | What is the formula behind "Total CTR" and "Profit Loss LTD"? | Stated definition (cost per traded) contradicts their own sheet math twice; every P&L read is suspended until resolved. |
| B | What feeds their cost field? | Their embedded cost basis ($10.9-25.2K/mo, decoded from CPS/CPA/CPF/CPT) matches real media spend in no month. Offer to supply our cost numbers as the feed. |
| C | Can the funnel be split by country? | Separates the media-quality story (start→submit collapse) from LATAM country-mix effects (Approve→Fund decline), given the funnel is all-LATAM by design (reverse solicitation) while paid is MX-only. |

## Before the July report ships

| # | Action | Owner | Detail |
|---|--------|-------|--------|
| 10 | Pull Bing conversion geo | EXEC (read-only) | Split the ~50 monthly submitted applications by country. If they are predominantly MX, true Mexico CPA is well under the $513 blended and the "CPA improves as geo tightens" story is provable. |
| 11 | Standing QA page in the monthly report | Reporting (this repo) | Per channel: platform clicks vs GA4 sessions, geo mix, viewability vs floor, capture vs trailing benchmark. Plus a property-level (all countries) traffic view. |
| 12 | UTM convention doc | Reporting (this repo) | Document the current convention (`meta / paid-social`, etc.) in `context/`; no mid-quarter changes without a dated note. Prevents a repeat of the `an / paid_social` forensics. |
| 13 | July MoM restatement notes | Reporting (this repo) | Two restatements to flag in the July narrative: paid search will read ~4x larger post-SA360-link; Bing MX-only CPA basis changes with the geo fix. |

## Launch checklist (standing, every new campaign from now on)
1. Geo targeting mode verified (presence-only whitelist on geo-restricted accounts).
2. Conversion goal wired and test-fired before spend.
3. UTMs per documented convention.
4. Quality floors set (viewability, placement exclusions) where the channel supports them.
5. Budget scale gates: >+50% MoM requires prior month's QA page clean.
