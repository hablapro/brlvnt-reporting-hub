# Amendment Request: add `utm_campaign` to the StoneX UTM standard

> **DO NOT SEND. Superseded in two places as of 2026-08-08.**
>
> 1. **The naming convention below was never approved.** Renzo stopped it on 2026-07-31. The
>    `{business_unit}_{market}_{channel}_{period}` pattern puts format into `utm_campaign`,
>    which is wrong: `utm_medium` already carries format, and CM360 campaigns are mixed-format
>    so no single campaign value can be correct. Standing recommendation is to use the CM360
>    campaign name, lowercased. Undecided.
> 2. **The native section is wrong.** It recommends `utm_medium=display` with the format held
>    in `utm_campaign`. That cannot work, for the reason above. Native handling is an open
>    decision: GA4 custom channel group, or merge into display. Undecided.
>
> The business case, the evidence, the paid-search carve-out and the implementation mechanism
> are all still valid and were proven in production. Rewrite the two sections above before
> this goes to StoneX. See `PROGRESS.md` in the UTM Channel Audit project folder.

**Drafted 2026-07-29 by Berelvant. For StoneX MKTTECHOPS review.**
Target document: `GA4 - UTM Tracking requirements`, `wiki.gaincapital.com/display/MKTTECHOPS/GA4+-+UTM+Tracking+requirements`, last modified 2025-10-21.

## The ask

Add `utm_campaign` to the standard for the channels that already require `utm_source` and `utm_medium`. No change to paid search, DV360, direct, organic or referral.

## Why

The current standard defines `utm_source` and `utm_medium` only. Both are working: Quantcast and Azerion clicks arrive in GA4 correctly attributed to vendor and channel. Campaign is a different story. GA4 has no campaign value for any of that traffic, so it reports `(referral)` or `(not set)`.

Measured on the Forex LAT property over the 14 days to 2026-07-28:

| Source and medium | Sessions | Campaign in GA4 |
|---|---|---|
| Azerion display, both casings | 1,186 | none |
| Quantcast display, both casings | 560 | none |
| Quantcast native | 329 | none |
| Azerion native | 27 | none |
| **Total** | **2,102** | **none** |

Every one of those sessions is attributable to a vendor and a channel, and none is attributable to a campaign. The practical effects:

- No campaign-level performance comparison in GA4 for display or native. Prospecting cannot be separated from retargeting, or Q2 creative from Q3 creative, on the analytics side.
- No way to reconcile GA4 sessions against CM360 delivery per campaign. The two systems can only be joined at vendor level.
- Optimisation decisions on display run on vendor-reported numbers alone, with no independent GA4 read at the level the budget is actually set.

Paid search does not have this problem, because the Google Ads and SA360 integrations pass campaign into GA4 directly. Display and native have no equivalent integration, which is exactly why the standard asks them to carry UTMs. Campaign is the parameter that got left out.

## What we are not asking to change

To pre-empt the obvious concern: **paid search stays untagged.** We agree with the current rule and we are not proposing to touch it. Adding manual UTMs to Google Ads or Bing would override the platform integrations and lose cost data, which is precisely what the standard prevents. We verified during this audit that both accounts are clean: no tracking parameters, no final URL suffix UTMs, at account, campaign, ad group or ad level.

Same for DV360, direct, organic and referral. No change.

## Proposed text for the standard

Add to the general guidelines:

> **Campaign parameter**
> Any channel required to include `utm_source` and `utm_medium` must also include `utm_campaign`.
> `utm_campaign` identifies the marketing campaign the click belongs to, using the naming convention below.
> Channels with a direct GA4 integration (paid search via Google Ads and SA360, display via DV360) must not include `utm_campaign`, for the same reason they do not include `utm_source` or `utm_medium`.

Applies to: display via direct deals and non-DV360 DSPs, affiliate, paid social, organic social, email, SMS, push, and the sales, content and trading platform catch-all.

### Naming convention

Lowercase, no spaces, underscores as separators, consistent with the existing global rules.

```
{business_unit}_{market}_{channel}_{period}
```

| Segment | Values |
|---|---|
| `business_unit` | `ggmi`, `gcg` |
| `market` | `latam`, `mx`, `us` |
| `channel` | `display`, `native`, `paidsocial`, `email`, `push` |
| `period` | `q3fy26` style, or `fy26` for always-on |

