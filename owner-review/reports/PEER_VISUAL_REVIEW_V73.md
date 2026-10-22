# v7.3 final internal visual review

Assessment: YES on A–E for the revised design candidate. Publication remains HOLD_PENDING_OWNER_VISUAL_APPROVAL.

This is an AI peer assessment of actual rendered screenshots and the produced source/HTML. It is not an external designer endorsement, human user study, automated QA certificate or owner visual approval. The owner may accept or reject the candidate after reviewing the complete evidence.

## Rendered evidence reviewed

- Final desktop hero at 1440 px: `review/screenshots/HERO_DESKTOP_1440_V73.png`.
- Phone hero at 390 px: `draft/hero-390.png`.
- Corrected tablet hero at 768 px: `draft/hero-768.png`.
- Fresh final-candidate 1920 px hero with reduced motion enabled: `draft/peer-hero-1920-final.png`.
- Complete desktop and mobile contact-sheet renders: `draft/contact-1440.jpg` and `draft/contact-390.jpg`.
- Fresh production homepage and content-preservation audit: `reports/HOMEPAGE_COVERAGE_AUDIT_v7_3.md` and `qa/homepage-coverage-peer-v73.json`.

The final 1920 px check rendered the current production output in headless Chromium with `prefers-reduced-motion: reduce`, waited for the actual fonts and portrait to decode, and captured the viewport. No horizontal overflow or canvas was present in that check. This scoped observation does not stand in for the separate full browser QA.

## A–E assessment

| Owner test | Internal judgment | Evidence and reasoning |
| --- | --- | --- |
| A. Looks like a real premium professional portfolio even without motion | YES | The static hero has clear identity, strong editorial type and a confident portrait composition. Photography, spacing and hierarchy carry the remaining page. The reduced-motion 1920 px capture retains the same design quality. |
| B. Feels elegant and high-end rather than effect-heavy | YES | The generic spatial meshes, wireframes, fake technical overlays and long pinned scene sequences are absent from the active homepage. Motion is a brief optional reveal and a restrained image hover scale. The controlled charcoal and blue brand palette stays consistent. |
| C. Represents all major supplied engineering work clearly | YES | Twenty classified photographic entries, two locked research presentations and the professional close account for all 23 required groups. Their exact titles, route targets and provenance statements were confirmed in current production HTML. |
| D. Homepage feels curated rather than crowded | YES | Six content groups after identity establish a readable sequence. Dominant Aji imagery, offset healthcare spreads, terrain work, the systems atlas, the specialist institutional suite, people/practice and research vary scale without becoming a card dashboard. On mobile the same coverage becomes a deliberate reading sequence with generous image area. |
| E. Premium, professional and credible to an experienced designer | YES, as an internal assessment | The composition, typography, restrained palette and clear visual hierarchy are consistent with a serious editorial portfolio. This is a design judgment about the candidate, not a statement that an external experienced designer or the owner has approved it. |

## Correction verified after the draft review

The 768 px hero no longer enlarges the face behind the name. A dedicated tablet stack separates the two-line name, full visible head, professional title and actions. The portrait has clear breathing room, keeps the hair and eyes visible and avoids accidental identity cropping. At 1920 px, the reduced title size and revised portrait placement leave the name outside the face. Both desktop sizes remain composed; the phone layout preserves its own hierarchy rather than scaling the desktop arrangement.

## Honest limits and retained holds

The homepage is still substantial because the owner requires 23 groups to be visible. Its roughly 12.6k desktop / 14.8k phone draft pixel lengths are a consequence of the coverage and photography, not evidence of a performance defect; final dimensions are recorded in fresh QA. Adding more scenes or spacer chapters would weaken the curation.

Several supplied images are conceptual/edited or montages. The layout makes them clear and valuable but cannot make them documentary. Zazi assignment, Saka Health Post before/after provenance/dates/scope, field-photo assignment and participant permissions remain unresolved. Labels and scope boundaries remain visible. Manual contrast review beyond automated sampling is a separate unresolved review item.

This visual review does not infer that route, accessibility, performance, SEO, security or media checks have passed. Their fresh reports control those conclusions. No project facts, logo geometry or portrait identity were changed by this assessment.

Release disposition: HOLD_PENDING_OWNER_VISUAL_APPROVAL.
