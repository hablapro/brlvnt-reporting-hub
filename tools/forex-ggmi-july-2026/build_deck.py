#!/usr/bin/env python3
"""GGMI July 2026 performance review deck.

Built from the approved narrative (output/GGMI-Jul-2026-narrative-draft.md,
Renzo-approved 2026-08-17) and figures.json. Slide order is the approved
14-slide list. All style comes from lib/housestyle.py; nothing is redefined
here. Slide 2 carries 'Pending' markers until Renzo's client-dashboard rows
land; swap them before delivery.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lib'))
from housestyle import (Deck, CORAL, GREEN, GOLD, DEEP, NAVY, MUTED, INK,
                        MARGIN, W)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                   'reports', 'forex', 'ggmi', '2026-07', 'output',
                   'GGMI_LATAM_July_2026_Performance_Review.pptx')

d = Deck(entity='GGMI (LATAM)', month='July 2026', n_slides=14)

# ---------------------------------------------------------------- 1 cover ----
d.cover(kicker='MONTHLY PERFORMANCE REVIEW',
        title='GGMI (LATAM) — Paid Media',
        subtitle='July 2026 Performance',
        channel_line='Bing Ads  ·  Quantcast  ·  Azerion  ·  Native  ·  Meta  ·  DOOH',
        footer='Reporting period: July 1–31, 2026   |   Currency: USD   |   Prepared by Berelvant')

# ------------------------------------------------- 2 blended funnel view ----
# June deck's slide 2 carried forward: same table, July column added.
# Jan-Jun columns verbatim from the June deck; July from the client file
# ("Submitted" basis, Renzo ruling 2026-08-17). MoM = July vs June.
s = d.content('SUMMARY  ·  BLENDED VIEW (ORGANIC + PAID)',
              'Submitted applications held near June on a 24% larger media month.')
d.text(s, MARGIN, 1.75, 12.3, 1.5, [
    '•  July submitted applications came in at 653, down 5% MoM; the submit '
    'rate on application starts rose to 27%, the highest since January.',
    '•  New approved came in at 180 with the approval rate at 28%. New funded '
    'came in at 21 and the fund rate at 12%; the application-to-funding step '
    'remains the funnel constraint. New traded closed at 19.',
    '•  Working media reached $149,896 in July, up 24% MoM and the biggest '
    'month of 2026. The growth sits in the new Native and DOOH lines; the '
    'four continuing channels spent $95,401 against June\u2019s total of '
    '$120,393, and paid submitted applications with a measured source '
    '(Bing plus Azerion) came in at 61.',
    '•  Mexico, the only market with paid media behind it, is the strongest '
    'converter in the client\u2019s country data: a 40% approval rate against '
    'the 28% blended average, and roughly one in four of all funded '
    'accounts.'], 10, False, INK, space=4)
d.table(s, MARGIN, 3.35, 12.33, 3.3, [
    ['GGMI — blended', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'MoM'],
    ['Working Media Spend', '$1,717', '$20,578', '$42,424', '$46,294',
     '$78,790', '$120,393', '$149,896', '+24%'],
    ['Submitted Applications', '1,029', '1,036', '900', '751', '732', '684',
     '653', '-5%'],
    ['Approved Clients', '288', '337', '261', '202', '195', '209', '180',
     '-14%'],
    ['Approval Rate', '28%', '33%', '29%', '27%', '27%', '31%', '28%', '-3pp'],
    ['New Funded Clients', '66', '59', '63', '38', '36', '32', '21', '-34%'],
    ['Fund Rate', '23%', '18%', '24%', '19%', '18%', '15%', '12%', '-3pp'],
    ['Cost per Funded Client', '$26', '$349', '$673', '$1,218', '$2,189',
     '$3,762', '$7,138', '+90%'],
    ['New Traded Clients', '56', '52', '57', '35', '36', '29', '19', '-34%'],
    ['Cost per Traded Client', '$31', '$396', '$744', '$1,323', '$2,189',
     '$4,151', '$7,889', '+90%'],
    ['Trading Volume', '$5.1B', '$2.5B', '$2.3B', '$2.1B', '$1.1B', '$1.1B',
     '—', '—'],
], col_widths=[2.61, 1.08, 1.08, 1.08, 1.08, 1.08, 1.14, 1.14, 1.04])
d.note(s, MARGIN, 6.72, 12.3, 0.3,
       'Funnel metrics are blended organic + paid, from the client dashboard. '
       'Working media per the budget tracker. MoM = July vs June. January '
       'cost figures reflect a near-zero media base ($1,717). July trading '
       'volume follows with the next dashboard refresh.')

# ------------------------------------------------------ 3 exec summary ----
s = d.content('EXECUTIVE SUMMARY',
              '$149,896 deployed in July, up 24%, the biggest GGMI media month of 2026.')
d.table(s, MARGIN, 1.9, 7.4, 3.05, [
    ['Channel', 'Spend', 'Impr', 'Clicks', 'Apps', 'Cost/app'],
    ['Bing (Search)', '$10,625', '90,394', '4,090', '20', '$531.25'],
    ['Quantcast (Display)', '$39,240', '50.48M', '19,188', '—', '—'],
    ['Azerion (Display)', '$37,509', '7.58M', '12,915', '41*', '$914.85*'],
    ['Native (QC + Azerion)', '$27,630', '18.18M', '9,953', '—', '—'],
    ['Meta (Social)', '$8,027', '4.25M', '74,489', '—', '—'],
    ['DOOH (Perion)', '$26,865', '—', '—', '—', '—'],
    ['Total', '$149,896', '80.58M', '120,635', '—', '—'],
], col_widths=[2.15, 1.15, 1.05, 1.05, 0.85, 1.15], total_last=True)
d.note(s, MARGIN, 5.0, 7.4, 0.75,
       '* Azerion applications are vendor-reported; Bing applications are '
       'SA360-reported, the account\u2019s conversion source of record. Conversions come from different systems per channel '
       'and are never summed; the combined Bing + Azerion view is the one '
       'sanctioned pairing. Meta clicks are link clicks. Spend per the '
       'client budget tracker.')
d.card(s, 8.1, 1.9, 4.7, 2.35, 'The scorecard',
       ['Bing and Azerion, the two channels with a submitted-application '
        'figure behind them, produced 61 applications combined at $789.08 '
        '(June: 92 at $660.00).',
        'The rise traces to Bing, which spent the first third of July '
        'rebuilding its campaign structure and the next third '
        'transitioning to it, not to Azerion, which held steady.'], GREEN)
d.card(s, 8.1, 4.45, 4.7, 2.35, 'The rebuilt structure',
       ['Bing’s rebuilt Mexico-only structure closed July at $237.12 per '
        'submitted application, less than half June’s $513.17.',
        'August’s first days confirm the run rate at $243, now converting '
        'across three products instead of one.'], CORAL)

# ------------------------------------------- 4 three findings for August ----
s = d.content('CONT’ EXECUTIVE SUMMARY', 'Three findings shape the August plan.')
d.blocker(s, MARGIN, 2.0, 4.05, 3.4, 'Priority',
          ['Scale the rebuilt Bing structure. It closed July at $237.12 '
           'per submitted application, less than half June’s $513.17.',
           'August’s first days track at $243, with three products '
           'converting.',
           'June’s Mexico commitment held: delivery concentrated in-market '
           'across the month.'], CORAL)
d.blocker(s, MARGIN + 4.25, 2.0, 4.05, 3.4, 'High',
          ['Hold programmatic quality on Quantcast. Viewability improved '
           '3.15 points to 54.45% and still sits under the 70% standard.',
           'The refreshed 66-site disallow list is the direct lever, led '
           'by tvazteca.com.'], GOLD)
d.blocker(s, MARGIN + 8.5, 2.0, 3.85, 3.4, 'New this month',
          ['Native ($27,630: Quantcast’s native placement plus Azerion’s '
           'native inventory) and DOOH ($26,865, Perion).',
           'Both upper-funnel. Native reports spend and delivery with no '
           'conversion claim; DOOH reports spend only this cycle.',
           'Both report in full once a second month allows comparison.'], GREEN)
d.strip(s, MARGIN, 5.75, W - 2 * MARGIN, 0.8,
        'The rebuilt structure delivered $237.12 per submitted application. August scales it.')

# ------------------------------------------------- 5 bing performance ----
s = d.content('BING ADS  ·  PERFORMANCE',
              'Three windows in one month. The rebuilt structure is the account’s current state.')
tiles = [('Spend', '$10,625', 'Jul 1–31'), ('Impressions', '90,394', 'CTR 4.52%'),
         ('Clicks', '4,090', 'avg CPC $2.60'), ('Submitted apps', '20', 'SA360 source of record'),
         ('CPA (full month)', '$531.25', 'June: $513.17'), ('CPA (rebuilt)', '$237.12', 'Jul 22–31')]
for i, (lbl, val, sub) in enumerate(tiles):
    d.tile(s, MARGIN + i * 2.08, 1.85, lbl, val, sub=sub, w=1.95)
days = list(range(1, 32))
spend = [0,0,0,0,0,0,0,0,0,0,436.55,364.63,441.88,562.23,559.9,699.13,614.23,
         670.31,406.84,518.09,448.17,577.22,639.51,322.88,230.02,218.3,582.18,
         559.63,723.75,607.16,442.33]
d.line_chart(s, MARGIN, 3.55, 7.9, 3.0, [str(x) for x in days],
             [('Daily spend ($)', spend)])
d.text(s, 0.8, 3.6, 2.4, 0.3, 'Jul 1–10 · rebuild', 9, True, MUTED)
d.text(s, 3.4, 3.6, 2.9, 0.3, 'Jul 11–22 · prior structure', 9, True, NAVY)
d.text(s, 6.5, 3.6, 2.4, 0.3, 'Jul 22–31 · new structure', 9, True, CORAL)
d.table(s, 8.6, 3.55, 4.2, 2.2, [
    ['Window', 'Spend', 'Apps', 'CPA'],
    ['Jul 1–10  rebuild', '$0', '0', '—'],
    ['Jul 11–22  prior structure', '$5,883', '0', '—'],
    ['Jul 22–31  new structure', '$4,742', '20', '$237.12'],
], col_widths=[1.7, 0.9, 0.6, 1.0])
d.note(s, 8.6, 5.8, 4.2, 1.1,
       'July was a planned rebuild: the first ten days went to constructing '
       'the new Mexico-only structure, the prior campaigns ran through the '
       'transition, and the new structure went live July 22. Two campaigns '
       'produced every July conversion: the TradingView theme (18 of 20) '
       'and one further new campaign (2).')

# -------------------------------------------------- 6 bing read & recs ----
s = d.content('BING ADS  ·  READ & RECOMMENDATIONS',
              'The rebuild superseded June’s campaign picks. August scales what works.')
d.card(s, MARGIN, 1.9, 6.1, 4.9, 'What the data shows',
       ['June’s deck named Platform Intercept the efficiency leader at $285 '
        'and recommended rebalancing toward it. Both named June campaigns '
        'produced zero July applications in the transition window and '
        'retired when the new structure launched July 22; the TradingView campaign is now the '
        'leader with 18 of 20 applications and 13.4% start-to-submission.',
        '84% of the prior structure\u2019s clicks landed on pages outside '
        'the application flow, and every one of the 207 application starts '
        'stopped at the second step. The rebuilt campaigns land on the '
        'Spanish-language site and convert. Landing destination and keyword '
        'intent changed together, so this is a strong signal rather than a '
        'proven single cause. The step data itself is unambiguous: the '
        'loss sits between a started and a submitted application.',
        'June’s Mexico commitment held: delivery concentrated in-market '
        'across the month, including on all six new campaigns.'], GREEN)
d.card(s, 6.9, 1.9, 5.9, 4.9, 'What we recommend',
       ['Scale the rebuilt structure behind the TradingView theme, holding '
        'the July close of $237.12 as volume grows. August’s first days track '
        'at $243, with three products converting.',
        'Read the account on the rebuilt structure’s results rather than '
        'the full-month average; the second half of July is the account’s '
        'current state.'], GOLD)

# --------------------------------------------- 7 quantcast performance ----
s = d.content('QUANTCAST  ·  PERFORMANCE',
              'Reach delivered at scale, all in Mexico. Viewability is the bill to manage.')
for i, (lbl, val, sub) in enumerate([
        ('Spend', '$39,240', 'main campaign'),
        ('Impressions', '50.48M', 'main campaign'),
        ('Clicks', '19,188', 'Advanced IVT'),
        ('Geo', '100.00% MX', 'spend + impressions'),
        ('Viewability', '54.45%', 'June: 51.3%  ·  floor 70%'),
        ('Results', '15', 'directional only')]):
    d.tile(s, MARGIN + i * 2.08, 1.85, lbl, val, sub=sub, w=1.95)
d.card(s, MARGIN, 3.3, 6.1, 3.4, 'What the data shows',
       ['Every impression and dollar delivered in Mexico; the geo cut '
        'confirms 100.00% in-market.',
        'Viewability improved 3.15 points to 54.45% and still sits under '
        'the 70% floor the account works against.',
        'Result volume (15) is too low to support a cost-per-result figure; '
        'the channel reads as an awareness and reach story this month.'], GREEN)
d.card(s, 6.9, 3.3, 5.9, 3.4, 'The site list is the lever',
       ['June’s 49-site blocklist is refreshed to 66 domains this month.',
        'tvazteca.com is the headline: spend on that single domain grew to '
        '$3,451.61 in July while its viewability held near 9.6%, the second '
        'consecutive month of the pattern. If one exclusion is actioned '
        'this month, that is the one.'], CORAL)

# --------------------------------------------- 8 quantcast read & recs ----
s = d.content('QUANTCAST  ·  READ & RECOMMENDATIONS',
              'Apply the refreshed list, then hold quality with a floor.')
d.card(s, MARGIN, 1.9, 6.1, 4.4, 'What the data shows',
       ['The disallow list is the direct lever on viewability: 66 domains '
        'flagged for exclusion, led by low-viewability news and utility '
        'inventory.',
        'The campaign-level viewability floor recommended in June has not '
        'yet been implemented; without it, excluded inventory is replaced '
        'by unscreened inventory as reach scales.'], GREEN)
d.card(s, 6.9, 1.9, 5.9, 4.4, 'What we recommend',
       ['Apply the refreshed 66-site disallow list, leading with '
        'tvazteca.com.',
        'Implement the campaign-level viewability floor carried forward '
        'from June. It is the structural fix that holds quality as reach '
        'scales.',
        'Keep the channel judged on reach and cost of reach until result '
        'volume supports more.'], GOLD)

# ----------------------------------------------- 9 azerion performance ----
s = d.content('AZERION  ·  PERFORMANCE',
              '41 vendor-reported applications; viewability now clear of the floor on both formats.')
for i, (lbl, val, sub) in enumerate([
        ('Spend', '$37,509', 'display'),
        ('Impressions', '7.58M', 'display'),
        ('Clicks', '12,915', 'display'),
        ('Applications', '41', 'vendor-reported'),
        ('Cost / app', '$914.85', 'vendor-reported'),
        ('Viewability', '82.47%', 'native 77.34%')]):
    d.tile(s, MARGIN + i * 2.08, 1.85, lbl, val, sub=sub, w=1.95)
d.card(s, MARGIN, 3.3, 6.1, 3.4, 'What the data shows',
       ['Applications are reported by the vendor’s own tracking rather '
        'than by SA360, the source of record behind Bing’s count; the '
        'distinction travels with the number.',
        'June’s viewability recommendation fully landed: display rose from '
        '68.5% to 82.47%, native came in at 77.34%, both clear of the 70% '
        'floor.',
        'Country-level delivery detail was requested from the vendor in '
        'early July; the follow-up runs with the August cycle. A '
        'data-completeness item.'], GREEN)
d.card(s, 6.9, 3.3, 5.9, 3.4, 'Ad-set economics rotated',
       ['June flagged Conversion_Commodities for reallocation (zero '
        'applications) and named Global Market the leader at $412. July '
        'reversed both: Commodities converted 6 at $500; Global Market '
        'fell to 2 at $1,660. The month’s leader was '
        'Conversion_Instruments, 9 at roughly $339.',
        'At this volume, ad-set winners rotate faster than a reallocation '
        'decision can act on them.'], DEEP)

# ----------------------------------------------- 10 azerion read & recs ----
s = d.content('AZERION  ·  READ & RECOMMENDATIONS',
              'Judge the channel at the monthly level. Close out the vendor confirmation.')
d.card(s, MARGIN, 1.9, 6.1, 4.4, 'What the data shows',
       ['The channel figure is the stable read: $914.85 per vendor-reported '
        'application, against $834 in June.',
        'Ad-set level winners rotated against June’s picks, which closes '
        'out June’s reallocation call; the flagged ad set converted well '
        'on its own.'], GREEN)
d.card(s, 6.9, 1.9, 5.9, 4.4, 'What we recommend',
       ['Hold the channel’s pace and judge it on the monthly figure '
        'rather than reallocating off one month’s ad-set data.',
        'Follow up with the vendor on the country-level delivery detail '
        'requested in early July, in the August cycle, and hold '
        'certification of that detail until it lands.'], GOLD)

# -------------------------------------------------- 11 meta performance ----
s = d.content('META  ·  SPEND & DELIVERY',
              'Reported on spend and delivery this month. Instagram testing delivered.')
for i, (lbl, val, sub) in enumerate([
        ('Spend', '$8,027', 'Mexico only'),
        ('Impressions', '4.25M', 'CPM ~$1.89'),
        ('Link clicks', '74,489', 'CTR 1.75% · June 2.06%'),
        ('Reach', '2,251,346', 'largest campaign'),
        ('Geo', 'Mexico', 'all campaigns'),
        ('Instagram', '10.2%', 'June: 0.3%')]):
    d.tile(s, MARGIN + i * 2.08, 1.85, lbl, val, sub=sub, w=1.95)
d.card(s, MARGIN, 3.3, 6.1, 3.4, 'What the data shows',
       ['Delivery held to Mexico across every campaign.',
        'Placement mix shifted toward Instagram: 10.2% of July delivery, '
        'up from 0.3%, answering the specific ask from the June review. '
        'Facebook carried 89.2%.'], GREEN)
d.card(s, 6.9, 3.3, 5.9, 3.4, 'Measurement note',
       ['July’s Meta reporting covers spend and delivery: impressions, '
        'reach, frequency, link clicks, CTR, CPC, CPM, landing-page views, '
        'placements and geo.',
        'The platform reports 117 submitted-application pixel fires; that '
        'figure is Meta-reported and unvalidated, is not compared to '
        'Bing’s SA360-reported count, and carries no cost-per-application '
        'figure.'], DEEP)

# ---------------------------------------------------- 12 native & dooh ----
s = d.content('NATIVE & DOOH  ·  NEW LINES',
              'First full month for both. Upper-funnel roles, reported on delivery.')
d.table(s, MARGIN, 2.0, 7.4, 1.75, [
    ['Line', 'Spend', 'Impressions', 'Clicks'],
    ['Native (Quantcast + Azerion)', '$27,630', '18.18M', '9,953'],
    ['DOOH (Perion)', '$26,865', '—', '—'],
], col_widths=[3.4, 1.3, 1.5, 1.2])
d.note(s, MARGIN, 3.9, 7.4, 0.6,
       'Native combines Quantcast’s dedicated native placement and '
       'Azerion’s native inventory. Azerion native viewability: 77.34%, '
       'clear of the 70% floor. DOOH reports spend only this cycle.')
d.card(s, 8.1, 2.0, 4.7, 3.2, 'How to read the new lines',
       ['Both are upper-funnel. Native carries a spend and delivery line '
        'with no conversion claim; DOOH carries spend only, with delivery '
        'detail out of scope this cycle.',
        'Both report in full once a second month of data gives them '
        'something to compare against.'], DEEP)

# ------------------------------------------------------------- 13 GA4 ----
s = d.content('SITE TRAFFIC  ·  GA4 (MEXICO)',
              'Context this month. The measurement fix makes August the first fully measured month.')
for i, (lbl, val, sub) in enumerate([
        ('Mexico sessions', '7,310', 'June: 9,236'),
        ('Unique visitors', '3,981', 'Mexico'),
        ('Key-event capture', 'Fixed', 'live since Jul 31'),
        ('GA4 corroboration', 'August', 'first full month')]):
    d.tile(s, MARGIN + i * 2.08, 1.85, lbl, val, sub=sub, w=1.95)
d.card(s, MARGIN, 3.3, 6.1, 3.4, 'What the data shows',
       ['A large share of July’s session dip tracks Bing’s own month: ten '
        'days of rebuild, then the transition window. Property-wide, '
        'sessions without source attribution (largely untagged paid '
        'search) fell sharply; attributed sessions grew.',
        'Venezuela’s session volume fell sharply as the prior campaigns '
        'retired, the same campaign-mix effect behind Bing’s in-market '
        'concentration this month.'], GREEN)
d.card(s, 6.9, 3.3, 5.9, 3.4, 'Measurement to close',
       ['The submitted-application key event began counting correctly on '
        'July 31 and has held at full capture since. July is reported on '
        'the SA360 count; August is the first month GA4 can corroborate it '
        'independently.',
        'Completion of the Bing-to-GA4 account link has not yet been '
        'verified; the paid-search restatement June’s deck flagged lands '
        'once it is, expected alongside August’s corroboration.'], DEEP)

# ------------------------------------------------- 14 priorities & next ----
s = d.content('CROSS-CHANNEL PRIORITIES + NEXT STEPS',
              'August priorities: scale the rebuilt structure, complete measurement, hold inventory quality.')
d.blocker(s, MARGIN, 1.95, 4.05, 2.3, 'Priority',
          ['Scale the rebuilt Bing structure on the July close of $237.12; '
           'August is tracking at $243 across three products.'], CORAL)
d.blocker(s, MARGIN + 4.25, 1.95, 4.05, 2.3, 'High',
          ['Apply the 66-site Quantcast disallow list, led by tvazteca.com, '
           'and hold delivery to the 70% viewability standard.'], GOLD)
d.blocker(s, MARGIN + 8.5, 1.95, 3.85, 2.3, 'Measurement to close',
          ['August is the first month GA4 can corroborate the '
           'submitted-application count.',
           'Close out Azerion’s country-level delivery confirmation with '
           'the vendor.'], DEEP)
d.blocker(s, MARGIN, 4.45, 4.05, 2.0, 'Opportunity',
          ['Hold Azerion’s pace; judge the channel monthly.',
           'Native and DOOH report in full with a second month of data.'], GREEN)
d.strip(s, MARGIN + 4.25, 4.45, 8.1, 2.0,
        'The rebuilt structure converted at $237.12 in July. August scales it, holds programmatic quality, and brings GA4 corroboration online.')
d.save(OUT)
print(f'OK  {d.verify()} slides  ->  {OUT}')
