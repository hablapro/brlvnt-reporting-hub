#!/usr/bin/env python3
"""GCG July 2026 performance review deck.

Built to the delivered GGMI July 13-slide template (docs/DOCTRINE.md §11):
evidence and decision on one slide per channel, granular client-facing
tables, no blended organic+paid summary, closer is a priorities narrative.
Source: output/GCG-Jul-2026-narrative-draft.md and figures.json. All style
comes from lib/housestyle.py; nothing is redefined here.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lib'))
from housestyle import (Deck, CORAL, GREEN, GOLD, DEEP, NAVY, MUTED, INK, W, MARGIN)
from pptx.enum.text import PP_ALIGN

def L(t):
    return {'t': t, 'a': PP_ALIGN.LEFT}

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                   'reports', 'forex', 'gcg', '2026-07', 'output',
                   'GCG_US_July_2026_Performance_Review.pptx')

d = Deck(entity='GCG (US Hispanic)', month='July 2026', n_slides=14)

# ---------------------------------------------------------------- 1 cover ----
d.cover(kicker='MONTHLY PERFORMANCE REVIEW',
        title='GCG (US Hispanic)  ·  Paid Media',
        subtitle='July 2026 Performance',
        channel_line='Google Search  ·  Google PMax  ·  Meta  ·  Quantcast  ·  Azerion  ·  Native',
        footer='Reporting period: July 1-31, 2026   |   Currency: USD   |   Prepared by Berelvant')

# -------------------------------------------- 2 summary, blended view -----
s = d.content('SUMMARY  ·  BLENDED VIEW (ORGANIC + PAID)',
              'Submitted applications came in at 404, up 24.3%, with '
              'working media at $136,224.')
d.text(s, MARGIN, 1.85, 3.85, 4.3, [
    'Submitted applications came in at 404, up 24.3% from June, and live '
    'applications reached 389, up 25.9%, even as website sessions fell '
    '41.6% to 39,446.',
    'Working media spend came in at $136,224, up 16.4% from June, with '
    'Google PMax added as a new line.',
    'The application-start rate doubled to 7.5% of sessions, from '
    'June’s 3.8%: the top of the funnel converted more efficiently on '
    'far fewer sessions.',
    'Approved applications rose 5.9% to 162, growing with the '
    'application volume; the approval rate came in at 40.1% as the '
    'application base grew faster. Funded accounts came in at 32, a '
    '19.8% rate against Q2’s 34.5% average, a step that happens inside '
    'FOREX.com’s application-review process after media’s handoff.',
    'Google’s ad-position work and Azerion’s audience shift are the '
    'levers behind July’s application growth; August extends both. '
    'Meta is paused entering August.'], 10, False, INK, space=8)
d.table(s, 4.6, 1.85, 8.23, 4.0, [
    ['Metric', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'MoM'],
    ['Working Media Spend', '—', '$2,237', '$49,106', '$58,324', '$76,274',
     '$117,024', '$136,224', '+16.4%'],
    ['Unique Sessions', '4,187', '5,075', '31,785', '43,192', '52,137',
     '67,545', '39,446', '-41.6%'],
    ['App Starts', '2,306', '1,871', '2,820', '2,767', '2,618', '2,592',
     '2,970', '+14.6%'],
    ['Live Apps Submitted', '431', '344', '391', '398', '289', '309',
     '389', '+25.9%'],
    ['Approved', '202', '150', '173', '187', '135', '153', '162', '+5.9%'],
    ['Approval Rate', '45.5%', '42.6%', '42.4%', '45.5%', '45.0%', '47.1%',
     '40.1%', '-7.0pts'],
    ['New Funded', '58', '48', '47', '66', '46', '52', '32', '-38.5%'],
    ['Fund Rate', '28.7%', '32.0%', '27.2%', '35.3%', '34.1%', '34.0%',
     '19.8%', '-14.2pts'],
    ['Cost per Funded', '—', '$47', '$1,045', '$884', '$1,658', '$2,250',
     '$4,257', '+89.2%'],
    ['New Traded', '47', '41', '36', '54', '37', '41', '24', '-41.5%'],
    ['Cost per Traded', '—', '$55', '$1,364', '$1,080', '$2,061',
     '$2,854', '$5,676', '+98.9%'],
], col_widths=[1.75, 0.81, 0.81, 0.81, 0.81, 0.81, 0.81, 0.81, 0.81])
d.note(s, MARGIN, 6.15, 12.3, 0.5,
       'Funnel metrics are blended organic + paid from the FOREX.com '
       'dashboard. Media spend comes from the FOREX.com budget tracker. '
       'MoM = July vs June. January-February cost rows reflect a '
       'near-zero media base; the paid-media baseline starts in March.')

# ------------------------------------------------------- 3 exec summary ----
s = d.content('EXECUTIVE SUMMARY',
              '$136,224 deployed in July across six lines, up 16.4% from June.')
d.table(s, MARGIN, 1.9, 7.4, 3.05, [
    ['Channel', 'Spend', 'Impr', 'Clicks', 'Apps', 'Cost/app'],
    ['Google Search', '$29,478', '125,392', '9,568', '73', '$403.81'],
    ['Google PMax (YouTube)', '$18,175', '792,667', '14,009', '49', '$370.91'],
    ['Meta', '$6,940', '493,027', '11,767', '—', '—'],
    ['Quantcast (Display)', '$29,857', '22.49M', '2,574', '—', '—'],
    ['Azerion (Display)', '$31,477', '4.77M', '8,892', '80', '$393.46'],
    ['Native (QC + Azerion)', '$20,298', '10.58M', '2,476', '—', '—'],
    ['Total', '$136,224', '39.25M', '49,286', '—', '—'],
], col_widths=[2.15, 1.15, 1.05, 1.05, 0.85, 1.15], total_last=True)
d.note(s, MARGIN, 5.0, 7.4, 0.75,
       'Channel results reflect each platform or partner’s reporting '
       'methodology and should be interpreted independently. Cross-channel '
       'totals and blended acquisition costs are not used because '
       'attribution systems are not directly comparable. Meta clicks are '
       'link clicks. Spend per the FOREX.com budget tracker.')
d.card(s, 8.1, 1.9, 4.7, 2.35, 'The scorecard, by channel',
       ['Google: 122 submitted applications at $390.60 each across Search '
        'and PMax.',
        'Azerion: 80 applications at $393.46 each, up from 58 at '
        '$510.10 in June.',
        'Search alone: 73 applications at $403.81, with the ad-position '
        'work already making Track A Trust the account’s most efficient '
        'audience.'], GREEN)
d.card(s, 8.1, 4.45, 4.7, 2.35, 'New this month',
       ['PMax launched the week of July 13 and matched Search’s '
        'efficiency in its first partial month: $370.91 per application.',
        'Meta added a campaign built specifically to drive applications, '
        'which carried 44% of a smaller, reallocated Meta budget this '
        'month. The account is flagged and paused entering August.',
        'Quantcast Native launched alongside Azerion Native; first full '
        'month for both.'], CORAL)

# --------------------------------------------- 4 google search performance --
s = d.content('GOOGLE SEARCH  ·  PERFORMANCE',
              '73 submitted applications at $403.81; the ad-position work is paying off.')
d.text(s, MARGIN, 1.55, 12.3, 0.3,
       'Target: non-brand Spanish-language search across Trust, Authority '
       'and Platform, plus a brand track, US only.', 9.5, False, MUTED)
tiles = [('Spend', '$29,478', '+30.9% MoM'), ('Impressions', '125,392', 'CTR 7.63%'),
         ('Clicks', '9,568', 'avg CPC $3.08'), ('Submitted apps', '73', '+9.0% MoM'),
         ('CPA', '$403.81', '+20.1% MoM')]
for i, (lbl, val, sub) in enumerate(tiles):
    d.tile(s, MARGIN + i * 2.45, 2.0, lbl, val, sub=sub, w=2.3)
d.table(s, MARGIN, 3.7, 7.4, 3.2, [
    ['Keyword', 'Track', 'Spend', 'Apps', 'CPA'],
    ['broker forex usa (broad)', 'Authority', '$4,233.86', '15', '$282.26'],
    ['broker estados unidos', 'Authority', '$2,850.14', '3', '$950.05'],
    ['plataforma de trading', 'Platform', '$2,445.17', '7', '$349.31'],
    ['invertir en forex', 'Trust', '$2,331.88', '2', '$1,165.94'],
    ['forex com español', 'Brand', '$2,061.70', '5', '$412.34'],
    ['plataforma trading profesional', 'Platform', '$1,367.44', '4', '$341.86'],
    ['forex confiable', 'Trust', '$1,288.42', '9', '$143.16'],
    ['como hacer trading (2nd ad group)', 'Trust', '$668.66', '6', '$111.44'],
], col_widths=[3.3, 1.1, 1.2, 0.7, 1.1])
d.note(s, MARGIN, 6.98, 7.4, 0.25, 'Top 8 of 20 keywords tracked, by spend.')
d.card(s, 8.1, 3.7, 4.7, 1.7, 'Track A Trust: what the ad-position work changed',
       ['Our ads now show for 32.6% of relevant searches, up from 27%.',
        'How often our ads lose the auction to competitors fell to 58.7% '
        '(the account’s best), down from the 64-76% range every group sat '
        'in during June.',
        'Cost per application (CPA): $433 to $390.86, and Trust is now '
        'the top-performing group with 28 applications.'], GREEN)
d.card(s, 8.1, 5.55, 4.7, 1.55, 'Where the work has not landed yet',
       ['Authority and Platform still lose the auction to competitors '
        '63.5% and 70.3% of the time, and Brand 79.0%, all worse than '
        'Trust’s 58.7%.',
        'DECISION: extend the same ad-position work to Authority and '
        'Platform before adding further budget.'], CORAL)

# ------------------------------------------------ 5 google pmax performance -
s = d.content('GOOGLE PMAX (YOUTUBE)  ·  PERFORMANCE',
              '49 submitted applications at $370.91 in its first partial month.')
d.text(s, MARGIN, 1.55, 12.3, 0.3,
       'Target: Spanish-language creative, US-only delivery, across '
       'Google’s automated Performance Max inventory (labeled “YT” on '
       'the FOREX.com budget tracker). New line, launched the week of '
       'July 13.', 9.5, False, MUTED)
tiles = [('Spend', '$18,175', '~18 days of delivery'), ('Impressions', '792,667', 'CTR 1.77%'),
         ('Clicks', '14,009', 'avg CPC $1.30'), ('Submitted apps', '49', 'final application step'),
         ('CPA', '$370.91', 'vs Search $403.81'), ('App source', '48 click / 1 view', '')]
for i, (lbl, val, sub) in enumerate(tiles):
    d.tile(s, MARGIN + i * 2.08, 2.0, lbl, val, sub=sub, w=1.95)
d.table(s, MARGIN, 3.7, 5.9, 1.75, [
    ['Week of delivery', 'Spend'],
    ['Jul 13-19', '$7,449'],
    ['Jul 20-26', '$5,597'],
    ['Jul 27-31 (partial)', '$5,129'],
], col_widths=[3.4, 2.5])
d.note(s, MARGIN, 5.55, 5.9, 0.3,
       'Campaign launched July 13; July reflects ~18 days of delivery.')
d.card(s, 7.2, 3.7, 5.6, 3.0, 'What the data shows',
       ['PMax matched Search’s per-application efficiency within its '
        'first three weeks. It’s tracked the same way, the final submit '
        'step of the application form: 48 of 49 applications followed an '
        'ad click, and 1 came from someone who saw the ad and applied '
        'later.',
        'No June comparison; this is the line’s first month.',
        'DECISION: give PMax a second full month before rebalancing spend '
        'between it and Search.'], GOLD)
d.note(s, MARGIN, 6.75, 12.3, 0.3,
       'Google combined (Search + PMax): 918,059 impressions, 100% US '
       'delivery.')

# --------------------------------------------------- 6 meta by objective ----
s = d.content('META  ·  CAMPAIGNS BY OBJECTIVE',
              'Meta spend came in at $6,940, down 77.4%, on the planned budget shift.')
d.text(s, MARGIN, 1.55, 12.3, 0.3,
       'Target: Spanish-speaking US audiences, Spanish-language ads on '
       'both campaign types.', 9.5, False, MUTED)
d.table(s, MARGIN, 2.05, 12.33, 1.85, [
    ['Campaign', 'Objective', 'Spend', 'Impr', 'Reach', 'CPM', 'CTR', 'Link clicks'],
    ['0426 Q2 · Traffic (paused after Jul)', 'Traffic', '$2,104', '206,014', '173,989', '$10.21', '2.72%', '4,988'],
    ['0726 Q3 · Traffic', 'Traffic', '$1,784', '169,241', '130,525', '$10.54', '3.47%', '5,521'],
    ['0726 Q3 · Conversion', 'Conversion', '$3,052', '117,772', '73,539', '$25.91', '1.69%', '1,258'],
], col_widths=[3.0, 1.03, 1.1, 1.4, 1.3, 1.1, 0.9, 1.5])
d.note(s, MARGIN, 3.9, 12.3, 0.75,
       'Reach (unique people reached) is counted per campaign and never '
       'added together across campaigns. The traffic campaigns and the '
       'application campaign are measured differently and never compared '
       'to each other. Traffic campaigns spent $3,888. The application '
       'campaign recorded 284 actions from Meta’s own site tracking, not '
       'submitted applications, directional only. Google Analytics '
       'recorded 7,902 site visits from all three Meta campaigns '
       'combined, two-thirds (67.2%) of Meta’s reported clicks; this '
       'month’s data can’t isolate visits to just the application '
       'campaign.')
d.card(s, MARGIN, 4.75, 6.0, 1.5, 'Traffic campaigns vs June',
       ['Cost per thousand impressions (CPM) across both traffic '
        'campaigns was $10.36, down from $11.35 in June.',
        'Click-through rate (CTR), the share of people who saw the ad '
        'and clicked it, held at 2.72% and 3.47%, against 2.76% in '
        'June.'], GREEN)
d.card(s, 6.7, 4.75, 5.63, 1.5, 'Reach, counted separately',
       ['The two traffic campaigns reached 173,989 and 130,525 people '
        'this month, each person seeing the ad 1.2 to 1.3 times on '
        'average. June’s single campaign reached 1,527,444 people at '
        '2.0 times each, the drop matching the 77.4% pullback in '
        'spend.'], DEEP)
d.blocker(s, MARGIN, 6.25, 12.33, 0.8, 'August operating status',
          ['The Meta account is flagged and delivery is paused entering '
           'August. July figures above reflect delivered activity for '
           'the month.'], DEEP)

# ------------------------------------------------- 7 meta creative perf -----
s = d.content('META  ·  CREATIVE PERFORMANCE',
              'The strongest ad creative for each campaign type, ranked for '
              'whenever delivery resumes.')
d.table(s, MARGIN, 1.9, 6.0, 2.2, [
    ['Conversion creative', 'Spend', 'Events', 'Cost/event', 'Ranking'],
    ['broker_trust_q2_trackA', '$1,656', '177', '$9.36', 'LEADER'],
    ['forex_plat_q2_trackB', '$236', '32', '$7.38', 'LEADER'],
    ['exp_plat_q2_trackB', '$743', '58', '$12.81', 'STEADY'],
    ['edu_trust_q2_trackA', '$382', '11', '$34.75', 'WEAKEST'],
    ['trading_proof_q2_trackA', '$33', '6', '—', 'STEADY'],
], col_widths=[2.1, 0.9, 0.85, 0.95, 1.2])
d.table(s, 6.7, 1.9, 5.63, 1.55, [
    ['Traffic creative (live campaign)', 'Spend', 'Clicks', 'CTR', 'Ranking'],
    ['forex_plat_q2_trackB', '$1,033', '3,171', '5.32%', 'LEADER'],
    ['broker_trust_q2_trackA', '$571', '1,597', '2.77%', 'STEADY'],
    ['exp_plat_q2_trackB', '$153', '649', '1.51%', 'STEADY'],
], col_widths=[2.2, 0.85, 0.8, 0.68, 1.1])
d.note(s, MARGIN, 4.15, 6.0, 0.5,
       'Events are actions recorded by Meta’s own site tracking, not '
       'submitted applications.')
d.note(s, 6.7, 3.55, 5.63, 0.5,
       'The paused Q2 traffic campaign’s creative rows are historical '
       'only and carry no forward call.')
d.card(s, MARGIN, 4.7, 12.33, 1.9, 'The order to revisit',
       ['Meta is paused entering August; the ranking above applies once '
        'delivery resumes. '
        'The forex_plat_q2_trackB ad performed best on both campaign '
        'types. The broker_trust_q2_trackA ad carried most of the '
        'application-campaign volume. The edu_trust_q2_trackA ad cost '
        '3.7 times more per action than the stronger ads, on meaningful '
        'spend.'], GOLD)

# ------------------------------------------ 8 quantcast display + native ----
s = d.content('QUANTCAST  ·  DISPLAY AND NATIVE',
              'Display spend held near flat at $29,857; Native ran its first full month.')
d.text(s, MARGIN, 1.55, 12.3, 0.3,
       'Target: Spanish-language US audiences reached through finance '
       'and trading websites in Quantcast’s network.', 9.5, False, MUTED)
tiles = [('Display spend', '$29,857', 'Jul 1-31'), ('Display impr', '22.49M', ''),
         ('Display clicks', '2,574', ''), ('Native impr', '9.41M', ''),
         ('Native clicks', '1,660', '')]
for i, (lbl, val, sub) in enumerate(tiles):
    d.tile(s, MARGIN + i * 2.45, 2.0, lbl, val, sub=sub, w=2.3)
d.card(s, MARGIN, 3.7, 6.0, 3.0, 'What the data shows',
       ['Display spend held close to flat, down 2.3% from June to '
        '$29,857; every dollar on both campaigns delivered in the '
        'United States.',
        'Native, within the shared $20,298 Native line, ran 9,411,481 '
        'impressions and 1,660 clicks in its first full month.',
        'Viewability was 49.26% on display (46.9% June) and 57.98% on '
        'native.'], GREEN)
d.card(s, 6.7, 3.7, 5.63, 3.0, 'The site list',
       ['A refreshed 35-domain site list accompanies this cycle for '
        'Quantcast, built on July delivery.',
        'Applying it concentrates spend on better-performing inventory.',
        'DECISION: send the refreshed list to Quantcast ahead of '
        'August.'], CORAL)

# -------------------------------------------- 9 azerion display performance -
s = d.content('AZERION DISPLAY  ·  PERFORMANCE',
              '80 submitted applications at $393.46, the line’s best application month.')
d.text(s, MARGIN, 1.55, 12.3, 0.3,
       'Target: six Spanish-language audience segments reached through '
       'finance and trading websites in Azerion’s network, US-only '
       'delivery.', 9.5, False, MUTED)
tiles = [('Spend', '$31,477', 'Jul 1-31'), ('Impressions', '4.77M', ''),
         ('Clicks', '8,892', ''), ('Applications', '80', 'June: 58'),
         ('Cost / app', '$393.46', 'June: $510.10'), ('CPM', '$6.60', 'June: $6.55')]
for i, (lbl, val, sub) in enumerate(tiles):
    d.tile(s, MARGIN + i * 2.08, 2.0, lbl, val, sub=sub, w=1.95)
d.table(s, MARGIN, 3.7, 5.9, 2.3, [
    ['Week', 'Spend', 'Apps', 'CPA'],
    ['Jul 1-7', '$8,829', '23', '$383.88'],
    ['Jul 8-14', '$7,956', '15', '$530.40'],
    ['Jul 15-21', '$8,033', '22', '$365.15'],
    ['Jul 22-28', '$2,895', '20', '$144.76'],
    ['Jul 29-31', '$902', '0', '—'],
], col_widths=[1.6, 1.5, 1.2, 1.6])
d.note(s, MARGIN, 6.05, 5.9, 0.3,
       'Weekly figures are Azerion’s delivery figures; the month total '
       'appears in the tiles above.')
d.card(s, 7.2, 3.7, 5.6, 3.0, 'What the data shows',
       ['Spend rose 6.4% to fund the added volume: applications rose '
        '37.9% (58 to 80) while cost per application fell 22.8% ($510.10 '
        'to $393.46).',
        'The week of July 22-28 was the efficiency peak: 20 applications '
        'at $144.76 on reduced spend, evidence that tighter delivery '
        'converts better. Viewability rose 6.15 points to 64.95%.',
        'Cost per thousand impressions (CPM), what display advertising '
        'is priced on, came in at $6.60, up from $6.55 in June.',
        'DECISION: rebalance spend toward the strongest audiences, '
        'detailed on the next slide.'], GREEN)

# --------------------------------------------- 10 azerion audience ranking ---
s = d.content('AZERION DISPLAY  ·  AUDIENCE RANKING',
              'Professional Tools and Trust lead on cost per application.')
d.table(s, MARGIN, 2.0, 7.7, 3.0, [
    ['Audience', 'Applications', 'Cost / app', 'August status'],
    ['Professional Tools', '18', '$197.43', 'PRIORITIZE'],
    ['Trust', '13', '$267.58', 'PRIORITIZE'],
    ['Trusted Broker', '11', '$312.01', 'MAINTAIN'],
    ['Broker 1', '13', '$316.36', 'MAINTAIN'],
    ['Language Broker', '16', '$420.48', 'MAINTAIN'],
    ['Spanish Platform', '9', '$812.31', 'REDUCE-REMOVE'],
], col_widths=[2.7, 1.7, 1.55, 1.75])
d.card(s, 8.4, 2.0, 3.93, 3.0, 'What we recommend',
       ['Spanish Platform carries the line’s largest spend and its '
        'weakest cost per application. It’s the candidate to shift '
        'budget away from.',
        'Professional Tools and Trust both improved sharply from '
        'June, when Trust was the line’s weakest performer.'], GOLD)

# ------------------------------------------- 11 azerion native creatives ----
s = d.content('AZERION NATIVE  ·  CREATIVE PERFORMANCE',
              'First full month for six ad creatives on Azerion’s share of '
              'the Native line.')
d.table(s, MARGIN, 2.0, 7.7, 3.0, [
    ['Creative', 'Spend', 'Clicks', 'CTR', 'August status'],
    ['City_view_MHTN', '$1,517', '143', '0.075%', 'SCALE'],
    ['Mobile_desktop_view', '$1,576', '143', '0.073%', 'SCALE'],
    ['Phone_closeup', '$1,570', '139', '0.071%', 'RETAIN-TEST'],
    ['Third_person_perspective_mobile', '$1,503', '134', '0.071%', 'RETAIN-TEST'],
    ['Trader_laptop_thinking', '$1,598', '132', '0.066%', 'RETAIN-TEST'],
    ['Multiple_screens_graph', '$1,598', '125', '0.063%', 'RETAIN-TEST'],
], col_widths=[2.9, 1.1, 0.9, 1.0, 1.8])
d.note(s, MARGIN, 5.05, 7.7, 0.3,
       'Native total: 1,170,255 impressions, 816 clicks, 72.68% '
       'viewability.')
d.card(s, 8.4, 2.0, 3.93, 3.0, 'What we recommend',
       ['Azerion’s Native reporting covers delivery metrics only, so '
        'this line is read on delivery quality. Click-through rate fell '
        'as delivery scaled, from 0.33% in week '
        'two to 0.05% in the final week.',
        'DECISION: scale the two strongest creatives by click-through '
        'rate, City_view_MHTN and Mobile_desktop_view; hold the rest '
        'for a second month before any removal, this is the line’s '
        'first full month.'], GOLD)

# --------------------------------------------------- 12 ga4 site traffic ----
s = d.content('SITE TRAFFIC  ·  GA4 (SPANISH AUDIENCE)',
              'Sessions fell 17.2% to 66,398 as Meta spend pulled back by design.')
for i, (lbl, val, sub) in enumerate([
        ('ES sessions', '66,398', 'June: 80,231'),
        ('ES users', '29,901', 'June: 41,795'),
        ('Meta capture', '67.2%', 'June: ~57%'),
        ('Jan-May base', '~70K', 'sessions, range')]):
    d.tile(s, MARGIN + i * 1.87, 2.0, lbl, val, sub=sub, w=1.75)
d.card(s, MARGIN, 3.4, 6.0, 3.2, 'What the data shows',
       ['Site visits gave back June’s paid-driven lift as Meta spend '
        'fell 77%, landing just under the roughly 70,000 base the '
        'channel held from January through May.',
        'This isn’t a decline in unpaid (organic) traffic; the softness '
        'tracks the paid pullback.',
        'GA4 recorded two-thirds (67.2%) of Meta’s reported clicks as '
        'site visits, up from about 57% in June.'], GREEN)
d.card(s, 6.7, 3.4, 5.63, 3.2, 'What to expect',
       ['TAKEAWAY: Meta is paused entering August; expect site visits to '
        'run lower without Meta’s contribution until delivery resumes.'],
       GOLD)

# -------------------------------------------------- 13 client funnel view ---
s = d.content('APPLICATION FUNNEL  ·  JULY VIEW',
              'Submitted applications rose 24.3% to 404 while website '
              'sessions fell 41.6%.')
d.text(s, MARGIN, 1.72, 12.3, 0.4,
       'Source: the FOREX.com application funnel export, Website = '
       'Forex.com US Spanish, Jan-Jul 2026. This is FOREX.com’s own '
       'website view; its session count differs in scope from the GA4 '
       'Spanish-audience cut on the prior slide.', 9.5, False, MUTED)
d.table(s, MARGIN, 2.15, 8.0, 3.35, [
    ['Metric', 'Q1 (Jan-Mar)', 'Q2 (Apr-Jun)', 'July'],
    ['Unique Sessions', '41,047', '162,874', '39,446'],
    ['App Starts', '6,997', '7,977', '2,970'],
    ['App Start Rate', '17.0%', '4.9%', '7.5%'],
    ['Submitted', '1,204', '1,036', '404'],
    ['Live', '1,166', '996', '389'],
    ['Approved', '525', '475', '162'],
    ['Approved Rate', '43.6%', '45.8%', '40.1%'],
    ['Funded', '153', '164', '32'],
    ['Funded Rate', '29.1%', '34.5%', '19.8%'],
    ['Traded', '124', '132', '24'],
], col_widths=[2.3, 2.0, 2.0, 1.7])
d.card(s, 8.7, 2.15, 3.63, 3.35, 'Top of funnel',
       ['June to July: submitted applications 325 to 404, sessions 67,545 '
        'to 39,446.',
        'The application-start rate doubled to 7.5% of sessions, from '
        'June’s 3.8%, on far fewer sessions.',
        'Live applications reached 389, up 25.9% from June’s 309, in step '
        'with submissions.'], GREEN)
d.card(s, MARGIN, 5.7, 12.33, 1.2, 'After submission: review and activation',
       ['Approvals rose 5.9% to 162, growing with the application '
        'volume; the approval rate came in at 40.1% as the application '
        'base grew faster. Funding is the step to watch: 32 accounts at '
        'a 19.8% rate against Q2’s 34.5% average, and 24 traded against '
        'June’s 41. Approval, funding and activation are FOREX.com’s '
        'application review and account-activation process.',
        'TAKEAWAY: the top of the funnel is converting more efficiently on '
        'fewer sessions; the funding rate is the step to monitor next cycle.'], DEEP)

# --------------------------------------- 14 cross-channel priorities close --
s = d.content('CROSS-CHANNEL PRIORITIES',
              'Google’s two lines closed July at 122 submitted applications and '
              '$390.60 per application; Azerion added 80 more at $393.46.')
d.blocker(s, MARGIN, 2.0, 2.95, 3.2, 'Priority',
          ['Extend the same ad-position work to Track B Authority and '
           'Platform.',
           'Track A Trust proves it works: our ads show up more often '
           'in relevant searches, they lose the auction to competitors '
           'less, cost per application is down, and it’s now the '
           'top-performing group.',
           'The other two groups still lose the auction to competitors '
           '63 to 70% of the time.'], CORAL)
d.blocker(s, MARGIN + 3.15, 2.0, 2.95, 3.2, 'High',
          ['Send the refreshed 35-domain Quantcast list ahead of August '
           'spend.',
           'It concentrates spend on stronger-performing inventory.'], GOLD)
d.blocker(s, MARGIN + 6.3, 2.0, 2.95, 3.2, 'Opportunity',
          ['Give PMax a second full month before moving further budget; '
           'it matched Search’s efficiency in its first month.',
           'Rebalance Azerion spend toward Professional Tools and Trust, '
           'the strongest audiences on cost per application.'], GREEN)
d.blocker(s, MARGIN + 9.45, 2.0, 2.88, 3.2, 'Downstream to watch',
          ['Approved applications grew with the application volume '
           '(162, +5.9%).',
           'Funding (19.8% vs Q2’s 34.5%) is the item to watch, inside '
           'FOREX.com’s application-review process; detail on the '
           'funnel slide.'], DEEP)
d.strip(s, MARGIN, 5.5, W - 2 * MARGIN, 0.9,
        'Google’s two lines and Azerion produced the month’s application '
        'volume through what’s already working; August scales it '
        'further.')

d.save(OUT)
print(f'OK  {d.verify()} slides -> {OUT}')
