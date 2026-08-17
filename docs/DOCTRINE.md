# Reporting Doctrine

The rules that govern what goes into a client artifact. Every one was ruled on
after something went wrong, and the cost of each is recorded in
`PROJECT_RETROSPECTIVE_AND_LESSONS_LEARNED.md`.

Read this before drafting, not after. `scripts/protection_scan.py` enforces the
mechanical half; the rest needs your judgment.

---

## 1. Numbers

**Client-facing spend equals the client's budget tracker.** Not the platform
figure, not the vendor invoice. When they differ, recalculate everything
downstream silently and keep the reconciliation in the Spend Tracker note and
the Billable tab. The client never sees adjustment commentary.

**Before writing any number the client can cross-check, find out what number
they already hold.** This rule arrived three separate times in three different
disguises during one cycle: the tracker for GGMI spend, the tracker again for
GCG, and a prior review deck for geo figures. It costs one message to ask and
two rounds of edits to skip.

**Conversions never sum across channels.** Four channels report four different
events from four different systems. The Total row gets a dash in the
conversion and CPA cells, plus the footnote: conversions come from different
systems and funnel stages, so no blended total is shown.

**Reconcile every sub-table to its channel total.** If a row was dropped for
space, add it back or label the table "top N of M."

**Never blend the entities.** GGMI and GCG stay separate in every sheet, deck
and model.

---

## 2. The agency scorecard

**We are measured on submitted applications and cost per submitted
application.** That is what media spend buys.

Approval, funding, activation and trading belong to the client's own
application-review and account-activation journey. Describe them neutrally
when they appear. Never own them, never apologise for them, and never put a
cost-per-funded or cost-per-traded figure on a slide without context, because
a near-zero denominator produces a number like $3,762 that says nothing except
that few accounts funded.

Cost per submitted application is the most protective number in any deck. Put
it in early rather than adding it last.

---

## 3. Voice

**Tone (Renzo ruling 2026-08-17): calm, direct, evidence-based, accountable,
collaborative.** The guiding formula for every finding, card and headline:
state the fact → explain the impact → state what needs to happen next. No
drama, no victory laps, no slogans; the evidence carries the weight.

- Active voice. A person or a channel acts; objects do not act on their own.
- No em dashes. Commas, periods, or a line break.
- Cut adverbs and throat-clearing.
- Two items beat three. No slogans, no pull-quote phrasing.
- Be specific. Name the metric instead of calling the numbers strong.
- **Never write "cheap."** Say low CPM, low CPC, or give the figure.

Run `stop-slop` on every client-facing draft. It catches AI tells. It does not
catch section 4, which needs its own pass.

---

## 4. Statements against interest

Any sentence where the grammatical actor causing a bad outcome is us. All of
these survived a stop-slop pass and had to be caught separately:

| Written | Problem | Rewrite as |
|---|---|---|
| "extra budget bought worse auctions" | we are buying the bad outcome | the delivery mechanics that produced it |
| "the inventory the June campaigns bought" | same, with the campaign as actor | what the diagnostic revealed |
| "our buying skewed older" | agency as cause | the objective's optimisation behaviour |
| "for most of H1" | time-scope creep | the reporting month, plus the fix |

Facts do not change. The grammatical actor does. A scale-up that revealed a
problem is a diagnostic that produced a map, and that is not spin, it is what
happened.

Do not extend a bad fact backward in time. The reporting month plus the fix is
the story.

---

## 5. Forbidden vocabulary

These never appear in a client artifact. `protection_scan.py` blocks on each.

`fee` · `raw` · `adjustment` · `adjusted` · `reconciled` · `reconciliation` ·
`basis` · `violation` · `breach` · `compliance` · `internal` · `cheap` ·
`wasted` · `blended CPA`

They expose billing mechanics, restatement, or an internal boundary the client
materials deliberately do not discuss.

---

## 6. Gaps read as plans

Every problem ships with its fix and an owner. Every gap reads as a plan with a
date.

"Pending vendor detail" became "an intentionally small first flight, reporting
in full next month." Same facts, and the second one does not hand the client an
open question.

Carry every commitment made in a prior deck. It is delivered, re-sequenced with
a stated reason, or you get asked about it live.

---

## 7. Compliance

### GGMI (LATAM, Mexico)

Mexico paid placements are limited to traditional commodities: oil, crops,
metals. No FX, forex, crypto, indices or equity references in the placements.

Brand-term bidding on the FOREX.com name is the accepted exception, and
platform-first terms (MetaTrader, TradingView, "trading online", "plataforma")
are the sanctioned workaround.

**Mask FX-adjacent strings in client-facing material.** A bare "forex.com"
keyword becomes "brand term." An ad set named "TradeForex" gets a neutral
relabel. Keep the internal mapping; do not expose the raw string in a deck the
compliance lead reads.

GGMI is Mexico-only, and that is a delivery rule, not a targeting preference.
Check where the money actually served every month.

### GCG (US Hispanic)

GCG is the US-regulated forex broker, so forex terms are expected. Do not mask
them.

Compliance bites when a deck reproduces ad copy, a headline or a landing-page
claim:

- No absolute exclusivity: not "the only," "the first," "the best," and not
  "el único," "el primero," "el mejor."
- No income or wealth promises. Pair opportunity framing with a risk reminder.
- No safety or protection guarantees. Use "regulated" and "regulado."
- Superlatives need a citation. A "#1" claim carries the CFTC footnote.
- "Regulado por la CFTC, miembro de la NFA" stays accurate, and nothing implies
  a government guarantee of funds.

When in doubt, paraphrase the performance rather than reproduce the claim.

---

## 8. Framing

**Account mechanics stay out of client decks (Renzo ruling 2026-08-17).**
A monthly report covers performance: what delivered, what it cost, what it
means, what happens next. Targeting settings, bid strategies, conversion-goal
configuration and platform internals are operations — they go to the
recommendations file for the account operator, and anything genuinely wrong
gets surfaced to Renzo directly, never to the client. Client-facing next
steps are limited to actions the client owns (vendor lists, their own
measurement, their own funnel) and performance direction (scale, hold, read).

Tracking gaps are measurement to close, not agency failures. Vendor and
cross-functional ownership gets tracked internally and not named in the client
deck.

Never offer a scope reduction or a spend-down exit. Paid media is the
engagement. When a channel underperforms, the move is to concentrate on the
proven converters and complete the measurement.

Do not confess to gaps the client owns, and do not repeat what they already
know.

---

## 9. Quarter-close decks

QBR-first: title, then a blended Summary lead slide in the client's own
monthly-table format, then the quarter story, then traffic and insight slides,
then the month detail, then the close.

Get the slide order approved as a numbered list before building. Prose hides
order, and a deck built in the wrong order gets rebuilt whole.

---

## 10. Delivery

Once Renzo edits the Google Slides file, that file is canonical. Never
re-upload a built PPTX over it. Edits go through `gws slides batchUpdate`
replaceAllText, longest strings first, verifying `occurrencesChanged` on each
call. Local and Drive PPTX files are exports of the Slides, not the source.

Verify every upload by reading the content back.

Never name a competitor in vendor or client communications.
