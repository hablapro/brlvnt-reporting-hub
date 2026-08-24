# GCG July 2026 — QA & Cross-Channel Model

Pulled 2026-08-19. Currency USD, TZ America/New_York. Comparison MoM vs June
2026. Client-facing spend basis = **client budget tracker** (standing ruling;
adjustments silent in client materials). July tracker total: **$136,224**.

**FIRST LINE DISCLOSURE: Quantcast pull completed 2026-08-19**, resolving last
week's BLOCKED state. One new tool issue hit and worked around (see Quantcast
section below): the `quantcast_metrics_report` `filters` parameter returned
empty results on every attempt (not the previously-documented
`quantcast_campaigns`/`quantcast_accounts` object-filter bug) — worked around
by pulling the account unfiltered and filtering client-side on Campaign Name,
consistent with the GGMI July pull's approach. The Domain/App breakdown also
hit the sync token limit and then an MCP session expiry on retry; recovered
via `quantcast_async_report`. Two client-facing gates remain open: July client
funnel rows and comms-since-last-report, both with Renzo.

## QA — platform vs client tracker

| Channel | Platform/vendor pull | Client tracker | Delta | Status |
|---|---|---|---|---|
| Google Search | $29,478.13 | $29,478 | $0.13 | ✅ exact |
| Google PMax (YT) | $18,174.60 | $18,175 | $0.40 | ✅ exact — NEW line, launched wk of Jul 13 |
| Meta | $6,939.50 | $6,940 | $0.50 | ✅ exact |
| Azerion (display) | $28,615.39 raw (+7.5% fee = $30,761.54, internal) | $31,477 | +$715.46 adj | ✅ normal June-pattern adjustment; tracker stands |
| Native (Azerion + Quantcast) | $9,362.04 (Azerion raw) + $10,002.73 (QC) = $19,364.77; with Azerion fee: $10,064.19 + $10,002.73 = $20,066.92 | $20,298 | $231.08 (1.1%), fee-inclusive basis | ✅ resolved — HOLD cleared. Composition: QC Native + fee-inclusive Azerion Native reconciles the tracker to within 1.1%, the same order of adjustment as the Azerion display line |
| Quantcast (display) | $29,854.75 | $29,857 | $2.25 (0.01%) | ✅ exact |
| **Total** | — | **$136,224** | — | +16.4% vs June $117,024 |

## QA checks (runbook Phase 2)

| Check | Result |
|---|---|
| Internal sums | PASS — Google campaign spend sums to Search+PMax totals and to the geo row ($47,652.73); Meta ad-level sums to campaign total ($6,939.50); Azerion ad-set rows sum to vendor totals (display and native) |
| Client tracker | PASS for Google/Meta/Azerion-display/Quantcast-display; PASS (1.1% delta) for Native once Quantcast is in the mix |
| Conversion source | PASS with two flags (below) — Google = Step 5 event; Azerion = vendor-reported; Meta = pixel rollup, non-scorecard; Quantcast Results = platform-attributed, internal only |
| Geo compliance | PASS — Google 100% US (geographic_view); Meta 100% US all 3 campaigns (country breakdown); Azerion vendor files US-filtered at source; Quantcast 100% US across both campaigns (52-state Region breakdown, zero non-US rows, delivery checked not just targeting). Targeting settings: Meta ad sets US-only verified in config; Google/PMax/Quantcast settings not separately verified (delivery clean) |
| Conversion maturity | PASS — pulled 19 days after month close; windows matured |
| Programmatic quality | PARTIAL — Azerion display viewability 64.95% computed, BELOW the 70% floor (vendor summary claims 71.28%; discrepancy flagged, computed figure used). Azerion Native 72.68%, above floor. Quantcast display 49.26% (June 46.9%, improving, still below floor) and Quantcast Native 57.98% (no June comparator, below floor) — both FAIL vs the 70% floor |
| GA4 cross-check | PASS — meta/paid-social 7,902 sessions vs 11,767 GCG link clicks = 67.2% capture (June ~57%). google/cpc not comparable at property level (client-run English campaigns share the property); noted, not blocking |
| Cross-source reconciliation (Bing/SA360) | n/a — GCG has no Bing line |

