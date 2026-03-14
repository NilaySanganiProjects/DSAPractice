# Industrial Project 6 — Mini Distributed Task Scheduler (Capstone)

**Phase:** 3 | **Week:** 23 | **Month:** 6

**Real company inspiration:** Celery (Python), BullMQ (Node.js), Apache Airflow, AWS Step Functions

---

## The Engineering Problem

You are an engineer at a fintech startup. The product has a batch processing pipeline: data ingestion jobs, transformation jobs, notification jobs. They have:

- **Priorities** — some jobs are urgent (SLA-bound) and must run before others.
- **Dependencies** — job B can only start after job A completes.
- **Retry logic** — if a job fails, retry up to 3 times with exponential backoff.
- **A worker pool** — multiple workers run concurrently; no two workers run the same job.

Your task: Build this from scratch. This project uses **almost everything** from the 6-month curriculum.

---

## System Architecture

```
Job Queue (min-heap by priority)
    ↓
Scheduler (runs the main loop)
    ↓ picks next eligible job (all dependencies met)
Worker Pool (N workers, run concurrently via threads or async)
    ↓
Job completes → mark done → unblock dependent jobs → re-enqueue eligible ones
    ↓
On failure → retry with backoff → after max retries → mark FAILED
```

---

## DSA Used (You Implement From Scratch)

| Component | DSA | Why |
|-----------|-----|-----|
| Job queue | Binary min-heap (by priority) | O(log n) enqueue and dequeue of highest-priority job |
| Dependency tracking | Adjacency list (job → list of jobs it blocks) | O(V+E) traversal when a job completes |
| Eligibility check | In-degree counter per job | When in-degree reaches 0, job is eligible to run |
| Execution order validation | Topological sort | Detect dependency cycles before scheduling begins |
| Retry scheduling | Min-heap with `(scheduled_time, job)` | Retry at `now + 2^attempt` seconds using heap |
| Worker pool | Thread pool (Python's `threading.Thread`) | Concurrent job execution |

---

## Job Specification

```python
@dataclass
class Job:
    id: str
    name: str
    priority: int           # lower number = higher priority (1 = urgent)
    dependencies: list[str] # list of job IDs that must complete first
    max_retries: int = 3
    payload: dict = field(default_factory=dict)

    # Runtime state (set by scheduler)
    status: str = "pending"    # pending, running, completed, failed
    attempt: int = 0
    result: any = None
```

---

## Project Structure

```
task-scheduler/
├── README.md               # You write this at the end
├── SPEC.md                 # This file
├── job.py                  # Job dataclass and status enum
├── heap.py                 # Binary min-heap (reuse or adapt from Project 4)
├── scheduler.py            # Main scheduler logic
├── worker.py               # Worker pool and job execution
├── dependency_graph.py     # Dependency tracking and topological sort
├── benchmark.py            # Schedule 1000 jobs, measure throughput
├── test_scheduler.py       # Correctness tests
└── examples/
    ├── simple_pipeline.py  # 5 jobs, linear dependency chain
    ├── parallel_jobs.py    # 10 jobs, parallel execution
    └── retry_demo.py       # Jobs that fail and retry
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Implement `Job` dataclass and `Status` enum (write `job.py`)
- [ ] **Milestone 2:** Implement the `MinHeap` with `(priority, timestamp, job)` tuples — timestamp breaks ties (write `heap.py`)
- [ ] **Milestone 3:** Implement `DependencyGraph` with topological sort and cycle detection (write `dependency_graph.py`)
- [ ] **Milestone 4:** Implement `Scheduler.schedule(jobs)` — validates dependencies, builds initial queue
- [ ] **Milestone 5:** Implement `Scheduler.run(workers=4)` — main scheduling loop with worker pool
- [ ] **Milestone 6:** Implement retry logic with exponential backoff in the scheduler
- [ ] **Milestone 7:** Run `simple_pipeline.py`, `parallel_jobs.py`, and `retry_demo.py`
- [ ] **Milestone 8:** Write `test_scheduler.py`
- [ ] **Milestone 9:** Run `benchmark.py`
- [ ] **Milestone 10:** Write `README.md`

---

## Capstone Challenge

At the end of Week 23, AXIOM gives you a new requirement that was **not in the original spec**:

> "We need to support job timeouts. If a job runs for more than `timeout_seconds`, kill it and mark it as failed (count as an attempt)."

Implement this without redesigning the scheduler from scratch. Can you extend what you have?

---

## README Requirements (You Write This)

1. Draw the architecture diagram (ASCII or described). Show how data flows from job submission to completion.
2. For each DSA component, explain: what problem does it solve, and what would break if you replaced it with a simpler structure (e.g., a list instead of a heap)?
3. What is the time complexity of `Scheduler.run()` per job completion event?
4. How does your retry logic work? Show the backoff schedule for a job with `max_retries=3`.
5. If you were deploying this to production, what are the 3 biggest things you would change? (Think: persistence, distributed workers, exactly-once delivery)
6. This is your capstone. Write a 3-sentence "engineering decision log" for the 3 most important design choices you made.
