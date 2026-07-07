# GGMI — GA4 / Tracking Recommendations — June 2026

Source: June 2026 GA4 reconciliation (`reports/forex/ggmi/2026-06/qa/qa-and-model.md`). Reporting repo does not execute changes; this file is the handoff for the execution agent.

## 1. Link the SA360 account to GA4 property 508849216 — HIGH, do before July reporting

**Evidence:** "(unlinked SA360 account)" is June's single largest source/medium in Mexico (2,451 sessions). With direct-tagged bing/cpc (663) that bucket makes "Unassigned" the #1 channel group (2,853 sessions, 31% of all June MX sessions).

**What happens now:** SA360 auto-tagging arrives on clicks, GA4 has no linked SA360 account to resolve it against, and every paid-search session lands unattributed. Channel reporting understates paid search by roughly 4x.

**Fix:** GA4 Admin → Product links → Search Ads 360 → link the GGMI SA360 account (customerId 5372690580 under manager 9697709980). One-time admin action, no tagging changes.

**Result:** paid-search sessions attribute correctly from link date forward; historical sessions stay Unassigned (note this in July MoM commentary).

## 2. Resolve the Meta landing-page tagging question — HIGH, blocks Meta conversion validation

**Evidence (updated after landing-page analysis, see `reports/forex/ggmi/2026-06/qa/ga4-deep-dive.md`):** Meta reported 407,136 link clicks and 249,972 LPVs in June; GA4 recorded 786 Meta-attributed Mexico sessions (0.19% capture; May baseline was 0.54%). The destination LPs are tagged and receiving sessions (`/es/lp/forex-brand-trust-live`, `/es/lp/tradingview-forex`, `/es`), so this is NOT a missing tag. Meta's claimed LPVs are 5x the entire property's June traffic across all countries; the inflation is platform-side, concentrated in cheap in-app inventory where the GA4 tag never executes.

**Benchmark that kills the "in-app loss is normal" defense (added 2026-07-07):** this same account's February flight (`GGMI_Q2_esp_mx_020426`, tagged `an / paid_social`) converted 84,961 clicks into 13,323 GA4 sessions — 15.7% capture, ~$0.55/session. March's CTR campaign ran 2.0%. June runs 0.19%, ~$33/session. Same pixel, same site, same market; the inventory changed, not the measurement. GCG's US flight in the same account captures at 73%.

**What to investigate:**
1. What fires `fb_pixel_custom`, and on which URL. 67 of the 86 June conversions come from one retargeting campaign with 126 LPVs (53% conversion rate) — not a believable application metric.
2. Placement/inventory quality: capture degraded 3x as spend scaled +291% ($1.31 CPM, FB-only, 63% of spend to 55+). Pull placement-level LPV vs GA4 sessions; expect Audience-Network-style inventory to explain most of the gap.
3. Whether Meta's LPV event standard (in-app browser DOM load) should be reported to the client at all; GA4 sessions are the defensible traffic number.

**Fix:** confirm the exact June destination URL(s) on every active Meta ad, check each for the GA4 tag (or identify which property they send to), and standardize UTMs. Until then the 86 pixel conversions stay out of client-facing reporting.

## 3. Carry-forward items (already documented elsewhere)
- Bing Mexico-only geo remediation: `GGMI-Bing-SA360-remediation-June-2026.md` (fix #1, $12,637 non-MX in June).
- Quantcast 49-site disallow + viewability floor: `GGMI-Quantcast-disallow-list-June-2026.md`.
- Azerion geo + funnel data request: email drafted (`GGMI-Azerion-email-June-2026.md`), not yet sent.
