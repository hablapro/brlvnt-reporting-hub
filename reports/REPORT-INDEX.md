# Forex Reporting — Master Index

Single source of truth for where every Forex report and supporting file lives (Google Drive + this repo). Last updated: 2026-08-04.

Client: FOREX.com (StoneX). Sub-clients: **GCG** (US Hispanic, Spanish) and **GGMI** (LATAM / Mexico).
Repo: `hablapro/brlvnt-reporting-hub`. Drive parent: **FX Report** (`1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55`).

***

## Client-facing deliverables (Google Drive)

| Report | Sub-client | Month | Type | Link |
|---|---|---|---|---|
| GCG (US ES) — Performance Report | GCG | June 2026 | Google Sheet | https://docs.google.com/spreadsheets/d/1cohpQ7FlvgnpxvQRAx55eip0yJu7xDOx5V-qce73GBU/edit |
| GCG (US ES) — Performance Review + Q3 QBR (working draft; Azerion/Native detail pending vendor) | GCG | June 2026 + Q3 | Google Slides | https://docs.google.com/presentation/d/1_QFFW_Ohvwz5jVWI3_NIljGihjZMgO4kIkDLNNO8OoE/edit |
| GGMI (LATAM) — Performance Report | GGMI | June 2026 | Google Sheet | https://docs.google.com/spreadsheets/d/1P3SIZEXgGsG289lz-33MOefgLRepgdkslaQN4sE09xE/edit |
| GGMI (LATAM) — Performance Review + Q3 FY2026 QBR (working draft, pending Renzo edit/send) | GGMI | June 2026 + Q3 | Google Slides | https://docs.google.com/presentation/d/1iNeaobJVJLF_Dr3NU2W6Wutsvh55xqJhRFGOL-P_mug/edit |
| GGMI (LATAM) — Performance Review (PPTX source of the above) | GGMI | June 2026 | Deck (PPTX) | https://drive.google.com/file/d/1yxhTuN7OxLffoAWQz9mZcT67puzJPxWu/view |
| GGMI (LATAM) — Performance Report | GGMI | May 2026 | Google Sheet | https://docs.google.com/spreadsheets/d/1XsQTZ-9qxyRaLPk44GHUrgQh_WXZAu85AslcguL1vME/edit |
| GGMI (LATAM) — Performance Review **(FINAL, client-sent)** | GGMI | May 2026 | Google Slides | https://docs.google.com/presentation/d/1npxoxCCbytXSRAjgliG7Ybv8UUS_OQwsUd4uzAaJd4o/edit |
| GCG (US ES) — Performance Report | GCG | May 2026 | Google Sheet | https://docs.google.com/spreadsheets/d/1CTY9mk2Y9qtfR4cOT5uI8It5GOhfgIEgZmuhsUvLmJM/edit |
| GCG (US ES) — Performance Review **(FINAL, client-sent)** | GCG | May 2026 | Google Slides | https://docs.google.com/presentation/d/1Dj7Gh8KJxnYH_8jPskpfSS9iEsDUjw7F1KW0iRjmXys/edit |
| GCG — Performance Review (corrected, fee-inclusive) | GCG | April 2026 | Deck (PPTX) | https://drive.google.com/file/d/1cRQ-uQn2AQiM4lAUxQYr3SxYthFFk7-S/view |
| GGMI — Performance Review (corrected, fee-inclusive) | GGMI | April 2026 | Deck (PPTX) | https://drive.google.com/file/d/1lpbBhQEJOP2jCdlXcInLVm9JvspqEpdh/view |

June deliverables folder (**06. June-data**): https://drive.google.com/drive/folders/1x1jeGRsh0AgYsB8hVLaW1O1FGPf6OF2Y
May deliverables folder (**May-data**): https://drive.google.com/drive/folders/1hWwGEgyU6HiybjSlylJIQrmJD02DK4gR
Corrected April decks folder: https://drive.google.com/drive/folders/1B3KlLKxvaltvDw87wNP_KH8499hP9S1c

> **Final May decks (2026-06-10):** the client-sent versions are the **Google Slides** linked above (GGMI `1npxoxCC…`, GCG `1Dj7Gh8K…`), edited by Renzo. The earlier PPTX (`report-client-decks/05.*` and Drive `1l57…`/`1DFD…`) are **Berelvant working drafts, superseded** by these. Internal data/QA reconciliation to the final Slides is pending (see BUILD-STATUS).

## Cross-month & internal (Google Drive)

| Item | Scope | Type | Link |
|---|---|---|---|
| Reported Spend Tracker (Mar–Jun; June = GGMI only, GCG pending) | Both | Google Sheet | https://docs.google.com/spreadsheets/d/1DmsIFkCketcWd3VXiXa7Nvz58DowS_SdWMyktezCzQg/edit |
| └ Billable Spend tab (7.5% tech-fee view) | Both | Tab (internal) | same sheet, "Billable Spend (internal)" tab |
| Conversion Tracking Review (Bing + Meta) | GGMI/GCG | Google Doc (internal) | https://docs.google.com/document/d/1Q0d76W37L2bL9pA7NJURT_4PK0QOnOh18OnQ5pNLQ6M/edit |

