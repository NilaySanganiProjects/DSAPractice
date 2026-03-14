# Industrial Project 4 — Route Optimizer Microservice

**Phase:** 2 | **Week:** 16 | **Month:** 4

**Real company inspiration:** Google Maps, Uber routing engine, DoorDash delivery optimization, Waze

---

## The Engineering Problem

You are a backend engineer at a last-mile delivery startup. The company has a graph of city nodes (warehouses, drop-off points, intersections) connected by road segments with two weights: distance (km) and estimated travel time (minutes, time-of-day-aware). Given a start and end node, find the optimal route and expose it as an API.

You will implement two algorithms and benchmark them:
1. **Dijkstra's algorithm** — exact shortest path, O((V+E) log V)
2. **A\* heuristic search** — guided by a heuristic (straight-line distance), typically faster in practice

---

## System Requirements

### API Endpoints

```
POST /route
Body: { "start": "node_id", "end": "node_id", "optimize_for": "distance" | "time" }
Response: {
  "path": ["A", "B", "C", "D"],
  "total_distance_km": 12.4,
  "total_time_min": 18,
  "algorithm": "dijkstra",
  "computation_ms": 0.3
}

GET /benchmark?start=A&end=Z&runs=100
Response: {
  "dijkstra_avg_ms": 1.2,
  "astar_avg_ms": 0.4,
  "paths_match": true
}
```

### Graph Format

Nodes have `(x, y)` coordinates (for A* heuristic). Edges have `distance_km` and `time_min`.

```json
{
  "nodes": {
    "A": {"x": 0, "y": 0},
    "B": {"x": 1, "y": 2},
    "C": {"x": 3, "y": 1}
  },
  "edges": [
    {"from": "A", "to": "B", "distance_km": 2.2, "time_min": 4},
    {"from": "B", "to": "C", "distance_km": 2.5, "time_min": 5},
    {"from": "A", "to": "C", "distance_km": 5.0, "time_min": 8}
  ]
}
```

---

## DSA Requirements (You Implement From Scratch)

| Requirement | DSA Used | Why |
|-------------|----------|-----|
| Graph representation | Adjacency list with weight dicts | O(V+E) space, O(1) neighbor lookup |
| Shortest path | Dijkstra's algorithm | Exact optimal path with non-negative weights |
| Guided search | A* with Euclidean heuristic | Explores fewer nodes by preferring nodes closer to goal |
| Priority queue | Binary min-heap (you implement) | O(log n) extract-min for Dijkstra and A* |

**You must implement your own binary min-heap** (`heap.py`) and use it for Dijkstra and A*. Do not rely on `heapq` for the core algorithm — the goal is to understand how the heap powers the priority-queue logic in both algorithms.

**You may NOT use:** `networkx` or any graph/routing library.

**You may use:** Python's `dict`, `list`, `math`, `json`, `http.server`, and `heapq` only in the benchmark to compare your implementation's performance.

---

## Project Structure

```
route-optimizer/
├── README.md               # You write this at the end
├── SPEC.md                 # This file
├── graph.py                # Graph loading and representation
├── heap.py                 # Your binary min-heap implementation
├── dijkstra.py             # Dijkstra's algorithm
├── astar.py                # A* algorithm
├── server.py               # HTTP API server
├── benchmark.py            # Compare Dijkstra vs A* on the same graph
├── test_routing.py         # Correctness tests
└── data/
    ├── small_city.json     # Small test graph (10 nodes)
    └── city_graph.json     # Larger benchmark graph (100+ nodes)
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Implement the binary min-heap (write `heap.py`)
- [ ] **Milestone 2:** Load and represent the graph (write `graph.py`)
- [ ] **Milestone 3:** Implement Dijkstra's algorithm using your heap (write `dijkstra.py`)
- [ ] **Milestone 4:** Implement A* with Euclidean heuristic (write `astar.py`)
- [ ] **Milestone 5:** Write correctness tests (write `test_routing.py`)
- [ ] **Milestone 6:** Build the HTTP API (write `server.py`)
- [ ] **Milestone 7:** Run `benchmark.py` and compare both algorithms
- [ ] **Milestone 8:** Write `README.md`

---

## Binary Min-Heap Specification

Your heap must support:
- `push(priority, item)` — insert with a given priority
- `pop()` → `(priority, item)` — extract the item with the minimum priority
- `peek()` → `(priority, item)` — view minimum without removing

Internal storage: a list. Parent of index `i` is at `(i-1)//2`. Children of `i` are at `2*i+1` and `2*i+2`.

---

## README Requirements (You Write This)

1. Explain Dijkstra's algorithm in plain English. What guarantee does it give and under what conditions?
2. Explain A*. What is the heuristic function? What property must the heuristic satisfy to guarantee correctness (admissibility)?
3. In your benchmark, by what factor is A* faster than Dijkstra on the city graph? Why?
4. What is the time complexity of both algorithms in terms of V (vertices) and E (edges)?
5. If you had to route 10,000 delivery requests per second, what would you change? (Think: precomputed shortest paths, graph partitioning, Contraction Hierarchies)
