# Phase 1 — Week 8: Recursion Basics + Phase 1 Review

## Theme
**"Recursion is not magic. It is a function that trusts a smaller version of itself — and handles exactly one base case."**

---

## Real-World Context

**Parsing engines:** Every programming language parser (Python's `ast` module, JavaScript's V8 parser) uses recursive descent parsing. Each grammar rule is a recursive function. Understanding recursion is essential before you can understand how compilers think.

**File system traversal:** `find`, `ls -R`, and every recursive file search use DFS with recursion. Day 3's problem is this exact problem.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Fibonacci Number (LC 509) | Basic recursion, then memoization | Easy |
| 2 | Power of Two (LC 231) | Recursion + bit insight | Easy |
| 3 | Flatten Nested List Iterator (LC 341) | Recursive flattening | Medium |
| 4 | Phase 1 Pattern Review — Arrays/Hashmaps | Mixed patterns | Medium |
| 5 | Phase 1 Pattern Review — Two Pointers/Sliding Window/Binary Search | Mixed patterns | Medium |

---

## Day 1 — Fibonacci Number

### Problem Statement

Given `n`, calculate `F(n)` — the nth Fibonacci number (F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)).

```
Input:  n = 4
Output: 3
```

**Your task:** Create `phase-1/week-8/day1_fibonacci.py`.

**Do this in three stages:**
1. **Stage 1:** Recursive solution. Write it. State its time and space complexity.
2. **Stage 2:** Add memoization (top-down DP). Measure the difference.
3. **Stage 3:** Bottom-up tabulation. No recursion.

This is your introduction to Dynamic Programming. The full DP curriculum is in Phase 2, but Fibonacci is where the call tree becomes visible.

**After Stage 1, AXIOM will draw the call tree for F(5) in ASCII and show you which subproblems are being recomputed.**

---

## Day 2 — Power of Two

### Problem Statement

Given an integer `n`, return `true` if it is a power of two, and `false` otherwise.

```
Input:  n = 1 → true (2⁰)
Input:  n = 16 → true (2⁴)
Input:  n = 3 → false
```

**Your task:** Create `phase-1/week-8/day2_power_of_two.py`. Solve it recursively first. Then find the O(1) bit manipulation solution.

---

## Day 3 — Flatten Nested List Iterator

### Problem Statement

You are given a nested list of integers `nestedList`. Each element is either an integer or a list of elements. Implement an iterator to flatten it.

```
Input:  [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
```

**Your task:** Create `phase-1/week-8/day3_flatten_nested.py`. Solve using recursion.

---

## Days 4–5 — Phase 1 Review

### Day 4: Mixed Pattern Drill (Arrays + Hashmaps)

Solve two problems from Phase 1 that you got wrong or struggled with. Re-solve them from memory, without looking at your previous solutions. Record your time.

### Day 5: Mixed Pattern Drill (Two Pointers + Sliding Window + Binary Search)

Same drill. Pick one problem from each domain. Time yourself.

**Goal:** By the end of Day 5, you should be able to:
- Identify the pattern from the problem description alone (before coding).
- State the optimal time and space complexity before you start coding.
- Solve an Easy in under 10 minutes, a Medium in under 25 minutes.

---

## Phase 1 Final Self-Assessment

Fill this in honestly before moving to Phase 2:

| Pattern | Can recognize it? | Can implement optimally? | Time to solve a Medium |
|---------|------------------|--------------------------|------------------------|
| Array scan / two pointers | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Hashmap grouping/counting | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Sliding window (fixed) | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Sliding window (variable) | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Binary search (sorted) | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Binary search on answer | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |
| Basic recursion | Yes / No / Sometimes | Yes / No / Sometimes | ___ min |

Any row where you answered "No" or "Sometimes" in the first two columns is a weak pattern. AXIOM will carry this forward into Phase 2's warm-up drills.

---

## Notes & Observations

> (Paste AXIOM feedback here.)
