"""
Day 3 — Remove Duplicates from Sorted Array (LeetCode 26)

Given a sorted integer array `nums`, remove duplicates **in-place** so that
each unique element appears only once. Return `k`, the number of unique
elements. The first `k` elements of `nums` must hold the unique elements in
their original order.

Pattern: Two pointers (slow writer / fast reader)
Time:    O(n)
Space:   O(1)

Examples:
    >>> nums = [1, 1, 2]
    >>> k = remove_duplicates(nums)
    >>> k, nums[:k]
    (2, [1, 2])

    >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    >>> k = remove_duplicates(nums)
    >>> k, nums[:k]
    (5, [0, 1, 2, 3, 4])
"""


def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates in-place; return count of unique elements.

    `write` points to the next position to fill with a unique value.
    `read` scans ahead looking for a value different from the last written.
    """
    if not nums:
        return 0

    write = 1  # position to place the next unique element

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write
