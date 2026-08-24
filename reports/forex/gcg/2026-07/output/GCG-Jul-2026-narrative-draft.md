# GCG (US Hispanic) — July 2026 Performance Narrative — DRAFT for deck build

Internal draft, pending Renzo review. Facts from `../qa/qa-and-model.md` and
`../figures.json`. Client-facing spend equals the client budget tracker. Built
to the delivered GGMI July 13-slide template (`docs/DOCTRINE.md` §11):
evidence and decision on one slide per channel, granular tables client-facing,
no blended total.

## Executive summary

July ran $136,224 across six lines, up 16.4% from June's $117,024. Google
added a second line, PMax, launched the week of July 13. Native added
Quantcast alongside Azerion, its first full month on both vendors.

Google's two lines closed the month at 122 submitted applications and $390.60
per application, on the same Step 5 tracking. Search alone carried 73
applications at $403.81, up from 67 at $336.18 in June: spend outgrew
applications again (+30.9% vs +9.0%), but by less than June's gap (+48% vs
-12%). The ad-rank work from June moved the numbers on Track A Trust, the one
track it reached this month: impression share rose from 27% to 32.6%, rank
losses fell to 58.7% from the 64-76% band every track was losing in June, and
Trust went from the account's worst CPA ($433) to its volume leader (28
applications at $390.86). Authority and Platform still lose 63 to 70% of
available impressions to rank. PMax matched Search's efficiency in its first
partial month: $370.91 per application against Search's $403.81, across the
18 days it delivered.

Meta's conversion-objective shift, promised in June, is live: one campaign
now runs on Meta's conversion objective, optimizing to the submitted-
application event, and carried 44% of a Meta line that fell 77.4% as the
prior traffic campaign wound down by design. The remaining two campaigns
still run on the traffic objective and are read on reach, impressions and
CPM; the conversion campaign is read on CTR, clicks and its own event volume.
We read the two objectives independently and never against each other.

Azerion had its best application month: 80 partner-attributed applications
at $393.46, against 58 at $510.10 in June (apps +37.9%, cost per app -22.8%).
Viewability improved to 64.95% from 58.8% but still sits under the 70%
industry floor. Azerion Native completed its first full month at
$9,362, delivery-only, viewability above the floor at 72.68%.

Quantcast's display line held close to flat (-2.3%) with viewability
improving for a second straight month (46.9% to 49.26%), still under the
floor. Quantcast Native launched in July, its first month on this line,
viewability 57.98%. The June disallow list was never applied: all 18 flagged
domains delivered again in July, $11,087 combined. A refreshed 35-domain list
goes out with this cycle.

Spanish-audience site traffic came in at 66,398 sessions, down 17.2% as Meta
spend pulled back by design; this sits just under the roughly 70,000 base the
channel held from January through May.

The client's own funnel shows submitted applications up 24.3% to 404 on
39,446 sessions, down 41.6% from June: the top of the funnel converted more
efficiently on far less traffic, with the application-start rate more than
doubling to 7.5% of sessions from June's 3.8%. Approved and funded rates
softened against June and the Q2 average, sitting in the client's own review
and account-activation journey.

## Channel detail

### Google Search — $29,478, 73 submitted applications, $403.81 CPA
- Target: non-brand Spanish-language search across three tracks (Trust,
  Authority, Platform) plus a brand track, US only.
- Spend +30.9% MoM, applications +9.0% (67 to 73), CPA +20.1% ($336.18 to
  $403.81). The direction from June is unchanged but less severe: spend still
  outgrows applications, just not by as much.
