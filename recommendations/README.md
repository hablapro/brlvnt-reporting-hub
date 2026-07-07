# Recommendations — Handoff Queue

This repository is **reporting only**. It pulls data, runs QA, models, and produces analysis and dashboards. It does **not** execute changes in any ad account, tracking platform, or production system.

Anything that requires an action — a bid change, a budget move, a geo exclusion, a negative-keyword add, a tracking/config change, a creative edit — gets written here as a recommendation, then handed to the agent or operator who owns execution (paid-media operator / PPC execution, analytics/tracking, etc.).

## How this folder works

```
recommendations/
  <client>/<sub-client>/
    <deliverable>.md      # findings + a mutation/action table (entity, current, proposed, reason, $ at stake, rollback)
```

## Rules

- **No execution from this repo.** Reporting agents pull and analyze; they never push mutations.
- Every action item states the entity, the current state, the proposed change, the reason, the dollars at stake, and the rollback.
- Production ad-account or tracking changes still require explicit human approval before the execution agent runs them.
- Once an item ships, note the outcome (done / date / by whom) or archive it.

## Current items

| Client | File | Summary | Priority |
|---|---|---|---|
| FOREX / GGMI | `forex/ggmi/GGMI-Bing-SA360-remediation-June-2026.md` | Bing bidding is blind (Manual CPC, conversions excluded from bidding); ~$8.2K/mo geo leakage. 8 fixes. | HIGH |
| FOREX / GGMI | `forex/ggmi/GGMI-Meta-recommendations-June-2026.md` | Meta traffic objective buys 55+/65+ (63% of spend); FB-only, thin creative; conversions unvalidated. 8 fixes. | HIGH |
| FOREX / GGMI | `forex/ggmi/GGMI-Quantcast-disallow-list-June-2026.md` (+ `.txt` block list) | 49 low-viewability / off-audience sites = $10.7K (32% of GGMI Quantcast spend) to block. Refresh monthly. | HIGH |
| FOREX / GGMI | `forex/ggmi/GGMI-Azerion-data-request-June-2026.md` | Azerion June report gaps: undefined conversions/funnel, overlapping weeks, blank attribution, missing geo/site/format/creative breakdowns. Send to Azerion. | HIGH |
