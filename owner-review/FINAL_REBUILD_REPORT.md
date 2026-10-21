# Final Rebuild Report — controlled v7.1

Generated 2026-10-21T14:29:46.375363+03:00

Status: HOLD for owner visual approval. Technical rebuild, required review captures and packaged-source reproducibility checks completed; external LinkedIn origin availability could not be established through the environment proxy. No publication authorization is inferred.

1. **Environment:** recovered and usable. Node24.19.0/npm11.9.0; local install/build/browser/Chromium/FFmpeg/Python operations succeeded. Vite development entry/HMR response also validated. Install/start draft saved; it was not activated or published. No fresh-task restoration claim.
2. **Inputs admitted:** Source7/7 parts and Review6/6 parts; exact size/hash, central directory, CRC and extraction passed. Portrait ZIP previously admitted and still accessible. Earlier transfer HOLD history preserved.
3. **Source input hash:** `de6f9dd8ef79cb42b4ef6db495a6b262c60d3a74294a3a3661804040f5d53c7f` (217578026 bytes).
4. **Review input hash:** `1e6480efee0b1f543443a7007295a3fbc9925e6d000b4cde541807220edfd3f5` (187449419 bytes).
5. **Hero source identity:** Friendly Outdoor Professional Portrait(1).png from DANIEL_APPROVED_HERO_PORTRAIT_ORIGINAL.zip (archive SHA-256 `f02cab6ae800aa9465869b70a059cd0a926333e85172e21f8cdfaa7e03532d9e`). Exact original PNG SHA-256 `c2e86ee1d675de11998f0e21f463e52bdece38b0b99fa641546cdfd26ce77a77`. No identity-altering operations.
6. **Files changed:** complete source-baseline delta listed below and in source-changes.json. Application project/research content, manifests/lockfile and deployment workflow unchanged. Existing Git checkout remains clean on branch work, HEAD59a53041351954950a52ebba8c9d89287dbbcfff; editable recovered source is separate at /workspace/portfolio-v7-rebuilt.
7. **Portrait locations:** homepage hero, About opening, Contact, legacy portrait configuration, route Person schema, and4 relevant social previews. Five retired public portrait derivatives removed. Canonical PNG and3 proportional WebPs included.
8. **Build:** locked npm ci passed using writable cache; npm run build typecheck/client/SSR/prerender/verification passed. Final Source ZIP extracted in isolation, freshly installed and built; all306 reviewed production members reproduced byte-for-byte. Initial default npm cache failed; corrected cache path restored verification without lockfile edits or disabling checks.
9. **Routes:**25 unique public routes ×2 widths =50 successful route loads;25 deep reloads passed; true404/noindex and JavaScript-disabled narratives passed. Hero CTA, desktop/mobile nav, filters, lightbox, comparison, history, lazy image behavior and resize/orientation passed. GitHub external HEAD200; LinkedIn CONNECT403 blocked remote availability verification.
10. **Cinematic QA:**20 scene WebGL checks passed; desktop/mobile captures reached page end, with0 page errors. GSAP/native scrolling, layered photography, research/institutional identity and fallback behavior preserved. See CINEMATIC_QA_REPORT.md.
11. **Desktop hero:** widths768,1024,1280,1440,1920 inspected/captured. Face/hair visible, no detected text overlap or horizontal overflow; full-name wordmark/title/CTA preserved.
12. **Mobile hero:** widths320,360,375,390,430 inspected/captured; separate upper portrait/lower typography composition.320×700 and390×740 usable.900×390 landscape CTA is below first screen; keyboard focus scrolls it into view and Enter reaches Aji.
13. **Accessibility:**50 axe WCAG-tagged scans,0 reported violations; practical keyboard/focus/menu/fallback checks passed. Automated coverage is not full WCAG or screen-reader certification.
14. **Performance:** fresh Lighthouse13.5.0: mobile84, LCP2.951s, CLS0, TBT404.5ms; desktop89, LCP1.239s, CLS0, TBT232ms. Accessibility/SEO/best-practices100 both. Mobile LCP and lab TBT are optimization opportunities. INP not measured.
15. **Security:** limited source/production scans found0 secret-pattern hits,0 public source maps,0 external script URLs or unsafe HTTP/javascript links. Fresh npm audit0 advisories. Private E certificate and retired selfie originals verified excluded from Source ZIP. Scope limits apply; no comprehensive security/rights certification.
16. **Production manifest:**306 members, exact per-file hash set verified in frozen tree, Production ZIP and isolated Source ZIP rebuild. Member manifests and package hashes supplied.
17. **Generated artifacts:** listed below. Recordings are103.666s desktop and68.049s mobile. Offline review uses relative local assets; review-package integrity checks are recorded by final packaging.
18. **Known limitations:** single cloud Chromium/software-WebGL laboratory; no physical Safari/iOS/Android device runs or field INP. Original supplemental fixed1.2s wait failed; condition-based equivalent retained assertions and passed. LinkedIn origin check blocked by CONNECT403. Portrait/provenance/participant rights are not independently certified. The source includes clearly historical reports; only rebuilt fresh evidence describes this output.
19. **Owner decisions:** review desktop/mobile heroes, comparisons, both recordings, offline review and QA/packages; approve or request visual corrections. Existing B/C image provenance/participant rights/institutional assignment and factual gaps remain owner decisions. A separate explicit publication authorization is required.
20. **Release disposition:** PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL. NO PUSH. NO MERGE. NO RELEASE. NO DEPLOYMENT. No GitHub Pages or live website modification.

