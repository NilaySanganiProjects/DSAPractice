# Phase 1 — Months 1–2: The Foundations Are Not What You Think

## Overview

Most people skip foundations because they think they already know arrays and strings. They don't. They know the syntax. AXIOM will teach you the *patterns* that sit on top of the syntax — patterns that appear in production systems at every major company.

---

## DSA Domains Covered

| Week | Domain | Real-World Context |
|------|--------|-------------------|
| 1 | Arrays & Strings | Feed deduplication (Instagram), log parsing (Splunk) |
| 2 | Hashmaps & Sets | Search ranking (Google), rate limiting (Cloudflare) |
| 3 | **Industrial Project 1** | Real-time log anomaly detector |
| 4 | Two Pointers | Feed deduplication (Facebook), memory-efficient search |
| 5 | Sliding Window | Rate limiter (Cloudflare), network packet analysis |
| 6 | Binary Search | Database index lookup (PostgreSQL), CDN cache |
| 7 | **Industrial Project 2** | Search autocomplete engine |
| 8 | Recursion basics + Phase 1 Review | Call stacks, parsing engines |

---

## Learning Philosophy for This Phase

**Before every new concept, AXIOM gives you the real-world context.** You do not learn sliding window in the abstract. You learn it because Cloudflare uses a sliding window counter to rate-limit API requests per IP. You are not learning DSA — you are learning the moves that engineers at real companies make.

**Pattern over problem.** After each problem, AXIOM asks: *What pattern did you just use?* Over time, you start seeing the pattern before you read the full problem statement. That is the goal.

---

## Weak Pattern Tracking

At the end of each week, AXIOM generates a pattern audit in your `/dsa-journal/WEEK_N_REPORT.md`. It flags:
- Patterns you **failed to recognize** before attempting the problem
- Patterns you **recognized but implemented wrong**
- Patterns you **solved correctly** and can now consider internalized

---

## Industrial Projects in This Phase

### Project 1 — Real-time Log Anomaly Detector
**Location:** [`projects/log-anomaly-detector/`](./projects/log-anomaly-detector/)
**Week:** Month 1, Week 3
**Real company inspiration:** Splunk, Datadog, AWS CloudWatch
**DSA used:** Sliding window (error spike detection) + Hashmap (IP frequency tracking)

### Project 2 — Search Autocomplete Engine
**Location:** [`projects/search-autocomplete/`](./projects/search-autocomplete/)
**Week:** Month 2, Week 7
**Real company inspiration:** Google Search, Elasticsearch
**DSA used:** Trie (prefix matching) + LRU Cache (hot-path optimization)

---

## Phase 1 Completion Checklist

- [ ] Week 1: Arrays & Strings — 5 problems solved
- [ ] Week 2: Hashmaps & Sets — 5 problems solved
- [ ] Week 3: Industrial Project 1 complete with benchmark
- [ ] Week 4: Two Pointers — 5 problems solved
- [ ] Week 5: Sliding Window — 5 problems solved
- [ ] Week 6: Binary Search — 5 problems solved
- [ ] Week 7: Industrial Project 2 complete with benchmark
- [ ] Week 8: Recursion + Phase 1 Review — 5 problems solved
- [ ] All 6 WEEK_N_REPORT.md files generated in `/dsa-journal/`
- [ ] Both project READMEs written and portfolio-ready
