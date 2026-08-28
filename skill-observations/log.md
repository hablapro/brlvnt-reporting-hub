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
