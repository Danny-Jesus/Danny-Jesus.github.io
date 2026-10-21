# Performance Report

Fresh Lighthouse 13.5.0 mobile and desktop runs against the frozen rebuilt production output. Chromium software-rendered WebGL in a cloud container; simulated throttling and lab evidence, not physical-device or field-user measurements. No prior scores reused.

| Mode | Performance | LCP | CLS | TBT | FCP | Speed index |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 84 | 2.951 s | 0 | 404.5 ms | 1.559 s | 2.391 s |
| desktop | 89 | 1.239 s | 0 | 232.0 ms | 0.370 s | 1.003 s |

Accessibility, best practices, and SEO each scored 100 in both runs. No Lighthouse run warnings. Mobile LCP is above the 2.5 s good threshold; TBT is above 200 ms in both runs. These are recorded performance limitations, not failed measurements. INP is not measured by this lab run; TBT is reported instead.

## Resource evidence

### mobile

Total measured transfer: 691634 bytes. Main thread: 2420.5 ms. JS boot/evaluation: 1663.8 ms.

```json
{
  "Document": {
    "requests": 1,
    "transfer_bytes": 5364,
    "resource_bytes": 30163
  },
  "Font": {
    "requests": 2,
    "transfer_bytes": 39944,
    "resource_bytes": 39544
  },
  "Script": {
    "requests": 3,
    "transfer_bytes": 285221,
    "resource_bytes": 1026238
  },
  "Stylesheet": {
    "requests": 1,
    "transfer_bytes": 9825,
    "resource_bytes": 43114
  },
  "Image": {
    "requests": 7,
    "transfer_bytes": 345479,
    "resource_bytes": 344078
  },
  "Manifest": {
    "requests": 1,
    "transfer_bytes": 639,
    "resource_bytes": 426
  },
  "Other": {
    "requests": 1,
    "transfer_bytes": 5162,
    "resource_bytes": 4961
  }
}
```

### desktop

Total measured transfer: 1802402 bytes. Main thread: 954.3 ms. JS boot/evaluation: 788.9 ms.

```json
{
  "Document": {
    "requests": 1,
    "transfer_bytes": 5364,
    "resource_bytes": 30163
  },
  "Font": {
    "requests": 2,
    "transfer_bytes": 39944,
    "resource_bytes": 39544
  },
  "Script": {
    "requests": 3,
    "transfer_bytes": 285221,
    "resource_bytes": 1026238
  },
  "Stylesheet": {
    "requests": 1,
    "transfer_bytes": 9825,
    "resource_bytes": 43114
  },
  "Image": {
    "requests": 6,
    "transfer_bytes": 1456247,
    "resource_bytes": 1455042
  },
  "Manifest": {
    "requests": 1,
    "transfer_bytes": 639,
    "resource_bytes": 426
  },
  "Other": {
    "requests": 1,
    "transfer_bytes": 5162,
    "resource_bytes": 4961
  }
}
```

Fonts are self-hosted with font-display:swap. Native lazy loading was exercised separately: a below-fold image went from unloaded to decoded after scrolling. There are no active homepage video elements, so video-network playback is not applicable. Review MP4s are owner-review artifacts, not site payload.

Three.js is lazy-loaded and demand-rendered. Real WebGL initialization and CSS fallbacks are verified separately. Its isolated GPU time cannot be established from Lighthouse aggregate main-thread measurements on software rendering. DPR is capped by the existing runtime.

Lighthouse suggests about 100 KiB of unused JavaScript savings. No framework/dependency upgrade or removal of cinematic scenes was made to chase a score. Raw mobile/desktop HTML and JSON reports are included under performance/.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
