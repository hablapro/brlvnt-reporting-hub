# {{MONTH_PRETTY}} Report — Build Status & Resume Handoff ({{ENTITY_LABEL}})

Cycle opened: YYYY-MM-DD. Reporting only; no account mutations from this repo.

Kickoff per `docs/RUNBOOK.md` phase 0. The two standing questions, answered
before any pull:
1. What does the client already hold for {{MONTH_PRETTY}}? (tracker pages, dashboards,
   comms sent since the last report) — answer:
2. How is the agency scored this month? (primary conversion + cost per it) — answer:

## Channel status

| Channel | Data pulled | QA | In model | Notes |
|---|---|---|---|---|
| Bing / SA360 | — | — | — | conversions MUST come from SA360, not the Bing API |
| Meta | — | — | — | judged against its own objective |
| Quantcast | — | — | — | site list + refreshed disallow list required |
| Azerion | — | — | — | vendor xlsx into `data/sources/`; tech fee internal only |
| Google Ads | — | — | — | GCG only |
| GA4 / client funnel | — | — | — | funnel rows only; client spend rows are broken |

## Carry-overs from last month
<!-- Every open item from the prior BUILD-STATUS and every commitment made in
     the prior deck. A commitment the client was given is either delivered,
     re-sequenced with a reason, or asked about live. -->

## Open items before this month can ship
<!-- Numbered. Each one names what is blocked and who owns it. -->

## Gate status
| Gate | Run | Result |
|---|---|---|
| QA reconciliations | — | |
| Tracker reconciliation | — | |
| `scripts/verify_numbers.py` | — | |
| `scripts/protection_scan.py` | — | |
| Render QA (slide count + visual) | — | |
