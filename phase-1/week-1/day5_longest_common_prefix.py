"""
Day 5 — Longest Common Prefix (LeetCode 14)

Write a function to find the longest common prefix string amongst an array of
strings. If there is no common prefix, return an empty string "".

Pattern: Vertical scanning (column by column across all strings)
Time:    O(n·m)  where n = number of strings, m = length of shortest string
Space:   O(1)

Examples:
    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'
    >>> longest_common_prefix(["dog", "racecar", "car"])
    ''
    >>> longest_common_prefix(["interview", "interview", "interview"])
    'interview'
"""


def longest_common_prefix(strs: list[str]) -> str:
    """Return the longest prefix shared by all strings in strs.

    Scan character by character (vertical scan). Stop as soon as a mismatch
    is found or the shortest string is exhausted.
    """
    if not strs:
        return ""

    for col, char in enumerate(strs[0]):
        for word in strs[1:]:
            if col >= len(word) or word[col] != char:
                return strs[0][:col]

    return strs[0]
