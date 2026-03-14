# Phase 1 — Week 1: Arrays & Strings

## Theme
**"Before you write code, know why it matters."**

Arrays are the foundation of almost every data structure. Strings are arrays of characters. This week you will internalize 3 fundamental patterns that sit on top of array syntax.

---

## Real-World Context

**Instagram feed deduplication:** When your Instagram feed loads, the backend fetches posts from multiple sources. Posts can appear from more than one source. Instagram uses a pointer-based scan on a sorted array of post IDs to deduplicate in O(n) — not O(n²). You will implement this pattern on Day 3.

**Splunk log parsing:** Splunk ingests millions of log lines per second. Its tokenizer uses index-based string scanning — essentially array manipulation — to extract fields without copying strings. You will work with a simplified version on Day 5.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty | File |
|-----|---------|---------|-----------|------|
| 1 | Two Sum (LC 1) | Hashmap lookup | Easy | `day1_two_sum.py` |
| 2 | Best Time to Buy and Sell Stock (LC 121) | Single-pass array scan | Easy | `day2_stock_profit.py` |
| 3 | Remove Duplicates from Sorted Array (LC 26) | Two pointers (in-place) | Easy | `day3_remove_duplicates.py` |
| 4 | Valid Anagram (LC 242) | Character frequency map | Easy | `day4_valid_anagram.py` |
| 5 | Longest Common Prefix (LC 14) | Vertical string scanning | Easy | `day5_longest_common_prefix.py` |

---

## Complexity Quiz

After completing all 5 problems, fill in the "Your" columns:

| Problem | Your Time Complexity | Your Space Complexity | Optimal Time | Optimal Space |
|---------|---------------------|----------------------|--------------|---------------|
| Two Sum | | | O(n) | O(n) |
| Stock Profit | | | O(n) | O(1) |
| Remove Duplicates | | | O(n) | O(1) |
| Valid Anagram | | | O(n) | O(n) |
| Longest Common Prefix | | | O(n·m) | O(1) |

---

## Run the Tests

```bash
python -m pytest phase-1/week-1/test_week1.py -v
```
