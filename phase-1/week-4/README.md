# Phase 1 — Week 4: Two Pointers

## Theme
**"Two pointers is not a trick. It is a decision to trade index bookkeeping for better complexity."**

---

## Real-World Context

**Facebook feed deduplication:** Facebook's feed algorithm fetches posts from multiple ranked sources and merges them. When two sorted streams are merged and deduplicated (e.g., two sorted arrays of post IDs), two pointers let you do it in O(n+m) instead of O((n+m) log(n+m)). You implement this merge on Day 3.

**Memory-efficient in-place reversal:** Networking libraries that manipulate byte buffers in-place (e.g., reversing headers) use two-pointer swapping. No extra allocation.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Valid Palindrome (LC 125) | Two pointers, inward scan | Easy |
| 2 | Two Sum II — Input Array Is Sorted (LC 167) | Two pointers on sorted array | Medium |
| 3 | Merge Sorted Array (LC 88) | Two pointers, reverse merge | Easy |
| 4 | 3Sum (LC 15) | Sorted + two pointers | Medium |
| 5 | Container With Most Water (LC 11) | Greedy two pointers | Medium |

---

## Day 1 — Valid Palindrome

### Problem Statement

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

```
Input:  s = "race a car"
Output: false
```

**Your task:** Create `phase-1/week-4/day1_valid_palindrome.py`.

**Before coding:** Draw two pointers on paper — one at index 0, one at index `len(s)-1`. What are the three cases when you advance a pointer?

---

## Day 2 — Two Sum II (Sorted Array)

### Problem Statement

Given a 1-indexed array of integers `numbers` that is sorted in non-decreasing order, find two numbers that add up to a specific target. Return their indices.

```
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Constraint:** You must use O(1) extra space.

**Your task:** Create `phase-1/week-4/day2_two_sum_sorted.py`.

**AXIOM question:** You already solved Two Sum with a hashmap in Week 1. Why can you use O(1) space here but not in Week 1's version? What changed?

---

## Day 3 — Merge Sorted Array

### Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. Merge `nums2` into `nums1` as one sorted array, in-place. `nums1` has length `m + n` where the last `n` elements are 0s.

```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Your task:** Create `phase-1/week-4/day3_merge_sorted.py`.

**Critical insight:** If you merge from the front, you overwrite elements you haven't compared yet. Where should you start merging from?

---

## Day 4 — 3Sum

### Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Your task:** Create `phase-1/week-4/day4_three_sum.py`.

**This is medium-hard.** The trick: fix one element, reduce to two-pointer Two Sum on the rest. But how do you avoid duplicates without using a set?

---

## Day 5 — Container With Most Water

### Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that, together with the x-axis, form a container that holds the most water. Return the maximum amount of water the container can store.

```
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

**Your task:** Create `phase-1/week-4/day5_container_water.py`.

**AXIOM question after you solve it:** The greedy choice here is to always move the pointer at the shorter wall. Why? Can you prove that moving the taller pointer can never increase the answer?

---

## Week 4 Wrap-Up

Update `/dsa-journal/WEEK_4_REPORT.md`. Fill in the Complexity Quiz.

### Complexity Quiz

| Problem | Your Time | Your Space | Optimal Time | Optimal Space |
|---------|-----------|------------|--------------|---------------|
| Valid Palindrome | | | O(n) | O(1) |
| Two Sum II | | | O(n) | O(1) |
| Merge Sorted Array | | | O(n+m) | O(1) |
| 3Sum | | | O(n²) | O(1) |
| Container With Most Water | | | O(n) | O(1) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
