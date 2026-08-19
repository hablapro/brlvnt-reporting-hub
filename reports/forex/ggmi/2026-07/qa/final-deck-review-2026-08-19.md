# Final-deck review — GGMI July 2026

Reviewed 2026-08-19. Compares the deck Renzo delivered to the client
(Google Slides `1IbiLHpMdu_EFG4zaiTv4Xu13boJKTgxLbayntrxH_o8`,
"GGMI_LATAM_July_2026_Review-final", 13 slides, canonical) against the
built PPTX (16 slides), and records Laura Acosta's comments from
2026-08-19. This diff is the template baseline for August and every
month after.

---

## 1. What Renzo changed before delivering

### Structure: 16 slides became 13

| Built (16) | Delivered (13) | What happened |
|---|---|---|
| 1 Title | 1 Title | Kept |
| 2 Summary, blended view (653 apps, organic + paid) | cut | Removed whole. Trading-volume dash and country-tab dependency went with it; open items 1 and 2 from RESUME resolved by removal |
| 3 Executive summary | 2 Executive summary | Kept, absorbed the scorecard framing and the programmatic decisions into one slide |
| 4 Cont'd executive summary (three findings) | cut | Folded into slide 2 |
| 5 Bing performance | 3 Bing performance | Kept; window table (Jul 1-10 / 11-22 / 22-31) and the scale-carefully read now live on the same slide |
| 6 Bing read and recommendations | cut | Merged into slide 3 |
| new | 4 Bing top keywords | Promoted from the internal partner-detail doc: top-10 keyword table with spend, clicks, apps, CPA, plus the outside-top-10 converter and a decision line |
| 7 Quantcast performance | 8 Quantcast display vs native | Two built slides became one. New content: Quantcast Native called out at $10,003 spend, 0 results, decision STOP QUANTCAST NATIVE |
| 8 Quantcast read and recommendations | cut | Merged into slide 8 |
| 9 Azerion performance | 5 Azerion performance | Kept |
| 10 Azerion read and recommendations | cut | Replaced by two new slides |
| new | 6 Azerion audience ranking | Audience table ranked by result (Instrument-focused 9 apps ~$339, Experience 10 apps ~$617, TV/Brand/Trust 0 apps) with an AUGUST STATUS column: PRIORITIZE / MAINTAIN / REDUCE-REMOVE |
| new | 7 Azerion display creative performance | Creative preview cards grouped by audience with the same status labels |
| new | 9 Azerion native creative performance | Four native creatives with spend, clicks, CTR each; labels SCALE / RETAIN-TEST / REMOVE |
| 11 Meta spend and delivery | 10 Meta July delivery + August status | Kept, retitled; August operating status (StoneX owns the flagged-account resolution) given its own block |
| 12 Native and DOOH, new lines | cut | Native folded into the channel slides; DOOH stands alone |
| 13 DOOH campaign overview | 11 DOOH campaign overview | Kept. Venue-mix table with dash placeholders dropped; open item 3 resolved by removal |
| 14 DOOH delivery by city | cut | Dropped |
| 15 GA4 site traffic | 12 GA4 site traffic | Kept |
| 16 Portfolio decisions table | 13 Cross-channel priorities + next steps | Table replaced with four narrative blocks (Bing, Programmatic, Operating constraint, Closeout) and a September FY2027 framing line |

### The pattern behind the edits

1. **Evidence and decision live on one slide per channel.** No separate
   "read and recommendations" slides. Each channel slide ends in a
   DECISION or TAKEAWAY line.
2. **Granular detail is client-facing now.** Keyword-level, audience-level
   and creative-level tables, which the built deck kept in the internal
   partner-detail doc, went into the client deck with explicit
   per-row actions (PRIORITIZE, REDUCE, SCALE, REMOVE, EXCLUDE, STOP).
3. **No blended organic+paid summary.** The 653-apps blended slide is gone;
   the deck opens on the channel table with dashes in the total row, which
   matches doctrine §1.
4. **Creative previews earn slides.** Two slides show the actual creatives
   with per-creative spend/clicks/CTR and a verdict each.
5. **Placeholder rows do not ship.** Every dash-placeholder block waiting on
   external data (trading volume, country tab, DOOH venue mix) was cut
   rather than delivered incomplete.
6. **The closer is a priorities narrative, not a table.**

## 2. Laura's comments (2026-08-19, all unresolved)

Four of five sit on the Meta slide. One is page-level on Azerion.

| # | Slide | Anchor text | Comment | Standing rule it implies |
|---|---|---|---|---|
| 1 | 5 Azerion | (page-level) | "please include the target we are using" | Every channel slide states the audience definition being targeted. Audience descriptions are performance context, distinct from the account-mechanics ban in doctrine §8 |
| 2 | 10 Meta | "10.2%" (Instagram share) | "is this good? this is data but not an insight" | No naked stat. Every number on a slide carries an interpretation: good, bad, expected, or why it moved |
| 3 | 10 Meta | paused-in-August note | "what was the best performance creative(s) in meta? i dont see the split on the different campaign we have. once again, we can't compare an engagement campaign with a conversion one. for engagement please include reach, impressions and CPM. for conversion CTR, sessions, conversions" | Meta reports per campaign, split by objective. Engagement campaigns: reach, impressions, CPM. Conversion campaigns: CTR, sessions, conversions. Plus best-performing creatives. "Once again" means she has asked before; this is a repeat miss |
| 4 | 10 Meta | "CPM ~$1.89" | "how was the CPM in June? higher or lower?" | Every KPI shown gets its prior-month comparator. The deck did this for CPA and CTR but not CPM or reach |
| 5 | 10 Meta | "largest campaign" (reach) | "did the update to 25+ on the target made any difference on reach or cpm? as the target was smaller now?" | When targeting changes mid-flight, quantify the before/after effect on delivery, not just note the change |

### What these mean for the August build

- Meta is the weakest slide in the eyes of the person who scores us. It
  needs the campaign-by-objective split, MoM on every metric, creative
  winners, and the 25+ targeting before/after read.
- Comment 3 says "once again". Check June comms for the first ask and
  treat objective-split Meta reporting as a standing requirement, not
  July feedback.
- Comment 1 partially tensions doctrine §8 (account mechanics out of
  client decks). Resolution applied: audience/target descriptions the
  client asks for are performance context and belong in the deck;
  platform configuration (bid strategies, settings, conversion plumbing)
  stays out. Flag to Renzo if he reads it differently.

## 3. Follow-ups

1. Laura's five comments need replies or resolution in the deck thread.
   Comments 4 and 5 are answerable from data we hold (June Meta CPM,
   pre/post 25+ delivery). Comment 3 defines the August Meta slide.
2. `build_deck.py` and the deck template get rebuilt to the 13-slide
   delivered structure before the August cycle.
3. Doctrine and runbook updated same day as this review (see §11 and
   Phase 7 respectively).
