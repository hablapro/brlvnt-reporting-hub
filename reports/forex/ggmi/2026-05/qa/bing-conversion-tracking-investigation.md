# FOREX.com — Conversion Tracking Review — Resolution Note (Bing) + Open Item (Meta)

Prepared by Berelvant · 2026-06-03 · Internal · GGMI (LATAM) and GCG (US)

## Resolution (Bing GGMI)
An audit confirmed **Bing conversion tracking is working correctly**. The earlier "tracking gap" was a **reading error on our side, not a tag or tracking failure**. The full application funnel fires and the Primary conversion — the agency's submitted-application KPI, which feeds Bing's bidding — is real: **33 for May (May 1–31); 29 in the May 4–Jun 2 audit window**, at a ~$484 CPA.

### What was misread (three things)
1. **The `-1777…` "second set" is not a duplicate or a second container.** It is the Bing-synced copy of the same goals, with a timestamp suffix to avoid name collisions. Same events, counted once.
2. **"Step 3/4 = 0" was not the tags failing.** Steps 3 and 4 fire fine (24 and 17). They only read 0 in the Bing-synced view, which was never set up to include Steps 3/4 — those live in the SA360 view. Our error: we queried `metrics.conversions` (Primary only) instead of `metrics.all_conversions`, so the funnel steps looked empty.
3. **"Submitted applications = 0" came from a dashboard pointed at the synced copy of the Live Confirmation goal**, where the count sits at 0 because the original goal carries the real 26.

### Evidence (SA360, all_conversions, May 4–Jun 2, campaign 23772629411)
G2 funnel: 558 App Form Step 1 → 66 Step 2 → 24 Step 3 → 17 Step 4 → **26 funded live accounts** (Primary). Plus **3 MT5** funded. **= 29 Primary submitted applications** feeding bidding. (May 1–31 calendar = 33.) The `-1777…` synced copies appear as parallel rows (Sitewide-1777, Step1-1777, Live Confirmation-1777, etc.) and must be counted once.

### One open check
Confirm which goal the **"Submitted applications" dashboard** reads:
- Points at the **original** Live Confirmation action → shows 26 (correct).
- Points at the **`-1777…` synced copy** → shows 0.
This is a dashboard pointer to fix, not a tag.

## Open item (Meta) — verify with the same lens
Meta's reported conversions split into StartApplication (GCG 108 / GGMI 4) and SubmittedApplication (GCG 1 / GGMI 0). Before concluding anything, apply the same review used for Bing: confirm which custom conversion is the **Primary / reported KPI** event and whether the low SubmittedApplication count is a real funnel result or a Primary-vs-secondary / pointer read (as Bing turned out to be). **Meta report numbers are held unchanged (GCG 109, GGMI 4) pending this confirmation** — do not assume a Meta tracking gap.

## Clean reference
- Google Ads (GCG): 76, all "PO App Form Step 5 Submission Completed" — tracking correctly.
- Azerion: DSP-reported applications (GCG 43, GGMI 37) — tracking correctly.

## Reporting status (May cycle)
- **Bing (GGMI):** corrected — 33 submitted applications at $484 CPA, the account's most efficient converter; no "gap" language.
- **Meta:** held as-is (GCG 109 / GGMI 4) pending the verification above.
