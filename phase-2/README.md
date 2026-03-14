# Phase 2 — Months 3–4: Thinking in Graphs and Trees

## Overview

Phase 1 taught you patterns on flat data (arrays, strings). Phase 2 teaches you to think in *connected* data — trees, graphs, and sequences with dependencies. This is where most engineers hit a wall. AXIOM will make you comfortable with recursive and iterative traversal, topological ordering, shortest paths, and the full spectrum of dynamic programming.

---

## DSA Domains Covered

| Week | Domain | Real-World Context |
|------|--------|-------------------|
| 9 | Linked Lists | Browser history (doubly linked list), undo/redo systems |
| 10 | Stacks & Queues | Call stack simulation, BFS queue, monotonic stack in parsers |
| 11 | Trees — BFS/DFS | File system traversal, DOM manipulation, org chart search |
| 12 | **Industrial Project 3** | Dependency resolver (npm-style) |
| 13 | Graphs — Dijkstra, Union-Find | Maps/GPS routing, social network components |
| 14 | Graphs — Topological Sort, Cycle Detection | Build systems, task scheduling |
| 15 | Dynamic Programming (1D → 2D → interval) | Text diff algorithms, optimal pricing |
| 16 | **Industrial Project 4** | Route optimizer microservice |

---

## Learning Philosophy for This Phase

**Every DP problem starts with pure recursion.** You will write the naive recursive solution first — no memoization, no table. Then AXIOM draws the call tree in ASCII to show you which subproblems are being recomputed. Only after you see the redundancy with your own eyes do we add memoization. Tabulation comes last.

This is not inefficiency — it is how you build the intuition that makes DP problems feel obvious rather than magical.

---

## Industrial Projects in This Phase

### Project 3 — Dependency Resolver
**Location:** [`projects/dependency-resolver/`](./projects/dependency-resolver/)
**Week:** Month 3, Week 12
**Real company inspiration:** npm, pip, Cargo (Rust's package manager)
**DSA used:** Graph representation + Topological Sort (Kahn's algorithm) + Cycle detection (DFS with coloring)

### Project 4 — Route Optimizer Microservice
**Location:** [`projects/route-optimizer/`](./projects/route-optimizer/)
**Week:** Month 4, Week 16
**Real company inspiration:** Google Maps, Uber routing, DoorDash delivery optimization
**DSA used:** Dijkstra's algorithm + A* heuristic search + Graph adjacency list

---

## Phase 2 Completion Checklist

- [ ] Week 9: Linked Lists — 5 problems solved
- [ ] Week 10: Stacks & Queues — 5 problems solved
- [ ] Week 11: Trees (BFS/DFS) — 5 problems solved
- [ ] Week 12: Industrial Project 3 complete with benchmark
- [ ] Week 13: Graphs (Dijkstra, Union-Find) — 5 problems solved
- [ ] Week 14: Topological Sort, Cycle Detection — 5 problems solved
- [ ] Week 15: Dynamic Programming — 5 problems solved
- [ ] Week 16: Industrial Project 4 complete with benchmark
- [ ] All weekly WEEK_N_REPORT.md files generated
- [ ] Both project READMEs written and portfolio-ready
