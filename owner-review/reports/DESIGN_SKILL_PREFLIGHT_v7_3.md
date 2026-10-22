# v7.3 design workflow preflight

Scope: current homepage and shared visual system, checked through source inspection, actual desktop/mobile/tablet render inspection and current production HTML. “Verified” below means the stated design property was inspected; it does not imply a complete accessibility or performance certification. Fresh browser, accessibility and performance reports remain separate controlling evidence.

| Skill check | Result | Evidence / applicability |
| --- | --- | --- |
| Design Read declared | Verified | Premium editorial engineering portfolio for clients and research collaborators. |
| Dials explicit | Verified | Layout variation 6, motion 2, visual density 3, justified by the owner's restrained direction. |
| Redesign audit before implementation | Verified | DESIGN_AUDIT_AND_COVERAGE_PLAN.md inventories brand, IA, SEO and preserve/retire decisions. |
| Aesthetic / system honestly identified | Verified | Custom architectural editorial aesthetic using existing React/TypeScript/native CSS; no claim to an unrelated product design system. |
| One page theme | Verified | Charcoal throughout, with a modest dark surface shift in the institutional suite. No light/dark inversion. |
| Consistent accent | Verified | Approved-logo blue #99c7ef used as the shared accent; muted neutrals carry normal copy. |
| Shape consistency | Verified | Sharp image, button and panel geometry; no arbitrary rounded-card system. |
| Typography and serif discipline | Verified | Self-hosted Newsreader display plus Manrope body. The owner's explicit editorial/luxury brief justifies the display serif. No Fraunces or Instrument Serif. |
| Font loading | Verified in source/render | Local WOFF2 with font-display:swap; fonts decoded before peer screenshots. No remote font request is required. |
| Hero hierarchy and copy count | Verified | Two-line name, professional title, short positioning sentence and actions. The hero headline fits two lines and actions are visible in reviewed initial viewports. |
| Hero name / face separation | Verified | Corrected tablet stack, phone composition and 1440/1920 render inspection; full hair/eyes visible. |
| Hero viewport stability | Verified in reviewed renders | Fixed image dimensions/aspect, explicit mobile/tablet layouts; no shrunken desktop composition. The complete ten-width test belongs to browser QA. |
| Header one line / height | Verified | Desktop header 80 px; navigation shares one row. Mobile header 74 px with compact approved brand lockup. |
| Eyebrow count | Verified | Three restrained section labels across seven macro sections including identity; no decorative section numbering. |
| Section-heading structure | Verified | Heading and explanation stack vertically, rather than oversized-left-title/tiny-right-copy repetition. |
| Layout repetition / zigzag | Verified with owner context | Dominant lead, offset healthcare spread, terrain/index, systems atlas, institutional suite and research spread vary composition. Repeated project-caption grammar serves 23 required coverage groups; it is not repeated framed cards. Mobile repetition is an intentional readable sequence. |
| No decorative photo labels | Verified | No pills, chapter counters or fake credits over images. Provenance below images is a mandatory truth label required by the owner, not decorative metadata. |
| No version labels, scroll cues or decorative dots | Verified | None in the rendered marketing homepage. Research step numbering expresses a real process order. |
| No decorative technical diagrams | Verified | Research panels describe the actual named methodology. No fabricated chart, synthetic result, floating mesh or pseudo dashboard is used. |
| Photography | Verified | Supplied images remain dominant, with exact class/provenance labels. The instruction to use generated or stock imagery is inapplicable because the owner requires preservation of supplied image evidence. |
| Brand, portrait and content preservation | Verified | Eight core identity/content files compare byte-identical with admitted v7.2; HOMEPAGE_COVERAGE_AUDIT_v7_3.md records hashes. |
| Copy self-audit / unsupported claims | Verified for redesigned content | No new project metrics, whole-building institutional claims, research results or passed PETRA gates. Exact approved names remain present. |
| Zero em dashes | Verified | None found in the 26 produced HTML files; the homepage parser also finds zero. Existing locked names and narratives retain their approved punctuation otherwise. |
| CTA contrast | Verified for primary palette | #f2f0e9 against #151717 = 15.78:1. Muted copy against canvas = 9.38:1; accent against canvas = 10.09:1; muted copy against #1d2020 panel = 8.55:1. This token calculation is not a whole-page manual contrast audit. |
| CTA wrap / intent | Verified in reviewed renders | Primary Explore projects and secondary About Daniel labels remain one line. Repeated standard header/footer destinations serve navigation, not competing hero actions. |
| Focus visibility / keyboard structure | Source verified; fresh behavior QA separate | Shared visible focus outline, skip link, native controls, menu expanded state and Escape handler preserved. Do not treat this row as a completed keyboard regression test. |
| Motion motivation | Verified | Short reveal supports entry hierarchy; slight image scale acknowledges hover. Neither is needed to read content. |
| Motion cleanup / reduced motion | Source verified; fresh behavior QA separate | IntersectionObserver disconnects and animations cancel on cleanup. Reduced-motion skips reveals and removes hover movement; 1920 reduced-motion render was inspected. |
| No scroll hijacking / scroll handler | Verified in active source | Native scrolling; no pinning, camera, wheel interception or scroll event animation loop in the new homepage. |
| Icons | Verified | Existing Phosphor library; approved logos are preserved brand assets, not invented UI icons. |
| Client motion isolation | Verified | Motion lives in the existing 'use client' Stories module; static HTML remains complete and visible. |
| Semantic headings and landmarks | Source/render verified; fresh axe separate | Header/nav/main/footer and one homepage H1. Twenty coverage articles and their titles exist in prerendered HTML. |
| Content density | Verified visually | Short project summaries, substantial photographs, six content groups after identity. No data-heavy table or fake precision on the public homepage. |
| Cards omitted where possible | Verified | Image spreads and captions use spacing rather than floating bordered cards. Research panels are substantive documents, not a feature-card grid. |
| Four or more layout families | Verified | Hero, dominant image spread, asymmetric paired work, systems atlas, institutional suite and research methodology layout. |
| Marquees, testimonials and logo walls | N/A | None requested or present. No fabricated client logo wall or quote. |
| Bento exact-cell / diversity rules | N/A | No bento interface. |
| Form labels, input contrast, field order | N/A | Contact uses existing external contact links; no form or new input flow was added. |
| Italic descender clearance | N/A | No decorative italic headline treatment. |
| Multi-mode theme testing | N/A | Owner explicitly requests a controlled dark palette; no light/auto mode is offered. |
| GSAP sticky/horizontal skeleton | N/A | User replaces effects-led scenes; no pinned GSAP or horizontal-scroll section is retained in the active homepage. |
| Empty/loading/error states | Context appropriate | Static portfolio content is prerendered; images retain alt text and dimensions; the established 404 route remains. Dynamic project filters and galleries retain their controls; regression results belong to browser QA. |
| Core Web Vitals | Separate fresh measurement | Do not infer LCP/CLS/TBT or INP from screenshots. PERFORMANCE_REPORT_v7_3.md must supply actual measurements and limits. |
| Fresh build, routes, accessibility, SEO and security | Separate fresh reports | This matrix does not reuse old PASS evidence or certify results still running. |

No unresolved provenance or manual contrast review item is promoted to PASS by this design matrix. Publication remains HOLD_PENDING_OWNER_VISUAL_APPROVAL.
