# GGMI scenario table rebuilt against planned September $205,000 — for Corah

**Mission:** cc0a693f (authoritative baseline: approved GGMI tracker, Renzo 08/06).
**From:** Marco (paid-media). **Date:** 2026-08-27.
**Self-check:** `verify_scenarios.py` — all asserts pass.

## Heads-up first: same-asset collision

The live draft `GGMI-spend-reduction-scenarios-DRAFT.md` was being actively rewritten by another session while I worked (title now "Reallocating Media Weight"; file changed 3x in ~25 min). I did **not** overwrite it. That draft already folds in the resolved Azerion data and its scenario **spend decisions are sound**. Its one gap against this mission: it measures savings against **approved August $125,000**, not the **planned September $205,000** the mission requires. This artifact re-expresses the *same spend decisions* against the $205K baseline. Nothing here contradicts the live draft's numbers — it completes the framing.

## Rebuilt scenario table (planned September $205,000 baseline)

Spend per line matches the live draft §4 exactly. Only the baseline and the held new lines are added.

| Line | Approved Sep | Controlled | Deep | Recommendation |
|---|---:|---:|---:|---|
| Bing | $30,000 | $30,000 | $30,000 | Fund to approved — only proven CPA ($379) |
| Quantcast | $35,000 | $10,968 | $0 | Retire superseded (0 results); hold half of productive as monitored |
| Azerion | $35,000 | $21,478 | $0 | Halve in Controlled, cut in Deep — CPA $978, rising every month, 2.6x Bing |
| Native | $25,000 | $0 | $0 | Cut — no attributed applications, was overpacing 115% |
| Meta | $30,000 | $0 | $0 | Hold — paused, no GGMI history to size a $30k relaunch |
| TikTok | $10,000 | $0 | $0 | Hold — never run for GGMI this FY, untested |
| Strategic Partnerships | $40,000 | $0 | $0 | Hold — not running, largest and least-evidenced item |
| DOOH | $0 | $0 | $0 | Already cancelled |
| **Total** | **$205,000** | **$62,446** | **$30,000** | |
| **Reduction vs planned Sep** | | **−$142,554 (69.5%)** | **−$175,000 (85.4%)** | |
| Reduction vs Aug in-market ($121,558) | | −$59,112 (48.6%) | −$91,558 (75.3%) | |

Scenarios differ by **$32,446/mo** (Azerion halved $21,478 + Quantcast $10,968). Meaningfully distinct.

## The honest September story (mission instruction #2 + #3)

- September's $205,000 plan is **+55% over August's approved working media of $132,000**.
- **Every dollar of the $73,000 net increase is new/returning lines**: Meta +$30k (returns), TikTok +$10k (new), Partnerships +$40k (new), offset only by removing the already-cancelled DOOH (−$7k). That is **$80,000 of untested commitment.**
- **Both scenarios hold all three at $0.** A pullback that quietly let them launch would not be a pullback. Each is recommended-against explicitly in the table above.

## August transition month (context, mission instruction #1)

Program is at **97% of approved active budget ($121,558 / $125,000)** — not underspending. The problem is allocation: Bing (best CPA) underpaces at 62%; Azerion (worst CPA, rising) overpaces at 123%; Native (no attributed apps) overpaces at 115%.

## Open items for you / Renzo (defaults attached)

1. **Baseline framing.** Live draft = Aug $125k; mission = Sep $205k. **Default: adopt the Sep $205k framing** in the client doc per the mission, keeping the Aug table as transition-month context. *(This is the only real change needed to the live draft.)*
2. **Azerion in Controlled: halve ($21,478) vs cut ($0).** Live draft halves it; the evidence (CPA rising every month, 2.6x Bing) also supports a full cut. Both satisfy the no-auto-protection ruling. **Default: keep the halve** (live draft's call) — reversible in 24h, keeps the only other line producing measurable applications.
3. **Model-sync nit:** figures.json still carries `deep_bing_only 18533`, but the live draft's Deep funds Bing to $30,000. If the $30k-Bing Deep is final, figures.json should be updated to match before the analytics gate runs on the integrated doc.

## Gate note

No new measured figures introduced — only the Sep-plan denominator arithmetic (self-verified). The measured inputs (Bing $379, Azerion $978 series, Quantcast decomposition, Aug 97% pace) are the already-verified figures.json values the live draft uses. The integrated client doc should still pass the analytics-diagnostician numbers gate before it reaches Renzo.
