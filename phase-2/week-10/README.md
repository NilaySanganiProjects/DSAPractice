# Phase 2 — Week 10: Stacks & Queues

## Theme
**"A stack is a reversed-access contract. A queue is a fairness contract. Both sit at the heart of how computers execute code."**

---

## Real-World Context

**Call stack:** Every function call pushes a frame onto the call stack. When a function returns, the frame is popped. Stack overflow literally means your call stack ran out of space. Day 1 simulates this.

**BFS in web crawlers:** Google's crawler uses a queue. It starts with a seed URL, enqueues all links on that page, and processes them in order — breadth-first. Day 3 is this pattern.

**Monotonic stack in parsers:** Expression parsers (for math, CSS, templating languages) use monotonic stacks to evaluate operators in precedence order. Day 5 is this pattern.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Valid Parentheses (LC 20) | Stack for matching pairs | Easy |
| 2 | Min Stack (LC 155) | Stack with O(1) minimum | Medium |
| 3 | Binary Tree Level Order Traversal (LC 102) | BFS with queue | Medium |
| 4 | Daily Temperatures (LC 739) | Monotonic stack | Medium |
| 5 | Largest Rectangle in Histogram (LC 84) | Monotonic stack (hard) | Hard |

---

## Days 1–5

**Your task:** Create `phase-2/week-10/day{N}_{name}.py` for each problem.

See problem statements on LeetCode. In ADVERSARY MODE, AXIOM presents these without solutions.

---

## Week 10 Wrap-Up

Update `/dsa-journal/WEEK_10_REPORT.md`.

### Complexity Quiz

| Problem | Optimal Time | Optimal Space |
|---------|--------------|---------------|
| Valid Parentheses | O(n) | O(n) |
| Min Stack | O(1) per op | O(n) |
| Level Order Traversal | O(n) | O(n) |
| Daily Temperatures | O(n) | O(n) |
| Largest Rectangle | O(n) | O(n) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
