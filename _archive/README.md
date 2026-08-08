# _archive

Retired components. Kept for reference, not in use. Nothing here is loaded,
imported or run.

| Item | Was | Retired because |
|---|---|---|
| `claude-AGENTS-retired/` | 10 project-local subagents in `.claude/AGENTS/` | Wrong-cased directory so Claude Code never discovered them, no `model:` lines, generic. The global Berelvant roster covers the same ground and is better specified. Routing now lives in `CLAUDE.md`. |
| `codex-agents-retired/` | The same 10 agents as `.codex/agents/*.toml` | A second copy of the above, free to drift. |
| `forex-reporting-deck.skill` | Zipped JS/pptxgenjs deck generator | Never registered as a skill and never used. Its design system and content rules were promoted to `docs/DESIGN-SYSTEM.md` and `docs/DOCTRINE.md`; its logos are in `assets/`. The Python path in `lib/` is what ships decks. |
| `dashboard-spec.md` | Generic dashboard structure doc | Never used. Deliverables are a 4-tab Sheet and a deck, both specified elsewhere. |
| `monthly-report-template.md` | Generic monthly report outline | Superseded by the real deck structure in `docs/DESIGN-SYSTEM.md` and the process in `docs/RUNBOOK.md`. |

Also deleted outright in the 2026-08-04 cleanup, recoverable from git history:
`download.html` (empty), `download.txt` (a plain-text dump of the May GCG deck).
