# Phase 2 — Week 14: Topological Sort & Cycle Detection

## Theme
**"Topological sort answers one question: in what order can I do these things if some must come before others?"**

---

## Real-World Context

**npm/pip install order:** When you run `npm install`, the package manager builds a dependency graph and runs topological sort to determine which packages must be installed first. If the graph has a cycle (Package A requires B, B requires A), it reports a conflict. This is exactly Industrial Project 3 (this week's project milestone builds on it).

**Build systems (Make, Bazel):** A `Makefile` is a dependency graph. `make` runs topological sort to figure out what to compile in what order, skipping files that haven't changed.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Course Schedule (LC 207) | Cycle detection in directed graph | Medium |
| 2 | Course Schedule II (LC 210) | Topological sort (Kahn's algorithm) | Medium |
| 3 | Alien Dictionary (LC 269) | Topological sort from constraints | Hard |
| 4 | Sequence Reconstruction (LC 444) | Topological sort uniqueness check | Medium |
| 5 | Minimum Height Trees (LC 310) | Leaf trimming / topological intuition | Medium |

---

## Day 1 — Course Schedule (Cycle Detection)

### Problem Statement

There are `numCourses` courses labeled 0 to `numCourses-1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` means you must take course `b` before course `a`. Return `true` if you can finish all courses, otherwise return `false`.

**Your task:** Create `phase-2/week-14/day1_course_schedule.py`.

**Two approaches:**
1. DFS with 3-color marking: white (unvisited), gray (in current DFS path), black (done). A gray→gray edge means cycle.
2. Kahn's BFS: track in-degrees, process nodes with in-degree 0. If all nodes are processed, no cycle.

Try both. AXIOM will ask you to compare them.

---

## Days 2–5

**Your task:** Create `phase-2/week-14/day{N}_{name}.py` for each remaining problem.

---

## Week 14 Wrap-Up

Update `/dsa-journal/WEEK_14_REPORT.md`.

---

## Notes & Observations

> (Paste AXIOM feedback here.)
