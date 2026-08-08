# Reports — Structure & Conventions

How monthly client reports are organized in this repo. Follow this for every client and every month.

## Folder layout

```
reports/
  README.md                     # this file, the convention
  REPORTING-LOG.md              # chronological log of every reporting session
  REPORT-INDEX.md               # where every deliverable lives (Drive + repo)
  forex/
    <sub-client>/               # gcg, ggmi
      <YYYY-MM>/                # one folder per monthly report
        BUILD-STATUS.md         # resume handoff, archived once the month ships
        figures.json            # approved client-facing figures + spend basis
        data/                   # one .xlsx workbook per channel
          sources/              # raw vendor files, untouched
        qa/qa-and-model.md      # QA checks + modeled summary
        model/                  # cross-channel model workbook
        output/                 # narrative draft, built Sheet, deck references
```

Scaffold a month with `./scripts/new_month.sh <ggmi|gcg> <YYYY-MM>` rather
than creating these by hand.

## Rules
- **One folder per monthly report**: `reports/<client>/<sub-client>/<YYYY-MM>/`.
- **All pulled data lives under `data/` as formatted `.xlsx` workbooks** (Sheets-ready), one per channel, e.g. `GGMI-<Channel>-Apr-Jun-2026-data.xlsx`. Do NOT store pulled data in markdown; markdown is for narrative/QA notes only. Raw vendor files (Azerion XLSX, CSV exports, oversized MCP dumps) go in `data/sources/`.
- Each channel workbook records: source + account ID, period, channel totals with MoM comparison, relevant breakdowns, and a short "Read"/Notes tab.
- **QA before modeling; model before commentary; narrative last.** Full process in `docs/RUNBOOK.md`.
- Never blend sub-clients (GGMI vs GCG) into one sheet.
- **Programmatic/display site-list + disallow (every report):** for Quantcast and any programmatic channel, pull the `Domain/App` breakdown with `Budget Delivered` each month, add "Site List" + "Disallow Candidates" tabs to the channel workbook, and write a refreshed disallow list to `recommendations/<client>/<sub-client>/` (a `.txt` block list + summary). Flag sites with viewability < 35% and 0–few results, or audience mismatch. Recommend a campaign-level viewability floor as the durable fix. Inventory rotates, so refresh monthly.
- **Reporting only — no execution.** Recommendations and any account-change actions go to `/recommendations/<client>/<sub-client>/` for the execution agent; this repo never pushes mutations.
- **`figures.json` is filled in phase 3** and is what `scripts/verify_numbers.py` checks the deliverables against. Declare `spend_basis` or the gate warns.
- Append a dated entry to `REPORTING-LOG.md` at the start and end of every reporting session.
- Active multi-step builds get a `BUILD-STATUS.md` resume handoff at the client level; delete or archive it once the report ships.

## Data sources by channel (Forex)
| Channel | Source | Account |
|---|---|---|
| Google Ads (GCG) | google-ads MCP | 4781995752 |
| Meta (both) | meta-ads MCP | act_1699453997689551 |
| Bing (GGMI) | bing-ads MCP for spend/clicks/config; **conversions from SA360 only** | 31003116 |
| Quantcast (both) | quantcast MCP | 9969644 |
| Azerion (both) | vendor XLSX dropped into `data/sources/` | — |
