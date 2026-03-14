# Phase 1 — Week 2: Hashmaps & Sets

## Theme
**"O(1) lookup is the most powerful tool in your arsenal — if you know when to reach for it."**

Hashmaps are not just for Two Sum. They are the core of how real systems do frequency counting, deduplication, grouping, and index building. This week you learn to see the hashmap not as a data structure but as a *design decision*.

---

## Real-World Context

**Google Search ranking:** When you type a query, Google's suggestion system counts the frequency of past queries that share a prefix using frequency maps. Before sorting or ranking, there is a hashmap counting how often each completion has been queried. You will build the counting layer this week; the prefix tree (trie) comes in Project 2.

**Cloudflare rate limiting:** Cloudflare's rate limiter tracks how many requests an IP has made in a time window. The core data structure is a hashmap: `{ip_address: request_count}`. If the count exceeds a threshold, the request is blocked. You will implement a simplified version as part of Project 1 next week.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Group Anagrams (LC 49) | Hashmap grouping | Medium |
| 2 | Top K Frequent Elements (LC 347) | Frequency map + bucket sort | Medium |
| 3 | Encode and Decode Strings (LC 271) | String encoding protocol | Medium |
| 4 | Contains Duplicate II (LC 219) | Sliding window + set | Easy |
| 5 | Longest Consecutive Sequence (LC 128) | Set-based O(n) scan | Medium |

---

## Day 1 — Group Anagrams

### Problem Statement (ADVERSARY MODE)

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

```
Input:  strs = [""]
Output: [[""]]
```

**Your task:** Create `phase-1/week-2/day1_group_anagrams.py` and write your solution.

**Before you start, ask yourself:**
- What is the "signature" of an anagram? Two strings are anagrams if and only if _________.
- How do you use that signature as a hashmap key?
- What is the time complexity of sorting each string vs. counting characters?

---

## Day 2 — Top K Frequent Elements

### Problem Statement (ADVERSARY MODE)

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

```
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

```
Input:  nums = [1], k = 1
Output: [1]
```

**Constraint:** Your algorithm must be better than O(n log n) time complexity.

**Your task:** Create `phase-1/week-2/day2_top_k_frequent.py` and write your solution.

**Hint if stuck for 15+ minutes:** Think about what a bucket represents when the bucket index is a frequency count.

---

## Day 3 — Encode and Decode Strings

### Problem Statement (ADVERSARY MODE)

Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and decoded back to the original list of strings.

```
encode(["lint","code","love","you"]) → "4#lint4#code4#love3#you"
decode("4#lint4#code4#love3#you") → ["lint","code","love","you"]
```

**Your task:** Create `phase-1/week-2/day3_encode_decode.py` and implement both `encode` and `decode`.

**Think about:** Why can't you just use a delimiter like `,`? What if a string contains a comma?

---

## Day 4 — Contains Duplicate II

### Problem Statement (ADVERSARY MODE)

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Your task:** Create `phase-1/week-2/day4_contains_duplicate_ii.py` and write your solution.

**Notice:** This is the sliding window pattern appearing in a set context. The "window" here is a set of size k.

---

## Day 5 — Longest Consecutive Sequence

### Problem Statement (ADVERSARY MODE)

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

```
Input:  nums = [100,4,200,1,3,2]
Output: 4  (The consecutive sequence is [1, 2, 3, 4])
```

```
Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Your task:** Create `phase-1/week-2/day5_longest_consecutive.py` and write your solution.

**Critical question AXIOM will ask:** You could sort this in O(n log n) and scan. Why doesn't that satisfy the O(n) constraint, and what does a set buy you that sorting doesn't?

---

## Week 2 Wrap-Up

After completing all 5 problems:

1. Update `/dsa-journal/WEEK_2_REPORT.md` (copy the template from `/dsa-journal/templates/WEEK_REPORT_TEMPLATE.md`).
2. Answer the Complexity Quiz below.
3. Proceed to Week 3: Industrial Project 1.

### Complexity Quiz

| Problem | Your Time Complexity | Your Space Complexity | Optimal Time | Optimal Space |
|---------|---------------------|----------------------|--------------|---------------|
| Group Anagrams | | | O(n·k log k) | O(n·k) |
| Top K Frequent | | | O(n) | O(n) |
| Encode/Decode | | | O(n) | O(n) |
| Contains Duplicate II | | | O(n) | O(min(n,k)) |
| Longest Consecutive | | | O(n) | O(n) |

---

## Notes & Observations

> (Paste AXIOM feedback, your "aha" moments, and mistakes here.)
