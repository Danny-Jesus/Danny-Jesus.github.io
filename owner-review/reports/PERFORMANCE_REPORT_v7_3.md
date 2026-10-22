# Fresh v7.3 performance results

Result: MEASURED

Laboratory Lighthouse measurements of the current production build. Mobile uses Lighthouse simulated mobile throttling; desktop uses 40 ms RTT, 10240 Kbps throughput and CPU slowdown 1. Chromium runs in a cloud environment. These are not field Core Web Vitals or physical-device measurements.

| Profile | Performance | LCP | TBT | CLS | FCP | Speed index |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 93 | 3.235 s | 0.0 ms | 0 | 1.360 s | 1.360 s |
| desktop | 100 | 0.687 s | 0.0 ms | 0 | 0.367 s | 0.367 s |

INP was not measured; TBT is the available laboratory responsiveness metric. Scores and timings are fresh, not reused from v7.2.

| Profile | Transfer bytes | Image bytes | Script bytes | Font bytes | WebGL runtime requests | Video requests |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 578190 | 337321 | 101701 | 122088 | 0 | 0 |
| desktop | 1596765 | 1355896 | 101701 | 122088 | 0 | 0 |

Raw Lighthouse HTML and JSON reports are included in performance/. Responsive photography, native lazy loading and font loading are represented in the actual resource records. Review MP4s are separate owner evidence, not website background video.

Opportunities and run warnings:
- mobile: {"warnings":[],"opportunities":[{"id":"unused-javascript","title":"Reduce unused JavaScript","value":"Est savings of 42 KiB"}]}
- desktop: {"warnings":[],"opportunities":[{"id":"unused-javascript","title":"Reduce unused JavaScript","value":"Est savings of 42 KiB"}]}

Production manifest fingerprint: 75421fdc47040eb2993a5f0f95e40088dfd88edfe752ea0010693e4074eeea98

Both requested profiles completed.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
