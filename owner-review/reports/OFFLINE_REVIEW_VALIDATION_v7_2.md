# Offline owner-review validation — v7.2 corrected

Served review result: PASS. All seven checks passed for the final HTML.

- All 23 review sections and visible coverage rows exist.
- All 121 local media/report references returned HTTP 200.
- Both MP4s expose playable browser metadata: desktop 1440×1000, 132.836 seconds; mobile 390×900, 107.378 seconds. Both reached readyState 4 without media errors.
- The review reflows at 390 and 1440 pixels, has one full-name H1, and loads the hero/brand images.
- Release HOLD and unresolved provenance items remain visible.
- No browser errors or external network requests were recorded.

The first check found a review-only overflow in the unbroken publication-status label at 390 pixels. That label now wraps; the final seven-check run passed. The original failed report is preserved separately.

Direct `file://` validation: HOLD. This cloud browser returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` for the local HTML URL. This is not represented as a local-file PASS. The complete review was tested through a local HTTP server, including both videos. No public server, tunnel or website publication was created by this validation. If a local browser applies the same file restriction, serve the extracted review folder through a local HTTP server.

Final HTML SHA-256: `00101d156b04890f8d8b0bb398b2098e4f049af3b812e5ce9d3bd6370f1cece5`.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL

The longer internal member-manifest filename also required link wrapping at 390 pixels. This review-only issue was fixed and the final seven-check run passed; the failed run is retained in qa/offline-review-long-manifest-link-failure.json.
