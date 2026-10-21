# Static content, portrait and provenance audit

Scope: read-only inspection of the admitted v7 source working copy at `/workspace/portfolio-v7-rebuilt` and prior review evidence. No build or browser execution was performed by this audit. Historical review reports are reference evidence, not fresh test results or authorization.

## Active portrait replacement locations

- `src/v7/Stories.tsx`: homepage portrait `portrait-480.webp` / `portrait-960.webp`; old selfie-specific SVG clipping path; old temporary-portrait note and old construction-vest alt text.
- `src/v7/site.css`: accumulated selfie-specific polygon/clipPath/masking/position rules must be replaced or overridden deliberately for the square approved portrait. Existing GSAP portrait transforms live in `src/v7/MotionRuntime.ts` and need responsive visual validation.
- `src/v7/Pages.tsx`: Contact uses old `portrait-480.webp`, 864×1536 dimensions and field-portrait alt. About currently uses documentary field/context image `PhotoImage id={54}` as its opening image; replace its primary portrait presentation with approved portrait without deleting id54 from the wider photo library.
- `src/entry-server.tsx`: Person structured-data image references `portrait-960.webp`. Keep/update to approved derivative.
- `scripts/prepare-social-v7.py`: contact/credentials social previews use old portrait; About uses id54; homepage social label says portrait approval pending. Regenerate applicable previews from approved image; keep truthful illustrative-background classification.
- `RELEASE_HOLD.json`: portrait-specific approved/temporary metadata is stale, but status/public-upload/release approvals must remain HOLD/false. `scripts/check-release-hold.mjs` must continue blocking publication.
- `src/data/site.ts` and `src/components/Portrait.tsx` contain inactive legacy field-portrait configuration. Active `src/App.tsx` imports only v7 pages. Avoid leaving primary-portrait source paths misleading if these modules are retained.

## Old portrait files currently copied to public output

All files under `public/` are copied by Vite whether imported or not. Existing portrait paths are:

- `public/images/cinematic/portrait-480.webp`
- `public/images/cinematic/portrait-960.webp`
- `public/images/cinematic/portrait-1600.webp`
- `public/images/daniel-field-480.webp` (inactive legacy public asset)
- `public/images/daniel-field-864.webp` (inactive legacy public asset)

The first three can become approved-image derivatives. The two inactive legacy selfie derivatives should be excluded from final production or replaced if preserving paths. Old original is `assets-originals/daniel-field-original.jpg`; three additional legacy crops are under `assets-originals/supplied-v4/portrait/`. These are private editable-source history, not current public primary portraits. Existing review screenshots/social images may also show old identity; use old imagery only in genuine comparison evidence, not final public output.

## Private/E-class exclusion

`PHOTO_LIBRARY_REGISTER.json` explicitly marks PHOTO-009 as E / Private / excluded. Exact byte-match search found one physical copy:

`assets-originals/photo-library/Photos/Comm Training/Certificat.png`

SHA-256: `cc9275b0292e874e6a49cbb421e1edae49a2b61bd1d2c495b86897d2bba689cc`

Exclude this certificate from rebuilt Source/Production/Review packages; preserve it unchanged in the admitted baseline/input archive. No corresponding public derivative exists. Other six unused registered photos are B/C contextual alternatives, not automatically private. Do not delete the wider documentary library merely because photos are unused on homepage.

## Public profile PDF

`public/documents/Daniel_Ashagrie_Ayele_Public_Profile.pdf` is readable, one page, 1,693 extracted characters. It is explicitly a public professional summary, with name, profession, supplied career/education/registration history, public portfolio/LinkedIn/GitHub links, and research summaries. It states current registration renewal needs confirmation and both research programs are ongoing. No private contact details, certificate serials, API credentials or proprietary PETRA implementation detail were found in the extracted text. Text extraction does not certify embedded-file/image metadata or legal publication rights.

## Content/route/provenance preservation

- `src/entry-server.tsx` declares 25 public routes plus generated 404; actual production needs fresh verification.
- `src/v7/content.ts` locks Aji → Anseta → Zazi → Barguada → UNDP → Press Secretariat → INSA, followed by XAUUSD and PETRA via Home. Exact required XAUUSD title/subtitle/descriptor is preserved.
- Institutional scope explicitly excludes whole-building responsibility. Three installation originals remain a shared unassigned archive.
- 55 selected photo-library entries remain represented across project/field pages. B/C/D labels are conservative; conceptual/generated context is distinguished from documentary evidence.
- PETRA boundary says research/review ongoing, makes no production-certification claim and excludes private research artifacts.

## Static security observations and limits

No obvious private-key blocks, common GitHub token patterns, AWS access-key IDs or OpenAI-style secret-key patterns were found in scanned text source/config/docs. No `.env`, private key files, public source maps or active mixed-content/script-evaluation patterns were found in the reviewed tree. This is a limited pattern scan, not a comprehensive credential/proprietary-material certification.

Existing `.github/workflows/deploy.yml` can deploy on a main push, but remains gated by release approval checks. Do not modify Pages workflow/configuration, push, merge, dispatch workflows, or deploy. Repository-local builds do not authorize remote publication.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
