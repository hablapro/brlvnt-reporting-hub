# Handover: Risks, Gaps and Open Items

What is missing, fragile, or dependent on one person. Read this before the
first cycle. Written 2026-08-04 for the incoming Performance Lead.

Nothing here blocks running the process. All of it will surface eventually,
and each item costs less when you see it coming.

---

## 1. Blocking dependencies

These stop a cycle when they slip.

### The client budget tracker

Every client-facing spend figure comes from it, and Renzo receives it. It has
arrived after the first build more than once, and each time the numbers were
rebuilt. Ask at kickoff, not at build time.

**Ask for:** the tracker page for both entities, for the reporting month.

### The Azerion vendor file

Azerion has no API. The vendor emails an XLSX, and it carries a channel worth
roughly $35K a month per entity. No file, no Azerion section.

The June file also arrived with real gaps: undefined conversion and funnel
definitions, overlapping weeks, blank attribution, and no geo, site, format or
creative breakdowns. A data request went out
(`recommendations/forex/ggmi/GGMI-Azerion-data-request-June-2026.md`) and the
reply status is unconfirmed. Check whether the current file still has the gaps
before building on it.

**Risk:** a single vendor email on the critical path, with no fallback.

### GA4 conversion tracking on the LAT property

The Forex LAT property (`508849216`) had a key-event designation gap. It is
documented in `reports/forex/GA4-conversion-tracking-gap-2026-06-CLIENT.md`
and the receipt test was proven, but the fix is client-owned. Confirm it holds
before relying on GA4 conversions for GGMI.

---

## 2. Access you need and may not have

Confirm each before the first cycle. Some take days to grant.

| Access | For | Notes |
|---|---|---|
| The three MCP secrets | Quantcast, GA4, CM360 | Renzo holds them. See `docs/SETUP.md`. |
| `gws` OAuth | All Google Workspace delivery | Run `gws auth login`. Token expires mid-session; see `KNOWN-BUGS.md`. |
| FX Report shared drive | Every deliverable | `1cPVbjlPnwuPbVUChgmBVp4c_HQ01Mr55`. Needs `supportsAllDrives: true`. |
| Reported Spend Tracker | Phase 6 | `1DmsIFkCketcWd3VXiXa7Nvz58DowS_SdWMyktezCzQg`, includes the internal Billable tab. |
| The canonical Google Slides decks | Editing in place | Per month per entity, listed in `reports/REPORT-INDEX.md`. |
| Azerion vendor email | The monthly file | Confirm you are on the distribution list. |
| GitHub `hablapro/brlvnt-reporting-hub` | Push access | See section 5. |
| Bing Ads UI | RSA creative depth | The MCP tool is broken; the UI is the only route. |

**SA360 note:** a second manager account (`7324418878`) exists and returns
permission denied. Not needed for the monthly cycle. Do not spend time on it.

---

## 3. Manual steps that will not automate soon

| Step | Why it stays manual |
|---|---|
| Azerion ingestion | No API |
| Client tracker reconciliation | The tracker is a human-maintained Sheet, and the adjustment is a judgment call |
| Narrative approval | One human gate by design |
| Slide-order approval on quarter-close | Prose hides order; a numbered list surfaces disagreement before the build |
| Render QA | A script can count slides; it cannot see a table overflowing its footer |
| Editing the canonical Slides | Once Renzo edits it, `replaceAllText` only, never a re-upload |
| RSA creative depth | `bing_ads_list_ads` returns 400 NullRequest |

---

## 4. Known-broken tooling

Full detail in `KNOWN-BUGS.md`. Consult it before diagnosing anything; these
are recorded so nobody re-derives them.

Two are dangerous because they return wrong data instead of an error:

- **`bing_ads_search_term_report` silently ignores `campaign_ids`.** Given a
  start date on which only some campaigns delivered, it can return a single
  day. Check covered spend against campaign totals before trusting it.
- **PowerPoint's AppleScript PDF export serves a stale cached copy.** An
  N-slide deck exports N-1 pages. Never conclude a slide did not save from a
  short PDF; check the source with python-pptx first.

Also recorded: `bing_ads_list_ads` returning 400 NullRequest, the `gws` token
expiring mid-session as a silent empty result, and Word's AppleScript PDF
export redirecting into the app sandbox container.

