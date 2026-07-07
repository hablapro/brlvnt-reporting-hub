# GGMI H1 2026 — Internal Agency Post-Mortem

**INTERNAL ONLY. Not client-facing in any form.**
Written 2026-07-07 after the June report build and GA4/GSC deep dive. Evidence: `2026-06/qa/qa-and-model.md`, `2026-06/qa/ga4-deep-dive.md`, `2026-06/model/GGMI-Jun-2026-cross-channel-model.xlsx`. Companion: `../gcg/GCG-Q2-2026-post-mortem.md`.

Scope: GGMI (Mexico-only mandate), ~$320K YTD media through June. Verdict up front: the buying works when pointed at the right country and inventory. The failures were enforcement and measurement, and they are ours.

## What went wrong, ranked

### 1. No geo enforcement on a Mexico-only account, for six months
- The Bing campaigns are ours (`_brlvnt` suffix). `FX_LATAM_spanish_AO_GEN_policytest_v2_brlvnt` spent $30,763 Jan–Mar at $0.67 CPC with no geo cap and zero conversion tracking; GA4 shows the sessions went overwhelmingly to Venezuela (Feb 3.5K → Mar 14.9K VE paid sessions).
- May was ~61% non-MX. June was 49% ($12,637). Venezuela was excluded June 3; Spain and the US then surfaced in June spend because we excluded countries reactively instead of whitelisting Mexico.
- Estimated out-of-market search spend YTD: **$45–55K of ~$88K**. Venezuela was the property's #1 traffic country from March through June.
- Root cause: no launch checklist item for geo targeting mode, and no monthly geo QA until June. The client rule was known the whole time.

### 2. Scaled Meta 4x into junk inventory with no site-side check
- February flight (`GGMI_Q2_esp_mx_020426`): 84,961 clicks → 13,323 GA4 sessions, **15.7% capture, ~$0.55/visit**. We know how to buy this market.
- June: 407,136 clicks → 786 sessions, **0.19% capture, ~$33/visit**, while spend went +291%. Inventory: in-app placements at $1.31 CPM, FB-only, 63% of spend to 55+.
- The 86 reported pixel conversions (67 from one retargeting campaign with 126 LPVs, a 53% "conversion rate") nearly reached a client deck.
- Root cause: no clicks-vs-sessions reconciliation during the month. The February benchmark existed in our own account and nobody compared against it.

### 3. Measurement hygiene below the spend level
- SA360 never linked to GA4: 27% of June MX sessions unattributed. A 5-minute admin action, unnoticed roughly three months.
- UTM convention changed mid-quarter (`an / paid_social` → `meta / paid-social`), making the H1 trend unreadable until reverse-engineered.
- A campaign named "policytest" ran three months at full budget with zero conversion tracking.
- No revenue tracking on any channel; ROAS unanswerable across the account.

### 4. Programmatic scaled without quality floors
- Quantcast: viewability fell 67% → 51% (IAB floor is 70%) while spend scaled +35%; 32% of June spend hit 49 sites we ourselves flagged as junk. The floor should have been a campaign setting before scaling, not a monthly cleanup.
- Azerion: months of delivery on a Mexico-only account with no geo verification; we first formally requested the breakdown 2026-07-07.

### 5. Nobody owned the whole-picture traffic read
- Organic search collapsed 64% property-wide starting February (GSC-confirmed: content decay on dated news articles plus mid-funnel ranking losses, brand intact). Channel reporting was diligent; no one was accountable for "does the total picture make sense." It took the account owner pushing back twice before we zoomed out.

## What went well
- **Search converts and it is verified:** 50 submitted applications at $513 (June), +52% on +61% spend, recovered via SA360 when Bing-native showed 0. True Mexico CPA is likely well under $513 given half the spend was out-of-market (pull conversion geo to confirm).
- **Azerion held efficiency through scale:** 42 applications, CPA +12% on +27% spend, 68.5% viewability. Pending geo, this is the steadiest performer.
- **February proved the Meta playbook:** quality MX traffic at $0.55/visit, in this account, with our creative. The benchmark to re-scale toward.
- **The site responds to media:** June sessions +61% MoM, unique visitors +26% Jan→Jun, defined submitted applications 70 (May) → 92 (June).
- **Stewardship artifacts:** the site-level disallow process, the SA360 conversion recovery, the attribution gap caught before July reporting.

## What we change (process, not one-offs)
1. **Launch checklist for every campaign:** geo targeting mode (presence-only whitelist on geo-restricted accounts), conversion goal wired and test-fired, UTMs per the documented convention. No spend without all three.
2. **Standing monthly QA:** platform clicks vs GA4 sessions per channel, geo mix per channel, viewability vs floor. This single page would have caught Venezuela in February and Meta in March.
3. **Quality floors are campaign settings**, not report findings: viewability ≥70%, placement exclusions maintained, capture-rate alert threshold (flag any channel under 25% of its own trailing benchmark).
4. **No mid-quarter UTM changes** without a dated note in the repo.
5. **Scale gates:** budget increases above +50% MoM on a channel require the prior month's QA page clean. June scaled three channels with open quality flags.
6. **Whole-picture owner:** the monthly report ships with a property-level traffic view (all countries, all channels), not just the target-market cut.

## Execution
Immediate actions and owners: `recommendations/forex/ggmi/GGMI-July-2026-action-checklist.md`. This repo is reporting-only; all account mutations go through the execution agent with per-batch approval.