## Conversion-counting flags (both material, both internal)

1. **Google `metrics.conversions` no longer equals submitted apps.** July
   Search reads 76, but 3 are offline GCLID events (2 approved, 1 funded)
   newly counted as primary. Scorecard = Step 5 only = **73**. June's 67 was
   pure Step 5, so 67 → 73 is the valid MoM. Never quote 76.
2. **PMax's 49 Step-5 conversions sit in `all_conversions` only** — the
   campaign goal config excludes Step 5 from primary (it reports 0
   conversions while driving 49 submitted apps, view-through = 1). The
   campaign is NOT optimizing to submitted applications. Goal-config fix →
   `recommendations/forex/gcg/` (account mechanics, never the deck).

## July model — FINAL (Phase 3 closed 2026-08-19)

Tracker spend basis. Source: channel workbooks in `data/`, all
tracker-reconciled above; model workbook
`model/GCG-July-2026-cross-channel-model.xlsx`; declared figures
`figures.json`.

| Channel | Spend | Impr | Clicks | Submitted apps / results | Cost per app | Viewability |
|---|---|---|---|---|---|---|
| Google Search | 29,478 | 125,392 | 9,568 | 73 (Step 5) | $403.81 | — |
| Google PMax (YT) | 18,175 | 792,667 | 14,009 | 49 (Step 5, all_conv) | $370.91 | — |
| Meta | 6,940 | 493,027 | 11,767 (link) | 284 pixel events (rollup, non-scorecard) | — | — |
| Quantcast (display) | 29,857 | 22,486,572 | 2,574 | 15 (platform, internal only) | — | 49.26% ⚠ below floor |
| Azerion (display) | 31,477 | 4,769,231 | 8,892 | 80 (vendor) | $393.46 | 64.95% ⚠ below floor (vendor claims 71.28%, flagged) |
| Native (QC+Azerion) | 20,298 | 10,581,736 (Azerion 1,170,255 + QC 9,411,481) | 2,476 (Azerion 816 + QC 1,660) | 10 (QC, platform, internal only) | — | Azerion 72.68% / QC 57.98% ⚠ QC below floor |
| **Total** | **136,224** | **39,248,625** | **49,286** | **never summed** | **—** | **—** |

Google Search+PMax combined impressions (the figure carrying the asterisk
in the prior provisional table) = 918,059 — Search alone 125,392, PMax
792,667; both platform Search Ads campaign totals, google-ads MCP. Total
row: conversions and CPA are never summed across channels, each reports a
different event from a different system; impressions and clicks are the
same metric class across channels and are summed. Tracker's own stated
total (136,224) is $1 off the sum of its six rounded line items (136,225)
— a rounding artifact in the tracker's own category subtotals, not
something reconciled away.

### MoM vs June 2026 (tracker basis)

| Channel | June spend | July spend | Spend MoM | June result | July result | Note |
|---|---|---|---|---|---|---|
| Google Search | 22,524 | 29,478 | +30.9% | 67 apps @ $336.18 | 73 apps @ $403.81 | Apps +9.0%, CPA +20.1%. June had no PMax line; Search is the like-for-like comparison. |
| Google PMax (YT) | — | 18,175 | new line | — | 49 apps @ $370.91 | Launched wk of Jul 13. No June comparator. |
| Meta | 30,711 | 6,940 | -77.4% | 136 pixel events (CTR) | 284 pixel events (conversion, 44% of spend) | June ran one CTR campaign; July split traffic and conversion objectives — compare within objective only. |
| Quantcast (display) | 30,559 | 29,857 | -2.3% | 15 results | 15 results | Viewability 46.9% → 49.26% (+2.36pts), second straight improving month, still below the 70% floor. |
| Azerion (display) | 29,586 | 31,477 | +6.4% | 58 apps @ $510.10 | 80 apps @ $393.46 | Apps +37.9%, CPA -22.8%. Viewability 58.8% → 64.95%, still below floor. |
| Native (QC+Azerion) | 3,645 | 20,298 | new structure | — | — | June was an Azerion-only pilot; July adds Quantcast Native, a brand-new campaign (created Jul 2) — not a like-for-like comparison, stated once. |
| **Total** | **117,024** | **136,224** | **+16.4%** | — | — | Conversions never summed; channel-level comparators above. |

