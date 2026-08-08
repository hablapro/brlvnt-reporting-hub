# Agent Instructions

This file exists for agents that read `AGENTS.md` rather than `CLAUDE.md`.

**Read `CLAUDE.md` in this directory. It is the project brief.** Then
`docs/RUNBOOK.md` for the process and `docs/DOCTRINE.md` before writing
anything client-facing.

## Shell hygiene

Use non-interactive flags. `cp`, `mv` and `rm` may be aliased to `-i`, which
hangs an agent waiting on a y/n that never comes.

```bash
cp -f source dest
mv -f source dest
rm -f file
rm -rf directory
```

## Issue tracking

This project has `bd` (beads) initialised in `.beads/`. It is optional. If you
use it: `bd ready` to find work, `bd update <id> --claim` to take it,
`bd close <id>` when done.

Per-month state does not live in beads. It lives in the month's
`BUILD-STATUS.md`, which is the resume handoff between sessions, and in
`reports/REPORTING-LOG.md`, which is the chronological record.

## Session close

1. Update the month's `BUILD-STATUS.md` so the next session can resume.
2. Append a block to `reports/REPORTING-LOG.md`.
3. Record any new tool failure in `KNOWN-BUGS.md`.
4. Commit.

**Do not push without approval.** This differs from the beads default
workflow: this repo holds client data and the remote is shared.
