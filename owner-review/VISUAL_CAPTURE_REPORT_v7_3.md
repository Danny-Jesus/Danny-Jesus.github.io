# Fresh v7.3 visual evidence capture

Result: PASS

Current production index SHA-256: `7d7920ba85cecaad2edfc3c7abc4f453e1233946e4bb4a893f1ce8654f5869e8`

Production member-manifest fingerprint: `75421fdc47040eb2993a5f0f95e40088dfd88edfe752ea0010693e4074eeea98`

Final font SHA-256: `d4635232acf2d656f82b9ed06f20167dfff389031d718943022ce7016a36e722`

Captured 2026-10-22T11:41:26.279Z to 2026-10-22T11:44:15.603Z. Browser: 154.0.8037.57.

## Still evidence

52 original browser PNG captures: desktop and mobile hero, two approved-logo header lockups, two full homepage images, and all 20 engineering/people articles plus both research programs and the credentials/about/contact close at both widths. Two additional contact sheets reproduce every source row of each full homepage screenshot in sequential, nonoverlapping tiles. All 15 specifically required visual outputs are present and independently hashed in required-visuals-check-v73.json.

Desktop viewport: 1440×1000. Mobile viewport: 390×900. Still captures use reduced-motion mode, establishing the actual static composition without effects. Hero and full-page captures retain normal navigation. Individual element captures temporarily hide only the fixed navigation so it cannot obscure the clipped article; source markup, imagery, text and layout are unchanged.

Full homepage source heights: 12588 desktop and 14803 mobile pixels. Contact-sheet-proof-v73.json records all source row intervals.

## Continuous browser recordings

Both recordings show actual native browser scrolling through the entire page. The harness drives scrollTo through requestAnimationFrame at a repeatable review pace. This does not add scroll hijacking to the website. Original CDP JPEG frames and actual timestamps are encoded into H264 variable-frame-rate MP4s. No simulated interface or generated footage is used.

| Recording | Dimensions | Duration | Decoded frames | Bytes | Full decode |
|---|---:|---:|---:|---:|---|
| videos/FINAL_SCROLL_REVIEW_DESKTOP_V73.mp4 | 1440×1000 | 52.520 s | 1424 | 18463630 | PASS |
| videos/FINAL_SCROLL_REVIEW_MOBILE_V73.mp4 | 390×900 | 60.547 s | 1689 | 10064728 | PASS |

Both outputs are H264, yuv420p, TV limited range, fast-start MP4. ffprobe counted every encoded frame. Full ffmpeg decoding completed with exit 0 and no errors. Encoded/captured durations are compared directly in video-validation-v73.json. The one extra encoded frame is the repeated final frame needed to close the concat demuxer timestamp.

No page exceptions, console errors/warnings, HTTP failures or failed asset requests occurred. The complete production member fingerprint remained identical throughout capture.

## Scope and superseded evidence

The first capture was stopped after a separate pixel-based contrast check identified insufficient desktop hero text/background contrast; it is preserved under ../review-attempt1 and excluded from final review. A later complete capture predates the final lossless font subset and is preserved under ../review-pre-font, with raw frames at ../capture-frames-final-pre-font. All final images and both recordings were captured afresh against the final font asset and production member manifest above.

This is headless Chromium cloud evidence, not physical-device testing or owner visual approval. Final raw browser frames and timestamps remain at /workspace/v73-premium-review/capture-frames-final and are excluded from the compact owner-review package. Capture proof, contact-sheet mapping and complete video decode results are included.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL

NO PUSH. NO MERGE. NO RELEASE. NO DEPLOYMENT.
