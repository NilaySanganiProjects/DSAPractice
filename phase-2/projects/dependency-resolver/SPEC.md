# Industrial Project 3 — Dependency Resolver

**Phase:** 2 | **Week:** 12 | **Month:** 3

**Real company inspiration:** npm (Node.js), pip (Python), Cargo (Rust), Gradle (Java)

---

## The Engineering Problem

You are an engineer at a developer tools company building a package manager CLI. Users define their project dependencies in a manifest file. Your job: given a set of packages and their dependencies, compute a valid installation order — or report a conflict if the dependency graph contains a cycle.

This is exactly what `npm install`, `pip install`, and `cargo build` do before they download anything.

---

## System Requirements

### Input Format

A JSON manifest file:

```json
{
  "packages": {
    "app": ["react", "lodash"],
    "react": ["react-dom"],
    "react-dom": ["scheduler"],
    "scheduler": [],
    "lodash": [],
    "circular-a": ["circular-b"],
    "circular-b": ["circular-a"]
  }
}
```

Each key is a package name. Each value is a list of its direct dependencies.

### Output

**Case 1 — Valid graph (no cycles):**
```
Install order: scheduler, react-dom, react, lodash, app
```

**Case 2 — Cycle detected:**
```
CONFLICT: Circular dependency detected
  circular-a → circular-b → circular-a
```

---

## DSA Requirements (You Implement From Scratch)

| Requirement | DSA Used | Why |
|-------------|----------|-----|
| Build dependency graph | Adjacency list (dict of lists) | O(V+E) space, standard graph representation |
| Compute install order | Topological Sort (Kahn's BFS algorithm) | Processes nodes with no remaining dependencies first |
| Detect cycles | DFS with 3-color marking (white/gray/black) | Any gray→gray back edge means cycle |
| Report cycle path | DFS with parent tracking | Reconstruct the cycle for the error message |

**You may NOT use:** `networkx`, `graphlib` (Python 3.9+), or any library that implements topological sort for you.

---

## Project Structure

```
dependency-resolver/
├── README.md               # You write this at the end
├── SPEC.md                 # This file
├── resolver.py             # Main implementation
├── graph.py                # Graph building from manifest
├── topo_sort.py            # Topological sort (Kahn's algorithm)
├── cycle_detector.py       # DFS cycle detection with path reporting
├── benchmark.py            # Your benchmark script
├── test_resolver.py        # Correctness tests
└── manifests/
    ├── simple.json         # 5-package graph, no cycles
    ├── complex.json        # 20-package graph, no cycles
    └── circular.json       # Graph with a cycle
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Parse the JSON manifest into an adjacency list (write `graph.py`)
- [ ] **Milestone 2:** Implement Kahn's topological sort (write `topo_sort.py`)
- [ ] **Milestone 3:** Implement DFS cycle detection with path reporting (write `cycle_detector.py`)
- [ ] **Milestone 4:** Wire everything in `resolver.py` — takes a manifest path, prints install order or conflict
- [ ] **Milestone 5:** Write the 3 test manifests and verify correct output for each
- [ ] **Milestone 6:** Write `test_resolver.py` with at least 6 test cases
- [ ] **Milestone 7:** Write `benchmark.py` — test on a generated 1000-package graph
- [ ] **Milestone 8:** Write `README.md`

---

## Benchmark Target

On a graph with 1,000 packages and ~3,000 dependency edges, resolve in under 10ms.

---

## README Requirements (You Write This)

1. What is topological sort and why is it the right algorithm for dependency resolution?
2. Why does Kahn's algorithm (BFS-based) detect cycles implicitly? (Hint: what happens to nodes that are part of a cycle when you process in-degree-0 nodes first?)
3. What is the time and space complexity of your resolver on a graph with V packages and E dependencies?
4. What would you change to handle version constraints (e.g., `"react": "^18.0.0"`)? Describe the algorithm change in 3 sentences.
5. Name one real bug that has occurred in the wild due to a circular dependency in a popular package manager.