June comparators taken verbatim from the delivered GCG June 2026
Performance Report Summary tab and June's qa-and-model.md.

## Validated findings so far (pre-Quantcast, pre-funnel)

1. **PMax arrived and performed.** Launched week of Jul 13; $18,175 for 49
   submitted apps at $370.91 in ~18 days — at or below Search's full-month
   CPA ($403.81), on the same Step 5 event, click-based. Config caveat above.
2. **Search: spend outgrew apps again, but less.** +30.9% spend, +9.0% apps
   (67→73), CPA $336→$404. The ad-rank story from June is unchanged in
   direction: lost-to-rank 59-79% vs lost-to-budget 8-12%. Where the rank
   work landed (Trust): IS 27%→32.6%, lost-to-rank →58.7% (account best),
   CPA $433→$390.86, and Trust became the volume leader (28 apps).
3. **The Meta conversion-objective commitment is DELIVERED.**
   0726_GCG_Q3_esp_us_CONV live on OUTCOME_SALES optimizing to the
   SubmittedApplication pixel event, 44% of the (much smaller) $6,940 line.
   Meta spend fell 77% by design as Q2 CTR wound down (paused after July).
4. **Azerion display had its best application month**: 80 vendor-reported
   apps (June 58, +37.9%) at $393.46 tracker CPA (June $510, -22.8%).
   Professional Tools is the new efficiency leader ($197, 18 apps); Spanish
   Platform is the reallocation candidate ($7.3K spend, 9 apps, $812).
   Viewability below floor (64.95%) — vendor flag.
5. **Azerion Native completed its first full month**: $9,362 raw, ramped to
   ~$3.4K/week by month end, viewability 72.7% above floor, CTR 0.070% and
   falling with scale — vendor proposes optimize-to-CTR. Upper-funnel,
   delivery-reported only.
6. **ES-audience traffic gave back the paid lift**: 66,398 sessions (-17.2%)
   as Meta spend fell; slightly below the ~70K Jan-May base. Meta GA4
   capture healthy at 67.2%.

## Quantcast — July 2026 (pulled 2026-08-19)

Source: `quantcast_metrics_report` + `quantcast_async_report`, account 9969644,
2026-07-01–2026-08-01, America/New_York. Workbook:
`reports/forex/gcg/2026-07/data/GCG-Quantcast-July-2026-data.xlsx`.

1. **Two live campaigns, tracker-tight.** Display `Forex_GCG_spanish_conversion_Q+campaign_us`
   $29,854.75 (tracker $29,857, delta 0.01%). Native
   `Forex_GCG_spanish_conversion_Q+campaign_NativeOnly_US_ES` $10,002.73 — a
   brand-new campaign, created 2026-07-02, first delivery month. Two other
   GCG campaigns (old-naming, paused) had $0 July spend.
2. **Native line reconciliation resolved.** QC Native $10,002.73 + Azerion
   Native (fee-inclusive, internal) $10,064.19 = $20,066.92 vs the $20,298
   tracker line — 1.1% delta, the same class of normal adjustment as the
   Azerion display line. Clears last week's HOLD.
3. **Geo: 100% US, PASS.** Every dollar across 52 states/territories in the
   Region breakdown; zero non-US rows on either campaign.
4. **Viewability improving but still below floor.** Display 49.26% (June
   46.9%, +2.4pts) — second straight month of improvement, still 20.7pts
   under the 70% IAB floor. Native 57.98% — no June comparator (new
   campaign), also below floor.
