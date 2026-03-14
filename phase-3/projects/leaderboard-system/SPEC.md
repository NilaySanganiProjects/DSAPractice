# Industrial Project 5 — Real-time Leaderboard System

**Phase:** 3 | **Week:** 19 | **Month:** 5

**Real company inspiration:** Codeforces, Steam achievements, Duolingo streaks, gaming platforms, Stack Overflow reputation

---

## The Engineering Problem

You are an engineer on the platform team at a competitive coding site (think Codeforces or HackerRank). Your leaderboard must support:

1. **Score update:** A user's score changes. Update in O(log n).
2. **Top-K query:** Return the top K users by score. In O(K log n).
3. **Rank query:** Given a user ID, return their current rank (1-indexed, rank 1 = highest score). In O(log n).

There are 1 million registered users. Score updates arrive at 1,000/second. Top-K queries arrive at 500/second. This cannot be a naive sort on every query.

---

## System Requirements

### API

```python
lb = Leaderboard(capacity=1_000_000)
lb.update_score("user_42", 1500)      # O(log n)
lb.update_score("user_7", 2100)       # O(log n)
lb.top_k(3)                            # → [("user_7", 2100), ("user_42", 1500), ...]
lb.rank_of("user_42")                  # → 2  (1-indexed)
```

### Constraints

- All scores are non-negative integers.
- A user's score can only increase (simplification).
- Rank is 1-indexed: the user with the highest score has rank 1.
- Ties: users with equal scores share the same rank.

---

## DSA: Fenwick Tree (Binary Indexed Tree)

A Fenwick Tree (also called a Binary Indexed Tree or BIT) supports:
- **Point update:** Increase value at index `i` by `delta`. O(log n).
- **Prefix sum query:** Sum of values from index 1 to `i`. O(log n).

For a leaderboard with max score `MAX_SCORE`:
- Use a BIT indexed by score value (1 to MAX_SCORE).
- `update(score, +1)` when a user's score increases to `score` (and `-1` at their old score).
- `rank_of(user_score)` = total users with score > `user_score` + 1 = `total - prefix_sum(user_score) + 1`.
- `top_k(k)` = binary search on the BIT to find the score threshold where the top-k users live.

**You may NOT use:** `sortedcontainers.SortedList`, Redis, or any external sorted-set implementation.

---

## Project Structure

```
leaderboard-system/
├── README.md               # You write this at the end
├── SPEC.md                 # This file
├── fenwick_tree.py         # Your Fenwick Tree implementation
├── leaderboard.py          # Leaderboard using Fenwick Tree
├── benchmark.py            # Performance benchmark
├── test_leaderboard.py     # Correctness tests
└── demo.py                 # Interactive demo
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Implement `FenwickTree` with `update(i, delta)` and `prefix_sum(i)` (write `fenwick_tree.py`)
- [ ] **Milestone 2:** Implement `Leaderboard.update_score(user, score)` (write `leaderboard.py`)
- [ ] **Milestone 3:** Implement `Leaderboard.rank_of(user)` using the BIT prefix sum
- [ ] **Milestone 4:** Implement `Leaderboard.top_k(k)` — binary search on BIT to find score threshold
- [ ] **Milestone 5:** Write `test_leaderboard.py` with edge case coverage
- [ ] **Milestone 6:** Run `benchmark.py` — 1M users, 100k updates, 50k rank queries
- [ ] **Milestone 7:** Write `README.md`

---

## Fenwick Tree Reference

The Fenwick Tree stores a BIT array where each cell `tree[i]` is responsible for a range of indices. The key operations:

```
update(i, delta):
    while i <= MAX_SCORE:
        tree[i] += delta
        i += i & (-i)   # move to next responsible index

prefix_sum(i):
    total = 0
    while i > 0:
        total += tree[i]
        i -= i & (-i)   # move to parent
    return total
```

The `i & (-i)` trick isolates the lowest set bit, which determines the range each cell covers.

**Your task:** Understand why this works before you implement it. Draw the binary representations of indices 1 through 8 and trace which cells cover which ranges.

---

## Benchmark Target

- 100,000 score updates in under 100ms
- 50,000 rank queries in under 50ms
- 10,000 top-10 queries in under 100ms

---

## README Requirements (You Write This)

1. What is a Fenwick Tree and what problem does it solve better than a sorted array or a segment tree?
2. Trace through a `rank_of` query step by step. Show which BIT cells are accessed.
3. What is the time and space complexity of each operation?
4. How does Codeforces (or a real gaming platform) actually implement its leaderboard at scale? Research and describe in 2 sentences.
5. What would you change to support score decreases?
