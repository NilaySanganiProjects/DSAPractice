"""
Route Optimizer — Starter Skeleton
Phase 2, Week 16 — Industrial Project 4

Implement each section marked with TODO.
"""

from __future__ import annotations
import math


# ---------------------------------------------------------------------------
# heap.py — Binary Min-Heap
# ---------------------------------------------------------------------------

class MinHeap:
    """
    Binary min-heap. Stores (priority, item) tuples.
    The item with the smallest priority is at the top.

    Internal storage: a Python list.
    Parent of index i: (i - 1) // 2
    Left child of i: 2 * i + 1
    Right child of i: 2 * i + 2
    """

    def __init__(self):
        """TODO: Initialize internal list."""
        raise NotImplementedError

    def push(self, priority: float, item) -> None:
        """
        Insert (priority, item) into the heap.
        Append to end, then bubble up.
        TODO: implement
        """
        raise NotImplementedError

    def pop(self) -> tuple[float, any]:
        """
        Remove and return the (priority, item) with the smallest priority.
        Swap root with last element, remove last, then sift down.
        Raises IndexError if heap is empty.
        TODO: implement
        """
        raise NotImplementedError

    def peek(self) -> tuple[float, any]:
        """Return (priority, item) at the top without removing it."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def _bubble_up(self, idx: int) -> None:
        """Restore heap property upward from index idx."""
        raise NotImplementedError

    def _sift_down(self, idx: int) -> None:
        """Restore heap property downward from index idx."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# graph.py — Graph representation
# ---------------------------------------------------------------------------

class Graph:
    """
    Weighted directed graph represented as an adjacency list.

    nodes: dict[str, dict]  — {node_id: {x: float, y: float}}
    edges: dict[str, list]  — {from_node: [{to, distance_km, time_min}]}
    """

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def from_json(cls, path: str) -> "Graph":
        """
        Load graph from a JSON file.
        TODO: implement
        """
        raise NotImplementedError

    def neighbors(self, node: str) -> list[dict]:
        """Return list of edge dicts from `node`."""
        raise NotImplementedError

    def euclidean_distance(self, a: str, b: str) -> float:
        """
        Compute Euclidean distance between two nodes using their (x,y) coords.
        Used as the A* heuristic.
        TODO: implement using math.hypot
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# dijkstra.py
# ---------------------------------------------------------------------------

def dijkstra(
    graph: Graph,
    start: str,
    end: str,
    weight_key: str = "distance_km",
) -> tuple[list[str], float] | tuple[None, None]:
    """
    Find the shortest path from `start` to `end` using Dijkstra's algorithm.

    Returns (path, total_cost) if a path exists, (None, None) otherwise.
    path is a list of node IDs from start to end.

    Algorithm:
    1. Initialize dist[start] = 0, dist[all others] = infinity.
    2. Push (0, start) into the min-heap.
    3. While heap is not empty:
       a. Pop (cost, node) with minimum cost.
       b. If node == end, reconstruct path and return.
       c. For each neighbor: if cost + edge_weight < dist[neighbor],
          update dist[neighbor] and push to heap.
    4. If end never reached, return (None, None).

    TODO: implement using your MinHeap

    Note: Use a `prev` dict to reconstruct the path (prev[node] = predecessor).
    """
    raise NotImplementedError


def _reconstruct_path(prev: dict, start: str, end: str) -> list[str]:
    """Backtrack through `prev` dict to reconstruct path from start to end."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# astar.py
# ---------------------------------------------------------------------------

def astar(
    graph: Graph,
    start: str,
    end: str,
    weight_key: str = "distance_km",
) -> tuple[list[str], float] | tuple[None, None]:
    """
    Find the shortest path from `start` to `end` using A* search.

    A* = Dijkstra + a heuristic h(node) that estimates the remaining cost.
    Priority = g(node) + h(node), where:
      g(node) = actual cost from start to node
      h(node) = Euclidean distance from node to end (admissible heuristic)

    The heuristic must be admissible: h(node) <= actual remaining cost.
    Euclidean distance is admissible for road networks.

    Returns (path, total_cost) if a path exists, (None, None) otherwise.

    TODO: implement using your MinHeap and graph.euclidean_distance
    """
    raise NotImplementedError
