# Route validation report — rebuilt v7.1

Disposition: PASS for all 25 expected public routes and intended 404 behavior.

## Fresh production results

- 50 successful route/viewport loads: 25 public routes × 390px and 1440px.
- 25 direct deep-link reloads returned HTTP 200 with stable route-specific titles and one H1.
- Canonical URLs equal https://danny-jesus.github.io plus each route.
- All main images decoded; no route horizontal overflow at the two tested widths.
- Unknown /missing-case/ returned HTTP 404 with noindex metadata (not a 200 application shell).
- Browser back/forward and Aji/Anseta deep-route refresh passed.
- Extended traversal reported 0 page errors, 0 console warnings/errors, 0 HTTP errors and 0 failed requests.

| Route | 390px | 1440px | Deep-link reload |
|---|---|---|---|
| / | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /research/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /field-community/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /about/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /credentials/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /contact/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/institutional-installation-documentation/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/gosh-meda-mch/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/anseta-opd/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/zazi-bridge/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/barguada-irrigation/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/aji-classroom/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/nefas-mewucha-road/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/insa-head-office/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/prime-ministers-office-press-offices/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/undp-head-office/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/water-wash/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/hydraulic-infrastructure/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/bisach-vet-post/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/ftc-facilities/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/warehouse-fdp/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /projects/maintenance-rehabilitation/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /research/xauusd-research/ | 200 / PASS | 200 / PASS | 200 / stable title |
| /research/petra-ai/ | 200 / PASS | 200 / PASS | 200 / stable title |

## Navigation and media

Hero Explore Projects native anchor navigation, all four desktop navigation links, mobile menu Enter/Tab/selection/Escape behavior, project filtering, lightbox, comparison slider and no-JavaScript content checks passed. Contact/footer LinkedIn and GitHub links use valid HTTPS URLs, new-tab targets and noopener. No messages were sent and no external account interaction was performed; URL syntax/attributes do not prove those external services permit access or remain available.

Native lazy-loading check: 18 homepage images, 16 declared lazy, 13 initially unloaded. A far-below-view image was unloaded initially and decoded successfully after scrolling into view (natural width 0 to 1440). This was checked without overriding loading to eager. No public homepage video element exists; video-loading behavior is therefore not applicable to that route.

## Supporting motion/fallback results

Condition-based supplemental checks passed actual WebGL startup, reduced-motion disposal, WebGL-unavailable fallback, save-data fallback and orientation/tablet resize. Original fixed-wait startup failure remains in supplemental-suite.log and review/supplemental-review.json; the sequential equivalent with unchanged assertions and readiness waits passed. Its old v4.3 baseline capture is explicitly skipped; separate untouched-v7 before screenshots exist.

## Limits

These results validate a local server serving the exact production tree. They do not validate a deployment or the live GitHub Pages server. External social destination availability was not asserted. The 900×390 hero CTA begins below the first screen (y=560–610), but keyboard Tab automatically scrolls it into view (y=211–261) with a solid 3px focus outline. Enter successfully activates Aji native-anchor navigation; no page errors were recorded.

Evidence: review/browser-review.json; fresh/extended-functional.json; fresh/landscape-cta.json; supplemental-condition-review.json; final-browser-suite.log. Additional hero viewport geometry and screenshots are in fresh/hero-responsive.json and fresh/screenshots/.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
NO PUSH. NO MERGE. NO DEPLOYMENT.

External destination check: GitHub profile HEAD returned200. LinkedIn HEAD was blocked before origin access (CONNECT403, curl56); site URL, target and noopener were validated, but remote profile availability is unverified. See external-links.json.
