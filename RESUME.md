# Resume Here

Read this first when picking the repo back up. Last updated 2026-08-08.

Delete or rewrite this file when the handover closes. It exists to carry state
between sessions, not to be permanent documentation.

---

## Where things stand

Two threads run in parallel. They do not block each other.

### Thread A: handover build (this thread) — CODE COMPLETE

The repo is cloneable and runnable. Docs, the design-system library and both
automated gates are committed (`2b1e90e`). Gates verified green at commit.

Blocked only on four decisions from Renzo. Nothing else is outstanding.

### Thread B: July 2026 GGMI cycle — IN PROGRESS, owned elsewhere

A parallel session pulled and verified Bing, Meta, Quantcast and GA4, and
committed `e02d4f1` on 08-08.

**Read `reports/forex/2026-07-BUILD-STATUS.md` fresh.** The July summary in
`docs/HANDOVER.md` §6 was written 08-04 and is now behind. Trust the build
status, not the handover doc, for July state.

---

## The four decisions

Nothing in Thread A moves until these are answered.

| # | Decision | Why it blocks | Suggested default |
|---|---|---|---|
| 1 | Push, and to where | 39 commits are local-only. The remote is a personal namespace holding StoneX vendor data and delivered decks. | Move to a private `Berelvant/` repo, then push |
| 2 | Hand over 3 MCP secrets | `QUANTCAST_MCP_API_KEY`, `GA_MCP_AUTHORIZATION`, `CM360_MCP_API_KEY`. Out of band; `.env` is gitignored. | — |
| 3 | Access grants | `docs/HANDOVER.md` §2. Lead time on the shared drive, Spend Tracker, canonical Slides, Azerion vendor email. | Confirm whether the internal Billable tab may be shared |
| 4 | Confirm 2 doctrine points | Inferred from the retrospective, not ruled on directly. Both are written into `docs/DOCTRINE.md` as standing rules. | Confirm as written |

Decision 4 in full, since it shapes every future deck:

- **Agency scorecard** is submitted applications and cost per submitted
  application. Approval, funding, activation and trading belong to the
  client's journey and are described neutrally.
- **Client-facing spend** equals the client budget tracker, not the platform
  figure. Downstream numbers recalculate silently; reconciliation detail stays
  internal.

---

## Lower priority, no rush

- **Repo location.** It sits in `/Users/rpro/AI-BRLVNT/`, which is neither the
  vault nor `dev/<category>/<project>/` per the deliverables rule. Moving it is
  a `mv` plus a registry pointer, but it breaks saved absolute paths.
- **June builders carry the pre-library palette.** `tools/forex-june-2026/` and
  `tools/forex-gcg-june-2026/` predate `lib/housestyle.py` and still use the
  old colours plus a separate restyle pass. New months import the library.
  Documented rather than retrofitted, because a parallel session was working
  in `tools/`.
- **Workbook builders are still forked per month per entity.** The deck path is
  deduplicated; `build_sheet.py` is not. First item in `docs/HANDOVER.md` §8.

---

## Carry-over into the next client-facing deliverable

`"$124 vendor-basis"` on slide 14 of the GCG June final is forbidden
vocabulary that survived two manual protection passes. June is closed and the
canonical Slides stay as presented, so it was not retro-fixed. Do not reuse
the phrasing, and run `scripts/protection_scan.py` before every delivery.

---

## Verify the repo still works

```bash
python3 lib/housestyle.py                       # renders a component smoke deck
python3 scripts/verify_numbers.py reports/forex/ggmi/2026-06/figures.json \
  "report-client-decks/06. GGMI_LATAM_June_2026_Performance_Review-final.pptx"
python3 scripts/protection_scan.py \
  "report-client-decks/06. GGMI_LATAM_June_2026_Performance_Review-final.pptx"
```

All three pass as of `2b1e90e`. The full setup check is `docs/SETUP.md` §4.
