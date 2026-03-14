# Phase 2 — Week 9: Linked Lists

## Theme
**"A linked list is not a worse array. It is a different contract: O(1) insert/delete at any known position, at the cost of O(n) random access."**

---

## Real-World Context

**Browser history (doubly linked list):** Your browser's back/forward buttons use a doubly linked list. Each page is a node. Forward navigation appends to the end; back navigation moves the current pointer left. Opening a new page while in the middle of history deletes all nodes forward of the current position. Days 1–2 implement parts of this.

**Undo/redo stacks in editors:** VS Code's undo/redo is a doubly linked list of edit operations. When you undo, the pointer moves back. When you make a new edit after undoing, the "redo" chain is discarded — same as the browser example.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Reverse Linked List (LC 206) | Iterative reversal | Easy |
| 2 | Merge Two Sorted Lists (LC 21) | Two-pointer merge | Easy |
| 3 | Linked List Cycle (LC 141) | Floyd's slow/fast pointer | Easy |
| 4 | Find the Duplicate Number (LC 287) | Floyd's cycle detection on implicit graph | Medium |
| 5 | LRU Cache (LC 146) | Hashmap + doubly linked list | Medium |

---

## Day 1 — Reverse Linked List

### Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed list's head.

```
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None
```

**Your task:** Create `phase-2/week-9/day1_reverse_list.py`.

**Two approaches:**
1. Iterative (O(1) space) — preferred
2. Recursive — can you see the recursion? "To reverse a list, reverse the tail, then attach the head at the end."

AXIOM will ask you to implement both and compare their space complexity.

---

## Day 2 — Merge Two Sorted Lists

### Problem Statement

Merge two sorted linked lists and return it as one sorted list.

```
Input:  l1 = 1 → 2 → 4, l2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4
```

**Your task:** Create `phase-2/week-9/day2_merge_sorted_lists.py`.

**Use a dummy head node.** This eliminates the special case for the first node and is a standard interview technique. AXIOM will ask why.

---

## Day 3 — Linked List Cycle Detection

### Problem Statement

Given the head of a linked list, determine if it contains a cycle.

**Your task:** Create `phase-2/week-9/day3_detect_cycle.py`.

**This is Floyd's Tortoise and Hare algorithm.** Use two pointers: a slow pointer that moves 1 step at a time, and a fast pointer that moves 2 steps. If they meet, there is a cycle.

**AXIOM question after you solve it:** Why does the fast pointer catching the slow pointer *prove* a cycle exists? Can you give a mathematical argument (not just intuition)?

---

## Day 4 — Find the Duplicate Number

### Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`, there is exactly one repeated number. Find the duplicate. You must not modify the array, and you must use O(1) extra space.

```
Input:  nums = [1, 3, 4, 2, 2]
Output: 2
```

**Your task:** Create `phase-2/week-9/day4_find_duplicate.py`.

**This is a hidden linked list problem.** Treat `nums[i]` as a pointer: from index `i`, follow the pointer to index `nums[i]`. The duplicate causes a cycle in this implicit linked list. Apply Floyd's algorithm.

---

## Day 5 — LRU Cache

### Problem Statement

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the `LRUCache` class with `get(key)` and `put(key, value)`, both running in O(1) time.

**Your task:** Create `phase-2/week-9/day5_lru_cache.py`.

**Note:** You already designed this for Project 2. This time, implement it from scratch without looking at your previous implementation. Time yourself.

---

## Week 9 Wrap-Up

Update `/dsa-journal/WEEK_9_REPORT.md`.

### Complexity Quiz

| Problem | Your Time | Your Space | Optimal Time | Optimal Space |
|---------|-----------|------------|--------------|---------------|
| Reverse Linked List | | | O(n) | O(1) iterative |
| Merge Sorted Lists | | | O(n+m) | O(1) |
| Cycle Detection | | | O(n) | O(1) |
| Find Duplicate | | | O(n) | O(1) |
| LRU Cache | | | O(1) per op | O(capacity) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
