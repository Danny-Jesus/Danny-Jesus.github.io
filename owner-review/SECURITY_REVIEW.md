# Security review — controlled v7.1 rebuild

Disposition: static checks completed with no findings in the narrowly defined scans below. Final source/package exclusions remain pending packaging verification. This is not a comprehensive security certification or a claim that every possible secret/private item is absent.

Audit time (UTC): 2026-10-21T11:17:42.736430+00:00
Evidence: `static-integrity.json`, `static-security-findings.md`, and `/workspace/rebuild-evidence/content-audit.md`.

## Checks actually performed

- Scanned 172 source/configuration/documentation text files for private-key blocks, common GitHub tokens/PATs, AWS access-key IDs, and OpenAI-style secret-key patterns. Found 0 pattern matches. No secret values were printed or copied into reports. Found 0 `.env`/private-key filename candidates in the source comparison scope.
- Inspected all 26 prerendered HTML documents: zero external script URLs and zero HTTP or `javascript:` resource/link URLs were found. This is a static URL check, not a full browser CSP or vulnerability assessment.
- Found zero `.map` files in the production tree. No claim is made about every possible information disclosure mechanism in shipped JavaScript.
- Dependency declarations and npm lockfile match the authoritative source byte-for-byte. No dependency updates were performed. Locked npm installation and package integrity checks were handled by the build workflow; a separate fresh npm audit completed with 0 reported advisories across all severities (see npm-audit.json).
- No active retired portrait URLs were found in prerendered HTML. No public file is byte-identical to any of the five known retired portrait derivatives. The removed files were three `/images/cinematic/portrait-*` derivatives and two `/images/daniel-field-*` derivatives. This is a known-file/hash check, not automatic recognition of every possible image variant.
- All 55 selected photo records / 165 registered derivatives match the authoritative source and register hashes; all three shared installation originals match the baseline. This supports asset integrity, not publication rights or specific facility assignment.
- Reviewed extracted text from `public/documents/Daniel_Ashagrie_Ayele_Public_Profile.pdf`: a one-page public career summary, without private contact details, certificate serials, credentials, or proprietary PETRA implementation detail in its extracted text. Embedded images/metadata and legal rights are not certified by that text review.
- Public PETRA/XAUUSD narratives retain research boundaries and do not add private implementation artifacts, profitability, production authorization, or passed-governance claims. This is a content review, not proof that every retained source-history document is suitable for public release.

## Final-package exclusions — verified

The working source retains originals so admitted evidence is preserved. The final Source ZIP inventory and all member hashes were checked. It excludes the E-class certificate and retired temporary portrait originals below:

- `assets-originals/photo-library/Photos/Comm Training/Certificat.png` — E/private certificate evidence; absent from `public/` and `dist/` in this audit.
- `assets-originals/daniel-field-original.jpg` — retired temporary primary portrait original.
- `assets-originals/supplied-v4/portrait/daniel-field-portrait-landscape.webp`.
- `assets-originals/supplied-v4/portrait/daniel-field-portrait-square.webp`.
- `assets-originals/supplied-v4/portrait/daniel-field-portrait-hero.webp`.

Dependency/build caches and credential/environment files must not be silently included. Source and Production ZIP integrity and per-member SHA-256 validation passed; exact sizes and hashes are in package-integrity-source-production.json. Old portrait use in the review-only before/after evidence remains intentional. Exclusion verification: PASS for the final Source ZIP (538 members); Production ZIP contains exactly the 306 reviewed output members.

## Release hygiene and limitations

`.github/workflows/deploy.yml` is unchanged from the admitted source. Its existence is not authority to run it. `RELEASE_HOLD.json` remains status HOLD, `review_only=true`, `public_upload_authorized=false`, and `release_owner_approved=false`; owner portrait approval is true and temporary portrait is false. The pending release approval has not been cleared.

No push, merge, release creation, workflow dispatch, live-site modification, or deployment was performed by this audit. Read-only external HEAD checks returned GitHub200; LinkedIn was blocked by the environment CONNECT proxy403 and remains unverified. No dynamic penetration test, malware scan of binaries, legal/image-rights clearance, or comprehensive private-data classification was performed. Browser console/network evidence and actual release-hold command results belong to the other fresh QA reports.

Production tree checked: 306 files; sorted content-member manifest SHA-256 `c4d49ef4121511dae19e85a99bc8c8734a1b76e1a7735371da50ac577d6e0512`.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL

NO PUSH. NO MERGE. NO DEPLOYMENT.
