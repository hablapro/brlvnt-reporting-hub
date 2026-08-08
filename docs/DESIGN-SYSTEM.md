# Design System — FOREX.com / GGMI Performance Review

Sampled from the March 2026 deck. All values are already encoded in `scripts/deck_builder.js`; this file is the human-readable spec. Do not introduce colors or fonts outside this list.

## Palette

| Token | Hex | Use |
|---|---|---|
| Deep navy | `0F1535` | Cover background, closing takeaway strip, "Measurement to close" header |
| Indigo navy | `1E2761` | Title bands, table headers, stat-card values, headline text |
| Coral | `F96167` | Band underline, stat-card left edge, read-box border, "Critical" header, cover accent bar |
| Gold | `E9B44C` | "What we recommend" card edge, "High" header |
| Green | `2E7D57` | "What the data shows" card edge, "Opportunity" header, positive MoM deltas |
| Ice blue | `CADCFC` | Cover month subtitle, summary-table Total row fill |
| Muted | `5A6072` | Stat labels, footer, footnotes |
| Border | `D0D4DC` | Card and table borders |
| Light | `F9FAFC` | Alternating table rows, blocker card body |
| Ink | `2B3147` | Body text |

One color dominates (navy), coral is the single sharp accent, gold and green are reserved for the read/recommend and priority semantics. Do not give them equal weight.

## Typography

- **Headers, titles, section labels, headlines, read-box titles:** Georgia, bold.
- **Body, bullets, tables, stat labels and values, footer:** Calibri.
- Georgia ships with Office and renders true there. In the LibreOffice QA render its width substitute is approximate, so title fit in the preview is indicative only. The title containers carry slack; do not shrink copy chasing the preview.

## Components

- **Title band:** full-width navy `1E2761` rectangle, 0.92" tall, white Georgia title left, Berelvant logo top-right; a 0.05" coral `F96167` rule directly beneath it. No accent line under the title text itself.
- **Headline:** navy Georgia bold, ~16pt, one line beneath the band.
- **Stat card:** white, thin border, a 0.06" coral left edge, gray uppercase label, navy bold value (~20pt), gray sub. Four per row.
- **Read box:** white, rounded, coral 1.25pt border, Georgia navy title, Calibri bullets. Used on performance slides and the exec summary.
- **Read / Recommend cards:** white, thin border, a 0.07" left edge — green for "What the data shows," gold for "What we recommend." Navy bold bullets.
- **Blocker cards:** light body, a full-width colored header band (coral / gold / green / navy), white Georgia label, Calibri bullets.
- **Closing strip:** full-width deep-navy `0F1535` bar with one white Georgia takeaway line.
- **Table:** navy `1E2761` header row, white bold text; body rows alternate white / `F9FAFC`; `D0D4DC` borders; first column left-aligned, numeric columns right-aligned. The summary Total row uses the ice-blue `CADCFC` fill with navy bold text, and a literal dash in any cell that must not be summed.
- **Footer:** thin `D0D4DC` rule, left label `"<entity>   |   <Month Year> Performance Review   |   Berelvant"`, right page number `n / total`. The cover has no footer.

## Logos

`assets/forex_logo.png` (FOREX.com by StoneX, white) and `assets/berelvant_logo.png` (Berelvant, white), both 700×200 (3.5:1). FOREX sits top-left on the cover; Berelvant sits top-right on every content band and bottom-right on the cover. Both are white-on-transparent, so they belong on navy, not on a white field.

## Layout

16:9, 10" × 5.625". Side margins 0.5". Footer rule at y≈5.30". Keep content above ~5.1" so it never collides with the footer. Dense channel tables and the four-card blocker grid are the two places to watch for overflow.
