# Newsreader safe optimization candidates

Recommended candidate: `newsreader-exact-fullaxes-english.woff2`. It is 96852 bytes, compared with 197,144 bytes for the current public font (50.9% smaller). It keeps the complete original weight 200–800 and optical-size 6–72 axes. It removes unused glyph coverage while retaining ASCII printable characters, all supported characters extracted from the current production HTML routes, and smart quotation marks, dashes, bullet, ellipsis, copyright, registered and trademark characters.

At weights 400 and 420 and optical sizes 24, 48 and 72, every retained glyph has exactly equal decomposed outline coordinates and advance widths compared with the current public font: maximum difference **0.0 font units**. The comparison includes unmapped alternates and ligatures through the saved glyph-index mapping.

The complete extracted route text (64090 characters) was also shaped with HarfBuzz at all six locations. Glyph identities, clusters, x/y advances and x/y offsets match exactly. See `report-exact-english.json`.

SHA-256: `d4635232acf2d656f82b9ed06f20167dfff389031d718943022ce7016a36e722`

The broader Latin-1 candidate is approximately 131 KB and passes the same checks.

## Rejected approach

Restricting the weight axis to 400–420 with fontTools instancer produced smaller files (~76 KB), but instancing introduced rounding differences up to 1.68 font units in outlines and 0.92 units in advances at weight 420. Those candidates are **not approved as exact replacements**. They remain separate experimental evidence only.

No public font, CSS, source or lockfile was modified by this optimization task. Root should admit the recommended candidate explicitly before replacing the public font and update the typography provenance document to the final admitted SHA. Font subsetting proof tooling uses temporary fontTools/Brotli/uharfbuzz tooling only and does not add app dependencies.
