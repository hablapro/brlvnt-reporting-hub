# FOREX.com Monthly Reporting

Produces the monthly paid-media performance report for FOREX.com (StoneX)
across two entities: **GGMI** (LATAM, Mexico) and **GCG** (US Hispanic).

Each cycle delivers, per entity, a formatted Google Sheet and a client-facing
deck, built from validated platform data and reviewed against a fixed set of
gates. Reporting only. This repo never changes an ad account.

Driven from [Claude Code](https://claude.com/claude-code), which loads
`CLAUDE.md` and the MCP servers in `.mcp.json` when you open the directory.

---

## Start here

| You want to | Read |
|---|---|
| Set up a machine from scratch | [`docs/SETUP.md`](docs/SETUP.md) |
| Run this month's report | [`docs/RUNBOOK.md`](docs/RUNBOOK.md) |
| Know what may go in a client artifact | [`docs/DOCTRINE.md`](docs/DOCTRINE.md) |
| Know what is missing or fragile | [`docs/HANDOVER.md`](docs/HANDOVER.md) |
| Build or change a deck | [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md), `lib/housestyle.py` |
| Diagnose a tool that is misbehaving | [`KNOWN-BUGS.md`](KNOWN-BUGS.md) |
| Understand why a rule exists | [`PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md`](PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md) |

New to the account: `docs/SETUP.md`, then `docs/HANDOVER.md`, then
`docs/RUNBOOK.md`. Roughly two hours of reading, against a cycle that has
historically lost days to items covered in them.

---

## The cycle

Seven phases per entity, twice a month. Full detail in `docs/RUNBOOK.md`.

| Phase | Does | Closes on |
|---|---|---|
| 0 Kickoff | Scaffold the month, gather client-held inputs | Two standing questions answered |
| 1 Pull | One channel at a time, into workbooks | Every channel reconciles internally |
| 2 QA | Reconcile against the client tracker and across sources | Every check resolved |
| 3 Model | Cross-channel model, declare `figures.json` | Spend basis declared |
| 4 Narrative | Draft the story, one approval gate | Renzo approves narrative and slide order |
| 5 Build | Sheet and deck from the model, then four gates | All four gates pass |
| 6 Deliver | Upload, update tracker, index, log | Client has it, repo committed |

```bash
./scripts/new_month.sh ggmi 2026-08                      # phase 0
python3 scripts/verify_numbers.py <figures.json> <file>  # phase 5 gate
python3 scripts/protection_scan.py <file>                # phase 5 gate
```

---

## Layout

```
docs/           SETUP, RUNBOOK, DOCTRINE, HANDOVER, DESIGN-SYSTEM
lib/            housestyle.py: the deck design system, one source of truth
scripts/        new_month.sh, verify_numbers.py, protection_scan.py
templates/      month scaffold stubs
tools/          per-month build scripts, one directory per entity per month
reports/        forex/<entity>/<YYYY-MM>/{data,qa,model,output} + figures.json
recommendations/ action handoffs for whoever owns execution
report-client-decks/ delivered decks, finals only, superseded in _archive/
mappings/       KPI dictionary, platform field mappings
clients/        account IDs, campaign patterns, per-channel notes
assets/         logos
_archive/       retired components, kept for reference
```

A month's folder is self-contained: raw vendor files, per-channel workbooks,
QA note, model and outputs all sit together. Vendor data is committed on
purpose, as the audit trail. Credentials never are.

---

## The four gates

Nothing reaches a client without all four. Two are scripts, two are human.

1. **`verify_numbers.py`** proves the deliverable agrees with the approved
   `figures.json`, in both directions. It catches an approved figure that is
   missing, and an unexplained figure that is present, which is how a stale
   number from last month gets caught.
2. **`protection_scan.py`** blocks forbidden vocabulary and statements against
   interest, and warns on downstream metrics and compliance-adjacent claims.
3. **Render QA.** Convert to PDF, check the page count against the source,
   look at every slide.
4. **The doctrine walk-through.** `docs/DOCTRINE.md`, section by section. The
   scripts cannot tell you a slide promises something undelivered.

The gates encode a specific history: about a third of the June 2026 cycle was
rework, and the retrospective traced nearly all of it to writing numbers before
asking what the client already held.

---

## Rules that do not bend

- **Client-facing spend equals the client budget tracker.** Not the platform
  figure. Reconciliation detail stays internal.
- **The agency is scored on submitted applications** and cost per submitted
  application. Downstream steps belong to the client's journey.
- **Conversions never sum across channels.** Four channels, four different
  events, four systems. The Total row carries a dash.
- **GGMI and GCG never blend.**
- **GGMI conversions come from SA360,** never the Bing API, which reads zero.
- **Once Renzo edits the Google Slides deck, it is canonical.** Edit in place
  via `replaceAllText`; never re-upload a PPTX over it.
- **No mutations from this repo.** Recommendations go to
  `recommendations/` for whoever owns execution.
- **Commit locally. Never push without approval.**
