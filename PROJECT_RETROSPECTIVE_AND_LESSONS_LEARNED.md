# Retrospective — June 2026 Reports + Q3 FY2026 QBR (GGMI + GCG)

Written 2026-07-17 at session close, covering the full arc from "finalize the June Performance report" (2026-07-16) through the GCG build and both agency-protection passes (2026-07-17). Written to be blunt. The goal is fewer revision rounds next cycle, not a record of what went well.

## 1. The original objective, and what it became

The request started as: finalize the GGMI June report (Sheet + deck, May pattern). It became, through nine distinct expansions: GGMI June deliverables → client-tracker spend alignment → Q3 QBR section → QBR-first restructure with a blended Summary lead → Renzo's market-volatility slides reviewed and fixed in place → a full GCG June build (pull to deliverables in one day) → Azerion/Native integration → two agency-protection passes → geo framing aligned to prior client comms. None of these expansions was wrong; the problem examined below is how many of them were reactions to something I had already built the other way.

## 2. Decisions made and how direction evolved

- **Spend basis:** model/raw numbers → client budget tracker numbers, silently adjusted (Azerion $35,026 GGMI, Meta $30,711 GCG), with adjustment detail internal-only.
- **Deck architecture:** May's 7-slide format → mirror of the client-sent 11-slide May final → 17-slide QBR-appended → **QBR-first** (Summary lead slide in the client's own monthly-table format, quarter story before June detail). This is now the standing shape for quarter-close decks.
- **Agency accountability:** cost-per-funded/traded reported naively → the KPI doctrine: the agency is measured on submitted applications and cost per submitted application; approval/funding/activation belong to the client's journey and are described neutrally, never owned, never blamed.
- **Sensitive topics:** each ended with the same pattern — acknowledged, quantified with the number the client already saw, marked corrected, verified next month. Bing geo ($8,612, not SA360's $12,637), Meta objective slip (forward-looking only), Native ($3,645 framed as an intentional small first flight reporting fully in July).
- **Tooling:** the canonical-deck rule (a Renzo-edited Google Slides file is never overwritten; edits go through `gws slides batchUpdate` replaceAllText with occurrence-count verification) and the discovery that gws serves every Google API.

## 3. Feedback Renzo gave more than once, or had to spell out

1. **"Client materials must match what the client already has."** This arrived three separate times in three costumes: the budget tracker for GGMI spend, the tracker again for GCG, and the Bing Ads review deck for geo figures. It is one rule and I learned it piecewise. The rule: before writing any number a client can cross-check, find out what number the client already holds.
2. **"Protect the agency"** was implicit in earlier feedback (polished deliverables, no competitor names) but I only ran a systematic protection pass when explicitly asked — twice, once per deck. It should have been part of the build, not a review stage.
3. **Gaps read as plans, not holes.** "Pending vendor detail" (Native) had to be corrected to "intentionally small pilot, full report in July." Same instinct as the QBR framing: never hand the client an open question.

## 4. Assumptions and approaches that caused delay

- **I trusted documentation over a 5-second test.** `gws --help` lists five services, so I burned a Zapier timeout detour, a failed OAuth token exchange, and a permission-classifier block before Renzo asked "why don't you use gws?" — and `gws slides` simply worked. Cost: ~8 tool calls and a user intervention.
- **I approved-plan-then-rebuilt anyway.** The QBR placement was proposed in prose ("insert after the Quantcast slide"), approved, built — then fully restructured when Renzo saw it. Prose hides order. A one-line slide-order mock (1. Title, 2. Summary, 3. Q3...) would have surfaced the disagreement before the build.
- **I reported platform truth into a client context.** SA360's $12,637 non-MX was correct and still wrong, because the client had been told $8,611.65 from Bing's own UI. Two rounds of geo edits instead of zero.
- **Substring replacement bit me twice.** "2 / 17" matched inside "12 / 17" in both the pptx path and nearly in the API path. The fix (longest-first ordering) is now in the muscle memory, but round one shipped two wrong footers.
- **The Drive connector's base64 upload silently produced an empty Sheet.** Caught only because I verify content after delivery. Verification-after-upload is not optional.

## 5. Where I overcomplicated, added noise, or misapplied feedback

- The original GGMI narrative applied "raw Azerion spend" as a new client-facing basis — a basis change the client never asked for, which Renzo then had to overrule with the tracker. I treated an internal bookkeeping preference as a reporting decision.
- I put cost-per-funded ($26 → $3,762) on a lead slide with zero context because the client's reference format had the row. Mirroring a format is not the same as inheriting its safety; the near-zero-base footnote existed only after the protection pass.
- The first Q3 applications blended-CPA math offered three candidate denominators in my head and I picked one without surfacing that cost-per-submitted-app (the agency KPI) wasn't on the slide at all. The single most protective number in both decks was added last.
- Self-indicting phrasing survived my own stop-slop pass: "extra budget bought worse auctions," "the inventory the June campaigns bought," "for most of H1." Stop-slop catches AI tells; it does not catch statements against interest. Those need their own check.

## 6. What Renzo could have provided earlier

- The **client budget tracker pages** at kickoff (both sub-clients). Every client-facing number depends on them; they arrived after the first build.
- The **Bing Ads review deck** existed before I wrote any geo framing; knowing prior client comms on a sensitive topic is a build input, not a review input.
- The **agency KPI doctrine** (submitted apps = our goal; downstream = theirs). One paragraph, stated on day one, would have shaped every table.
- The **QBR-first preference and the reference slide** at the moment the QBR was requested rather than after the first version.
- The Meta objective slip context ("I don't know what happened") — earlier knowledge that this was an internal miss would have shaped the Meta slides from the start instead of after review.

None of this is blame; most of it he provided the moment its absence showed. The fix is a kickoff checklist (Section 9) so its absence shows before the build.

## 7. What I should have identified, inferred, or challenged sooner

- The May build status already recorded "client-confirmed" Quantcast reconciliations — evidence that client-side numbers override platform pulls. I had the pattern in the repo and didn't generalize it until instructed.
- When Renzo said "adjust the final spend... and adjust whatever calculations you need. Do you understand?" — that was the moment to ask for every other client-held artifact (tracker pages, dashboards, prior comms) in one request, instead of receiving them across four messages.
- The 49% geo figure went into a client deck without me asking "has this been communicated, and with what number?" — for a compliance-adjacent topic that question is mandatory.
- I should have proposed the protection pass unprompted after the first deck build. Renzo asked "as always, I want to protect the agency" — the "as always" says this was already the standard.

## 8. What we should both do differently on resume

**Me:** run the Section 9 checklist before building; write client-visible numbers only from client-held sources; run the protection scan (Section 10) before handing anything over, not on request; test a tool before declaring it can't do something; keep the deliverable pipeline (scripts → verify → upload in place → verify again) exactly as it now works.

**Renzo:** at cycle start, drop in one message: current tracker pages (both sub-clients), any client dashboards to reference, any client comms sent since the last report on sensitive topics, and any new framing rules. Approve slide ORDER (the numbered list), not just slide content. Flag "this metric is not ours" the moment a draft scores the agency on it.

## 9. Kickoff checklist for the next report cycle (July)

1. Client budget tracker pages (GGMI + GCG) — spend truth.
2. Client funnel/BvA dashboards — outcome truth (funnel rows only; their spend rows are broken).
3. Vendor files (Azerion both subs, Native first full read — **promised to the client for July, mandatory**).
4. Any client-facing comms since June on sensitive topics.
5. Confirm carry-overs: GGMI geo verification (~$8.6K/month redirected — deck promises July confirms), SA360→GA4 link restatement (~4x paid search, must be flagged), Meta conversion-objective proof (both subs), placement-audit outcome, blocklist/viewability-floor status, client questions A–D.
6. Then pull → QA vs tracker → model → narrative (one approval gate) → build QBR-first via `tools/forex-*-june-2026/` script pattern → protection scan → stop-slop → verify → deliver in place → tracker/billable → logs.

## 10. The protection scan (now a standard build step)

Before any client deliverable leaves the shop, check every slide for:
- **Metrics we don't control tied to our spend** (cost per funded/traded) — context or replace with cost per submitted application.
- **Statements against interest**: any sentence where the grammatical actor buying/causing a bad outcome is us ("bought worse auctions," "the campaigns bought," "our buying skewed"). Reframe as diagnostic-that-produced-the-map, delivery/objective mechanics, or benchmark-isolated cause — facts unchanged.
- **Numbers the client can cross-check** against sources they hold — match theirs.
- **Open questions on the page**: every problem ships with its fix and owner; every gap reads as a plan with a date.
- **Commitments made in prior decks** (May: "conversion campaigns launch June"; June: "full Native pilot in July," "July confirms geo") — either delivered, sequenced with a rationale, or expect the question live.
- **Time-scope creep**: don't extend a bad fact backward ("for most of H1") when the reporting month plus the fix is the story.
- **Forbidden vocabulary in client materials**: fee, raw, adjustment, reconciled, basis, violation, compliance, internal. Verify programmatically.

## 11. Standing rules carried into future sessions (all in memory)

- Client-facing spend = client budget tracker; adjustments recalculated silently; reconciliation detail internal only.
- Agency KPI = submitted applications at low cost per submitted app; downstream neutral ("application-review and account-activation journey").
- Quarter-close decks are QBR-first: Summary (client-format monthly table + bullets) → quarter slides → traffic/insight slides → month detail → close.
- A Renzo-edited Google Slides file is canonical: never re-upload a built PPTX over it; edit via `gws slides batchUpdate` replaceAllText, longest-strings-first, verify occurrencesChanged; keep local/Drive PPTX as exports of it.
- gws is discovery-driven (every Google API); shared drives need `supportsAllDrives:true`; never use the Drive connector's base64 upload for Office files; verify uploads by reading content back.
- Every report: Quantcast site list + disallow refresh; geo check per sub-client; conversions never summed across channels; Meta judged per its objective; commit locally, never push.
- Build scripts live in `tools/` in the repo (the May /tmp loss does not repeat).

## 12. Why it took longer than necessary — the honest one-paragraph answer

Roughly a third of this session's work was rework: rebuilding numbers after the tracker arrived, restructuring a deck whose order I had already built the other way, re-editing geo framing twice, and adding protection and the agency KPI after the fact. Nearly all of it traces to one root cause: **I built from the best data I had instead of first asking what the client already holds and how the agency wants to be scored.** Those are two questions. They cost one message each. Everything else — the tooling detours, the substring bug, the empty-upload catch — was minor by comparison and is now either fixed or fenced with verification. Next cycle starts with the two questions.
