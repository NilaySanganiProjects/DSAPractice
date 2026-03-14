"""
Real-time Leaderboard System — Starter Skeleton
Phase 3, Week 19 — Industrial Project 5

Implement each section marked with TODO.
"""

from __future__ import annotations

MAX_SCORE = 10_000  # maximum possible score in this system


# ---------------------------------------------------------------------------
# fenwick_tree.py
# ---------------------------------------------------------------------------

class FenwickTree:
    """
    Binary Indexed Tree (Fenwick Tree).

    Supports:
    - update(i, delta): add delta to position i in O(log n)
    - prefix_sum(i): sum of positions 1..i in O(log n)

    Index is 1-based.
    """

    def __init__(self, size: int):
        """
        Initialize a Fenwick Tree of given size.
        All values start at 0.
        TODO: implement
        """
        self.size = size
        # TODO: internal array of size+1 (1-indexed)
        raise NotImplementedError

    def update(self, i: int, delta: int) -> None:
        """
        Add `delta` to position `i`.

        The update propagates upward using the lowbit trick:
            i += i & (-i)

        TODO: implement
        """
        raise NotImplementedError

    def prefix_sum(self, i: int) -> int:
        """
        Return the sum of positions 1..i.

        The query traverses downward using the lowbit trick:
            i -= i & (-i)

        TODO: implement
        """
        raise NotImplementedError

    def range_sum(self, l: int, r: int) -> int:
        """
        Return the sum of positions l..r.
        Uses prefix_sum(r) - prefix_sum(l-1).
        TODO: implement
        """
        raise NotImplementedError

    def find_kth(self, k: int) -> int:
        """
        Find the smallest index i such that prefix_sum(i) >= k.
        This is a binary search on the BIT, O(log n).

        Used in top_k to find which score bucket the kth user falls in.

        TODO: implement (optional optimization — can also binary search externally)
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# leaderboard.py
# ---------------------------------------------------------------------------

class Leaderboard:
    """
    Real-time leaderboard supporting O(log n) updates and rank queries.

    DSA:
    - FenwickTree indexed by score (1..MAX_SCORE)
    - tree[score] = number of users currently at this score
    - dict: {user_id: current_score}
    """

    def __init__(self, max_score: int = MAX_SCORE):
        """
        TODO: Initialize FenwickTree and user score dict.
        """
        raise NotImplementedError

    def update_score(self, user_id: str, new_score: int) -> None:
        """
        Update the score for `user_id` to `new_score`.

        If the user already has a score:
          - Decrement the FenwickTree at their old score.
          - Increment the FenwickTree at their new score.

        If new user:
          - Increment FenwickTree at new_score.

        Update the user dict.

        TODO: implement
        """
        raise NotImplementedError

    def rank_of(self, user_id: str) -> int | None:
        """
        Return the 1-indexed rank of `user_id`.
        Rank 1 = highest score. Ties share the same rank.

        Formula: rank = (number of users with score STRICTLY GREATER than user's score) + 1
               = total_users - prefix_sum(user_score) + count_at_user_score
               Wait... think carefully. prefix_sum(user_score) = number of users with score <= user_score.
               Users with score > user_score = total_users - prefix_sum(user_score).
               Rank = users_with_higher_score + 1.

        TODO: implement

        Returns None if user_id not found.
        """
        raise NotImplementedError

    def top_k(self, k: int) -> list[tuple[str, int]]:
        """
        Return the top `k` users as a list of (user_id, score) tuples,
        sorted by score descending.

        Strategy: Binary search on the FenwickTree to find the minimum
        score S such that the number of users with score >= S covers k users.
        Then return users at score >= S.

        TODO: implement

        Note: This is harder to implement efficiently. A simpler O(n log n)
        fallback: sort all users by score. Acceptable for the first milestone.
        """
        raise NotImplementedError

    @property
    def total_users(self) -> int:
        """Total number of users tracked."""
        raise NotImplementedError
