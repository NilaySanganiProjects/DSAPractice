# Phase 1 — Week 1: Arrays & Strings

## Theme
**"Before you write code, know why it matters."**

Arrays are the foundation of almost every data structure. Strings are arrays of characters. This week you will internalize 3 fundamental patterns that sit on top of array syntax.

---

## Real-World Context

**Instagram feed deduplication:** When your Instagram feed loads, the backend fetches posts from multiple sources (people you follow, ads, suggested content). Posts can appear from more than one source. Instagram uses a pointer-based scan on a sorted array of post IDs to deduplicate in O(n) — not O(n²). You will implement this pattern on Day 3.

**Splunk log parsing:** Splunk ingests millions of log lines per second. Its tokenizer uses index-based string scanning — essentially array manipulation — to extract fields without copying strings. You will work with a simplified version on Day 5.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Two Sum (LC 1) | Hashmap lookup | Easy |
| 2 | Best Time to Buy and Sell Stock (LC 121) | Single-pass array scan | Easy |
| 3 | Remove Duplicates from Sorted Array (LC 26) | Two pointers (in-place) | Easy |
| 4 | Valid Anagram (LC 242) | Character frequency map | Easy |
| 5 | Longest Common Prefix (LC 14) | Vertical string scanning | Easy |

---

## Day 1 — Two Sum

### Problem Statement (ADVERSARY MODE)

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. You may assume exactly one solution exists. You may not use the same element twice.

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

```
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Constraints:**
- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- Only one valid answer exists.

**Your task:** Solve this in your preferred language. Create a file `phase-1/week-1/day1_two_sum.py` (or `.js`, `.java`, etc.) and write your solution there.

**Before you start, ask yourself:**
- What is the brute-force approach? What is its time complexity?
- Can you do better than O(n²)?
- What data structure lets you look up a value in O(1)?

**After you solve it, AXIOM will:**
1. Ask you to state the time and space complexity of your solution.
2. Ask you what happens if `nums = []` or `nums = [3, 3]` and `target = 6`.
3. Dissect your code line by line.

---

## Day 2 — Best Time to Buy and Sell Stock

### Problem Statement (ADVERSARY MODE)

You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`. You want to maximize your profit by choosing a single day to buy and a single day to sell. Return the maximum profit. If no profit is possible, return 0.

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5  (buy on day 2 at price 1, sell on day 5 at price 6)
```

```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0  (prices only decrease, no profitable transaction)
```

**Your task:** Create `phase-1/week-1/day2_stock_profit.py` and write your solution.

**Before you start, ask yourself:**
- What makes this different from finding the maximum element in an array?
- You must buy *before* you sell. How does that constrain your approach?

---

## Day 3 — Remove Duplicates from Sorted Array

### Problem Statement (ADVERSARY MODE)

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. Return the number of unique elements `k`. The first `k` elements of `nums` must contain the unique elements in the order they were originally present.

```
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
```

```
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```

**Your task:** Create `phase-1/week-1/day3_remove_duplicates.py` and write your solution.

**Constraint:** You must do this in-place — O(1) extra space.

**Real-world connection:** This is the Instagram deduplication move. When you solve it, look back at the real-world context at the top of this file. The pattern is identical.

---

## Day 4 — Valid Anagram

### Problem Statement (ADVERSARY MODE)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word formed by rearranging the letters of a different word using all the original letters exactly once.

```
Input:  s = "anagram", t = "nagaram"
Output: true
```

```
Input:  s = "rat", t = "car"
Output: false
```

**Your task:** Create `phase-1/week-1/day4_valid_anagram.py` and write your solution.

**Edge cases to consider:** What if `len(s) != len(t)`? What if both are empty strings?

---

## Day 5 — Longest Common Prefix

### Problem Statement (ADVERSARY MODE)

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

```
Input:  strs = ["flower", "flow", "flight"]
Output: "fl"
```

```
Input:  strs = ["dog", "racecar", "car"]
Output: ""
```

**Your task:** Create `phase-1/week-1/day5_longest_common_prefix.py` and write your solution.

**Edge cases to consider:** What if `strs = []`? What if `strs = ["a"]`? What if all strings are identical?

---

## Week 1 Wrap-Up

After completing all 5 problems:

1. Open `/dsa-journal/WEEK_1_REPORT.md` and fill in the **Problems Solved** section.
2. Answer the Complexity Quiz at the bottom of this file.
3. AXIOM runs a Pattern Audit and updates your weak-pattern score.

### Complexity Quiz (fill in before proceeding to Week 2)

| Problem | Your Time Complexity | Your Space Complexity | Optimal Time | Optimal Space |
|---------|---------------------|----------------------|--------------|---------------|
| Two Sum | | | O(n) | O(n) |
| Stock Profit | | | O(n) | O(1) |
| Remove Duplicates | | | O(n) | O(1) |
| Valid Anagram | | | O(n) | O(n) |
| Longest Common Prefix | | | O(n·m) | O(1) |

Fill in the "Your" columns. If they don't match the "Optimal" columns, that is your drill for next session.

---

## Notes & Observations

> (Use this space during and after sessions — paste AXIOM's Socratic questions, your "aha" moments, mistakes you made, etc.)
