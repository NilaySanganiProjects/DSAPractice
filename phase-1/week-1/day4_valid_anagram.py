"""
Day 4 — Valid Anagram (LeetCode 242)

Given two strings `s` and `t`, return True if `t` is an anagram of `s`, and
False otherwise. An anagram uses all the original letters exactly once,
rearranged.

Pattern: Character frequency map (Counter / hashmap)
Time:    O(n)
Space:   O(k)  — where k is the number of distinct characters (≤ 26 for lowercase English letters)

Examples:
    >>> is_anagram("anagram", "nagaram")
    True
    >>> is_anagram("rat", "car")
    False
    >>> is_anagram("", "")
    True
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """Return True if t is an anagram of s.

    Early-exit on length mismatch, then compare character frequency maps.
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