5. **The June disallow list was not applied.** All 18 domains flagged in
   June's list (`recommendations/forex/gcg/GCG-Quantcast-disallow-June-2026.txt`)
   still received July spend — $11,087 combined. yahoo.com, June's single
   largest flag at $2,270, grew to $2,359. Refreshed list: 35 domains,
   $13,456 (34% of spend), same criteria as June (spend ≥$100, viewability
   <40%) — `recommendations/forex/gcg/GCG-Quantcast-disallow-July-2026.md`
   and `.txt`.
6. **Tool issues, both worked around, no data gap.** The `metrics_report`
   `filters` parameter returned empty results on every breakdown this
   session (new finding, not the previously-documented `quantcast_campaigns`
   object-filter bug) — worked around with unfiltered pulls filtered
   client-side on Campaign Name; every total ties to the cent against the
   account-level campaign summary. The Domain/App breakdown exceeded the
   sync call's token limit and then hit an MCP session expiry on retry;
   recovered via `quantcast_async_report` (CSV export), which ties to the
   account total within $2.68 — expected two-decimal rounding across 10,586
   CSV rows, not a data issue.

## Phase 3 (Model) — CLOSED 2026-08-19

Model workbook and `figures.json` built via
`tools/forex-gcg-july-2026-model/build_model.py`: 56 declared figures,
spend basis stated, history (June, verbatim from the delivered June
report) and MoM table above. `verify_numbers.py` run against the model
xlsx returns 29 MISSING — expected and non-blocking: the script's xlsx
reader (`protection_scan.text_from`) only scans string cells, and the
model stores its figures as numeric cells, same as the GGMI July model
(confirmed by running the same check against
`reports/forex/ggmi/2026-07/model/GGMI-July-2026-cross-channel-model.xlsx`,
which returns 38 MISSING for the identical reason). This gate is a Phase
5 check on the built deck/report, not on the Phase 3 model; it reruns
clean once the narrative and deck carry these figures as text.

## Open before narrative (Phase 4) can start

1. ~~July client funnel rows (submitted/live/approved/funded/traded) —
   Renzo.~~ RESOLVED 2026-08-21, see the Client funnel section below.
2. Comms since the June report — Renzo. Still open, unconfirmed.

Neither blocks the model (all six channels are tracker-reconciled and in
`figures.json`). Comms remains a genuine open item; the narrative was
drafted without a confirmed answer and should be checked against it before
delivery.

## Phase 4-5 (Narrative + Build) — 2026-08-20

Narrative drafted (`output/GCG-Jul-2026-narrative-draft.md`) without the two
open items above; the funnel slide is cut per the delivered-deck doctrine
(external data not on hand does not ship as a placeholder). Deck built to 12
slides (`tools/forex-gcg-july-2026-deck/build_deck.py`). Two figures added
to `figures.json` at build time for the currency-floor gate: the June
disallow domains still delivering in July ($11,087) and the refreshed
35-domain list total ($13,456), both already sourced in the Quantcast section
above and in `recommendations/forex/gcg/GCG-Quantcast-disallow-list-July-2026.md`.

`verify_numbers.py` on the deck: 4 MISSING (0 UNSOURCED), all accepted —
three are negative-valued figures.json entries that ARE in the deck text in
natural phrasing (a `verify_numbers.py` sign-matching limitation, recorded in
`KNOWN-BUGS.md`); one (`azerion.viewability_vendor_claim`, 71.28%) was
deliberately kept out of the client deck since it is the vendor's own figure
conflicting with the computed 64.95% already used everywhere — flagged to
Renzo rather than resolved unilaterally. `protection_scan.py`: PASS, 0
BLOCK, 0 WARN. Render QA could not complete in this session (PowerPoint
AppleScript automation unresponsive); slide count and shape-bounds verified
programmatically only. Full detail in `../BUILD-STATUS.md`.

