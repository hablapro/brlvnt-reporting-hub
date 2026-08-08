# FOREX.com Monthly Reporting

Monthly paid-media performance reporting for FOREX.com (StoneX), two entities:
**GGMI** (Gain Global Markets Inc, LATAM/Mexico) and **GCG** (GAIN Capital
Group LLC, US Hispanic).

**Reporting only. Never mutate an ad account, tracking config or production
system from this repo.** Actions go to `recommendations/<client>/<sub-client>/`
for whoever owns execution.

## Read before working

| Task | Read first |
|---|---|
| Running a monthly cycle | `docs/RUNBOOK.md` |
| Writing anything client-facing | `docs/DOCTRINE.md` |
| Building or editing a deck | `docs/DESIGN-SYSTEM.md`, `lib/housestyle.py` |
| A tool behaving oddly | `KNOWN-BUGS.md` |
| Anything unfamiliar about the account | `docs/HANDOVER.md` |

`PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md` explains why the rules exist.
Read it at cycle start.

## The two standing questions

Before pulling data for a new month:

1. What does the client already hold? Tracker pages, dashboards, comms since
   the last report.
2. How is the agency scored? The primary conversion event and cost per it.

Roughly a third of the June 2026 cycle was rework, and nearly all of it traced
to skipping these.

## Workflow

Kickoff, pull, QA, model, narrative, build, deliver. A phase does not start
until the previous one closes. QA before modeling, modeling before commentary.
Full detail in `docs/RUNBOOK.md`.

Start a month with `./scripts/new_month.sh <ggmi|gcg> <YYYY-MM>`.

## Data sources

MCP first, always. Eight servers in `.mcp.json`.

| Channel | Entity | Source | Account |
|---|---|---|---|
| Bing (spend, clicks, config) | GGMI | `bing-ads` | `31003116` |
| Bing conversions | GGMI | **`sa360` only** | customer `5372690580`, login `9697709980` |
| Google Ads | GCG | `google-ads` | `4781995752` |
| Meta | both | `meta-ads`, shared account, split by campaign name | `act_1699453997689551` |
| Quantcast | both | `quantcast` | `9969644` |
| Azerion | both | vendor XLSX into `data/sources/` | no API |
| GA4 | GGMI / GCG | `google-analytics` | `508849216` / `325353267` |
| Organic | GGMI | `gsc` | forex.com |

GGMI conversions are offline-imported, so the Bing API reads zero. SA360 is the
only valid source.

## Non-negotiable rules

- **Client-facing spend equals the client budget tracker.** Recalculate
  downstream silently; reconciliation detail never reaches a client artifact.
- **Never sum conversions or blend CPA across channels.** Different events,
  different systems. Total row gets a dash plus the footnote.
- **Never blend GGMI and GCG.**
- **The agency is scored on submitted applications** and cost per submitted
  application. Downstream steps are the client's journey, described neutrally.
- **Judge Meta against its own objective.**
- **Geo every month:** GGMI is Mexico-only, GCG is US. Check delivery, not just
  the targeting setting.
- **Programmatic every month:** site list, refreshed disallow list, viewability
  against the 70% floor.
- **Data lives in workbooks,** not markdown. Markdown is for narrative and QA.
- **Disclose every tool failure** on the first line of the handoff. Two
  retries maximum, then stop and record it in `KNOWN-BUGS.md`.
- **Commit locally. Never push without approval.**

## Output

Google Sheets first. Deliverables are a formatted Sheet and a deck per entity,
both generated from the model, never hand-keyed. Deck builders import
`lib/housestyle.py`; never redefine a colour or a font in a build script.

**Once Renzo edits the Google Slides file, it is canonical.** Never re-upload a
built PPTX over it. Edit via `gws slides batchUpdate` replaceAllText, longest
strings first, verifying `occurrencesChanged`. Verify every upload by reading
the content back.

## Gates before delivery

```bash
python3 scripts/verify_numbers.py reports/forex/<entity>/<month>/figures.json <deliverable>
python3 scripts/protection_scan.py <deliverable>
```

Plus render QA (page count against the source, then look at every slide) and a
walk through `docs/DOCTRINE.md`. A BLOCK is a stop. If a flagged word is
genuinely required, get it ruled on and add the exception to the doctrine, not
silently to the script.

## Specialist routing

Use the global Berelvant roster rather than defining agents here:
`reporting-strategist` for the narrative, `analytics-diagnostician` for GA4 and
tracking, `ppc-expert` for Bing and Google, `meta-ads-specialist` for Meta,
`programmatic-display-specialist` for Quantcast and Azerion,
`strategy-advisor` for QBR strategy sections.

Load the gate skills before the work starts: `dataviz` for any chart,
`stop-slop` for any prose, `karpathy-guidelines` for any code change.
