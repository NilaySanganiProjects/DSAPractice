# Phase 2 — Week 15: Dynamic Programming

## Theme
**"DP is not a magic algorithm. It is a decision: 'I've already solved this subproblem — I'll reuse the answer instead of recomputing it.'"**

---

## The AXIOM DP Protocol

Every DP problem in this week follows this strict 3-stage process:

**Stage 1 — Pure Recursion:** Write the naive recursive solution. No memoization. Get it working. State its exponential time complexity.

**Stage 2 — Memoization (Top-Down):** AXIOM draws the call tree in ASCII. You identify the repeated subproblems. Add a cache (dictionary). Measure the time complexity drop.

**Stage 3 — Tabulation (Bottom-Up):** Convert to an iterative table-filling approach. No recursion. Identify the base cases and the recurrence relation.

Do not skip stages. The insight from Stage 2 is what makes DP intuitive.

---

## Real-World Context

**Text diff algorithms (edit distance):** Git's `diff` command uses edit distance (Levenshtein distance) — a 2D DP problem. The "hunks" in a git diff are the result of traceback through the DP table. Day 3 is this problem.

**Optimal pricing (0/1 Knapsack):** A/B testing platforms use knapsack-style DP to select which features to show within a budget (computation budget, screen space, etc.). Day 5 is this problem.

---

## Weekly Schedule

| Day | Problem | Stage 1 | Stage 2 | Stage 3 |
|-----|---------|---------|---------|---------|
| 1 | Climbing Stairs (LC 70) | Recursion | Memo | Tabulation |
| 2 | Coin Change (LC 322) | Recursion | Memo | Tabulation |
| 3 | Edit Distance (LC 72) | Recursion | Memo | Tabulation |
| 4 | Longest Increasing Subsequence (LC 300) | Recursion | Memo | Tabulation |
| 5 | 0/1 Knapsack (classic) | Recursion | Memo | Tabulation |

---

## Day 1 — Climbing Stairs (Stage-by-Stage)

### Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```
Input:  n = 3
Output: 3  (1+1+1, 1+2, 2+1)
```

**Your task:** Create `phase-2/week-15/day1_climbing_stairs.py`.

**Stage 1:** `ways(n) = ways(n-1) + ways(n-2)`. Write this. Run it for `n=40`. How slow is it?

**Stage 2:** After Stage 1 is working, paste your code and AXIOM draws the call tree for `n=5` in ASCII. You will see `ways(3)` computed twice, `ways(2)` three times. Add memoization.

**Stage 3:** Build the table `dp[0..n]`. Fill left to right. No recursion.

---

## Days 2–5

**Your task:** Create `phase-2/week-15/day{N}_{name}.py` for each problem. Follow all 3 stages.

---

## Week 15 Wrap-Up

Update `/dsa-journal/WEEK_15_REPORT.md`.

### Reflection Questions

After completing all 5 problems, answer these:

1. Can you identify which DP problems are 1D (single array of states) vs 2D (matrix of states) from the problem statement alone?
2. What is the difference between "overlapping subproblems" and "optimal substructure"? Give an example of each.
3. For which of this week's problems did memoization give the most dramatic speedup? Why?

---

## Notes & Observations

> (Paste AXIOM call-tree ASCII art here. Paste your "aha" moments.)
