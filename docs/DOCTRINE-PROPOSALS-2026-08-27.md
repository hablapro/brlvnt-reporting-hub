# Doctrine proposals, 2026-08-27

Four proposed edits to `docs/DOCTRINE.md`, arising from the GGMI August cycle.
Per the retro-loop rule these are proposals, not applied. Each carries a
recommended default so this can be settled in one pass.

Evidence for all four is in `PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md`
addendum A1 to A8, and in the two new `KNOWN-BUGS.md` entries.

---

## Proposal 1: a figure is not accepted until it is re-derived from source

**The failure.** Three figures in one `figures.json` were wrong at the same
time, each carrying a plausible provenance sentence that nobody reproduced.
The Azerion one came from a mis-picked spreadsheet cell, was wrong by 6.8x,
and inverted a finding: it produced "Azerion collapsed 84%" and a false 65%
programme pacing when the channel was running at 123% of its approved budget.
The document was rebuilt around that false finding before Renzo caught it.

**Proposed rule.** A figure does not enter `figures.json` until it has been
reproduced from source in a separate pull or read. Recording where a number
came from is a claim about it, not a check on it. The `spend_basis` field
states the source; a second, independent derivation is what admits the figure.

**Where.** New rule under the analytical standards section, alongside "use the
authoritative number" and "reconcile detail to totals".

**Cost.** One extra pull per figure at model-build time. Against roughly four
hours of rework in this cycle and a client document rebuilt twice.

**Default: adopt.**

---

## Proposal 2: the no-blending rule covers counts, not only costs

**The failure.** The draft summed Bing and Azerion submitted-application
counts into a single total four paragraphs after stating that the two are not
comparable. Bing counts come from SA360 floodlight attribution and Azerion
counts from the vendor's own reporting; a prospect who saw an Azerion ad and
clicked a Bing ad is plausibly in both.

The existing rule reads "never sum conversions or blend CPA across channels",
which does cover this. I read it as being about CPA and totals rows in tables
and did not apply it to a modelled projection. That is a reading failure, but
the wording invites it.

**Proposed rule.** State explicitly that the prohibition covers modelled and
projected counts as well as reported ones, and that channel-level figures are
presented independently with a do-not-sum note wherever two attribution
systems are in play. If a deduplicated source-level count exists, say so
explicitly and cite it; only then may counts be combined.

**Where.** Amend the existing non-negotiable rather than adding a new one.

**Default: adopt as an amendment.**

---

## Proposal 3: derived artifacts are rebuilt whenever the model changes

**The failure.** `figures.json` was corrected at 14:37 with an explicit defect
fix. The deliverable had been generated at 14:16 and was never rebuilt, so the
model was correct while the document still carried the defect, and the stale
document was reviewed as if current.

**Proposed rule.** Any change to `figures.json` invalidates every artifact
generated from it. Rebuild and re-verify before the artifact is read, reviewed
or sent. Where a rebuild is deferred, the artifact is marked stale in its own
first line, not in a note elsewhere.

**Where.** The gates-before-delivery section.

**Default: adopt.**

---

## Proposal 4: a data gap is declared only after a folder inventory

**The failure.** The draft named "no forward approved monthly budget in the
source material" as its single data gap. The client's approved budget tracker
was in the same directory, dated, with September and Q4 broken out by channel.
It changed the baseline, both headline percentages and the recommendation. The
document also asked the client to supply something they had already supplied.

**Proposed rule.** Before declaring a data gap in a client-facing artifact,
list the contents of the report month's directory and the client-supplied
inputs, and state in the QA note that this was done. A gap that turns out to
be on disk is worse than a gap, because it asks the client for something they
have already given us.

**Where.** The gates-before-delivery section, next to the protection scan.

**Default: adopt.**

---

## Not proposed as doctrine

Four other lessons from this cycle are recorded in the retrospective addendum
and do not need doctrine text, either because a rule already exists or because
they are judgement rather than process:

- Verify inherited third-party research to the same standard as our own pulls
  (A4). Covered by the existing source-labels rule.
- Claim scope is as checkable as claim truth (A5). Written to memory as
  `feedback_claims_must_not_exceed_evidence`.
- Programmatic checks are not review; render and look (A6). Already added to
  `CLAUDE.md` Output this session, with `scripts/format_doc.py`.
- Do not self-correct past the instruction (A7). Judgement, not process.
