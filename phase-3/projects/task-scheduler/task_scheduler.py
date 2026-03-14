"""
Mini Distributed Task Scheduler — Starter Skeleton
Phase 3, Week 23 — Industrial Project 6 (Capstone)

This is the capstone project. It uses almost every DSA concept
from the 6-month curriculum:
  - Binary min-heap (priority queue)
  - Topological sort (dependency ordering)
  - DFS cycle detection
  - Thread pool (concurrency)
  - Retry with exponential backoff

Implement each section marked with TODO.
"""

from __future__ import annotations
import time
import threading
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# job.py
# ---------------------------------------------------------------------------

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


@dataclass
class Job:
    """Represents a single unit of work in the scheduler."""
    id: str
    name: str
    priority: int                   # lower = higher priority (1 = most urgent)
    dependencies: list[str]         # job IDs that must complete before this job runs
    execute: callable               # the function to call to run this job
    max_retries: int = 3
    timeout_seconds: float = 30.0
    payload: dict = field(default_factory=dict)

    # Runtime state — set by the scheduler, do not set manually
    status: Status = Status.PENDING
    attempt: int = 0
    result: Any = None
    error: Exception | None = None
    scheduled_at: float = 0.0      # Unix timestamp for retry scheduling


# ---------------------------------------------------------------------------
# heap.py — reuse/adapt from Project 4
# ---------------------------------------------------------------------------

class MinHeap:
    """
    Binary min-heap storing (priority, timestamp, job) tuples.
    timestamp breaks ties by insertion order (FIFO within same priority).
    """

    def __init__(self):
        raise NotImplementedError

    def push(self, priority: int, job: Job) -> None:
        """Push job with given priority. Use time.monotonic() as tiebreaker."""
        raise NotImplementedError

    def pop(self) -> Job:
        """Pop and return the highest-priority (lowest priority number) job."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        return len(self) == 0


# ---------------------------------------------------------------------------
# dependency_graph.py
# ---------------------------------------------------------------------------

class DependencyGraph:
    """
    Manages job dependencies and determines execution eligibility.

    - adjacency: {job_id: [job_ids_that_are_blocked_by_this_job]}
    - in_degree: {job_id: number_of_uncompleted_dependencies}
    """

    def __init__(self, jobs: list[Job]):
        """
        Build the dependency graph from a list of jobs.

        TODO: implement
        - Build adjacency list: if B depends on A, add B to adjacency[A]
        - Compute in_degree for each job
        - Validate: all dependency IDs exist in the job list
        """
        raise NotImplementedError

    def has_cycle(self) -> bool | list[str]:
        """
        Check for cycles using DFS with 3-color marking.
        Returns False if no cycle, or a list of job IDs forming the cycle.

        TODO: implement (reuse logic from Project 3)
        """
        raise NotImplementedError

    def get_eligible_jobs(self) -> list[str]:
        """
        Return a list of job IDs with in_degree == 0 (no remaining dependencies).
        These jobs are ready to be enqueued.

        TODO: implement
        """
        raise NotImplementedError

    def mark_completed(self, job_id: str) -> list[str]:
        """
        Mark `job_id` as completed. Decrement in_degree of all jobs
        that were waiting on it. Return the list of job IDs that
        are now newly eligible (in_degree just reached 0).

        TODO: implement
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# worker.py
# ---------------------------------------------------------------------------

class Worker(threading.Thread):
    """
    A worker thread that pulls jobs from a queue and executes them.
    Reports results back to the scheduler via a callback.
    """

    def __init__(self, worker_id: int, job_queue: MinHeap, on_complete: callable, lock: threading.Lock):
        super().__init__(daemon=True)
        self.worker_id = worker_id
        self.job_queue = job_queue
        self.on_complete = on_complete
        self.lock = lock
        self._stop_event = threading.Event()

    def run(self) -> None:
        """
        Main worker loop.
        - Acquire the lock, check for a job, release lock.
        - Execute the job (without holding the lock).
        - Call on_complete(job, success, error).
        - Sleep briefly if no job available.

        TODO: implement
        """
        raise NotImplementedError

    def stop(self) -> None:
        self._stop_event.set()


# ---------------------------------------------------------------------------
# scheduler.py
# ---------------------------------------------------------------------------

class Scheduler:
    """
    Main task scheduler.

    Usage:
        scheduler = Scheduler(workers=4)
        scheduler.schedule(jobs)
        scheduler.run()  # blocks until all jobs complete or fail
    """

    def __init__(self, num_workers: int = 4):
        self.num_workers = num_workers
        self._job_map: dict[str, Job] = {}
        self._queue = MinHeap()
        self._dep_graph: DependencyGraph | None = None
        self._lock = threading.Lock()
        self._completed = 0
        self._failed = 0

    def schedule(self, jobs: list[Job]) -> None:
        """
        Register all jobs with the scheduler.
        Validate: no cycles in dependencies.
        Enqueue all jobs with in_degree == 0.

        TODO: implement

        Raises ValueError if a cycle is detected.
        """
        raise NotImplementedError

    def run(self) -> dict[str, Job]:
        """
        Start the worker pool and run until all jobs are completed or failed.
        Returns the final job map {job_id: job} for inspection.

        TODO: implement

        Loop:
        1. Start num_workers Worker threads.
        2. Wait until all jobs are in a terminal state (completed or failed).
        3. Stop all workers.
        4. Return self._job_map.
        """
        raise NotImplementedError

    def _on_job_complete(self, job: Job, success: bool, error: Exception | None) -> None:
        """
        Called by a worker when a job finishes.

        If success:
          - Mark job as COMPLETED.
          - Find newly eligible jobs and enqueue them.

        If failure:
          - If job.attempt < job.max_retries: schedule retry with backoff.
          - Else: mark job as FAILED.

        TODO: implement (call with self._lock held or acquire it here)
        """
        raise NotImplementedError

    def _schedule_retry(self, job: Job) -> None:
        """
        Schedule a retry for `job` with exponential backoff.
        Backoff: 2^(attempt) seconds.
        Re-enqueue the job after the backoff delay.

        TODO: implement
        """
        raise NotImplementedError

    def print_summary(self) -> None:
        """Print a summary of job statuses after run() completes."""
        print("\n--- Scheduler Summary ---")
        for job in self._job_map.values():
            print(f"  {job.id:20s} {job.status.value:12s} (attempts: {job.attempt})")
        print(f"\nCompleted: {self._completed} | Failed: {self._failed}")
        print("-------------------------\n")
