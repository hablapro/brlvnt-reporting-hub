# August 2026 FOREX.com September Planning, Build Status

Updated 2026-08-28.

## Current state

The evidence-first revision of the GCG and GGMI September Recommended Spend and Minimum Spend proposals is complete.

**Evidence base:** `reports/forex/September_Budget_Evidence_Base.md`

**Revised proposals:**

- `reports/forex/gcg/2026-08/GCG-September-budget-proposal-MATEUS-REVISION.md`
- `reports/forex/ggmi/2026-08/GGMI-September-budget-proposal-MATEUS-REVISION.md`

## Final September decisions

### GCG, FOREX.com US Spanish

- Recommended authorization: up to **$110,000**
- Committed at launch: **$105,000**
- Conditional reserve: **$5,000**, available only to qualifying established lines
- Minimum Investment Plan: **$55,000**
- New or returning September initiatives: **$0**

### GGMI, FOREX.com Mexico

- Recommended Plan: **$90,000**
- Minimum Investment Plan: **$60,000**
- New or returning September initiatives: **$0**
- Azerion remains at **$0** until written Mexico delivery controls and a minimum 95% Mexico delivery standard are confirmed. Confirmation is required by September 3. If the gate is not met, neither plan remains authorized as designed and the allocation returns for a revised decision.

## Decision design

Every retained or tested line now has:

- a defined channel role;
- an evidence classification and confidence statement;
- a hypothesis and media action;
- a KPI and numeric threshold;
- a valid evaluation window;
- explicit meet, miss, and low-volume actions; and
- an operating condition identifying agency, shared, or client and system dependencies.

The GCG recommendation separates maximum authorization from committed launch spend so the final $5,000 remains optional rather than becoming a delivery obligation. The GGMI recommendation makes geographic control a launch condition rather than treating it as a retrospective reporting caveat.

## QA status

- Budget arithmetic and scenario totals: pass
- Decision-band and low-volume assertions: pass
- Protection scan: 0 blocking findings, 0 warnings
- Markdown whitespace check: pass
- Client-safety and house-language scan: pass
- Independent reporting-strategist review across correctness, traceability, decision usability, and client risk: pass

## Source boundary

The Aug 27 Renzo-final proposals in `reports/forex/_final-delivered/2026-09/` remain the pre-feedback baselines. August draft and backup files remain working history. Channel outcomes use different measurement methods and are not added into a cross-channel application total.

## Tracking

Bead `Reporting-Analytics-7u7` is complete. No live media or tracking changes were made.