---

## 5. Repository state

**36 local commits have never been pushed** to `hablapro/brlvnt-reporting-hub`.
Everything since roughly the May cycle exists on one laptop. Push it early,
after confirming with Renzo that the remote is still the right home and that
committed client data is acceptable there.

**Client data is committed on purpose.** Vendor XLSX files, delivered decks and
performance workbooks are all tracked, about 15MB of history. That is the audit
trail, and it is why a month's folder is self-contained. The repo must stay
private, and it must never carry credentials. `.env` is gitignored, and
`.mcp.json` reads secrets as `${VAR}` rather than storing them.

**Push and commit require approval.** Standing rule.

---

## 6. Carry-over items as of 2026-08-04

From `reports/forex/2026-07-BUILD-STATUS.md`. Verify each rather than assuming
it is still true.

### Open, GGMI

1. **The Mexico-only geo breach is dormant, not fixed.** All nine enabled
   campaigns still carry `PRESENCE_OR_INTEREST`, and Venezuela, the largest
   leak in both June and July, is still not excluded. July's 2.7% non-Mexico
   is a low-volume artifact plus the pausing of leaking legacy campaigns.
   **Do not tell the client the geo issue is resolved.**
2. **Conversion goals still carry `ExcludeFromBidding = TRUE`,** and every
   campaign runs manual CPC. Third consecutive month carried.
3. **The legacy zero-conversion anomaly is unexplained.** 207 application
   starts, zero Step 3, zero submitted, across three campaigns over 11 days.
   The funnel data says drop-off rather than import lag. Needs one focused
   look before it appears in client-facing material.
4. **The July client tracker had not arrived** at the time of writing.
5. **Conversion maturity:** July's newest clicks were four days old at pull
   time against a 90-day window. Re-pull before finalising.

### Commitments made to the client

- A full Native read was promised for July. Mandatory.
- July was promised as the confirmation of the geo correction. Given item 1,
  that needs careful framing.
- The SA360-to-GA4 link restatement is roughly 4x on paid search and must be
  flagged when it lands.

### Housekeeping

155 paused legacy campaigns and about 40 dead conversion goals still sit in
the Bing account.

### Found while building these gates, 2026-08-04

`protection_scan.py` flagged one BLOCK in a deck that already shipped:
**"$124 vendor-basis" on slide 14 of the GCG June final.** "Basis" is
forbidden vocabulary because it signals a restatement the client did not ask
for, and it survived two manual protection passes.

The June cycle is closed and the canonical Google Slides stays as presented,
so this is not a retro-fix. Two things follow from it. Do not reuse that
phrasing in July, and treat it as evidence that the manual scan misses things
a script catches, which is the whole argument for running gate 2 before every
delivery.

Both June finals otherwise pass: GGMI 0 BLOCK, GCG 1 BLOCK. Every deck from
March through May fails, which is expected, since they predate the doctrine.

---

## 7. What this repo does not do

- **No mutations.** Reporting only. Every action goes to
  `recommendations/<client>/<sub-client>/` for whoever owns execution, and
  production changes need explicit human approval.
- **No scheduling.** Nothing is automated on a timer. A person starts the
  cycle.
- **No dashboards.** Google Sheets is the output layer, with Looker Studio
  optional on top.

---

## 8. Suggested improvements, not yet built

Ordered by value against effort. None is required to run the process.

1. **Channel workbook builders in `lib/`.** The deck path is deduplicated; the
   workbook path is not. `build_sheet.py` is still forked per month per entity
   with the same six helpers copied each time.
2. **A conversion-maturity re-pull check.** Every month asks "have conversions
   matured since the pull," and every month it is answered by hand. A script
   comparing a fresh pull against the booked figure would close it.
3. **A geo-setting assertion.** The single most repeated finding is a targeting
   setting that reads `PRESENCE_OR_INTEREST` when it must be presence-only. One
   scripted check per cycle turns a recurring finding into a pass or fail.
4. **Tracker ingestion.** If the tracker Sheet ID is stable, phase 3 could read
   it directly and populate `figures.json` instead of transcribing it.
5. **A cycle-close checklist script.** Phase 6 has seven steps done by hand and
   at least one gets missed each cycle.
