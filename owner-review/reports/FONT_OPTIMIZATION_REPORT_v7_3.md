# Newsreader safe optimization candidates

Recommended candidate: `newsreader-exact-fullaxes-english.woff2`. It is 96852 bytes, compared with 197,144 bytes for the current public font (50.9% smaller). It keeps the complete original weight 200–800 and optical-size 6–72 axes. It removes unused glyph coverage while retaining ASCII printable characters, all supported characters extracted from the current production HTML routes, and smart quotation marks, dashes, bullet, ellipsis, copyright, registered and trademark characters.

At weights 400 and 420 and optical sizes 24, 48 and 72, every retained glyph has exactly equal decomposed outline coordinates and advance widths compared with the current public font: maximum difference **0.0 font units**. The comparison includes unmapped alternates and ligatures through the saved glyph-index mapping.

The complete extracted route text (64090 characters) was also shaped with HarfBuzz at all six locations. Glyph identities, clusters, x/y advances and x/y offsets match exactly. See `report-exact-english.json`.

SHA-256: `d4635232acf2d656f82b9ed06f20167dfff389031d718943022ce7016a36e722`

The broader Latin-1 candidate is approximately 131 KB and passes the same checks.

## Rejected approach

Restricting the weight axis to 400–420 with fontTools instancer produced smaller files (~76 KB), but instancing introduced rounding differences up to 1.68 font units in outlines and 0.92 units in advances at weight 420. Those candidates are **not approved as exact replacements**. They remain separate experimental evidence only.

No public font, CSS, source or lockfile was modified by this optimization task. Root should admit the recommended candidate explicitly before replacing the public font and update the typography provenance document to the final admitted SHA. Font subsetting proof tooling uses temporary fontTools/Brotli/uharfbuzz tooling only and does not add app dependencies.

## Admission and measurement

The exact96,852byte subset was admitted into public/fonts/newsreader-latin-variable.woff2. Source was rebuilt and measured afresh. Mobile performance improved88→93, LCP3.911→3.235seconds; desktop99→100, LCP1.006→0.687seconds. Both profiles retain TBT0ms/CLS0. These are laboratory results, not field Core Web Vitals.

A separate experiment removing font preloads was rejected: mobileFCP2.112s/LCP3.387s/score90 and small layoutshift were worse than the admitted preload configuration. It did not modify the application or validated production output. No visual quality was reduced to optimize the score. Mobile laboratory LCP remains above the2.5second good threshold and is reported as a limitation.
