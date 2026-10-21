# SEO and metadata review — controlled v7.1 rebuild

Disposition: PASS for the static production checks listed below. This is local output evidence, not a statement about search indexing, remote hosting, or field behavior.

Audit time (UTC): 2026-10-21T11:17:42.736430+00:00
Evidence: `static-integrity.json`, `static-security-findings.md`, `content-audit.md`, and the reviewed production files. Browser route checks and Lighthouse results are reported separately; earlier v7 scores are not treated as fresh measurements.

## Production metadata checks

- Found 25 public HTML routes and one dedicated 404 page. The sitemap contains 25 public URLs.
- All 26 HTML documents have a nonempty unique title, nonempty description, one H1, syntactically valid JSON-LD, existing Open Graph image, matching Twitter image URL, and existing favicon references.
- All 25 public canonicals match `https://danny-jesus.github.io` plus the route path. These intended canonical URLs do not indicate a deployment.
- Homepage title: `Daniel Ashagrie Ayele | Civil Engineer & Quantitative Developer`.
- Primary identity remains Daniel Ashagrie Ayele; profession remains Civil Engineer & Quantitative Developer. The Person schema image points to `/images/cinematic/portrait-approved-960.webp` in all 26 documents.
- The home, About, Contact, and Credentials social image files are updated with the approved portrait. Other social images are unchanged from the admitted source. Home image alternative metadata now describes the approved portrait. Conceptual project/research social assets remain distinguished from documentary evidence.
- Open Graph and Twitter social image references resolve to nonempty local production assets. Public social endpoint fetching and platform-specific preview behavior were not tested.
- Favicon references include `/favicon.svg`, `/favicon-32.png`, `/apple-touch-icon.png`, `/favicon.ico`, and `/favicon-16.png`; all exist. The compact DA mark remains secondary to the full-name brand.
- `robots.txt` allows ordinary crawling and declares `https://danny-jesus.github.io/sitemap.xml`.
- `404.html` has title `Page unavailable | Daniel Ashagrie Ayele` and `robots=noindex`. Its preserved canonical is `https://danny-jesus.github.io/404/`; no claim is made that this nonexistent content route should be indexed. Actual local HTTP 404 behavior is covered by the route/browser report.
- No missing alt attributes were found in the static rendered image markup. This checks attribute presence; meaningful wording, contrast, and rendered usability require accessibility/visual review.

## Public route inventory

| Route | Title | Static metadata |
|---|---|---|
| `/about/` | About Daniel Ashagrie Ayele &#124; Daniel Ashagrie Ayele | PASS |
| `/contact/` | Contact Daniel Ashagrie Ayele &#124; Daniel Ashagrie Ayele | PASS |
| `/credentials/` | Professional Credentials &#124; Daniel Ashagrie Ayele | PASS |
| `/field-community/` | Field, Training & Community &#124; Daniel Ashagrie Ayele | PASS |
| `/` | Daniel Ashagrie Ayele &#124; Civil Engineer & Quantitative Developer | PASS |
| `/projects/aji-classroom/` | Aji Four-Classroom Construction &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/anseta-opd/` | Anseta OPD Facility &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/barguada-irrigation/` | Barguada Irrigation Canal &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/bisach-vet-post/` | Bisach Vet Post &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/ftc-facilities/` | FTC Facilities &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/gosh-meda-mch/` | Gosh Meda MCH Facility &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/hydraulic-infrastructure/` | Irrigation, Dam & Reservoir Systems &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/` | Engineering Projects &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/insa-head-office/` | INSA Head Office &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/institutional-installation-documentation/` | Shared Installation Documentation &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/maintenance-rehabilitation/` | Maintenance & Rehabilitation &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/nefas-mewucha-road/` | Nefas Mewucha-Lay Gayint Road &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/prime-ministers-office-press-offices/` | Press Secretariat of the Prime Minister’s Office &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/undp-head-office/` | UNDP Head Office &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/warehouse-fdp/` | Warehouse, FDP & Operational Support Infrastructure &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/water-wash/` | Water & WASH Infrastructure &#124; Daniel Ashagrie Ayele | PASS |
| `/projects/zazi-bridge/` | Zazi Bridge Infrastructure Project &#124; Daniel Ashagrie Ayele | PASS |
| `/research/` | Research Programs &#124; Daniel Ashagrie Ayele | PASS |
| `/research/petra-ai/` | PETRA AI &#124; Daniel Ashagrie Ayele | PASS |
| `/research/xauusd-research/` | XAUUSD Market Structure & Quantitative Research &#124; Daniel Ashagrie Ayele | PASS |

## Limits and outstanding review

No live-site request, crawler submission, social scraper request, push, merge, release, or deployment was performed. Indexability of the local output does not authorize publication. No unsupported certification, profitability, or completed PETRA gate was introduced by these metadata changes. Source-reported career details and unresolved ownership/provenance decisions remain subject to the owner review described in the rebuilt reports.

Production tree checked: 306 files. SHA-256 of the sorted content-member manifest: `c4d49ef4121511dae19e85a99bc8c8734a1b76e1a7735371da50ac577d6e0512`. Final ZIP member equivalence is a separate packaging check.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
