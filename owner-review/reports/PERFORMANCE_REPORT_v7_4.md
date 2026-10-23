# Fresh v7.4 performance results

Result: PASS

Target: desktop performance >=95 and mobile >=90. Actual target result: PASS.

Laboratory Lighthouse measurements of the current production build. Mobile uses Lighthouse simulated mobile throttling; desktop uses 40 ms RTT, 10240 Kbps throughput and CPU slowdown 1. Chromium runs in a cloud environment. These are not field Core Web Vitals or physical-device measurements.

| Profile | Performance | LCP | TBT | CLS | FCP | Speed index |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 91 | 3.457 s | 8.5 ms | 0 | 1.507 s | 1.507 s |
| desktop | 100 | 0.723 s | 0.0 ms | 0 | 0.386 s | 0.386 s |

INP was not measured; TBT is the available laboratory responsiveness metric. Scores and timings are fresh, not reused from earlier versions.

| Profile | Transfer bytes | Image bytes | Script bytes | Font bytes | WebGL runtime requests | Video requests |
|---|---:|---:|---:|---:|---:|---:|
| mobile | 633924 | 373588 | 107405 | 122088 | 0 | 0 |
| desktop | 981811 | 721475 | 107405 | 122088 | 0 | 0 |

Raw Lighthouse HTML and JSON reports are included in performance/. Responsive photography, native lazy loading and font loading are represented in the actual resource records. Review MP4s are separate owner evidence, not website background video.

Opportunities and run warnings:
- mobile: {"warnings":[],"opportunities":[{"id":"unused-javascript","title":"Reduce unused JavaScript","value":"Est savings of 41 KiB"}]}
- desktop: {"warnings":[],"opportunities":[{"id":"unused-css-rules","title":"Reduce unused CSS","value":"Est savings of 12 KiB"},{"id":"unused-javascript","title":"Reduce unused JavaScript","value":"Est savings of 41 KiB"}]}

Production manifest fingerprint: bd6ecdde31ef8c7ea708bcfd8ee599c5f13584085c7b9d6f42e52b8c0a4b5bf8

Both requested profiles completed. Target status: PASS.

PUBLICATION: HOLD_PENDING_OWNER_VISUAL_APPROVAL