## Supporting data, QA & modeled tables (this repo)

| Path | Contents |
|---|---|
| `reports/forex/2026-05-BUILD-STATUS.md` | May build status + handoff |
| `reports/forex/ggmi/2026-05/data/` | GGMI channel data (bing, meta, azerion, quantcast) + `sources/` vendor XLSXs |
| `reports/forex/ggmi/2026-05/qa/qa-and-model.md` | GGMI QA + modeled KPI tables |
| `reports/forex/ggmi/2026-05/qa/bing-conversion-tracking-investigation.md` | Bing/Meta conversion-tracking resolution note |
| `reports/forex/gcg/2026-05/data/` | GCG channel data + `sources/` vendor XLSXs |
| `reports/forex/gcg/2026-05/qa/qa-and-model.md` | GCG QA + modeled KPI tables |
| `report-client-decks/` | Delivered decks, finals only. Superseded revs and backups in `_archive/`. The canonical client-facing versions are the Google Slides above. |
| `reports/forex/<entity>/2026-04/data/sources/` | Raw April Azerion vendor XLSXs (moved out of the old `data-dump/` 2026-08-04) |
| `docs/reference/forecast/` | FOREX.com native advertising forecast |
| `reports/README.md`, `reports/REPORTING-LOG.md` | Folder convention + session log |
| `docs/RUNBOOK.md` | The end-to-end monthly process |
| `docs/DOCTRINE.md` | What may go in a client artifact |
| `docs/HANDOVER.md` | Risks, gaps, access, open carry-overs |
| `reports/forex/<entity>/<YYYY-MM>/figures.json` | Approved client-facing figures for that month |

## Generator scripts
- **Design system:** `lib/housestyle.py` owns the palette, fonts and every deck component. Build scripts import it; none redefines a colour. Run it directly to render a component smoke-test deck.
- **Per month:** `tools/forex-<entity>-<month>/`. Copy the prior month's directory for the same entity and edit the numbers and copy.
- June 2026: `tools/forex-june-2026/` (GGMI), `tools/forex-gcg-june-2026/` (GCG). These predate `lib/housestyle.py` and carry the old palette plus a separate restyle pass; new months should import the library instead.
- May 2026 scripts lived in `/tmp/` and were lost on reboot. Build scripts live in the repo now.

## Source-of-truth references (accounts / properties)

| System | Identifier |
|---|---|
| SA360 — GGMI (LATAM) | customerId `5372690580`, loginCustomerId `9697709980` (Bing campaign `627590412`) |
| SA360 — GCG (US ES) | customerId `4781995752`, loginCustomerId `5700106280` |
| Quantcast | account `9969644` |
| Bing Ads (GGMI) | account `31003116` |
| Meta Ads | `act_1699453997689551` |
| GA4 — GGMI / LATAM | property `508849216` (Forex LAT) |
| GA4 — GCG / US | property `325353267` (Forex US) |
| GA4 — Rest of World | property `326422211` (QA: our paid traffic not counted here) |

## Status flags (read before sharing externally)
- **GGMI June deck:** Google Slides above is the Berelvant working draft (built 2026-07-16 from the approved narrative v2, mirroring the final May deck structure + a new Site Traffic slide). Renzo edits and sends; the client-sent version supersedes it.
- **GGMI June spend = client-tracker figures (Renzo ruling 2026-07-16):** client materials must match the client's own tracker with no adjustment commentary. June: Azerion **$35,026** (vendor raw $34,555.83 + $470.17 adjustment), Quantcast $33,784 (matches), total **$120,393** (+53% vs May $78,790). Azerion CPA $834; ad-set spends scaled pro-rata to reconcile. Adjustment detail lives ONLY here, in the Spend Tracker note, and the Billable tab — never in the deck or report.
- **Meta June conversions:** held from all June client materials (placement audit + pixel-event review pending); delivery metrics reported normally.
- **GCG June:** not started — data pull, QA, model, narrative, deliverables all pending.
- **GGMI Bing geo:** May data is pre-fix (campaign delivered ~68% Venezuela; targeting set to presence-only + VE/BR excluded on 2026-06-03). June is the clean read. Reminder set for 2026-06-10.
- **Meta KPI:** held pending verification (StartApplication vs SubmittedApplication). Reported figures left unchanged in the reports (GCG 109, GGMI 4 — these are the pixel rollup, mostly application starts).
- **Azerion fee:** tiered tech fee — Mar/Apr 5.5%, May 7.5%; client deliverables show fee-inclusive Azerion. Internal raw→fee→billable on the Spend Tracker "Billable Spend" tab.
- **Repo state (2026-08-04):** 36 commits are local-only and have never been pushed to `hablapro/brlvnt-reporting-hub`. See `docs/HANDOVER.md` section 5.
