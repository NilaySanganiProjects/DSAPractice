# Phase 3 — Week 17: Heaps

## Theme
**"A heap is not a sorted array. It is a partial-order structure that answers one question in O(log n): 'What is the minimum (or maximum) right now?'"**

---

## Real-World Context

**Task schedulers (priority queues):** Operating system schedulers use a min-heap to always run the highest-priority process next. Python's `asyncio` event loop uses a min-heap to schedule coroutines by their scheduled wakeup time.

**K-way merge in databases:** When a database merges k sorted runs during a sort-merge join (external sort), it uses a min-heap of size k to always take the smallest element across all runs in O(log k) per step.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Kth Largest Element in a Stream (LC 703) | Min-heap of size k | Easy |
| 2 | K Closest Points to Origin (LC 973) | Max-heap of size k | Medium |
| 3 | Task Scheduler (LC 621) | Greedy + max-heap | Medium |
| 4 | Find Median from Data Stream (LC 295) | Two heaps (max + min) | Hard |
| 5 | Merge K Sorted Lists (LC 23) | Min-heap k-way merge | Hard |

---

## Day 1 — Kth Largest Element in a Stream

### Problem Statement

Design a class to find the kth largest element in a stream. Note that it is the kth largest in sorted order, not the kth distinct element. Implement `KthLargest(k, nums)` and `add(val)`.

```
KthLargest(3, [4,5,8,2])
add(3)  → 4
add(5)  → 5
add(10) → 8
add(9)  → 8
add(4)  → 8
```

**Your task:** Create `phase-3/week-17/day1_kth_largest_stream.py`.

**Key insight:** Maintain a min-heap of size k. The top of the heap is the kth largest element. Why does a *min*-heap give you the kth *largest*?

---

## Day 4 — Find Median from Data Stream (Two Heaps)

### Problem Statement

Design a data structure that supports `addNum(num)` and `findMedian()`. `findMedian` returns the median of all elements added so far.

**Your task:** Create `phase-3/week-17/day4_median_stream.py`.

**This is the canonical two-heap problem.** Maintain two heaps:
- `lower_half`: max-heap of the smaller half
- `upper_half`: min-heap of the larger half

After each insert, balance the heaps so `|len(lower) - len(upper)| <= 1`. The median is either the top of the larger heap or the average of both tops.

**AXIOM question:** Why two heaps and not one? What would break with a single sorted structure?

---

## Days 2, 3, 5

**Your task:** Create `phase-3/week-17/day{N}_{name}.py` for each remaining problem.

---

## Week 17 Wrap-Up

Update `/dsa-journal/WEEK_17_REPORT.md`.

---

## Notes & Observations

> (Paste AXIOM feedback here.)
