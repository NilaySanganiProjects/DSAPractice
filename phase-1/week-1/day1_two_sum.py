"""
Day 1 — Two Sum (LeetCode 1)

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. You may assume exactly one solution
exists. You may not use the same element twice.

Pattern: Hashmap lookup
Time:    O(n)
Space:   O(n)

Examples:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to target.

    Uses a hashmap to achieve O(n) time by storing each number's index as we
    scan. For every element, we check whether its complement (target - num)
    has already been seen.
    """
    seen: dict[int, int] = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # no solution found (problem guarantees one exists)
