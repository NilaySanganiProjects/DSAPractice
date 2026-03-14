"""
Correctness tests for the Search Autocomplete Engine.
Run with: python test_autocomplete.py

These tests check that your Trie and LRU Cache are
functionally correct before you run the benchmark.
"""

import sys

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def assert_equal(actual, expected, test_name: str):
    if actual == expected:
        print(f"  PASS: {test_name}")
    else:
        print(f"  FAIL: {test_name}")
        print(f"        Expected: {expected}")
        print(f"        Actual:   {actual}")
        sys.exit(1)


def assert_contains(actual: list, expected_items: list, test_name: str):
    for item in expected_items:
        if item not in actual:
            print(f"  FAIL: {test_name} — '{item}' not in {actual}")
            sys.exit(1)
    print(f"  PASS: {test_name}")


# ---------------------------------------------------------------------------
# Trie tests
# ---------------------------------------------------------------------------

def test_trie():
    from autocomplete import Trie

    print("Trie tests:")

    t = Trie()

    # Basic insert and search
    t.insert("apple", 100)
    t.insert("app", 50)
    t.insert("application", 80)
    t.insert("apply", 60)
    t.insert("banana", 200)

    results = [word for _, word in t.search("app", limit=10)]
    assert_contains(results, ["apple", "app", "application", "apply"], "search('app') returns all app* words")

    # Frequency ordering
    freqs_words = t.search("app", limit=10)
    words_in_order = [w for _, w in freqs_words]
    assert_equal(words_in_order[0], "apple", "search('app') first result is highest-frequency word")

    # Prefix not in trie
    results_empty = t.search("xyz", limit=10)
    assert_equal(results_empty, [], "search('xyz') returns empty list")

    # Exact word match
    results_exact = [w for _, w in t.search("banana", limit=10)]
    assert_equal(results_exact, ["banana"], "search('banana') returns only 'banana'")

    # Limit respected
    results_limited = t.search("app", limit=2)
    assert_equal(len(results_limited), 2, "search('app', limit=2) returns exactly 2 results")

    # Empty prefix
    results_all = t.search("", limit=100)
    assert_equal(len(results_all), 5, "search('') returns all 5 words")

    print()


# ---------------------------------------------------------------------------
# LRU Cache tests
# ---------------------------------------------------------------------------

def test_lru_cache():
    from autocomplete import LRUCache

    print("LRU Cache tests:")

    cache = LRUCache(capacity=3)

    # Basic put and get
    cache.put("app", ["apple", "apply"])
    assert_equal(cache.get("app"), ["apple", "apply"], "get after put")

    # Miss
    assert_equal(cache.get("xyz"), None, "get on missing key returns None")

    # LRU eviction
    cache.put("ban", ["banana"])
    cache.put("cat", ["category", "catalog"])
    # Cache is now full: app, ban, cat (app is LRU)
    cache.get("app")  # Access app → now: ban is LRU
    cache.put("dog", ["dog"])  # Evicts ban (LRU)

    assert_equal(cache.get("ban"), None, "evicted LRU entry is gone")
    assert_equal(cache.get("app"), ["apple", "apply"], "recently accessed entry is retained")
    assert_equal(cache.get("dog"), ["dog"], "newly inserted entry is present")

    # Capacity 1
    tiny = LRUCache(capacity=1)
    tiny.put("a", [1])
    tiny.put("b", [2])
    assert_equal(tiny.get("a"), None, "capacity-1 cache evicts on second insert")
    assert_equal(tiny.get("b"), [2], "capacity-1 cache retains latest")

    print()


# ---------------------------------------------------------------------------
# Integration test
# ---------------------------------------------------------------------------

def test_autocomplete_integration():
    from autocomplete import Autocomplete

    print("Autocomplete integration tests:")

    engine = Autocomplete(cache_capacity=10)
    engine.trie.insert("apple", 100)
    engine.trie.insert("application", 80)
    engine.trie.insert("apply", 60)
    engine.trie.insert("apt", 40)

    # First query hits Trie
    r1 = engine.query("app", limit=10)
    assert_contains(r1, ["apple", "application", "apply"], "first query returns correct results")

    # Second identical query hits cache
    r2 = engine.query("app", limit=10)
    assert_equal(r1, r2, "cached query returns same results")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 50)
    print("Search Autocomplete — Correctness Tests")
    print("=" * 50)
    print()
    test_trie()
    test_lru_cache()
    test_autocomplete_integration()
    print("All tests passed.")
