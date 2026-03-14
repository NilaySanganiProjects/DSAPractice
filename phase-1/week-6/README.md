# Phase 1 — Week 6: Binary Search

## Theme
**"Binary search is not just for sorted arrays. It is a way of eliminating half your search space in one move — anywhere that half can be safely discarded."**

---

## Real-World Context

**PostgreSQL B-tree index lookup:** When you run `SELECT * FROM users WHERE id = 42`, PostgreSQL does not scan every row. It traverses a B-tree index — which is essentially a multi-level binary search on disk blocks. Binary search is at the heart of every database index lookup. Your Day 1 problem is the pure form.

**CDN cache expiry:** A CDN (like Cloudflare or Fastly) uses binary search to find the first expired cache entry in a time-sorted log of cache insertions. Instead of scanning from the start, it binary searches the sorted timestamp array. Day 3 is this pattern.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Binary Search (LC 704) | Classic binary search | Easy |
| 2 | Search a 2D Matrix (LC 74) | Flattened binary search | Medium |
| 3 | Find Minimum in Rotated Sorted Array (LC 153) | Binary search on rotated array | Medium |
| 4 | Search in Rotated Sorted Array (LC 33) | Binary search with pivot | Medium |
| 5 | Koko Eating Bananas (LC 875) | Binary search on answer space | Medium |

---

## Day 1 — Binary Search

### Problem Statement

Given an array of integers `nums` sorted in ascending order, and an integer `target`, write a function to search for `target` in `nums`. If it exists, return its index. Otherwise, return `-1`.

```
Input:  nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

```
Input:  nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

**Your task:** Create `phase-1/week-6/day1_binary_search.py`.

**Do not use any built-in search methods.** Implement the loop yourself.

**Critical question:** When do you use `mid = (left + right) // 2` vs `mid = left + (right - left) // 2`? When does it matter?

---

## Day 2 — Search a 2D Matrix

### Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if it is in the matrix, or `false` otherwise.

```
Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Your task:** Create `phase-1/week-6/day2_search_2d_matrix.py`.

**AXIOM will ask:** Can you treat the entire matrix as a single sorted array? What is the formula to convert a flat index to a `(row, col)` position?

---

## Day 3 — Find Minimum in Rotated Sorted Array

### Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between 1 and n times. Given the rotated array `nums` of unique elements, return the minimum element.

```
Input:  nums = [3,4,5,1,2]
Output: 1
```

```
Input:  nums = [4,5,6,7,0,1,2]
Output: 0
```

**Your task:** Create `phase-1/week-6/day3_min_rotated.py`.

**AXIOM question:** The array is not sorted end-to-end. Yet you must use O(log n). How do you know which half to discard when you cannot compare `nums[mid]` to a target?

---

## Day 4 — Search in Rotated Sorted Array

### Problem Statement

Given the rotated array `nums` and an integer `target`, return the index of `target` if it is in the array, or `-1` if it is not.

```
Input:  nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

```
Input:  nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Your task:** Create `phase-1/week-6/day4_search_rotated.py`.

**This builds on Day 3.** In any window `[left, right]`, one half is always sorted. Determine which half is sorted, check if `target` falls in it, and discard accordingly.

---

## Day 5 — Koko Eating Bananas

### Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas; the `i`th pile has `piles[i]` bananas. Koko can eat at most `k` bananas per hour. She wants to eat all the bananas before the guards return in `h` hours. Return the minimum integer `k` such that she can eat all bananas within `h` hours.

```
Input:  piles = [3,6,7,11], h = 8
Output: 4
```

**Your task:** Create `phase-1/week-6/day5_koko_bananas.py`.

**This is a "binary search on the answer" problem.** You are not searching in an array — you are searching in the *space of possible values of k*. The insight: for any candidate `k`, you can check feasibility in O(n). The feasibility function is monotonic (if `k` works, `k+1` also works). Binary search the answer.

---

## Week 6 Wrap-Up

Update `/dsa-journal/WEEK_6_REPORT.md`.

### Complexity Quiz

| Problem | Your Time | Your Space | Optimal Time | Optimal Space |
|---------|-----------|------------|--------------|---------------|
| Binary Search | | | O(log n) | O(1) |
| Search 2D Matrix | | | O(log(m·n)) | O(1) |
| Min in Rotated | | | O(log n) | O(1) |
| Search Rotated | | | O(log n) | O(1) |
| Koko Bananas | | | O(n log m) | O(1) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
