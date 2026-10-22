# Performance report — v7.2 corrected

Fresh Lighthouse 13.5.0 laboratory measurements against the final production build. Other browser suites and build work were stopped during measurement. Chromium uses cloud CPU and software rendering; these are simulated device profiles, not field measurements.

| Profile | Performance | LCP | TBT | CLS | FCP | Speed index |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 95 | 2.933 s | 4.5 ms | 0 | 1.569 s | 1.569 s |
| desktop | 99 | 0.930 s | 0.0 ms | 0 | 0.382 s | 0.642 s |

Both profiles meet the requested practical score target of 90. Mobile LCP is above the 2.5-second good threshold; no field Core Web Vitals or INP pass is claimed. INP was not measured. TBT is the available laboratory responsiveness metric.

## Transfer and startup evidence

| Profile | Total transfer | Image transfer | Script transfer | Font transfer | Initial Three.js runtime requested |
|---|---:|---:|---:|---:|---|
| mobile | 1,365,148 B | 1,157,861 B | 147,948 B | 39,944 B | No |
| desktop | 1,243,383 B | 1,036,096 B | 147,948 B | 39,944 B | No |

The initial two script requests comprise the application and GSAP/ScrollTrigger enhancement. The Three.js runtime remains a separate lazy chunk below the 20 photographic chapters; photographic scenes and hero create no WebGL canvas. Native lazy loading fetches some near-fold photos early, which is reflected in the measured image weight. Responsive cover sizing deliberately retains image detail. Duplicate mask planes reuse the same image URLs.

Self-hosted WOFF2 fonts use swap behavior; Manrope is preloaded. No background video is used by the app, so initial video transfer is zero. The two review MP4s are separate review artifacts and are not app resources.

## Spatial enhancement cost and fallback

Fresh browser checks verified research WebGL initialization at both desktop and mobile, live reduced-motion canvas disposal, forced WebGL failure fallback, and orientation/resize handling. DPR is capped at 1 on mobile and 1.5 on desktop. Rendering stops outside the viewport; unchanged progress skips drawing. All photographic chapters retain their source images without WebGL. Reduced motion and Save-Data keep static planes and full source montages/wide images.

This task did not measure physical GPU energy, field INP, physical-device frame rate or real-network delivery. Native review recording frame cadence is capture evidence, not a hardware performance benchmark.

Lighthouse flags approximately 64 KiB of unused initial JavaScript as an opportunity on both profiles. No dependency upgrades, loss of photographic quality or new generic effects were introduced to improve a score.

Raw HTML and JSON reports are included under `qa/performance/`; exact numeric summaries are in `qa/performance-summary.json`. Scores are fresh and have not been reused from v7.1.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
