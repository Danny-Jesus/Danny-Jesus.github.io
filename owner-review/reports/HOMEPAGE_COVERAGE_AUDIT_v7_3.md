# Homepage coverage audit v7.3

Result: PASS for all 23 required coverage groups in the fresh production HTML. This is a content/route-target audit, not a browser interaction, accessibility or performance result.

Production index SHA-256: `7d7920ba85cecaad2edfc3c7abc4f453e1233946e4bb4a893f1ce8654f5869e8`

The homepage comprises identity plus six grouped editorial sections: signature works, infrastructure systems, institutional works, people/practice, research and the professional close. Twenty individually classified photographic articles supply the engineering and field coverage; two research presentations and one professional close complete the 23 required groups.

| Required coverage | Homepage group | Route target | Result |
| --- | --- | --- | --- |
| Aji Four-Classroom Construction | signature-works | `/projects/aji-classroom/` | PASS |
| Anseta OPD Facility | signature-works | `/projects/anseta-opd/` | PASS |
| Gosh Meda MCH Facility | signature-works | `/projects/gosh-meda-mch/` | PASS |
| Zazi Bridge Infrastructure Project | signature-works | `/projects/zazi-bridge/` | PASS |
| Barguada Irrigation Canal | signature-works | `/projects/barguada-irrigation/` | PASS |
| Nefas Mewucha–Lay Gayint Road | signature-works | `/projects/nefas-mewucha-road/` | PASS |
| Water & WASH infrastructure | infrastructure-systems | `/projects/water-wash/` | PASS |
| Bisach Vet Post | infrastructure-systems | `/projects/bisach-vet-post/` | PASS |
| Maintenance & Rehabilitation | infrastructure-systems | `/projects/maintenance-rehabilitation/` | PASS |
| Irrigation / dam / reservoir systems | infrastructure-systems | `/projects/hydraulic-infrastructure/` | PASS |
| FTC Facilities | infrastructure-systems | `/projects/ftc-facilities/` | PASS |
| Warehouse / FDP / Rub Hall | infrastructure-systems | `/projects/warehouse-fdp/` | PASS |
| Road / bridge / culvert infrastructure | infrastructure-systems | `/projects/nefas-mewucha-road/` | PASS |
| UNDP Head Office | institutional-works | `/projects/undp-head-office/` | PASS |
| Press Secretariat of the Prime Minister’s Office | institutional-works | `/projects/prime-ministers-office-press-offices/` | PASS |
| INSA Head Office | institutional-works | `/projects/insa-head-office/` | PASS |
| Training / artisan training | people-practice | `/field-community/` | PASS |
| Supervision / field practice | people-practice | `/field-community/` | PASS |
| WASH / community training | people-practice | `/field-community/` | PASS |
| Community participation / awareness | people-practice | `/field-community/` | PASS |
| XAUUSD Market Structure & Quantitative Research | research-innovation | `/research/xauusd-research/` | PASS |
| PETRA AI | research-innovation | `/research/petra-ai/` | PASS |
| Credentials / About / Contact | credentials | `/credentials/, /about/, /contact/` | PASS |

## Checks performed

Parsed the current `dist/index.html` rather than inferring coverage from source alone. Each of the twenty photographic entries contains its exact approved title, a link to its intended route, an existing prerendered route file, the exact image provenance statement and the expected hold/classified state. The research names and subtitles are present with their intended deep links. Credentials, About and Contact are all linked in the professional close. There is one H1. All coverage is ordinary rendered content, not content accessible only through a carousel or accordion. Actual desktop/mobile contact sheets were visually reviewed separately.

## Content and identity preservation

The following files compare byte-for-byte identical with the admitted v7.2 corrected source:

| File | Candidate SHA-256 |
| --- | --- |
| `src/v7/home-chapters.json` | `7731e9e65f3d0ebef6881a010741e09edc5500b6215bfa365caa2c5a6cb2529b` |
| `src/data/projects.ts` | `915f7c60cbfc4dc5b6a56ba945a2e208bf5006c34b5f3a75b44d1cc2f48ed9b1` |
| `src/data/career.ts` | `2439f8a5afc0d7f913b037763d6952498cffdafe534a0eb4944830224053d2be` |
| `src/data/credentials.ts` | `5ea1bc33aa11e0569ff9ae5d177cbccc9294a8a63a429f0b7693e748d53e9ebf` |
| `src/data/site.ts` | `2d173a0c614b6b315d8b1546ac175475bc52cdb30c96597054608f4c41908ba0` |
| `src/data/socials.ts` | `1952d3da942ea73a9c8e3d74aa645ffe2c69d3938d0af39d86959de62a25805e` |
| `public/brand/logo-mark.svg` | `220044aa4d23626fd6d5e798e7a94aa710a469e583eaba820f0e1ab17ac93ea0` |
| `assets-originals/approved-portrait/Friendly Outdoor Professional Portrait(1).png` | `c2e86ee1d675de11998f0e21f463e52bdece38b0b99fa641546cdfd26ce77a77` |

The case-study definitions in `src/v7/content.ts` also preserve their engineering facts. The sole change in that file is the XAUUSD public-boundary sentence: it now describes a public methodology schematic instead of the retired synthetic spatial view. Its prohibition on inferred market results, profitability, backtests and trading signals remains intact.

No unsupported project quantities, impact numbers, whole-building institutional responsibility or research-completion claims were introduced by the homepage regrouping. The institutional section explicitly limits scope to specialist interiors; shared authentic installation records stay unassigned.

## Provenance holds preserved

- Zazi image assignment remains unconfirmed.
- Saka Health Post before/after provenance, dates and exact scope remain unconfirmed.
- Field photograph assignment and participant permissions remain unconfirmed.
- Training/community event, date and participant assignment remain unconfirmed.

This audit does not turn those items into PASS and does not replace the separate manual contrast review requirement.

Evidence: `qa/homepage-coverage-peer-v73.json`; `src/v7/home-chapters.json`; current prerendered homepage; baseline/source byte comparisons.

Publication: HOLD_PENDING_OWNER_VISUAL_APPROVAL.
