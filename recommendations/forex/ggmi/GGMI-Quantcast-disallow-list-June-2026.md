# GGMI (LATAM) — Quantcast Site Disallow List — June 2026

**Account:** Quantcast 9969644 — GGMI campaigns (mx)
**Period analyzed:** June 1–30, 2026 · USD
**Prepared:** 2026-07-07, Berelvant
**Status:** Handoff artifact. This repository is reporting only. This list is a recommendation to send to Quantcast (client or Quantcast rep applies the block). Nothing was changed in the account.

**Deliverables:**
- `GGMI-Quantcast-disallow-June-2026.txt` — the plain domain block list to send (one domain per line).
- `reports/forex/ggmi/2026-06/data/GGMI-Quantcast-Apr-Jun-2026-data.xlsx` — tabs "Site List (Domain-App)" and "Disallow Candidates" with the underlying numbers.

---

## What this is

June GGMI Quantcast spend went across 5,951 sites, and it concentrates fast: the top 12 sites carry 50% of spend. Pulling the Domain/App view against Budget Delivered exposes where the cheap, low-quality impressions landed. The disallow list is the set of sites to block so next month's budget moves to viewable, on-audience inventory.

**49 sites qualify, carrying $10,734 — 32% of June GGMI spend.**

## How a site earns a spot on the list

A site is a disallow candidate when either holds:

1. **Low viewability.** Under 35% viewable (the IAB standard is 70%), with meaningful spend and zero to few results. Money on ads that are rarely on screen. This is the bulk of the list.
2. **Audience mismatch.** Games, entertainment, or non-finance utility sites unlikely to hold forex prospects, even when viewable. Examples this month: `poki.com`, `garticphone.com`, `crazygames.com` (games), `biblegateway.com`, `fandom.com`.

## The worst offenders (top of the list)

| Domain | Spend | Impr | Viewability | Results | Reason |
|---|---|---|---|---|---|
| tvazteca.com | $1,346 | 2.0M | 9% | 0 | Low viewability |
| heraldodemexico.com.mx | $1,170 | 2.1M | 9% | 0 | Low viewability |
| milenio.com | $929 | 966K | 23% | 1 | Low viewability |
| poki.com | $790 | 1.1M | 84% | 0 | Audience mismatch (games) |
| biblegateway.com | $642 | 854K | 47% | 0 | Audience mismatch |
| fandom.com | $525 | 470K | 30% | 0 | Audience mismatch |
| eluniversal.com.mx | $511 | 619K | 17% | 0 | Low viewability |
| ebay.com | $505 | 484K | 3% | 0 | Low viewability |
| mediotiempo.com | $430 | 519K | 18% | 0 | Low viewability |
| as.com | $404 | 513K | 31% | 0 | Low viewability |

Full 49-site list: the `.txt` file and the workbook's "Disallow Candidates" tab.

## Notes for whoever applies it

- Send the `.txt` to the Quantcast rep as a domain/app block list, or apply it as a site exclusion on the GGMI campaigns.
- Two of the low-viewability sites are mainstream Mexican news (tvazteca, heraldodemexico, eluniversal, milenio). They are not brand-unsafe; they are being bought as low-viewability inventory (sticky/below-the-fold slots at ~9–23% viewable). Blocking the domain is the blunt fix; a viewability floor on the campaign is the better structural fix and would catch these plus future offenders automatically. Raise both with Quantcast.
- Re-pull and refresh this list every month. Inventory rotates; last month's clean site can be this month's offender.

---

## STANDING PROCESS — run this every monthly report

**Every monthly report that includes Quantcast (or any programmatic/display channel) must include a Domain/App site-list pull and a refreshed disallow list.** Programmatic budgets leak into low-viewability and off-audience inventory continuously, and the only way to catch it is to look at the site level each month.

Steps:
1. Pull the `Domain/App` breakdown with `Budget Delivered` (plus Impressions, Viewability, Results) for the reporting month, per sub-client.
2. Rank sites by spend; flag disallow candidates (viewability < 35% with 0–few results, or audience mismatch).
3. Add a "Site List" and "Disallow Candidates" tab to the channel workbook.
4. Write the disallow list to `recommendations/<client>/<sub-client>/` as a `.txt` block list plus this summary doc.
5. Hand to the client / Quantcast rep to apply. Recommend a campaign-level viewability floor as the durable fix.

This note is mirrored in `reports/README.md` so it is part of the reporting convention, not a one-off.
