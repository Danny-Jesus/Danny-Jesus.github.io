# Fresh v7.2 accessibility results

Executed: 2026-10-22T05:43:08.903Z to 2026-10-22T05:44:21.776Z

50/50 Axe scans completed across all 25 routes at 390 and 1440 px. Actual violations: 0. Rule tags: WCAG 2 A/AA, 2.1 A/AA and 2.2 AA.

No automated violations were recorded in completed scans.

Axe incomplete checks (manual review) remain recorded per route in browser-review-v72.json. Automated checks do not establish full WCAG conformance. Keyboard skip link/menu, filtering, lightbox trapping/Escape, and before/after slider were exercised; actual results appear in the JSON and route report.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL

<!-- V72_PAIRED_RENDER_CONTRAST -->
## Supplemental rendered photographic-text contrast

**Paired-render photographic-text check: PASS; 240/240 text contexts, 40/40 chapter/viewport pairs, 0 held contexts; lowest measured ratio 4.163:1. This sampled the settled 50% chapter scroll position only, not every transition or the whole site.**

Method recorded by analyzer: Rendered photographic chapters at settled 50%native scroll at1440x1000 and390x900. Background sampled beneath actual glyph/shadow pixels via paired color-transparent capture; opaque containers retained. Conservative pixel sampling supplements Axe incomplete image-background contrast checks; this is not whole-site WCAG certification.

At 1440×1000 and 390×900, each of the 20 photographic chapters was held at its settled 50% native-scroll position. A screenshot with text and a paired screenshot with text color/text shadow transparent retained the image and opaque-container backgrounds. The analyzer sampled backgrounds under changed glyph/shadow pixels and calculated WCAG relative-luminance ratios against computed text colors. Thresholds: 3:1 for the headings at least 24px and 4.5:1 for smaller text. The six sampled contexts per chapter were the heading, summary, kicker, CTA, provenance caption and chapter strip. The paired-render sampling is conservative and is not a replacement for a complete manual accessibility audit.

Fresh capture index fingerprint matches this production output: **YES**. Analysis result: **PASS**. Sampled minimum contrast ratio: **4.163:1**. Actual held contexts: **0**.

No held contexts recorded in the completed fresh sample.

The first rendered contrast review exposed real failures and sampling gaps. Its evidence remains under `candidate-2-contrast/`; fixes to the text strip/kicker and photographic shade were followed by a fresh capture. Historical failures are not represented as a fresh PASS.

Axe color-contrast incompletes remain recorded separately: 40 route/viewport scans, 606 repeated node instances. The 240-context supplement covers homepage photographic text at one settled scroll position. It does not close every Axe incomplete item on every dedicated page or guarantee contrast throughout all animation states. All 240 sampled photographic text contexts across 40 chapter/viewport pairs, at settled 50% scroll, meet the 3:1 large-text or 4.5:1 small-text thresholds. This does not cover every route and transition state. Axe incomplete items remain recorded; zero automated violations are not a WCAG certification.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
