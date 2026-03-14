# Phase 2 — Week 13: Graphs — Dijkstra & Union-Find

## Theme
**"A graph is just a generalized tree — with cycles allowed and parent pointers removed. Everything you know about trees applies to graphs, plus one new problem: cycles."**

---

## Real-World Context

**Google Maps routing (Dijkstra):** When Google Maps finds the shortest path from A to B, it runs a variant of Dijkstra's algorithm on a graph of intersections (nodes) and roads (edges with distance/time weights). Your Day 3 problem is exactly this.

**Social network components (Union-Find):** Facebook's "People You May Know" feature groups users into connected components. If you and a friend have a mutual connection, you are in the same component. Union-Find (Disjoint Set Union) does this in near O(1) per operation with path compression and union by rank.

---

## Weekly Schedule

| Day | Problem | Pattern | Difficulty |
|-----|---------|---------|-----------|
| 1 | Number of Islands (LC 200) | DFS/BFS on grid graph | Medium |
| 2 | Clone Graph (LC 133) | BFS with hashmap | Medium |
| 3 | Network Delay Time (LC 743) | Dijkstra's algorithm | Medium |
| 4 | Number of Connected Components (LC 323) | Union-Find | Medium |
| 5 | Redundant Connection (LC 684) | Union-Find cycle detection | Medium |

---

## Day 3 — Network Delay Time (Dijkstra)

### Problem Statement

You are given a network of `n` nodes labeled `1` to `n` and a list of travel times as directed edges `times[i] = (u, v, w)` where `u` is the source node, `v` is the target node, and `w` is the travel time. You send a signal from node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. Return -1 if impossible.

**Your task:** Create `phase-2/week-13/day3_network_delay.py`.

**Before coding:** Dijkstra uses a min-heap (priority queue). In Python you will use `heapq`. The algorithm: start at `k`, greedily visit the nearest unvisited node, relax its neighbors. Why does the greedy choice work?

**AXIOM question:** What property of the edge weights makes Dijkstra correct? (Hint: what breaks if a weight is negative?)

---

## Days 1, 2, 4, 5

**Your task:** Create `phase-2/week-13/day{N}_{name}.py` for each remaining problem.

---

## Week 13 Wrap-Up

Update `/dsa-journal/WEEK_13_REPORT.md`.

### Complexity Quiz

| Problem | Optimal Time | Optimal Space |
|---------|--------------|---------------|
| Number of Islands | O(m·n) | O(m·n) |
| Clone Graph | O(V+E) | O(V) |
| Network Delay (Dijkstra) | O((V+E) log V) | O(V+E) |
| Connected Components | O(n·α(n)) amortized | O(n) |
| Redundant Connection | O(n·α(n)) amortized | O(n) |

---

## Notes & Observations

> (Paste AXIOM feedback here.)