Example: `https://www.forex.com/es/?utm_source=quantcast&utm_medium=display&utm_campaign=ggmi_latam_display_fy26`

### Mapping for campaigns live today

| CM360 campaign | ID | Proposed `utm_campaign` |
|---|---|---|
| FX_GGMI_Spanish | 35506122 | `ggmi_latam_display_fy26` |
| GGMI_spanish_q3 | 36170375 | `ggmi_latam_native_q3fy26` |
| GCG_Q2_esp_us_030526 | 35343547 | `gcg_us_display_q2fy26` |
| Forex_GCG_spanish_conversion_campaign_us | 35436206 | `gcg_us_conversion_fy26` |

We are not proposing to rename the CM360 campaigns. New campaigns should be named to match their slug from the start, so the two converge over time without a migration.

## Implementation

CM360 supports a click-through URL suffix that inherits from advertiser to campaign to ad. We confirmed on 2026-07-29 that no suffix is set at any level in either advertiser, and that no campaign or ad overrides inheritance. The chain is free.

That makes this a four-edit change, not a per-ad change:

| Step | Where | Edits | Effect |
|---|---|---|---|
| Set campaign-level click-through URL suffix to `utm_campaign={slug}` | CM360, both advertisers | 4, one per campaign | Every ad in the campaign inherits it, including ads added later |
| Verify | Seeded click plus GA4 receipt | 1 per campaign | Confirms the parameter lands |

The alternative, editing each ad's click-through URL, would touch several hundred ads and would need repeating every time a creative is trafficked. The suffix approach applies automatically to new ads.

Paid social is a separate implementation. Meta supports dynamic URL tags at ad level, so `utm_campaign` can be populated from the campaign name macro. That needs the Meta account audited first; it has not been reviewed yet and it carries known tagging errors on `utm_medium`.

Owner and effort:

| Work | Owner | Effort |
|---|---|---|
| Approve the amendment and publish to Confluence | StoneX MKTTECHOPS | n/a |
| CM360 suffix on 4 campaigns, plus verification | Berelvant, behind the standing mutation gate | under a day |
| Meta URL tags | Berelvant, after the Meta audit | to be scoped |
| Email, SMS, push templates | StoneX, SFMC | to be scoped |

## Risk

Low. Adding `utm_campaign` to display and native adds a dimension GA4 currently has no value for. It does not change how those sessions are classified into channel, source or medium, so historical channel reporting stays comparable. Sessions before and after the change will differ only in that campaign stops reading `(not set)`.

The one thing to watch: `utm_campaign` values must stay lowercase with no spaces. The same casing inconsistency that currently splits `Azerion` from `azerion` into two GA4 rows would split campaign rows the same way.

## Related items, not part of this request

Two defects found during the audit are being fixed separately and do not depend on this amendment: a GCG campaign whose default landing page sends US traffic to the LAT page credited to Quantcast, and a set of untagged ad clicks arriving through the creative CDN with no parameters at all.

Two open questions for StoneX, also separate:

1. **Native has no approved `utm_medium` value, and the value in use puts the traffic in Unassigned.** Live native ads run `utm_medium=native`, which the standard does not contain. Verified on the LAT property, 14 days to 2026-07-28: `Quantcast / native` (315 sessions) and `Azerion / native` (30) both land in the **Unassigned** default channel group, while every display variant lands correctly in **Display**. GA4's default Display definition accepts `display`, `banner`, `expandable`, `interstitial` and `cpm`. It does not accept `native`. So 345 sessions of paid media over two weeks are not classified as paid anywhere in default reporting. Our recommendation is `utm_medium=display` for native, with the format captured in `utm_campaign` (`ggmi_latam_native_q3fy26`), which puts the whole vendor buy in one channel group and keeps native separable. The alternative, keeping `native` as an approved value, requires StoneX to build and maintain a custom channel group on both properties or the traffic stays in Unassigned.
2. `cid` appears in every example in the standard but has never been issued. We are treating it as deferred and not flagging its absence. Confirm that is correct, and tell us when the IDs are available so we can plan a second tagging pass.
