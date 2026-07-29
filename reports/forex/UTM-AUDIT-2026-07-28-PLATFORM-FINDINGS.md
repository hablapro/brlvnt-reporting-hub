# UTM Implementation Audit — Google Ads, Bing Ads, CM360
**Run 2026-07-28. Read-only, live API pulls. No mutations executed. Companion to `UTM-AUDIT-HANDOVER.md`.**
Enforced against `~/.claude/ecosystem/business/clients/stonex/utm-convention.md` (last verified 2026-07-09).

## Headline

Paid search carries no UTM parameters at all. Not a partial gap, not a casing problem: zero UTM parameters exist anywhere in the Google Ads or Bing accounts, at account, campaign, ad group, or ad level. Both rely entirely on click-ID plumbing (gclid, the SA360 DoubleClick clicktracker), and the SA360 link to the LAT property is still missing, which is why roughly a third of LAT sessions sit unassigned.

Display and native do carry UTMs, and they are the only channels that do. They carry two of the five parameters, in two casings, from two different tagging paths.

Three findings are new. One corrects an assumption in the handover.

## New finding 1: a GCG US campaign defaults its ads onto the LAT page, tagged as Quantcast

CM360 advertiser 16576650 (GCG) holds two landing pages both named **"Default"**:

| ID | Name | URL |
|---|---|---|
| 42586964 | Default | `https://www.forex.com/es-us/` |
| 42594570 | Default | `https://www.forex.com/es/?utm_source=quantcast&utm_medium=display` |

Campaign `Forex_GCG_spanish_conversion_campaign_us` (35436206) points its `defaultLandingPageId` at **42594570**, the second one.

Verified against a live ad: `635959376` ("300x250 Default Web Ad"), active, assigned to 12 placements, resolves to `computedClickThroughUrl: https://www.forex.com/es/?utm_source=quantcast&utm_medium=display`. Five sibling default ads exist at 970x250, 300x600, 320x50, 160x600 and 728x90.

Three consequences, all live right now:
1. GCG US clicks land on the LAT Spanish page instead of `/es-us/`. This is the mechanism behind the handover's open item "GCG US campaigns appear on the LAT property."
2. Those clicks are credited to Quantcast regardless of which vendor served them, including Azerion.
3. Two landing pages sharing the name "Default" means nobody selecting one in the CM360 UI can tell which they picked.

The GGMI advertiser has the same hardcoded page (42592842) wired as the default for campaign 35506122. Its newer Q3 campaign 36170375 defaults to `GGMI_es_default` (`https://www.forex.com/es/`), which carries no UTMs at all and is the likely source of the `s0.2mdn.net / referral` untagged leakage.

## New finding 2: the capitalized traffic comes from a second tagging path, not from the audited ads

GA4 LAT property 508849216, last 14 days, sessions by source, medium and landing page:

| Source / medium | Sessions | Top landing pages |
|---|---|---|
| `Azerion / display` | 704 | (not set) 623, `/es/lp/broker-de-confianza/` 31, `/es/lp/tradingview-forex/` 29 |
| `azerion / display` | 482 | (not set) 431, `/es/` 44, `/es/about-us/overview/` 7 |
| `Quantcast / display` | 412 | (not set) 148, `/es/lp/broker-de-confianza/` 144, `/es/lp/tradingview-forex/` 80 |
| `Quantcast / native` | 329 | `/es/trading-platforms/trading-tools/` 145, `/es/trading-platforms/trading-central/` 132 |
| `quantcast / display` | 148 | `/es/` 66, `/es/about-us/overview/` 43 |
| `Azerion / native` | 27 | trading-tools 14, trading-central 13 |

The split is clean and it is not random. Lowercase display traffic lands on `/es/` and `/es/about-us/overview/`, the exact URLs sitting on the CM360 display ads. Capitalized display traffic lands on the `/es/lp/` campaign landing page set, which appears on none of the CM360 display ads inspected here or in the prior session.

