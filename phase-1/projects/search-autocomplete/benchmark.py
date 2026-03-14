"""
Benchmark for the Search Autocomplete Engine.
Run with: python benchmark.py

Measures:
  - Trie load time
  - Lookup throughput (queries/sec)
  - Cache hit rate
  - P95 latency per lookup
"""

import time
import random
import statistics

# ---------------------------------------------------------------------------
# Word list generator (simulates a real word-frequency dataset)
# ---------------------------------------------------------------------------

PREFIXES = ["app", "pre", "com", "pro", "con", "dis", "un", "re", "in", "de",
            "su", "tr", "st", "pl", "gr", "br", "fr", "sp", "sc", "sk"]

SUFFIXES = ["tion", "ment", "ness", "ity", "er", "ing", "ed", "ly", "al", "ic",
            "ous", "ive", "ful", "less", "able", "ible", "ent", "ant", "ary", "ory"]

MIDDLES = ["a", "e", "i", "o", "u", "ar", "or", "er", "ir", "ur",
           "al", "el", "ol", "ul", "an", "en", "in", "on", "un", "at"]


def generate_word_list(n: int) -> list[tuple[str, int]]:
    """Generate n synthetic (word, frequency) pairs."""
    words = set()
    result = []
    random.seed(42)
    while len(result) < n:
        word = (
            random.choice(PREFIXES)
            + random.choice(MIDDLES)
            + random.choice(SUFFIXES)
        )
        if word not in words:
            words.add(word)
            freq = random.randint(1, 10000)
            result.append((word, freq))
    return result


def generate_query_prefixes(words: list[tuple[str, int]], n: int) -> list[str]:
    """Generate n query prefixes (2–5 chars) from the word list."""
    random.seed(99)
    prefixes = []
    for _ in range(n):
        word, _ = random.choice(words)
        length = random.randint(2, min(5, len(word)))
        prefixes.append(word[:length])
    return prefixes


# ---------------------------------------------------------------------------
# Benchmark
# ---------------------------------------------------------------------------

def run_benchmark():
    from autocomplete import Autocomplete

    print("=" * 60)
    print("Search Autocomplete Engine — Benchmark")
    print("=" * 60)

    # ---- Load phase ----
    word_list = generate_word_list(50_000)
    engine = Autocomplete(cache_capacity=1000)

    load_start = time.perf_counter()
    for word, freq in word_list:
        engine.trie.insert(word, freq)  # direct Trie insert for benchmarking
    load_elapsed = time.perf_counter() - load_start
    print(f"Loaded {len(word_list):,} words in {load_elapsed:.3f}s")

    # ---- Query phase ----
    query_prefixes = generate_query_prefixes(word_list, 10_000)
    latencies = []
    cache_hits = 0

    total_start = time.perf_counter()
    for prefix in query_prefixes:
        t0 = time.perf_counter()
        results = engine.query(prefix, limit=10)
        t1 = time.perf_counter()
        latencies.append((t1 - t0) * 1000)  # convert to ms

    total_elapsed = time.perf_counter() - total_start
    throughput = len(query_prefixes) / total_elapsed

    p95 = statistics.quantiles(latencies, n=20)[18]  # 95th percentile
    p99 = statistics.quantiles(latencies, n=100)[98]

    print(f"Ran {len(query_prefixes):,} queries in {total_elapsed:.3f}s")
    print(f"Throughput: {throughput:,.0f} queries/sec")
    print(f"P95 latency: {p95:.3f}ms")
    print(f"P99 latency: {p99:.3f}ms")
    print()

    # ---- Validation ----
    passed = True
    if throughput < 10_000:
        print(f"FAIL: Throughput {throughput:,.0f} < 10,000 target")
        passed = False
    else:
        print(f"PASS: Throughput {throughput:,.0f} >= 10,000 queries/sec")

    if p95 > 1.0:
        print(f"FAIL: P95 latency {p95:.3f}ms > 1ms target")
        passed = False
    else:
        print(f"PASS: P95 latency {p95:.3f}ms <= 1ms")

    print()
    if passed:
        print("All benchmarks passed.")
    else:
        print("One or more benchmarks failed. See above.")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmark()
