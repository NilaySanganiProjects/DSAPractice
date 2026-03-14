# Phase 1 — Week 5: Sliding Window

## Theme
**"A sliding window is a fixed or variable-size subarray that moves through a larger array, avoiding redundant recomputation."**

---

## Real-World Context

**Cloudflare rate limiting:** Cloudflare tracks requests per IP in a sliding time window. The window slides forward in time; old requests fall out the back, new ones come in the front. The constraint ("no more than 100 requests per 60 seconds") is maintained by updating a counter as the window slides — not recomputing from scratch each time. Your Day 1 problem is a direct analogue.

**Network packet analysis:** Intrusion detection systems scan byte streams for patterns using sliding windows. If a certain byte sequence appears within a window of N bytes, it triggers an alert. Day 3 is this pattern.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Maximum Sum Subarray of Size K | Fixed window | Easy |
| 2 | Longest Substring Without Repeating Characters (LC 3) | Variable window | Medium |
| 3 | Minimum Window Substring (LC 76) | Variable window with target | Hard |
| 4 | Permutation in String (LC 567) | Fixed window with frequency map | Medium |
| 5 | Sliding Window Maximum (LC 239) | Window + monotonic deque | Hard |

---

## Day 1 — Maximum Sum Subarray of Size K

### Problem Statement

Given an array of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.

```
Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9  (subarray [5, 1, 3])
```

```
Input:  nums = [2, 3, 4, 1, 5], k = 2
Output: 7  (subarray [3, 4])
```

**Your task:** Create `phase-1/week-5/day1_max_sum_subarray.py`.

**Before coding:** What is the brute-force O(n·k) approach? Now: when the window slides one position right, what changes? What stays the same? You should be able to move from one window sum to the next in O(1).

---

## Day 2 — Longest Substring Without Repeating Characters

### Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

```
Input:  s = "abcabcbb"
Output: 3  ("abc")
```

```
Input:  s = "bbbbb"
Output: 1  ("b")
```

```
Input:  s = "pwwkew"
Output: 3  ("wke")
```

**Your task:** Create `phase-1/week-5/day2_longest_no_repeat.py`.

**This is the canonical variable-window problem.** The window expands when a new character is valid, and contracts when a duplicate is found. Your left pointer must jump to the right position — not just move one step.

**AXIOM will ask:** Why is this O(n) and not O(n²)?

---

## Day 3 — Minimum Window Substring

### Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such window, return `""`.

```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

```
Input:  s = "a", t = "a"
Output: "a"
```

**Your task:** Create `phase-1/week-5/day3_min_window_substring.py`.

**This is hard.** Take your time. When stuck for 15+ minutes, say "stuck" and AXIOM gives you a shape, not the solution.

---

## Day 4 — Permutation in String

### Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true  ("ba" is a permutation of "ab")
```

```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Your task:** Create `phase-1/week-5/day4_permutation_in_string.py`.

**Key insight:** Two strings are permutations of each other if and only if their character frequency maps are identical. Use a fixed window of size `len(s1)` and slide it across `s2`.

---

## Day 5 — Sliding Window Maximum

### Problem Statement

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` which moves from the very left to the very right. At each step, you can only see the `k` numbers in the window. Return the max value in each window position.

```
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Your task:** Create `phase-1/week-5/day5_sliding_window_max.py`.

**This is hard.** The naive approach is O(n·k). The optimal is O(n). The key data structure is a **monotonic deque** (double-ended queue). Don't look it up yet — try to figure out what property the deque must maintain.

---

## Week 5 Wrap-Up

Update `/dsa-journal/WEEK_5_REPORT.md`.

### Complexity Quiz

| Problem | Your Time | Your Space | Optimal Time | Optimal Space |
|---------|-----------|------------|--------------|---------------|
| Max Sum Subarray K | | | O(n) | O(1) |
| Longest No Repeat | | | O(n) | O(min(m,n)) |
| Min Window Substring | | | O(m+n) | O(m+n) |
| Permutation in String | | | O(n) | O(1) |
| Sliding Window Maximum | | | O(n) | O(k) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
