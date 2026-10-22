# Fresh v7.3 hero contrast sampling

Result: PASS within the measured scope. 49/49 visible text contexts passed; 0 unresolved sampled failures. Ten widths:320,360,375,390,430,768,1024,1280,1440,1920px. The hidden secondary CTA at1024px was excluded, yielding49visible contexts.

Method: paired browser screenshots of actual hero glyphs and the same composition with text colors made transparent. Opaque button containers were retained. Background contrast is sampled underneath actual changed glyph pixels, using WCAG relative luminance. The required ratio is3:1 for large text and4.5:1 for small text. Minimum measured H1 contrast: 3.251:1. Minimum measured small-text contrast: 9.376:1.

A genuine issue was found in the first composition: desktop name lettering crossed the bright portrait background. The CSS left transition was lengthened from29% to45%, preserving the supplied portrait pixels and face. All final captures and tests use the rebuilt corrected composition. Earlier failed evidence remains outside the final review package as recovery history.

The initial two zero-difference screenshot pairs were capture timing failures, not contrast measurements. Final paired capture waits for hydration/paint; all visible contexts contain sampled pixels. The current raw capture records, paired images and provenance are included under qa/contrast/.

Automated Axe checks and sampled pixel tests do not establish full-site WCAG conformance. Manual contrast review outside this scope remains a known owner-review item.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
