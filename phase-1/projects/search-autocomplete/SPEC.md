# Industrial Project 2 — Search Autocomplete Engine

**Phase:** 1 | **Week:** 7 | **Month:** 2

**Real company inspiration:** Google Search, Elasticsearch, Algolia

---

## The Engineering Problem

You are a backend engineer at a developer tools company. Your product has a search bar that needs to provide instant autocomplete suggestions as the user types. The current implementation does a full-text scan of all entries for every keystroke — it is O(n) per query and noticeably slow at 100k entries.

Your task: Build a search autocomplete engine that handles 10,000 lookups per second, returns results in under 1ms at the 95th percentile, and does not use any external search library.

---

## System Requirements

### API

```
GET /autocomplete?q=<prefix>&limit=<k>
→ { "results": ["apple", "application", "apply"], "latency_ms": 0.3 }
```

### Behavior

1. **Prefix matching:** Given a prefix string `q`, return up to `limit` words that start with `q`, sorted by frequency (most popular first).
2. **Frequency-aware:** Each word has a search frequency (e.g., "apple" queried 10,000 times, "applejack" queried 3 times). Higher-frequency words rank first.
3. **LRU Cache:** The most recently queried prefixes are cached. Cache size: 1000 entries. Eviction policy: LRU (Least Recently Used).

### Input Data

The engine is pre-loaded from a word-frequency file:
```
apple 10000
application 8500
apply 7200
appetizer 1200
applejack 3
...
```

---

## DSA Requirements (You Implement From Scratch)

| Requirement | DSA Used | Why |
|-------------|----------|-----|
| Prefix matching | Trie (prefix tree) | O(m) lookup where m = prefix length, independent of vocabulary size |
| Result ranking | Max-heap per Trie node (or sorted list on insert) | Return top-k by frequency efficiently |
| Hot-path caching | LRU Cache (hashmap + doubly linked list) | O(1) get and put; evict least recently used on capacity |

**You may NOT use:**
- `sortedcontainers`, `heapq` (implement your own heap), or any prefix-tree library
- Python's `functools.lru_cache` — implement LRU from scratch

**You may use:** Python's built-in `dict`, `list`, basic I/O, `http.server` for the REST endpoint.

---

## Project Structure

```
search-autocomplete/
├── README.md                  # You write this at the end
├── SPEC.md                    # This file
├── trie.py                    # Your Trie implementation
├── lru_cache.py               # Your LRU Cache implementation
├── autocomplete.py            # Combines Trie + LRU Cache
├── server.py                  # Simple HTTP server exposing the API
├── benchmark.py               # Your benchmark script
├── data/
│   └── words_with_freq.txt    # Sample word-frequency file
└── test_autocomplete.py       # Basic correctness tests
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Implement `Trie` with `insert(word, frequency)` and `search(prefix) → list[str]` (write `trie.py`)
- [ ] **Milestone 2:** Implement `LRUCache` with `get(key)` and `put(key, value)`, both O(1) (write `lru_cache.py`)
- [ ] **Milestone 3:** Wire `Trie` + `LRUCache` into `Autocomplete` class (write `autocomplete.py`)
- [ ] **Milestone 4:** Load word-frequency data and serve the REST API (write `server.py`)
- [ ] **Milestone 5:** Write correctness tests (write `test_autocomplete.py`)
- [ ] **Milestone 6:** Run `benchmark.py` and prove 10k lookups/sec
- [ ] **Milestone 7:** Write `README.md`

---

## Benchmark Target

The engine must handle **10,000 autocomplete lookups per second** (single-threaded, in-process, excluding HTTP overhead).

```bash
python benchmark.py
```

Expected output:
```
Loaded 50,000 words into Trie
Running 10,000 lookups with varied prefixes...
Completed in 0.89 seconds
Throughput: 11,236 lookups/sec
Cache hit rate: 67.3%
P95 latency: 0.08ms
All benchmarks passed.
```

---

## Trie Design Notes

A Trie node stores:
- A dictionary mapping each character to a child TrieNode
- A boolean `is_end` marking end of a word
- The word's frequency (if `is_end` is True)
- Optionally: a list of the top-k (word, freq) pairs reachable from this node (cached at insert time to make prefix search O(k) instead of O(subtree))

The second design (pre-caching top-k at each node) is what Google uses in production to achieve sub-millisecond autocomplete. Try the simpler version first, then optimize.

---

## LRU Cache Design Notes

An LRU Cache requires O(1) get AND O(1) put with eviction. This requires two data structures:
1. A **hashmap** for O(1) key lookup → `{key: node}`
2. A **doubly linked list** to maintain access order (most recent at head, least recent at tail)

On `get(key)`: look up in hashmap, move node to head → O(1)
On `put(key, value)`: insert at head; if capacity exceeded, remove tail node and its hashmap entry → O(1)

You implement the doubly linked list node by node — no `collections.deque`.

---

## README Requirements (You Write This)

1. What is a Trie and why does it outperform a hashmap for prefix queries? Give the complexity comparison.
2. How does your LRU Cache work? Draw a diagram showing the state of the doubly linked list after 5 operations.
3. What is the time complexity of `autocomplete(prefix, k)`? Is it different with and without the node-level top-k cache?
4. What would you change to handle 1 million lookups/second? (Think: multi-threading, prefix sharding, Redis Sorted Sets)
5. Where in the real world would you encounter this exact system? Name at least 3 companies and the product feature.