So a second tagging path is pushing capitalized `Source / display` at the LP set, and it now outweighs the audited CM360 display path 1,116 sessions to 630. Normalizing casing inside CM360 would leave the larger half untouched. Locate that path before scoping any casing fix. The candidates are ads in GGMI campaign 36170375 beyond the sampled page, or vendor-side tagging applied by Quantcast and Azerion directly.

This also corrects the handover's "15:1" figure, which was a single-day Quantcast-only reading. Over 14 days the real ratio across both vendors is closer to 1.8:1.

## New finding 3: the Bing tracking template carries a `utm_content` that never fires

**Updated 2026-07-29. The SA360 access block was a client-side error, not a missing permission. Both business-unit managers are reachable when `loginCustomerId` is passed explicitly. What follows is read, not inferred.**

Every Bing campaign carries SA360 custom parameters (`{_dscampaign}`, `{_dsadgroup}`, `{_dsaccountid}=5372690580`), and every ad group carries its own. No tracking template exists at campaign, ad group or ad level. The template lives on engine account `5372690580` (FOREX.com LATAM Bing), under manager `9697709980`:

```
trackingUrlTemplate:
https://ad.doubleclick.net/searchads/link/click?{_dssagcrid}&{_dssadxid}&ds_e_adid={AdId}
&ds_e_target_id={TargetId}&{ifpla: ... &utm_content={QueryString}& ... }
&ds_e_network={network}&ds_url_v=2&ds_dest_url={unescapedlpurl}

finalUrlSuffix:
gclid={msclkid}&gclsrc=3p.ds&{_dsmrktparam}
```

One UTM parameter exists in the entire paid search stack, and it is dead. `utm_content={QueryString}` sits inside an `{ifpla:...}` conditional, which renders only for product listing ads. Every campaign in this account is Search, so the block never fires and the parameter never reaches a URL. Someone intended UTM tagging here and wired it into the wrong conditional.

The final URL suffix maps Bing's `msclkid` into a `gclid` parameter with `gclsrc=3p.ds`, the standard SA360 cross-engine pattern. It carries no UTM parameters. Auto-tagging is off at the SA360 level for Bing and on for Google.

The GCG side resolves to engine account `4781995752`, the same account audited through the Google Ads API, and both surfaces return identical template and suffix values. Nothing is being rewritten between SA360 and Google Ads.

The insertion point is now confirmed: `finalUrlSuffix` on each engine account, appended to what is already there, edited in SA360.

## Platform detail

### Google Ads — GCG US, customer 4781995752

| Level | Tracking template | Final URL suffix | UTM params |
|---|---|---|---|
| Account | SA360 DoubleClick clicktracker (`ds_a_cid=7805662062`) | `gclsrc=aw.ds&{_dsmrktparam}` | none |
| Campaign (6, five enabled) | none | none | none |
| Ad (13 RSAs) | none | none | none |

All 13 ads point at bare `https://www.forex.com/es-us`. Auto-tagging is enabled, so gclid is the only attribution carrier. Campaigns: `GCG_LeadPMax_q3_FY26` (PMax), `GCG_US_Esp_Brand_Search_Google`, two NonBrand Track B, one NonBrand Track A, plus a paused competitor campaign.

Correction for the handover: GCG search ads land on `/es-us`, not `/es/`. The GCG traffic showing up on the LAT property comes from the CM360 default-ad path in finding 1, not from search.

### Bing Ads — LATAM, account 31003116

169 campaigns, 9 active, all named `FX_LATAM_Spanish_MX_*_brlvnt`. The account is shared across regions and business units, and the name prefix alone does not isolate Berelvant's work: `FX_LATAM*` matches 104 campaigns, 95 of them paused legacy across MX, BRZ, ARG, COL and PER. Scope every pull on two conditions, prefix `FX_LATAM` **and** contains `brlvnt`, which returns 14 campaigns (9 active, 5 paused). The account also holds APAC `CIMA_*` campaigns.

