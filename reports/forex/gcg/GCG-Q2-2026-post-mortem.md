# GCG (US Hispanic) Q2 FY2026 — Campaign Post-Mortem

Prepared for Q4 planning. Sources: the approved Q2 brief (FOREX.com US Hispanic launch, $532,500, Jan–Mar) and the May 2026 performance data. Read this as a delayed soft-launch review, not a full-quarter verdict. The campaign ran late, ran short, and ran on 4 of the 9 planned channels.

## Context in one line
The Q2 plan budgeted $532,500 across nine channels for a dual-track persona test and a channel-efficiency test. The live campaign started mid-April, ran about six weeks, and the May deck puts cumulative spend near 12% of the annual budget. Most of the Q2 plan never ran.

## What happened
- The launch slipped from the planned Jan–Mar window to a mid-April live date. By the end of May we had one clean month of data.
- Four channels went live: Google Search, Meta, Azerion (display/programmatic), and Quantcast (display/programmatic).
- Five planned channels did not run: TikTok, LinkedIn, and Native (the three TEST channels), plus CTV Spanish and YouTube. The channel-efficiency test, a primary Q2 objective, did not happen.
- The dual-track persona test (Track A trust/emerging vs Track B platform/experienced) ran inside Search and Meta, not across the planned channel mix.
- We diagnosed and repaired tracking during the flight: Google Ads conversion tracking stabilized in May, Meta ran on a traffic objective with conversion measurement still being validated, the Quantcast pixel was fixed in April, and GA4 per-channel sessions were still incomplete at month-end.
- May results, measured on submitted applications (the agency KPI):
  - **Google Ads:** $15,201 → 76 submitted apps at a $200 CPA. Track B drove 52 of 76 at $122–169. Brand Search hit its budget cap (60% impression share lost to budget).
  - **Azerion:** $26,472 → 1,398 application starts at $18.93, 43 submitted, $616 CPA.
  - **Meta:** $12,243 → about 108 application starts, 1 submitted. Traffic objective.
  - **Quantcast:** $22,359 → 8 submitted (7 view-through), $2,795 CPA.

## What went wrong
- **Timing killed the test.** A roughly three-month slip compressed the window and left most of the Q2 plan unspent. The quarter never reached the scale the brief designed for.
- **The channels that defined Q2 never launched.** TikTok, LinkedIn, and Native carried explicit kill criteria. Without them we cannot answer the core Q2 question: which test channel scales. CTV and YouTube also sat out.
- **Measurement was not ready at launch.** We spent the live window fixing Google, Meta, and Quantcast tracking. Early reads were unreliable, so the brief's kill thresholds (CPL under $50, cost per funded under $350) were never genuinely measurable.
- **The KPIs and the reporting did not match.** The brief targets demo CPL and cost per funded. Reporting measured submitted applications, a different funnel stage. We have no clean demo → funded → traded read, so we cannot grade Q2 against the approved targets.
- **Meta ran on the wrong objective.** A traffic objective optimized for cheap clicks and landing-page views that mostly never became real site sessions (in-app browser loss). 108 starts and 1 submission is what optimizing for traffic instead of applications produces.
- **The funnel leaks at start to submit.** Azerion generated 1,398 starts but 43 submissions (about 3%); Meta went 108 to 1. Media created intent cheaply and the application flow lost it. That is the binding constraint, and the quarter did not address it.

## What we learned
- **Spanish search converts, and it is the clearest path.** Google Search produced submitted applications at $200, with Track B at $122–169. Brand Search hit its cap with demand still on the table.
- **Track B beats Track A on efficiency.** The experienced bilingual trader looking for pro tools in Spanish (Hispanic Alex) outperformed the emerging/trust persona (Luis) in the channels that ran. Early signal, not a final read.
- **Programmatic builds starts and pools, it does not close.** Azerion creates application starts and a retargeting audience at $18.93. Its value is upper and mid funnel, not last-click submissions.
- **Objective design decides Meta's outcome.** On a traffic objective Meta returns vanity LPV and CTR. It has to run on conversions and be judged on GA4 sessions to evaluate fairly.
- **Tracking has to be live and validated before launch.** Spending the first weeks instrumenting the campaign invalidated the early decisions the kill criteria depended on.
- **Media is cheap and abundant. The landing page and application flow are the real lever.**

## What went well
- **A proven conversion path emerged:** Google Search plus Track B, at an efficient submitted-app CPA, with clear evidence of unmet brand-search demand.
- **The persona test produced a usable signal** at small scale: lead with Track B, keep testing Track A.
- **Azerion built a large, cheap retargeting pool** (1,398 starts) that Q4 can activate.
- **Tracking is now in place.** We fixed Google, Meta, and Quantcast measurement, so Q4 can start clean. The brand-gap thesis (regulated, Spanish-first) held up where we could measure it.

## Conclusions and recommendations for Q4
1. **Instrument first, launch second.** Stand up GA4 per-channel, CM360/server-side, and the full demo → submitted → funded → traded events before any spend. Do not launch until the funnel is measurable end to end. Everything else depends on this.
2. **Restate the KPIs to match what you measure.** Either align the brief's targets (demo CPL, cost per funded) to the events you actually track, or commit to tracking demo and funded directly. One KPI per funnel stage.
3. **Fund the proven path first.** Lead Q4 with Google Search and Track B, and remove the Brand Search budget cap before anything else. It is the highest-confidence spend you have.
4. **Move Meta to a conversion objective** optimized to submitted applications and judged on GA4 sessions, not LPV or CTR. Retarget the Azerion and Meta application-start pools.
5. **Run Azerion as a starts-and-pool engine.** Concentrate on the top converting sets (Language Broker, Broker 1, Trusted Broker) and push the start-to-submit rate. Cap Quantcast or tighten it toward higher-viewability supply, and stop counting view-through as submissions.
6. **Fix the application flow.** Confirm both landing pages (Trust and Platform) are live and mobile-first, find the start-to-submit drop, and set a measurable Q4 lift target. This unlocks every channel at once.
7. **Decide the test channels deliberately.** Either run TikTok, LinkedIn, and Native properly in Q4 with clean tracking and the original kill criteria, or deprioritize them on the record. Do not carry an untested "test" forward.
8. **Plan realistic pacing.** With roughly 12% of the annual budget deployed, scale the proven converters with the funnel fixed rather than spreading thin across nine channels at once.

**Bottom line for the strategist:** Q2 was a delayed soft launch. It validated one thing (Spanish search plus experienced-trader messaging converts) and exposed one thing (measurement and the application funnel, not media, are the constraint). Make Q4 smaller in channel count, sequenced behind tracking, and concentrated on the proven path while the funnel gets fixed.
