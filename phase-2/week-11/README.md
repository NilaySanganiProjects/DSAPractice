# Phase 2 — Week 11: Trees — BFS & DFS

## Theme
**"Trees are recursive structures. Every subtree is itself a tree. Once you internalize that, tree problems become almost formulaic."**

---

## Real-World Context

**DOM manipulation:** The browser's Document Object Model is a tree. React's virtual DOM diff algorithm uses tree DFS to find changed nodes. Day 2's tree path problem is the same pattern React uses internally.

**File system traversal:** `find /usr -name "*.py"` is a DFS on the directory tree. Day 3 implements this.

**Org chart / hierarchy search:** LinkedIn's "degrees of separation" feature uses BFS on the employee tree. Day 4 is BFS on a tree.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Invert Binary Tree (LC 226) | DFS (recursive) | Easy |
| 2 | Binary Tree Maximum Path Sum (LC 124) | DFS with post-order return | Hard |
| 3 | Lowest Common Ancestor (LC 236) | DFS with backtracking | Medium |
| 4 | Binary Tree Right Side View (LC 199) | BFS level-by-level | Medium |
| 5 | Validate Binary Search Tree (LC 98) | DFS with valid range | Medium |

---

## Days 1–5

**Your task:** Create `phase-2/week-11/day{N}_{name}.py` for each problem.

---

## Week 11 Wrap-Up

Update `/dsa-journal/WEEK_11_REPORT.md`.

---

## Notes & Observations

> (Paste AXIOM feedback here.)