Bulk export of the 9 active campaigns, 28 ad groups and 28 responsive search ads:

| Level | Tracking template | Final URL suffix | Final URL |
|---|---|---|---|
| Campaign (9) | none | none | n/a |
| Ad group (28) | none | none | n/a |
| RSA (28) | none | none | `https://www.forex.com/es/` on all 28 |

`AutoTagType: Preserve`, so msclkid is appended without overwriting existing parameters. GA4 does not read msclkid, which makes UTMs the only viable attribution carrier for Bing until SA360 is linked.

### CM360 — profile 10604084, account 5877

Advertiser 16624558 (GGMI) and 16576650 (GCG), the latter audited here for the first time.

| Check | GGMI 16624558 | GCG 16576650 |
|---|---|---|
| Campaigns | `FX_GGMI_Spanish` 35506122, `GGMI_spanish_q3` 36170375 | `GCG_Q2_esp_us_030526` 35343547, `Forex_GCG_spanish_conversion_campaign_us` 35436206 |
| Default LP wired to hardcoded quantcast URL | yes (35506122) | yes (35436206) |
| Default LP with no UTMs | yes (36170375 → `/es/`) | no |
| Duplicate "Default" landing page names | no | yes, two |
| Click-through URL suffix at advertiser, campaign or ad level | none set, `overrideInheritedSuffix: false` throughout | same |

Ads verified in GCG campaign 35436206 (90 active returned, list paginated so more exist): 72 standard display, 12 native tracking, 6 default web ads.

| Ad | Type | Resolved click-through URL |
|---|---|---|
| 635961782 Azerion display | standard | `.../es-us/about-us/why-us/?utm_source=azerion&utm_medium=display` |
| 645206955 Azerion native | tracking | `.../es-us/about-us/why-us/?utm_source=Azerion&utm_medium=native` |
| 635959376 default web ad | default | `.../es/?utm_source=quantcast&utm_medium=display` |

GCG mirrors GGMI exactly: display lowercase, native capitalized, no `utm_campaign` or `utm_content` on either.

One useful negative: no click-through URL suffix is set anywhere in CM360, at any level. The advertiser-level suffix field is free, which makes it the cheapest single insertion point for constant parameters.

## Pass/fail against the StoneX convention

| Check | Google Ads | Bing | CM360 display | CM360 native |
|---|---|---|---|---|
| `utm_source` present | FAIL, absent | FAIL, absent | PASS | PASS |
| `utm_medium` present | FAIL, absent | FAIL, absent | PASS | PASS |
| `utm_medium` exactly `display`, no variants | n/a | n/a | PASS | FAIL, `native` |
| `utm_source` lowercase and matches publisher | n/a | n/a | PASS | FAIL, `Azerion`, `Quantcast` |
| `cid` parameter present | n/a | n/a | n/a | n/a |
| Auto-tagging off where manual UTMs required | n/a for search | n/a for search | PASS | PASS |
| No conflicting or duplicate params | PASS | PASS | FAIL, default LP hardcodes a vendor | PASS |

Two notes on this table, both resolved on 2026-07-29. `cid` is scored `n/a` rather than FAIL: StoneX has not issued the IDs, so the parameter is not in force on any channel. And the search rows are scored against the wrong reference here; the client standard forbids UTMs on paid search, so those rows are compliant. See the corrected standard section below, which supersedes this table wherever they disagree.

## The standard, corrected 2026-07-29

**A proposed taxonomy sat here. It has been withdrawn.** StoneX already has a written, authoritative standard: `GA4 - UTM Tracking requirements`, on the GAIN Capital Confluence wiki at `wiki.gaincapital.com/display/MKTTECHOPS/GA4+-+UTM+Tracking+requirements`, created by madalina.grigoriu, last modified by Wanda Harang on 2025-10-21. The vault convention doc was a partial summary of its display section only. Enforce the Confluence page.

