"""
Search Autocomplete Engine — Starter Skeleton
Phase 1, Week 7 — Industrial Project 2

Implement each section marked with TODO.
Run test_autocomplete.py to check correctness.
Run benchmark.py to check performance.
"""


# ---------------------------------------------------------------------------
# trie.py
# ---------------------------------------------------------------------------

class TrieNode:
    """
    A single node in the Trie.

    Each node represents one character in the path from root to word.
    """

    def __init__(self):
        """
        TODO: Initialize:
          - children: dict mapping character -> TrieNode
          - is_end: bool, True if this node is the end of a valid word
          - word: str, the complete word (only meaningful if is_end is True)
          - frequency: int, query frequency of this word
          - top_completions: list of (frequency, word) tuples, sorted descending
                             This is the optional optimization — pre-cache top-k
                             completions at every node so prefix search is O(k)
                             instead of O(subtree_size)
        """
        # TODO: implement
        raise NotImplementedError


class Trie:
    """
    A prefix tree (Trie) supporting insert and prefix search.

    DSA: Tree where each edge represents one character.
    Insert: O(m) where m = len(word)
    Search: O(m + k) where k = number of results returned
    """

    def __init__(self):
        """TODO: Initialize root node."""
        raise NotImplementedError

    def insert(self, word: str, frequency: int) -> None:
        """
        Insert `word` with its `frequency` into the Trie.

        After inserting, update the `top_completions` list at every
        node along the path (optional optimization).

        TODO: implement
        """
        raise NotImplementedError

    def search(self, prefix: str, limit: int = 10) -> list[tuple[int, str]]:
        """
        Return up to `limit` (frequency, word) tuples for words
        that start with `prefix`, sorted by frequency descending.

        Returns an empty list if no words match the prefix.

        TODO: implement

        Hint: Traverse to the end of the prefix in the Trie.
              Then either use the pre-cached top_completions (fast path)
              or DFS the subtree to collect all completions (slow path).
        """
        raise NotImplementedError

    def _collect_completions(
        self,
        node: TrieNode,
        results: list,
        limit: int,
    ) -> None:
        """
        DFS helper: collect all (frequency, word) pairs reachable
        from `node`, appending to `results`.

        TODO: implement (only needed if not using pre-cached top_completions)
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# lru_cache.py
# ---------------------------------------------------------------------------

class _DLLNode:
    """Doubly linked list node for the LRU Cache."""

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev: _DLLNode | None = None
        self.next: _DLLNode | None = None


class LRUCache:
    """
    Least Recently Used Cache.

    get(key): O(1)  — returns value or None if not found
    put(key, value): O(1)  — inserts; evicts LRU entry if at capacity

    DSA: hashmap + doubly linked list
      - hashmap: {key: DLLNode} for O(1) lookup
      - DLL: maintains insertion order (head = most recent, tail = least recent)
    """

    def __init__(self, capacity: int):
        """
        TODO: Initialize:
          - capacity (int)
          - hashmap (dict)
          - sentinel head and tail nodes (simplifies edge cases)
          - current size counter
        """
        # TODO: implement
        raise NotImplementedError

    def get(self, key: str) -> list | None:
        """
        Return the cached value for `key`, or None if not present.
        Move the accessed node to the head (most recently used).

        TODO: implement
        """
        raise NotImplementedError

    def put(self, key: str, value: list) -> None:
        """
        Insert or update `key` with `value`.
        Move to head. If capacity is exceeded, evict the tail node.

        TODO: implement
        """
        raise NotImplementedError

    def _move_to_head(self, node: _DLLNode) -> None:
        """Remove node from its current position and insert after head."""
        # TODO: implement
        raise NotImplementedError

    def _remove(self, node: _DLLNode) -> None:
        """Unlink a node from the doubly linked list."""
        # TODO: implement
        raise NotImplementedError

    def _insert_after_head(self, node: _DLLNode) -> None:
        """Insert a node immediately after the sentinel head."""
        # TODO: implement
        raise NotImplementedError


# ---------------------------------------------------------------------------
# autocomplete.py
# ---------------------------------------------------------------------------

class Autocomplete:
    """
    Combines Trie + LRU Cache into the autocomplete engine.
    """

    def __init__(self, cache_capacity: int = 1000):
        """TODO: Initialize Trie and LRU Cache."""
        raise NotImplementedError

    def load(self, word_freq_file: str) -> None:
        """
        Load words and frequencies from a file.
        File format (one per line): <word> <frequency>

        TODO: implement
        """
        raise NotImplementedError

    def query(self, prefix: str, limit: int = 10) -> list[str]:
        """
        Return up to `limit` words matching `prefix`, sorted by
        frequency descending.

        Check the LRU cache first. On cache miss, query the Trie
        and store the result in the cache.

        TODO: implement
        """
        raise NotImplementedError