- The rank work landed where it was applied. Track A Trust: impression share
  27% to 32.6%, rank losses down to 58.7% (the account's best), CPA $433 to
  $390.86, and it became the volume leader at 28 applications. Track B
  Authority and Platform still lose 63 to 70% of available impressions to
  rank; the brand track loses 79%.
- Strongest keywords: "forex confiable" at $143.16 per application (9
  applications), "como hacer trading" on its second ad group at $111.44 (6
  applications), "broker forex usa" broad match at $282.26 (15
  applications, the account's highest-volume single keyword).
- Weakest spend concentration: "invertir en forex" at $2,331.88 for 2
  applications, and three Spanish-spelling variants of "trading en
  espanol/español" that combined for over $2,000 with zero applications.
- DECISION: extend the rank work to Authority and Platform before adding
  further budget; Trust proves the lever works.

### Google PMax — $18,175, 49 submitted applications, $370.91 CPA
- Target: Spanish-language creative, US-only delivery, Google's automated
  Performance Max inventory. New line, launched week of July 13.
- 49 applications in roughly 18 days of delivery at $370.91, at or below
  Search's full-month CPA of $403.81, on the same Step 5 event. No June
  comparator; this is the first month.
- DECISION: give PMax a second full month before rebalancing spend between
  it and Search; early efficiency already matches the established line.

### Meta — $6,940, three campaigns split by objective
- Target: US adults 18-65 (age is locked to this range across every active
  ad set by Meta's own Financial Products and Services category, not a
  targeting choice we control), Advantage+ Audience on, Spanish-language
  creative on both objectives. No targeting change in July; this range and
  setting held all month.
- Spend fell 77.4% against June's tracker figure as the prior traffic
  campaign wound down and the conversion campaign launched: this was the
  planned reallocation, not a pullback in the channel.
- Traffic objective, two campaigns: $3,888, 375,255 impressions, 10,509 link
  clicks, CPM $10.36 against June's $11.35, CTR 2.72% and 3.47% against
  June's 2.76%. Reach is not summed across campaigns; the two traffic
  campaigns reached 173,989 and 130,525 people respectively, both below
  June's single-campaign reach of 1,527,444 in proportion to the 77% spend
  reduction, at a lower frequency (1.2 to 1.3 versus June's 2.0).
- Conversion objective, one campaign: $3,052, 1,258 link clicks, 1,032
  landing-page views (82.0% of clicks), 284 conversion-pixel events. Its
  CPM of $25.91 is expected for a conversion objective bidding a narrow
  action and is not read against the traffic line's CPM.
- DECISION: hold the current split through a second full month before
  moving further budget between objectives; the conversion campaign has
  one month of data.

### Meta — creative performance
- Conversion objective: broker_trust_q2_trackA carries the volume (177
  events on $1,656.39, most efficient large-spend creative on this side)
  and scales. forex_plat_q2_trackB is the most efficient single creative
  ($7.38 per event on $236.29) and has room to grow. exp_plat_q2_trackB
  holds at $12.81 per event. edu_trust_q2_trackA is the weakest with
  meaningful spend ($34.75 per event on $382.20) and comes out.
  trading_proof_q2_trackA has too little spend to score yet.
- Traffic objective (the live Q3 campaign only; the Q2 campaign paused
  after July and carries no forward call): forex_plat_q2_trackB leads at
  3,171 clicks and a 5.32% link CTR and scales. broker_trust_q2_trackA
  holds at 2.77% CTR. exp_plat_q2_trackB is thin on spend ($152.76) and
  holds for a second read.
- DECISION: scale forex_plat_q2_trackB on both objectives and
  broker_trust_q2_trackA on conversion; remove edu_trust_q2_trackA from
  the conversion rotation.

### Quantcast — $39,860 across display and Native
- Target: Spanish-language US audiences across Quantcast's FX-vertical
  inventory; geo verified at 100% US across every state row on both
  campaigns.
- Display: $29,857, viewability 49.26% against June's 46.9%, a second
  straight month of improvement, still under the 70% industry floor.
- Native: its first full month on this line, viewability 57.98%, no June
  comparator.
- The June disallow list was not applied: all 18 flagged domains delivered
  again in July, $11,087 combined, and the largest single flag
  (yahoo.com) grew from $2,270 to $2,359. A refreshed 35-domain list,
  $13,456 of July spend, goes out with this cycle.
- DECISION: confirm the refreshed list reaches Quantcast and is applied
  before August spend; this is the second cycle the same floor has been
  proposed.

### Azerion Display — $31,477, 80 submitted applications, $393.46 CPA
- Target: six Spanish-language audience segments across Azerion's FX
  vertical (Spanish Platform, Language Broker, Broker 1, Professional
  Tools, Trust HTML, Trusted Broker), US-only delivery.
- Best application month on this line: applications +37.9% (58 to 80),
  cost per application -22.8% ($510.10 to $393.46).
- Viewability improved to 64.95% from 58.8% (up 6.15 points), still under
  the 70% floor.
- DECISION: rebalance spend toward the audiences with the strongest cost
  per application below.

### Azerion Display — audience ranking
| Audience | Applications | Cost / app | August status |
|---|---|---|---|
| Professional Tools | 18 | $197.43 | PRIORITIZE |
| Trust HTML | 13 | $267.58 | PRIORITIZE |
| Trusted Broker | 11 | $312.01 | MAINTAIN |
| Broker 1 | 13 | $316.36 | MAINTAIN |
| Language Broker | 16 | $420.48 | MAINTAIN |
| Spanish Platform | 9 | $812.31 | REDUCE-REMOVE |

Spanish Platform carries the largest spend on this line and the weakest
cost per application; it is the reallocation candidate. Professional Tools
and Trust HTML both improved sharply from June, when Trust HTML was the
line's weakest performer.

### Azerion Native — first full month, delivery-only
- $9,362 across six creatives, ramped from a near-zero first week to
  roughly $3,400 in the final week. Viewability 72.68%, above the 70%
  floor. No conversion tracking on this line; read on delivery and
  viewability.
- Click-through rate fell as delivery scaled (from 0.33% in week two to
  0.05% in the final week), the pattern behind the creative table below.

| Creative | Viewability | CTR | August status |
|---|---|---|---|
| Phone_closeup | 76.9% | 0.071% | SCALE |
| Mobile_desktop_view | 76.7% | 0.073% | SCALE |
| Trader_laptop_thinking | 76.0% | 0.066% | RETAIN-TEST |
| Third_person_perspective_mobile | 66.8% | 0.071% | RETAIN-TEST |
| City_view_MHTN | 66.8% | 0.075% | RETAIN-TEST |
| Multiple_screens_graph | 72.3% | 0.063% | RETAIN-TEST |

- DECISION: scale the two strongest creatives on viewability and CTR
  together; hold the rest for a second month before any removal, this is
  the line's first full month.

## Site traffic — GA4

- Spanish-audience sessions on the US property came in at 66,398, down
  17.2% as Meta spend pulled back by design; this sits just under the
  roughly 70,000 base the channel held from January through May.
  Unique visitors came in at 29,901, down from 41,795 in June.
- Meta's session capture improved to 67.2% of link clicks from
  approximately 57% in June, a healthy rate for a paid-social line.
- DECISION: watch August as Meta's new split settles; no organic decline
  sits under this line, the softness tracks the paid pullback.

## Client funnel — July view

- Source: the client's own application funnel export (Website = Forex.com
  US Spanish), Jan-Jul 2026. This is a different measurement scope from the
  GA4 read above; the two session counts are not reconciled and never
  appear on the same slide.
- Top of funnel: submitted applications came in at 404, up 24.3% from
  June's 325, on sessions of 39,446, down 41.6% from June's 67,545. The
  application-start rate came in at 7.5% of sessions, up from June's 3.8%,
  more than double on far fewer sessions. Live applications came in at
  389, up 25.9% from June's 309.
- Downstream, the client's own review and account-activation journey:
  approved came in at 162 at a 40.1% rate against June's 47.1%; funded
  came in at 32 at a 19.8% rate against Q2's 34.5% average; traded came in
  at 24 against June's 41.
- June's figures in this section come from the same export as July's, not
  the June deck's published snapshot; approvals and funding continue to
  mature after month close, so the client's current system of record is
  the correct comparison basis.
- TAKEAWAY: the top of the funnel is converting more efficiently on fewer
  sessions; the downstream steps are the client's own journey to watch
  alongside media.

## Data quality and measurement

1. Google Search reconciles to the tracker exactly; the submitted-
   application definition is unchanged.
2. PMax is a new line with one partial month; its efficiency read is
   directional until a full month closes.
3. Meta's two objectives are read independently and never compared to
   each other; reach is never summed across campaigns.
4. Azerion and Quantcast results are each read on their own partner
   reporting, never summed or blended into a single per-application cost.
5. The client funnel export arrived scoped correctly (Website = Forex.com
   US Spanish) and is used for both July and its June comparator; the
   client's own session count is a different measurement scope from GA4
   and the two are never shown together.

## Recommended next steps (August)

1. Extend the search rank program to Track B Authority and Platform;
   Track A Trust proves the lever moves both share and cost.
2. Give PMax and the Meta conversion objective a second full month before
   moving further budget; both launched or shifted mid-quarter.
3. Confirm the refreshed 35-domain Quantcast list reaches the platform and
   is applied; this is the second cycle the same floor has been proposed.
4. Rebalance Azerion spend toward Professional Tools and Trust HTML, the
   two strongest audiences on cost per application; hold Spanish Platform
   for review.
5. Watch the client's downstream steps: approved and funded rates softened
   against June and the Q2 average this month. This sits in the client's
   own journey; the media-side action is to keep the top of funnel
   converting the way it did in July.

## Answering June's five commitments

1. **Meta conversion-objective shift.** Delivered. One campaign runs on
   Meta's conversion objective, optimizing to the submitted-application
   event, 44% of July's Meta spend.
2. **Search ad-rank program before budget.** Partially delivered. Track A
   Trust shows the full effect (impression share up, rank loss down, cost
   per application down, volume leadership). Authority and Platform have
   not yet had the same work applied and still lose 63 to 70% of available
   impressions to rank; spend outgrew applications again in July.
3. **Apply the Quantcast blocklist.** Not applied. All 18 flagged domains
   delivered again in July at $11,087 combined. A refreshed 35-domain list
   goes out with this cycle.
4. **Concentrate Azerion on Trusted Broker and Broker 1; shift format
   weight.** Partially delivered. Both audiences held efficient, but
   Professional Tools is now the line's actual leader and becomes the
   priority audience for August. The format-level breakdown (728x90 versus
   300x600) was not present in this month's vendor file, so the shift
   cannot be verified; the ask goes back to the vendor for August.
5. **Put the start-to-submit funnel step on the joint roadmap.** Delivered.
   The correctly-scoped funnel export arrived and is on the deck this
   cycle: the start-to-submit step improved (application-start rate 3.8%
   to 7.5%), while approved and funded rates softened against June and
   the Q2 average, both the client's own downstream journey.