What it mandates:

| Channel | `utm_source` | `utm_medium` | Notes |
|---|---|---|---|
| Paid search | none | none | **UTMs explicitly forbidden.** GA4's Google Ads and SA360 integrations classify the traffic. Manual UTMs override them and lose cost data. |
| Display, DV360 | none | none | Direct GA4 integration |
| Display, direct deals and non-DV360 DSPs | publisher name | `display` | No variation. Avoid auto-tagging, it defaults the display click ID. |
| Affiliate | affiliate ID | `affiliate` | |
| Paid social | social network name | `paidsocial` | One word, no hyphen, no variation |
| Organic social | social network name | `social` | |
| Email | type of email | `email` | |
| SMS | type of send | `sms` | |
| Push | not required | `push` | Medium only |
| Sales, content, trading platform, anything else | category | `referral` | Catch-all for every channel not listed above |
| Direct, organic, referral | none | none | GA4 resolves these itself |

Global rules: lowercase everywhere, no spaces, underscores as separators.

Every example URL in the standard carries `?cid=00012345`. **`cid` is not in force.** StoneX has not issued the IDs, held up by an internal process on their side, so no channel is expected to carry it and its absence is not a finding. Treat it as a deferred requirement owned by StoneX. When the IDs are issued, `cid` becomes a live requirement on every tagged URL and this audit needs a second pass.

Three things the standard does not do, all of which matter here:

1. **It never mentions `utm_campaign`, `utm_content` or `utm_term`.** The standard is source and medium only. Campaign-level attribution, the goal of this project, is outside it. Reaching that goal means amending the Confluence page, not fixing implementations against it.
2. **It does not define native.** CM360 native ads run `utm_medium=native`, a value the standard does not contain. Read strictly, the catch-all sends native to `referral`, which is wrong for paid display inventory. StoneX needs to rule.
3. **Its paid search logic assumes the GA4 integrations are live.** On the LAT property the SA360 link is missing, so the premise fails there and roughly 49% of `live_start` events land in `(unlinked SA360 account)`. The fix is the link, not UTMs.

### What this corrects in this audit

The earlier headline, that paid search carries no UTM parameters and that this is the gap, was wrong. Google Ads and Bing carrying no UTMs is **compliance with the standard, not a defect.** The earlier recommendation to add a UTM set to both through the SA360 final URL suffix would have broken exactly what the standard protects, and it is withdrawn. Do not implement it.

The paid search finding is narrower than stated: the SA360 to GA4 link on the LAT property is missing, which invalidates the standard's own premise on that property. That item was already in the backlog under StoneX ownership and it is now the whole of the paid search fix.

The `utm_medium` value proposed here as `paid-social` was also wrong. The standard says `paidsocial`.

### Compliance against the real standard

| Channel | Live state | Verdict |
|---|---|---|
| Google Ads paid search | no UTMs | Compliant |
| Bing paid search | no UTMs, one dead `utm_content` inside an `{ifpla:}` block | Compliant, with dead code to remove |
| Quantcast and Azerion display, lowercase | `quantcast\|azerion` + `display` | Compliant |
| Quantcast and Azerion display, capitalized | `Quantcast\|Azerion` + `display` | **Violation**, lowercase rule |
| Quantcast and Azerion native | `Azerion` + `native` | **Violation** on casing. Medium value undefined in the standard. |
| Meta, `meta / paid-social` | hyphenated | **Violation**, standard says `paidsocial` |
| Meta, `Meta / social` | capitalized, organic medium on paid traffic | **Violation** twice. Paid Meta tagged `social` is being counted as organic social. |
| Email, `et / email` | | Compliant |
| Push, `LATAM_NA_PN / Push` | capital P | **Violation**, lowercase rule |
| TradingView widget, `tradingview / display` | partnership widget tagged as display | **Violation.** Not a direct deal or DSP. The catch-all sends it to `referral`, and tagging it `display` inflates display. |
| `cid` parameter | absent on every URL on every platform | Not a finding. Deferred by StoneX, IDs not yet issued. |

