# Skill Observation Log

Observations captured during task-oriented work.

**Status key:** OPEN = not yet actioned | ACTIONED (YYYY-MM-DD) = skill
updated/created | DECLINED (YYYY-MM-DD) = user decided not to pursue,
resolved statuses always carry their resolution date

---

## 2026-08-28

### Observation 1: Establish artifact lineage before validating the numbers

**Status:** OPEN
**Date:** 2026-08-28
**Session context:** Building a cross-market evidence base from current proposals, working drafts, raw exports, normalized workbooks, and append-only calculation files.
**Skill:** data-analytics:analyze-data-quality
**Type:** open-source
**Phase/Area:** Source discovery and validation order

**Issue:** Numeric validation alone did not identify the authoritative planning artifact. Multiple current-looking drafts, backup files, declared-data files, and later final-delivered documents contained different scenario states. A technically correct value from a superseded artifact could therefore be reintroduced into a new deliverable.

**Suggested improvement:** Add an artifact-lineage gate before field-level validation: identify the current decision artifact, distinguish measured data from planning narrative, label current, historical, and superseded sources, and document field-level exceptions when a declared-data file mixes current values with append-only history.

**Principle:** Data quality starts with deciding which artifact is authoritative for which claim; validating a number from the wrong document preserves the wrong answer more precisely.

### Observation 2: Separate authorization from committed launch spend

**Status:** OPEN
**Date:** 2026-08-28
**Session context:** Revising a paid-media recommendation where the total remained commercially viable but no established channel had evidence to absorb the final increment at launch.
**Skill:** paid-ads
**Type:** open-source
**Phase/Area:** Budget scenario design and conditional allocation

**Issue:** A single Recommended Spend number can create pressure to deliver every authorized dollar even when channel capacity depends on a mid-period performance signal. Lowering the recommendation discards useful flexibility, while forcing the full amount weakens the evidence logic.

**Suggested improvement:** Add a scenario pattern that distinguishes maximum authorization from committed launch spend. Hold the difference as a named reserve with eligible existing lines, numeric release gates, an approval rule, and an explicit statement that the reserve remains unspent when no line qualifies.

**Principle:** A budget ceiling should preserve optionality without becoming a delivery obligation; conditional capacity belongs behind a measurable release gate.

## 2026-08-31

### Observation 4: Reconcile narrative claims to runnable analysis outputs

**Status:** OPEN
**Date:** 2026-08-31
**Session context:** Reviewing a client findings report whose headline claims were derived from a reproducible workbook analysis package.
**Skill:** data-analytics:validate-data
**Type:** open-source
**Phase/Area:** Report validation and calculation lineage

**Issue:** Several narrative claims were numerically plausible but did not follow from the runnable checks as written. One script returned an empty analytical subset because a mislabeled numeric column was filtered as a currency code, while the report used manually derived figures without preserving that corrected calculation path. Other copy treated missing dates as proof that an event never occurred even though status fields contradicted that inference.

**Suggested improvement:** Add a claim-lineage gate that maps every material narrative claim to one runnable calculation and checks status, timestamp, and amount fields for contradictions. Fail the validation when the source script returns an empty subset, when a report uses a different calculation than its recorded output, or when missingness is interpreted as a negative event without a corroborating status.

**Principle:** Reproducible analysis requires the delivered claim, the runnable calculation, and the recorded output to agree; plausible arithmetic is not enough when field semantics or missingness can reverse the conclusion.

### Observation 5: Keep downstream constraints in their proper portfolio role

**Status:** OPEN
**Date:** 2026-08-31
**Session context:** Resetting a paid-media strategy after a downstream KYC finding had been turned into a blanket spend-release gate for the whole portfolio.
**Skill:** paid-ads
**Type:** open-source
**Phase/Area:** Portfolio strategy and full-funnel planning

**Issue:** A material downstream constraint dominated the initial recommendation even though the source data lacked channel lineage and could not identify which media created stronger funded customers. The resulting plan reduced brand, demand-creation, and learning investment without evidence that those channels caused the downstream loss.

**Suggested improvement:** Require portfolio recommendations to assign distinct jobs and role-level KPIs to brand, demand creation, intent capture, audience quality, CRM, and learning. Treat downstream constraints as forecast, measurement, and client-dependency inputs unless source-linked evidence shows that they should gate a specific channel.

**Principle:** A full-funnel portfolio should not collapse into one downstream bottleneck when the evidence cannot connect that bottleneck to channel performance.
