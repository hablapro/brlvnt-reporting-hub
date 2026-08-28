---
name: brlvnt-executive-doc-format
description: Format client-facing Google Docs and Word documents in brlvnt's compact executive-report style, including the title system, typography, tables, footer, spacing, and rendered-page QA. Use for budget proposals, recommendation memos, performance reports, and similar dense business documents. Do not use for slide decks, websites, or casual internal notes.
---

# brlvnt Executive Document Format

This is an internal brlvnt skill. It governs presentation, not facts, analysis, or recommendations. Preserve the user's content and the authority of supplied sources.

## Scope

Use this system when a document should match the approved brlvnt executive-report look: restrained navy hierarchy, compact Calibri typography, banded data tables, and clear page furniture.

- If the user supplies a Google Doc as the template, keep the work native and follow the Google Docs template-preservation route.
- If no native template constrains the output, create a polished DOCX and import it as a native Google Doc when Google Docs is the requested destination.
- Never copy client facts, dates, amounts, names, links, or decisions from a formatting reference. Reuse only the visual and structural system.

## Format Specification

### Page

- Page size: US Letter, 612 x 792 pt.
- Margins: 64.8 pt top, 57.6 pt bottom, 72 pt left and right.
- Header and footer distance: 35.4 pt.
- Usable content width: 468 pt.
- Background: white. Use no decorative imagery unless the user asks for it.

### Color and type

| Role | Value |
| --- | --- |
| Primary navy | `#1F3864` |
| Slate | `#44546A` |
| Body ink | `#1A1A1A` |
| Table header fill | `#EAEEF5` |
| Alternating row fill | `#F6F8FB` |
| Table/footer rule | `#BFC7D6` |
| Typeface | Calibri throughout |

Do not introduce extra colors. Use bold weight and spacing before adding more visual treatments.

### Opening block

1. Eyebrow or market label: 10 pt, bold, slate, 3 pt after.
2. Document title: 19 pt, bold, primary navy, 10 pt after.
3. Add a 1.5 pt primary-navy bottom border to the title paragraph with 10 pt border padding.
4. Follow with a borderless two-column metadata table, 110 pt and 358 pt columns.
5. Metadata labels: 10 pt, bold, slate. Values: 10 pt, body ink. Use 2 pt vertical cell padding.

### Headings and body

- Heading 1: 13 pt, bold, primary navy; 19 pt before and 8 pt after; 1 pt primary-navy bottom border with 6 pt padding; keep with the following paragraph or table.
- Heading 2: 11 pt, bold, slate; 13 pt before and 5.5 pt after; keep with the following paragraph.
- Body: 10.5 pt, body ink, 110% line spacing, 7 pt after.
- Lists: 10.5 pt, 110% line spacing, 4.5 pt after; 23 pt start indent and 8 pt hanging/first-line offset. Keep numbering consecutive only within one list block.
- Source note: 8.5 pt, italic, slate, single-spaced, kept together. Separate it from the conclusion with a primary-navy rule.

Use numbered Heading 1 sections for the main argument. Use Heading 2 for channels, conditions, or subordinate decisions. Bold short inline labels such as `Success threshold:` and the value that controls the decision.

### Tables

Use tables for comparisons, budgets, ownership, and conditions. Use prose when a table would force long paragraphs into narrow cells.

- Fit every table within the 468 pt content width. Set fixed column widths based on the semantic load of each column.
- Use 10 pt Calibri in all cells.
- Header row: `#EAEEF5` fill, bold primary-navy text.
- Body rows: alternate white and `#F6F8FB`.
- Rules: 0.5 pt `#BFC7D6` horizontal borders. Avoid visible vertical borders.
- Cell padding: 3.5 pt top and bottom, 5.5 pt left and right.
- Align labels and prose left. Align currencies, percentages, and other comparable numbers right.
- Bold recommended values, minimum values, decision-driving figures, and total rows. Use the header fill for the total row.
- Bold channel or category names in the first column of role, evidence, and conditions tables.
- Repeat the header row when a table continues to another page.
- Prevent every table row from splitting across pages. Keep tables of 12 rows or fewer together when they fit on one page. Longer tables may continue across pages, but each row must remain intact.

### Footer

- Add a 0.5 pt `#BFC7D6` top rule with 6 pt padding.
- Use 8 pt Calibri in slate.
- Left side: `[Entity]  |  [Document title]`.
- Right side: `Page X of Y`, aligned to a 468 pt right tab stop.
- Insert a real tab before `Page`. Verify the rendered footer does not concatenate the title and page label.

## Page Rhythm

- Keep Heading 1 and Heading 2 paragraphs with the content that follows.
- Do not leave a section heading as the last line of a page.
- Do not split table rows. A repeated header may begin a new page only above a complete row.
- Prefer natural pagination. Add a manual page break only when a major section or short table would otherwise break awkwardly.
- Keep the conclusion and source note visually distinct from the body.

## Pre-Flight

Before delivery, re-read this specification and check the actual output:

1. Confirm Letter size, margins, Calibri, and the three-level title/heading hierarchy.
2. Confirm the title and Heading 1 rules span the content width.
3. Confirm table fills, horizontal borders, cell padding, numeric alignment, bold decision values, and fixed widths.
4. Confirm no table row splits, no heading is orphaned, and short tables stay together when they fit.
5. Confirm the footer has a top rule, a real tab before `Page`, and correct `Page X of Y` fields.
6. Confirm no facts or distinctive copy leaked from a formatting reference.
7. For Google Docs, verify native structure through connector readback, export to PDF, rasterize every page, and inspect every rendered page. Do not claim visual QA from metadata or a thumbnail.

Reject the deliverable if any page has clipping, overlapping text, broken table geometry, a split row, an orphaned heading, a malformed footer, or inconsistent typography.
