# Phase 3 — Months 5–6: Elite Engineering Under Pressure

## Overview

Phase 3 is where you stop being a student and start being an engineer. The problems are harder, the projects are production-level, and AXIOM shifts into Simulator Mode for 3 mock interviews per week. By the end of Month 6, you solve hard LC problems in under 35 minutes with optimal complexity.

---

## DSA Domains Covered

| Week | Domain | Real-World Context |
|------|--------|-------------------|
| 17 | Heaps | Priority queues in task schedulers, k-way merge in databases |
| 18 | Tries | Autocomplete (revisited at depth), IP routing (longest prefix match) |
| 19 | **Industrial Project 5** | Real-time leaderboard system |
| 20 | Segment Trees & Monotonic Stack/Queue | Range queries in databases, stock span problems |
| 21 | Backtracking | Constraint solvers, game AI, permutation generation |
| 22 | Bit Manipulation | Flags, masks, XOR tricks, low-level system code |
| 23 | **Industrial Project 6 (Capstone)** | Mini distributed task scheduler |
| 24 | Final mock interview week + portfolio polish | All domains |

---

## Simulator Mode Protocol (Weeks 19–24)

Starting Week 19, every session includes at least one **SIMULATOR MODE** interview. The schedule:

| Days | Activity |
|------|---------|
| Mon, Wed, Fri | Full mock interview (45 minutes, simulated FAANG format) |
| Tue, Thu | DSA drill + project milestone |
| Sat | Weekly debrief + pattern audit |
| Sun | Rest or catch-up |

Mock interviews are recorded in `/dsa-journal/` as `MOCK_INTERVIEW_WNN_DN.md` files.

---

## Industrial Projects in This Phase

### Project 5 — Real-time Leaderboard System
**Location:** [`projects/leaderboard-system/`](./projects/leaderboard-system/)
**Week:** Month 5, Week 19
**Real company inspiration:** Codeforces, Steam, gaming platforms, Duolingo
**DSA used:** Fenwick Tree (Binary Indexed Tree) for O(log n) rank queries + score updates

### Project 6 — Mini Distributed Task Scheduler (Capstone)
**Location:** [`projects/task-scheduler/`](./projects/task-scheduler/)
**Week:** Month 6, Week 23
**Real company inspiration:** Celery (Python), BullMQ (Node.js), Apache Airflow
**DSA used:** Binary heap (priority), adjacency list (dependencies), topological sort (execution order), retry logic

---

## Phase 3 Completion Checklist

- [ ] Week 17: Heaps — 5 problems solved
- [ ] Week 18: Tries — 5 problems solved
- [ ] Week 19: Industrial Project 5 complete with benchmark
- [ ] Week 20: Segment Trees + Monotonic Stack — 5 problems solved
- [ ] Week 21: Backtracking — 5 problems solved
- [ ] Week 22: Bit Manipulation — 5 problems solved
- [ ] Week 23: Industrial Project 6 (Capstone) complete
- [ ] Week 24: 3 mock interviews, all scored Hire or Strong Hire
- [ ] All 8 WEEK_N_REPORT.md files generated
- [ ] Both project READMEs written and portfolio-ready
- [ ] Hard LC problem cold-solved in under 35 minutes
