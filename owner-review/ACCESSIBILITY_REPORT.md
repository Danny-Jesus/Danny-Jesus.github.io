# Accessibility report — rebuilt v7.1

Disposition: PASS for the automated and selected practical checks listed below. This is not a WCAG certification or a substitute for a screen-reader user review.

## Fresh evidence

Final production browser run: 2026-10-21T11:17:15.923Z; Chromium 154.0.8037.57. The final browser rerun completed successfully (final-browser-suite.log).

- 50 axe scans: 25 public routes at 390px and 1440px.
- Tags requested: wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa.
- Reported violations: 0 across all scans.
- Unhandled page errors: 0.
- Every tested page has one H1, decoded main images, canonical metadata, and no horizontal overflow at the two route widths.
- The automated rules checked applicable semantics, landmarks, accessible names/labels, contrast, and touch-target rules. Decorative empty alt text remains intentional; the approved portrait has descriptive alt text.

## Practical keyboard and responsive checks

- Mobile menu opens with Enter; Tab moves to Projects and Research; Enter selects Research and closes the menu.
- Escape closes the menu and restores focus to its toggle.
- Installation lightbox opens, supports arrow navigation, retains keyboard focus inside the dialog, closes with Escape, and restores trigger focus.
- Rehabilitation comparison range control responds to ArrowRight (50 to 51).
- Hero Explore Projects link performs native anchor navigation to Aji; all four desktop navigation links work.
- Focus-visible CSS specifies a 3px outline with 6px offset. Focus restoration was asserted by the browser tests; a full visual focus review on every interactive element was not performed.
- 640px reflow (a 200% zoom equivalent check) passed. Homepage widths 320, 360, 375, 390, 430, 768, 1024 and 1440 passed the existing reflow assertions; the separate hero report covers all ten owner-requested widths.
- At 320×700 and 390×740, the approved portrait face/hair and CTA remain in the viewport with no face/text overlap.
- At 900×390, the face/hair remains in the viewport without face/text overlap. The CTA lies below the initial viewport because the hero retains a 680px minimum height. A fresh keyboard check passed: Tab focused Explore Projects, the browser scrolled from y=0 to y=349 so the CTA occupied y=211–261 in the 390px viewport, and a visible solid 3px focus outline was present. Enter activated the link and positioned Aji at y=82. No page errors occurred.
- Prerendered homepage and Gosh Meda content remain usable without JavaScript.
- Changing reduced-motion preference disposes live WebGL and retains HTML/CSS content; forced WebGL unavailability and save-data fallback passed.
- No contact form is rendered; Contact uses external profile links. The existing comparison slider is labelled.

## Preserved initial failure and supported retry

The original supplemental command failed at its fixed 1.2-second startup delay: identity data-render was null, expected webgl. No page error accompanied that observation. A diagnostic subsequently observed one live WebGL canvas; the external supplemental-condition-review.mjs retains the original assertions and uses readiness predicates instead of fixed waits. The sequential equivalent passed. The original failed log and JSON remain preserved; they are not presented as a pass. The historical v4.3 baseline capture was explicitly skipped by that suite because its checkout is absent; fresh untouched-v7 baseline evidence was captured separately.

## Limits

Automated zero-violation results apply to the tested Chromium states and viewport sizes. They do not establish universal WCAG compliance, screen-reader behavior on every platform, or complete manual contrast/focus/touch assessment. Institutional participant permissions and factual provenance remain owner-review decisions. Review-package recordings are not embedded public-site videos; no video elements were present on the active homepage.

Evidence: review/browser-review.json; fresh/extended-functional.json; fresh/landscape-cta.json; supplemental-condition-review.json; final-browser-suite.log; supplemental-suite.log; supplemental-condition-suite.log; review/supplemental-review.json (initial failure).

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
