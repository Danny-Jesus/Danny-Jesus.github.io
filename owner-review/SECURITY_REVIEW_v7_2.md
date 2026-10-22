# Security and release hygiene — v7.2 corrected

Scoped static and final package-hygiene result: PASS. The final Source ZIP was inspected independently for known private-file exclusion, member safety and configuration. This is not a comprehensive security or rights certification.

- Fresh npm audit completed successfully: 0 reported vulnerabilities ({'info': 0, 'low': 0, 'moderate': 0, 'high': 0, 'critical': 0, 'total': 0}). Raw response npm-audit-v72.json and stderr preserved. No dependencies were updated by this audit.
- Limited secret-pattern scan: 185 source/config/documentation text files; 0 findings, 0 sensitive filename candidates. Values are never printed. Patterns cover private-key blocks, common GitHub tokens, AWS access-key IDs and OpenAI-style keys; this cannot establish absence of all secrets.
- Public source maps: 0. Remote active script URLs: 0. Active HTTP/javascript URLs: 0. Unsafe blank-target links: 0.
- Known E-class certificate remains in original/working source, never in public or dist; exact byte-match exposure count: 0. Required source-package exclusion path: `assets-originals/photo-library/Photos/Comm Training/Certificat.png`. Final Source ZIP exclusion is PASS by exact member name and exhaustive member-hash search, including renamed copies. Retired portrait originals, build caches, node_modules, environment/key filename candidates and unsafe archive members are absent.
- Public PDF remains byte-identical to admitted source. Fresh extracted-text review found a one-page public professional summary, no private contact data, certificate serials, API credentials or proprietary PETRA implementation detail. Embedded metadata and legal rights are outside that text review.
- Public PETRA text describes research/review controls and holds unresolved gates; no private datasets, implementation modules or measured certification artifacts are linked by the active public routes. This is a scoped content inspection.
- Dependency declarations and locked resolution graph are unchanged from the validated v7.1 Source package: True / True. Candidate version metadata is now 7.2.0; test:* script entries point at the current QA runners. Raw package/lock hashes consequently differ; only top-level lock version and packages[''].version are ignored for the resolution comparison. Existing deploy workflow unchanged: True. Release metadata retains HOLD/public_upload_authorized=false/release_owner_approved=false.
- Audit performed no push, merge, release, deployment, Pages configuration change or remote mutation.

- Final Source ZIP: Daniel_Ashagrie_Ayele_Portfolio_FINAL_Cinematic_v7_2_CORRECTED_Source.zip (217134600 bytes; 562 members), SHA-256 `67155df4b3e0b8473b533c49ea58dfe9b6e862fc9063e744da2dd2a51b77d0fb`. All member hashes/CRC and editable configuration/portable QA files verified. Its 184 packaged text files have 0 limited secret-pattern findings.
- Final Production ZIP: SHA-256 `d6e8bdf2e91c3527fbd0f2ec938d4a95c66c2875af6fcde74a2ff7e2ba8f4a28`. All 318 members match the final reviewed static production manifest exactly. The separately recorded fresh-source extraction, locked npm ci and build reproduce those 318 members byte-for-byte.

Evidence: static-audit-v72.json, FINAL_PACKAGE_HYGIENE_v7_2.json and SOURCE_REPRODUCIBILITY_v7_2.json. Owner visual approval and provenance decisions remain required.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
