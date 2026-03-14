"""
Dependency Resolver — Starter Skeleton
Phase 2, Week 12 — Industrial Project 3

Implement each section marked with TODO.
Run test_resolver.py to check correctness.
"""

from __future__ import annotations
import json
from pathlib import Path


# ---------------------------------------------------------------------------
# graph.py (inline)
# ---------------------------------------------------------------------------

def load_manifest(path: str) -> dict[str, list[str]]:
    """
    Load a package manifest JSON file and return an adjacency list.

    The JSON format is:
        { "packages": { "pkg_name": ["dep1", "dep2"], ... } }

    Returns a dict: { package_name: [dependency_names] }

    TODO: implement
    """
    raise NotImplementedError


def build_graph(packages: dict[str, list[str]]) -> tuple[dict, dict]:
    """
    Build an adjacency list and in-degree map from the packages dict.

    Returns:
        adjacency: dict[str, list[str]]  — edges (pkg → its dependencies)
        in_degree: dict[str, int]        — number of packages that depend on each pkg

    Note: In a dependency graph, if A depends on B, then B must be installed
    before A. The edge goes A → B, and B has in-degree += 1 (from A's perspective
    B is a prerequisite, so in Kahn's algorithm we track how many packages
    are waiting on each package to be installed).

    TODO: implement — be careful about edge direction for Kahn's algorithm
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# topo_sort.py (inline)
# ---------------------------------------------------------------------------

def kahn_topological_sort(
    packages: dict[str, list[str]],
) -> tuple[list[str] | None, list[str] | None]:
    """
    Perform Kahn's BFS-based topological sort on the dependency graph.

    Returns:
        (install_order, None)  if the graph has no cycles
        (None, cycle_path)     if the graph has a cycle

    Kahn's algorithm:
    1. Compute in-degree of every node.
    2. Add all nodes with in-degree 0 to a queue.
    3. While the queue is not empty:
       a. Dequeue a node, add it to the result.
       b. For each node that depends on this node (reverse edges),
          decrement their in-degree.
       c. If any neighbor's in-degree reaches 0, enqueue it.
    4. If the result length < total nodes, there is a cycle.

    TODO: implement

    Note: For step 4, if there is a cycle, also call cycle_detector
    to find the actual cycle path for the error message.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# cycle_detector.py (inline)
# ---------------------------------------------------------------------------

# Node colors for DFS cycle detection
WHITE = 0   # unvisited
GRAY = 1    # currently in DFS call stack
BLACK = 2   # fully processed


def find_cycle(packages: dict[str, list[str]]) -> list[str] | None:
    """
    Use DFS with 3-color marking to find a cycle in the dependency graph.
    Returns the cycle path as a list of package names, or None if no cycle.

    Algorithm:
    - WHITE: node not yet visited
    - GRAY: node is in the current DFS path (ancestor in current recursion)
    - BLACK: node is fully processed (no cycle through this node)

    A cycle exists when DFS encounters a GRAY node (back edge).

    TODO: implement
    """
    raise NotImplementedError


def _dfs_find_cycle(
    node: str,
    packages: dict[str, list[str]],
    color: dict[str, int],
    path: list[str],
) -> list[str] | None:
    """
    DFS helper for cycle detection. Returns cycle path or None.
    TODO: implement
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# resolver.py — main logic
# ---------------------------------------------------------------------------

def resolve(manifest_path: str) -> None:
    """
    Main resolver function.
    Loads the manifest, runs topological sort, and prints the result.

    TODO: implement
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python resolver.py <manifest.json>")
        sys.exit(1)
    resolve(sys.argv[1])
