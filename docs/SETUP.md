# Setup

Everything a new operator installs, connects and verifies before the first
reporting cycle. Budget two hours, most of it waiting on access grants.

Work through the four sections in order. Section 4 is a verification pass you
run before you touch a real month, and again any time a pull behaves oddly.

---

## 1. Local tooling

| Tool | Why | Install |
|---|---|---|
| Claude Code | The repo is driven from it. Loads `CLAUDE.md` and `.mcp.json` on open. | https://claude.com/claude-code |
| Python 3.10+ | Deck and workbook generation (`lib/`, `scripts/`). | `brew install python` |
| `gws` CLI | Google Workspace delivery layer: Sheets, Slides, Drive, Docs. | `npm i -g @googleworkspace/cli` (0.13.3 in use) |
| poppler | `pdfinfo` and `pdftoppm` for render QA. | `brew install poppler` |
| Microsoft PowerPoint | Renders the built PPTX to PDF for visual QA. LibreOffice also works and needs no license. | Office 365, or `brew install --cask libreoffice` |
| `bd` (beads) | Issue tracking. Optional. The `.beads/` directory is already initialised. | https://github.com/steveyegge/beads |

```bash
git clone https://github.com/hablapro/brlvnt-reporting-hub.git
cd brlvnt-reporting-hub
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then fill it in, see section 2
```

Confirm the deck library renders before anything else:

```bash
python3 lib/housestyle.py     # builds _scratch/housestyle-smoke.pptx
```

That prints `OK 3 slides` and writes a three-slide deck exercising every
component. Open it. If the navy band, the coral rule, the Georgia headers and
the four blocker colours look right, the visual system is intact.

---

## 2. MCP servers

Eight servers, all declared in `.mcp.json` at the repo root. Claude Code
prompts you to approve them the first time you open the repo. Approve all
eight.

| Server | Carries | Auth | Needed for |
|---|---|---|---|
| `sa360` | GGMI conversions, geo, funnel steps, daily trend | Worker-side | **Every GGMI report.** The only valid source of GGMI conversions. |
| `bing-ads` | GGMI spend, impressions, clicks, keywords, goal config, search queries | Worker-side | Every GGMI report |
| `google-ads` | GCG search performance | Worker-side | Every GCG report |
| `meta-ads` | Both entities, one shared account | Worker-side | Every report |
| `quantcast` | Programmatic delivery, Domain/App site list | `QUANTCAST_MCP_API_KEY` | Every report |
| `google-analytics` | GA4 sessions, channel groups, source/medium, geo | `GA_MCP_AUTHORIZATION` | Every report |
| `gsc` | Organic search, the SEO slides | Worker-side | GGMI reports with an SEO section |
| `cm360` | Floodlight config and firing, trafficking QA | `CM360_MCP_API_KEY` | Tracking investigations, not the monthly pull |

Five of the eight authenticate inside the Cloudflare Worker, so the URL is
enough. Three need a secret in `.env`, and Renzo holds them. Ask for the FX
reporting MCP key bundle.

One caveat on `gws`: it is Google's CLI but not an officially supported Google
product, and the repo depends on it for every Workspace delivery step. Pin the
version that works rather than tracking latest.

Two things to know about the secrets:

- `.mcp.json` reads them as `${VAR}`. Never paste a real key into that file;
  it is committed.
- `.env` is gitignored. Keep it `chmod 600` and do not echo it into a
  terminal that gets shared.

**Azerion has no MCP and never will.** The vendor emails an XLSX each month.
That file is a hard external dependency on the reporting calendar, and it has
arrived late enough to hold a deck. See `docs/HANDOVER.md`.

### Exporting these to another machine

`.mcp.json` travels with the repo, so a clone gets all eight server
definitions automatically. The clone needs two things the repo does not carry:

1. `.env`, with the three secrets, transferred out of band.
2. `gws auth login`, run once on the new machine.

To check what a clone actually resolved, run `/mcp` in Claude Code. All eight
should list as connected. A server that shows connected can still fail per
tool, so run section 4.

---

## 3. Skills

The monthly cycle depends on skills, not just MCPs. Install these before the
first cycle. Skills marked **gate** must be loaded before the work starts,
not after; project rules treat a missing gate as an error to correct, not a
style preference.