Team-lead's render-QA round (2026-08-20) found 5 issues, all fixed: a
table/card overlap clipping status columns on slides 9-10, an em dash in the
cover title, a missing Jul 29-31 row in the Azerion weekly table (now
reconciles to the month), a Meta conversion-campaign sessions gap (Laura
checklist #3 — disclosed as unavailable this month rather than omitted, not
fully MET), and a column-width wrap on slide 6. Full list in
`../BUILD-STATUS.md`. Gates re-run clean after fixing.

## Client funnel — added 2026-08-21

**Source:** `data/sources/GCG-client-funnel-Jan-Jul-2026.xlsx`, sheet
"Export". Scope filter verified in the file's own footer row: "Website es
Forex.com US Spanish", months Jan-Jul 2026 — the correctly-scoped segment,
replacing the earlier whole-site export that was rejected as unusable for
this deck. Pulled/filed 2026-08-21.

**Maturation basis:** June's figures in this export (submitted 325, live
309, approved 153, funded 52, traded 41) differ from the June deck's
published snapshot (322/306/145/41/30) because approvals and funding
continue to land after month close; this is the client's own dashboard
maturing, not a discrepancy to explain. Per instruction, THIS export is the
comparison basis for both July and June — the published June-deck snapshot
is not used in any MoM calculation and is not referenced on the deck (no
restatement commentary; the client's data, described neutrally).

**GA4-divergence note:** the client's own July session count (39,446) and
GA4's ES sessions (66,398) diverge by scope and are not reconciled — same
ruling as June. The funnel slide uses only the client's own session figure;
the GA4 slide is untouched and the two numbers never appear together on one
slide.

**July / Q1 / Q2 figures used (verified against the source file):**

| Metric | Q1 (Jan-Mar) | Q2 (Apr-Jun) | June (comparator) | July |
|---|---|---|---|---|
| Unique Sessions | 41,047 | 162,874 | 67,545 | 39,446 |
| App Starts | 6,997 | 7,977 | 2,592 | 2,970 |
| App Start Rate | 17.0% | 4.9% | 3.8% | 7.5% |
| Submitted | 1,204 | 1,036 | 325 | 404 |
| Live | 1,166 | 996 | 309 | 389 |
| Approved | 525 | 475 | 153 | 162 |
| Approved Rate | 43.6% | 45.8% | 47.1% | 40.1% |
| Funded | 153 | 164 | 52 | 32 |
| Funded Rate | 29.1% | 34.5% | 34.0% | 19.8% |
| Traded | 124 | 132 | 41 | 24 |

Added to the deck as slide 12 (`CLIENT FUNNEL · JULY VIEW`), positioned
after GA4 site traffic and before the cross-channel closer, now slide 13.
`figures.json` extended with the 30 figures above (as `funnel.*` keys) plus
the 10 June comparator values in `history`. Gates re-run: `verify_numbers.py`
same 4 previously-accepted MISSING (0 UNSOURCED, all new funnel figures
matched clean); `protection_scan.py` PASS 0/0; shape-bounds 13/13 clean.

## Viewability demoted (2026-08-24)

DOCTRINE §11 standing ruling (2026-08-17, GGMI cycle): viewability is a
vanity metric — data-point mention only, no headline, no KPI tile, no 70%
floor language in a client deck. Applied across slides 7/8/10/13; see
`../BUILD-STATUS.md` for the full change list. `mom.quantcast_viewability_pts`
moved to the accepted-MISSING set on `verify_numbers.py` (5 accepted total
now) since its only deck occurrence, a "2.36 points" delta sentence, was
removed along with the rest of the viewability emphasis. `protection_scan.py`
PASS 0/0.

## §8 sweep — June-list-not-applied ruled internal (2026-08-24)

Renzo ruling: the June Quantcast disallow list's never-applied status
($11,086.71 still delivered on 18 domains, yahoo.com $2,270→$2,359) is an
internal accountability matter Renzo handles directly, not client-deck
material. Removed from slide 7's site-list card and slide 13's HIGH
blocker; both figures.json entries that existed solely to source that text
(`quantcast.june_disallow_spend_still_delivered`,
`quantcast.july_disallow_refresh_spend`) removed too. The evidence itself
is untouched and stays the internal record: this section above, plus
`recommendations/forex/gcg/GCG-Quantcast-disallow-list-July-2026.md`, which
now opens with an explicit "Internal, not client-facing" marker per the
ruling. Full 13-slide §8 sweep run fresh; only slides 7 and 13 held
violations, the other 11 read clean on a fresh pass (target statements,
performance framing, and the funnel slide's client-journey neutrality all
held up). Gates re-run: `verify_numbers.py` unchanged at 5 accepted MISSING
(the two figure removals matched the two text removals exactly);
`protection_scan.py` PASS 0/0; shape-bounds 13/13 clean.

## Azerion spend-basis unification (2026-08-25)

Slides 9-10's weekly and audience tables carried Azerion's vendor-delivery
basis ($28,615.386 total) while the same slides' headline/tiles already used
the tracker basis ($31,477) — two bases on one channel. Renzo ruled: tracker
basis throughout, per DOCTRINE §1's standing "recalculate downstream
silently" rule. Scale factor = 31,477 / 28,615.386 = 1.10000263..., matching
the account's known ~1.10 fee-and-adjustment relationship to the cent.

**Vendor-delivery basis (original, source of truth for QA and vendor
conversations, kept here):**

| Week | Spend (vendor) | Apps | CPA (vendor) |
|---|---|---|---|
| Jul 1-7 | $8,829.17 | 23 | $383.88 |
| Jul 8-14 | $7,955.99 | 15 | $530.40 |
| Jul 15-21 | $8,033.27 | 22 | $365.15 |
| Jul 22-28 | $2,895.14 | 20 | $144.76 |
| Jul 29-31 | $901.81 | 0 | — |
| **Total** | **$28,615.39** | **80** | **$357.69** |

| Audience | Spend (vendor) | Apps | Cost/app (vendor) |
|---|---|---|---|
| Professional Tools | $3,553.65 | 18 | $197.43 |
| Trust | $3,478.55 | 13 | $267.58 |
| Trusted Broker | $3,432.16 | 11 | $312.01 |
| Broker 1 | $4,112.62 | 13 | $316.36 |
| Language Broker | $6,727.63 | 16 | $420.48 |
| Spanish Platform | $7,310.78 | 9 | $812.31 |
| **Total** | **$28,615.39** | **80** | — |

**Tracker basis (deck, as of 2026-08-25), scaled by 1.10000263, whole
dollars, residual placed in the largest week/audience:**

| Week | Spend (tracker) | Apps | CPA (tracker) |
|---|---|---|---|
| Jul 1-7 | $9,711 | 23 | $422.22 |
| Jul 8-14 | $8,752 | 15 | $583.47 |
| Jul 15-21 | $8,837 | 22 | $401.68 |
| Jul 22-28 | $3,185 | 20 | $159.25 |
| Jul 29-31 | $992 | 0 | — |
| **Total** | **$31,477** | **80** | — |

| Audience | Spend (tracker) | Apps | Cost/app (tracker) |
|---|---|---|---|
| Professional Tools | $3,909 | 18 | $217.17 |
| Trust | $3,826 | 13 | $294.31 |
| Trusted Broker | $3,775 | 11 | $343.18 |
| Broker 1 | $4,524 | 13 | $348.00 |
| Language Broker | $7,400 | 16 | $462.50 |
| Spanish Platform | $8,043 | 9 | $893.67 |
| **Total** | **$31,477** | **80** | — |

Both tables' scaled totals sum to $31,477 exactly. Ranking order is
unchanged in both tables (pure scaling is order-preserving) — verified
Professional Tools < Trust < Trusted Broker < Broker 1 < Language Broker <
Spanish Platform on both bases, so PRIORITIZE/MAINTAIN/REDUCE-REMOVE and the
"July 22-28 produced the strongest weekly reported CPA" read both still
hold. `figures.json` extended with all twelve new tracker-basis figures.
Gates re-run: `verify_numbers.py` and `protection_scan.py` results in
`../BUILD-STATUS.md`.
