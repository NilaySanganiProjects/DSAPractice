"""Tests for Phase 1, Week 1 — Arrays & Strings."""

import pytest

from day1_two_sum import two_sum
from day2_stock_profit import max_profit
from day3_remove_duplicates import remove_duplicates
from day4_valid_anagram import is_anagram
from day5_longest_common_prefix import longest_common_prefix


# ---------------------------------------------------------------------------
# Day 1 — Two Sum
# ---------------------------------------------------------------------------


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_non_zero_indices(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_duplicate_values(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_negative_numbers(self):
        assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    def test_large_values(self):
        result = two_sum([1_000_000_000, -1_000_000_000], 0)
        assert result == [0, 1]


# ---------------------------------------------------------------------------
# Day 2 — Best Time to Buy and Sell Stock
# ---------------------------------------------------------------------------


class TestMaxProfit:
    def test_basic_profit(self):
        assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    def test_no_profit(self):
        assert max_profit([7, 6, 4, 3, 1]) == 0

    def test_single_element(self):
        assert max_profit([5]) == 0

    def test_empty(self):
        assert max_profit([]) == 0

    def test_two_elements_profit(self):
        assert max_profit([1, 2]) == 1

    def test_buy_at_start_sell_at_end(self):
        assert max_profit([1, 2, 3, 4, 5]) == 4


# ---------------------------------------------------------------------------
# Day 3 — Remove Duplicates from Sorted Array
# ---------------------------------------------------------------------------


class TestRemoveDuplicates:
    def test_basic(self):
        nums = [1, 1, 2]
        k = remove_duplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_longer(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]

    def test_no_duplicates(self):
        nums = [1, 2, 3]
        k = remove_duplicates(nums)
        assert k == 3
        assert nums[:k] == [1, 2, 3]

    def test_all_same(self):
        nums = [7, 7, 7, 7]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [7]

    def test_single_element(self):
        nums = [42]
        k = remove_duplicates(nums)
        assert k == 1
        assert nums[:k] == [42]

    def test_empty(self):
        nums = []
        assert remove_duplicates(nums) == 0


# ---------------------------------------------------------------------------
# Day 4 — Valid Anagram
# ---------------------------------------------------------------------------


class TestIsAnagram:
    def test_is_anagram(self):
        assert is_anagram("anagram", "nagaram") is True

    def test_not_anagram(self):
        assert is_anagram("rat", "car") is False

    def test_different_lengths(self):
        assert is_anagram("ab", "abc") is False

    def test_empty_strings(self):
        assert is_anagram("", "") is True

    def test_single_chars_equal(self):
        assert is_anagram("a", "a") is True

    def test_single_chars_different(self):
        assert is_anagram("a", "b") is False

    def test_repeated_characters(self):
        assert is_anagram("aab", "baa") is True


# ---------------------------------------------------------------------------
# Day 5 — Longest Common Prefix
# ---------------------------------------------------------------------------


class TestLongestCommonPrefix:
    def test_basic(self):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    def test_no_common_prefix(self):
        assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    def test_all_identical(self):
        assert longest_common_prefix(["interview", "interview", "interview"]) == "interview"

    def test_empty_list(self):
        assert longest_common_prefix([]) == ""

    def test_single_string(self):
        assert longest_common_prefix(["alone"]) == "alone"

    def test_one_empty_string(self):
        assert longest_common_prefix(["", "abc"]) == ""

    def test_prefix_is_full_word(self):
        assert longest_common_prefix(["ab", "abc", "abcd"]) == "ab"
