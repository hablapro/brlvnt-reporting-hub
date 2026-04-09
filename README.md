# Brlvnt Reporting Hub

Multi-agent marketing intelligence system for paid media reporting across Meta, Google Ads, Bing, SA360, and programmatic. Designed to run inside [Claude Code](https://claude.com/claude-code).

See `CLAUDE.md` for the full project rules, KPI definitions, workflow order, and output conventions. Claude Code loads it automatically when you open the repo.

## What's in the repo

- `CLAUDE.md` — project instructions loaded automatically by Claude Code
- `.claude/AGENTS/` — specialist subagents (orchestrator, data-ingestion-qa, data-modeling, dashboard-builder, meta-analyst, google-ads-analyst, bing-ads-analyst, sa360-analyst, programmatic-analyst, narrative-reporting)
- `.mcp.json` — MCP server config (SA360 preconfigured)
- `mappings/` — shared KPI dictionary and platform field mappings
- `dashboards/` — dashboard specs
- `clients/` — per-client context
- `reports/` — monthly report template and client report outputs

## Installation

### 1. Prerequisites
- [Claude Code](https://claude.com/claude-code) installed and authenticated
- `git`

### 2. Clone
```bash
git clone https://github.com/hablapro/brlvnt-reporting-hub.git
cd brlvnt-reporting-hub
```

### 3. Open in Claude Code
```bash
claude
```
On first launch in this directory, Claude Code will:
- Load `CLAUDE.md` as project instructions
- Discover the agents in `.claude/AGENTS/`
- Prompt you to approve the SA360 MCP server from `.mcp.json`

Approve the SA360 server when prompted.

### 4. Add additional MCP servers (as needed)
`CLAUDE.md` references these data sources, but only SA360 is preconfigured in `.mcp.json`. Add any you need to either `.mcp.json` (project-scoped) or your user-level MCP config:

- Google Ads
- Meta (Facebook/Instagram Ads)
- Google Analytics
- Google Search Console
- Quantcast

Each MCP server will require its own auth (OAuth, API key, etc.) — follow the installation instructions from the respective MCP server's documentation.

### 5. Verify
In Claude Code, try:
```
/agents
```
You should see the 10 specialist agents listed. Then ask the orchestrator to confirm data source availability before running a real report.

## Workflow

Follow the workflow in `CLAUDE.md`:
1. Clarify the request
2. Pull source data (via MCP)
3. Run QA
4. Normalize/model data
5. Run channel analysis
6. Build dashboard outputs
7. Generate narrative reporting
8. Flag blockers before final delivery

Output layer is Google Sheets-first — see the Output Format Rule in `CLAUDE.md`.

## Notes

- Do not commit client credentials or raw data exports
- Reports go under `reports/<client>/<account>/<YYYY-MM>/`
- Update `mappings/kpi-dictionary.md` when KPI definitions change