### Delivery layer, used every month

| Skill | Used for |
|---|---|
| `gws-sheets` | Building and reading the 4-tab performance Sheet |
| `gws-slides` | Editing the canonical Google Slides deck in place |
| `gws-drive` | Uploading deliverables, moving files into the shared drive |
| `gws-docs` | The conversion-tracking and tracking-gap docs |

### Gates

| Skill | Gate on |
|---|---|
| `dataviz` | **gate** for any chart, graph or dashboard, including deck charts |
| `stop-slop` | **gate** for the narrative, the deck copy, any client-facing prose |
| `karpathy-guidelines` | **gate** for any change to `lib/` or `scripts/` |
| `executive-communications` | The executive summary and QBR framing |

### Channel analysis

| Skill | Channel |
|---|---|
| `ppc-bing-audit`, `ppc-playbooks`, `ppc-core` | Bing, and the recurring GGMI config audit |
| `ppc-google-audit` | GCG Google Ads |
| `sa360-ppc-agency` | SA360 cross-engine, conversion sourcing |
| `meta-ads-account-auditor`, `meta-ads-reporting-hub`, `meta-ads-performance-optimizer` | Meta |
| `programmatic-display-qa`, `programmatic-display-strategy` | Quantcast and Azerion |
| `utm-governance` | UTM standard enforcement and the destination-URL audit |
| `cm360-trafficking-qa` | Floodlight firing and trafficking QA |
| `analytics-tracking` | GA4 gaps, conversion tracking investigations |
| `seo-audit`, `ai-seo` | The organic-search slides in the GGMI deck |

### Review

| Skill | Used for |
|---|---|
| `the-roast` | Adversarial pass on a finished deck. Both June decks went through it and both changed as a result. |

### Exporting skills to another machine

Skills live in `~/.claude/skills/`, and plugin skills come from installed
plugins, so a repo clone does not bring them. On a new machine, list what is
installed (`ls ~/.claude/skills/`), copy the directory across or reinstall
from source, then confirm the ones this repo depends on resolve. In Claude
Code the skill list is visible via `/help`, or invoke one directly.

Anything missing gets installed before the cycle starts, not mid-build. A
skill that fails twice in one build is a blocker: stop and raise it rather
than quietly working around it.

Two skills apply globally rather than per phase: `graphify` for querying an
existing knowledge graph before hand-searching files, and `task-observer` for
the session observation log.

---

## 4. Verification pass

Run this before the first real cycle. It takes ten minutes and catches the
failures that otherwise surface halfway through a build.

```bash
# 1. Deck library renders
python3 lib/housestyle.py

# 2. Protection scan reads every format it claims to
python3 scripts/protection_scan.py "report-client-decks/06. GGMI_LATAM_June_2026_Performance_Review-final.pptx"
#    expect: 0 BLOCK. That deck shipped after two protection passes.

# 3. Numbers verification, against the worked example
python3 scripts/verify_numbers.py reports/forex/ggmi/2026-06/figures.json \
  "report-client-decks/06. GGMI_LATAM_June_2026_Performance_Review-final.pptx"
#    expect: PASS, 0 MISSING, 0 UNSOURCED.

# 4. Month scaffold works and does not clobber
./scripts/new_month.sh ggmi 2099-01 && rm -rf reports/forex/ggmi/2099-01

# 5. Google Workspace auth is live
gws drive files list --page-size 1
#    a 401 invalid_grant means run: gws auth login
```

Then the MCP checks. In Claude Code, one read per server against a known
account:

| Check | Expect |
|---|---|
| `sa360` customer `5372690580`, login `9697709980` | Conversions for the last closed month |
| `bing-ads` account `31003116` | Spend matching SA360 to within rounding |
| `google-ads` account `4781995752` | GCG campaigns |
| `meta-ads` account `act_1699453997689551` | Both GGMI and GCG campaigns |
| `quantcast` account `9969644` | Delivery plus a Domain/App breakdown |
| `google-analytics` property `508849216` | Mexico sessions for last month |
| `gsc` | The forex.com property, if the SEO section is in scope |

Read `KNOWN-BUGS.md` before you conclude a tool is broken. Four failures are
already documented with workarounds, including two MCP tools that return
wrong data rather than an error.