## Files changed

- changed: `README.md`
- changed: `RELEASE_HOLD.json`
- added: `assets-originals/approved-portrait/Friendly Outdoor Professional Portrait(1).png`
- added: `docs/v7/APPROVED_PORTRAIT_DERIVATIVES.json`
- removed: `public/images/cinematic/portrait-1600.webp`
- removed: `public/images/cinematic/portrait-480.webp`
- removed: `public/images/cinematic/portrait-960.webp`
- added: `public/images/cinematic/portrait-approved-1254.webp`
- added: `public/images/cinematic/portrait-approved-480.webp`
- added: `public/images/cinematic/portrait-approved-960.webp`
- removed: `public/images/daniel-field-480.webp`
- removed: `public/images/daniel-field-864.webp`
- changed: `public/social/about-social.jpg`
- changed: `public/social/contact-social.jpg`
- changed: `public/social/credentials-social.jpg`
- changed: `public/social/home-social.jpg`
- added: `scripts/prepare-approved-portrait.py`
- changed: `scripts/prepare-social-v7.py`
- changed: `scripts/prepare-v7-assets.py`
- added: `scripts/rebuild-hero-review.mjs`
- added: `scripts/record-v7-rebuilt.mjs`
- changed: `src/data/site.ts`
- changed: `src/entry-server.tsx`
- changed: `src/v7/Pages.tsx`
- changed: `src/v7/Stories.tsx`
- changed: `src/v7/site.css`

## Output artifacts

- `Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_1_REBUILT_Source.zip`
- `Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_1_REBUILT_Production.zip`
- `Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_1_REBUILT_Review_Package.zip`
- `FINAL_VISUAL_REVIEW_v7_1_REBUILT.html`
- `HERO_DESKTOP_1440.png`
- `HERO_MOBILE_390.png`
- `HERO_BEFORE_AFTER_COMPARISON.png`
- `FINAL_CINEMATIC_SCROLL_REVIEW.mp4`
- `FINAL_MOBILE_SCROLL_REVIEW.mp4`
- `FINAL_REBUILD_REPORT.md`
- `INPUT_ADMISSION_REPORT.md`
- `ROUTE_VALIDATION_REPORT.md`
- `ACCESSIBILITY_REPORT.md`
- `PERFORMANCE_REPORT.md`
- `SECURITY_REVIEW.md`
- `ASSET_INTEGRITY_REPORT.md`
- `REBUILD_SHA256_MANIFEST.txt`

## Source and Production package integrity

| Package | Exact bytes | SHA-256 |
|---|---:|---|
| Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_1_REBUILT_Source.zip | 217078620 | `4bb48ccb3388d27154298006f8761840337a1aa2b7adcfbc6c8b4771800eae93` |
| Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_1_REBUILT_Production.zip | 34568784 | `71b4da6a60552911f6005be390322fa6158f6b9e6093cac0745fbc5853e13371` |

The external final SHA-256 manifest includes all three final archive hashes. This report inside the Review ZIP does not attempt a circular self-hash.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL

## Review artifact verification

Local static-server owner-review test: PASS. All review images decoded, four gallery controls worked, both MP4s played with metadata and advancing playback, no page errors, and390/1440px review layouts had no horizontal overflow. Native wheel and PageDown scrolling on the portfolio advanced450px and1165px respectively. Direct file:// opening remains unverified because cloud Chromium returned ERR_BLOCKED_BY_ADMINISTRATOR; no policy bypass was attempted. Relative packaged-file inventory is verified separately.