Two findings survive the reframe unchanged, because both are defects under any standard: the GCG campaign defaulting onto the LAT page credited to Quantcast, and the untagged `s0.2mdn.net` leakage from the no-UTM default landing page.

## Fix backlog, split into approval batches

CM360 changes are mutation-gated. Each batch below gets its own mutation table and its own explicit yes. They are ordered by severity over effort.

**Batch 1. Repoint the GCG default landing page.** Change campaign 35436206 `defaultLandingPageId` from 42594570 to 42586964, then rename 42594570 so no one picks it by accident. Affects 6 active default web ads across 12+ placements. Stops GCG US traffic landing on the LAT page credited to Quantcast. Smallest diff, largest correction.

**Batch 2. Repoint the GGMI default landing page.** Campaign 35506122 from 42592842 (hardcoded quantcast) to a properly tagged GGMI default. Requires creating that page first, since `GGMI_es_default` currently carries no UTMs.

**Batch 3. Normalize native casing.** `Azerion` and `Quantcast` to lowercase on the 12 GCG native ads and their GGMI equivalents. Hold this batch until the second tagging path from finding 2 is located, or the fix covers the smaller half of the traffic.

**Batch 4. Add `utm_campaign` and `utm_content`.** All vendor click-through URLs, both advertisers. Largest batch, needs a bulk approach given the ad count, and needs the taxonomy above approved first.

**Client-owned, no Berelvant mutation.** SA360 to GA4 link on the LAT property. Account-level final URL suffix on Google Ads and Bing, applied in SA360. Both sit with StoneX and both are already in flight through the Roshni document.

## Access gaps and open items

| Item | Status |
|---|---|
| ~~SA360 API access~~ | **RESOLVED 2026-07-29.** Not a permission gap. The MCP's default login does not cover these managers, so `loginCustomerId` must be passed on every call: its own ID for a manager, the parent manager for an engine account. GGMI `9697709980` to Bing `5372690580`, GCG `5700106280` to Google Ads `4781995752`. The `3332505241` in the old account map is a stale ID and does deny; it is superseded. |
| ~~Bing account-level tracking template~~ | **RESOLVED 2026-07-29.** Read from SA360. See finding 3. |
| CM360 pagination | Landing page, campaign and ad lists all returned `next_page_token` and the MCP tools accept no page token. Both advertisers may hold more landing pages and campaigns than listed here. |
| CM360 ad inventory in campaign 35436206 | 90 returned, more exist. The 248-ad figure in the handover is unsourced and should be re-derived. |
| Source of capitalized `/es/lp/` traffic | Open. See finding 2. Blocks batch 3. |
| Meta, email, push | Out of scope for this run. Meta remains the largest unaudited channel by spend. |
| `(not set)` landing page on 623 of 704 Azerion display sessions | Consistent with the open page_view gap. Same diagnostic. |

## Reproduce

- Google Ads: `run_gaql_query` on 4781995752, three queries over `customer`, `campaign`, `ad_group_ad`, selecting `tracking_url_template`, `final_url_suffix`, `url_custom_parameters`, `final_urls`.
- Bing: `bing_ads_list_campaigns` on 31003116 to find the 9 active IDs, then `bing_ads_bulk_download` scoped to those IDs with entities Campaigns, AdGroups, Ads.
- CM360: `cm360_list_landing_pages` and `cm360_list_campaigns` per advertiser, then `cm360_get_ad` for resolved routing. The list endpoints do not return click-through URLs, only `get_ad` does.
- GA4: `runReport` on 508849216, dimensions `sessionSource`, `sessionMedium`, `landingPagePlusQueryString`, metric `sessions`, 14 days, limit 400. Filter locally, the MCP `dimensionFilter` is still broken.
