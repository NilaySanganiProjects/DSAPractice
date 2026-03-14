# Industrial Project 1 — Real-time Log Anomaly Detector

**Phase:** 1 | **Week:** 3 | **Month:** 1

**Real company inspiration:** Splunk, Datadog, AWS CloudWatch Logs Insights

---

## The Engineering Problem

You are a backend engineer at a mid-size SaaS company. Your servers generate thousands of log lines per minute. Right now, when an anomaly happens (a sudden spike in 5xx errors, a single IP hammering the API), your on-call engineer finds out 20 minutes later via an alert from a third-party service.

Your task: Build a service that reads a stream of log lines, detects anomalies in real time, and emits alerts — **with zero external dependencies**.

---

## System Requirements

### Input

The service reads log lines from stdin (simulating a stream). Each line is in Apache Common Log Format:

```
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
192.168.1.1 - - [10/Oct/2000:13:55:37 -0700] "POST /api/login HTTP/1.1" 500 512
```

Fields: `ip`, `user`, `timestamp`, `method`, `path`, `status_code`, `response_size`

### Anomaly Detection Rules

1. **Error Spike (Sliding Window):** If more than `ERROR_THRESHOLD` (default: 10) requests with status codes 5xx are seen within a `WINDOW_SECONDS` (default: 60) second sliding window, emit an alert:
   ```
   ALERT: Error spike detected — 15 errors in last 60 seconds
   ```

2. **IP Abuse (Frequency Map):** If a single IP makes more than `IP_THRESHOLD` (default: 100) requests within `WINDOW_SECONDS`, emit an alert:
   ```
   ALERT: Suspicious IP 192.168.1.1 — 143 requests in last 60 seconds
   ```

### Output

Print alerts to stdout. Continue processing (do not stop on first alert).

---

## DSA Requirements (You Implement From Scratch)

| Requirement | DSA Used | Why |
|-------------|----------|-----|
| Error spike detection | Sliding window (deque of timestamps) | O(1) amortized per log line; no rescanning the window |
| IP frequency tracking | Hashmap `{ip: deque[timestamps]}` | O(1) lookup per IP; window maintained per IP |

**You must implement your own deque** for the sliding window (a Python `list` with head/tail index tracking or a custom linked-list node — no `collections.deque`). This is a learning exercise: the goal is to understand how a deque enables O(1) amortized window maintenance. Once your implementation passes the benchmark, AXIOM will show you how `collections.deque` compares.

**You may NOT use:** `collections.deque`, external time-series libraries, or any library that implements the sliding window for you.

**You may use:** Python's built-in `dict` (this is the hashmap — implementing a hash function from scratch is not the goal here), file I/O, `time`, `sys`.

---

## Project Structure

```
log-anomaly-detector/
├── README.md                  # You write this at the end
├── SPEC.md                    # This file
├── detector.py                # Your main implementation
├── parser.py                  # Log line parser
├── sliding_window.py          # Your sliding window implementation
├── ip_tracker.py              # Your IP frequency tracker
├── benchmark.py               # Your benchmark script
├── test_logs/
│   ├── normal_traffic.log     # Sample input: normal traffic
│   ├── error_spike.log        # Sample input: triggers error spike alert
│   └── ip_abuse.log           # Sample input: triggers IP abuse alert
└── sample_output.txt          # Expected output for each test log
```

---

## Milestone Checklist

- [ ] **Milestone 1:** Parse a log line into its fields (write `parser.py`)
- [ ] **Milestone 2:** Implement a sliding window that tracks timestamps and evicts old entries (write `sliding_window.py`)
- [ ] **Milestone 3:** Implement the IP frequency tracker using the sliding window (write `ip_tracker.py`)
- [ ] **Milestone 4:** Wire everything into `detector.py` — reads stdin, emits alerts
- [ ] **Milestone 5:** Create the 3 test log files and verify correct alert behavior
- [ ] **Milestone 6:** Write `benchmark.py` — generate 100k log lines and measure throughput (lines/sec)
- [ ] **Milestone 7:** Write `README.md` explaining the system design decision

---

## Benchmark Target

Your detector must process at least **50,000 log lines per second** on a modern laptop (single-threaded).

Run the benchmark with:
```bash
python benchmark.py
```

Expected output:
```
Processed 100,000 lines in 1.87 seconds
Throughput: 53,475 lines/sec
Alerts emitted: 3
```

---

## README Requirements (You Write This)

Your `README.md` must answer these questions:

1. **What problem does this solve?** (1 paragraph, written as if explaining to a new engineer on the team)
2. **What DSA decision did you make and why?** Explain why a sliding window is better than recomputing the count from scratch on every log line. Give the complexity comparison.
3. **What is the time and space complexity of your solution?** Per log line. For the entire stream of N lines.
4. **What would you change if you had to handle 1 million lines/second?** (Think: parallelism, sharding by IP, approximate counting with Count-Min Sketch)
5. **How would you explain this system to an interviewer in 2 minutes?**

---

## AXIOM Builder Mode Notes

When you start working on this project, tell AXIOM: `mode: builder`

AXIOM will act as the Staff Engineer reviewing your design decisions. It will not tell you how to implement the sliding window — it will ask you engineering questions:

- "The requirement says O(1) per log line. Walk me through how your deque achieves that."
- "What happens if two log lines have the same timestamp?"
- "Your IP tracker uses a dict of deques. What is the memory usage if you have 1 million unique IPs over 24 hours?"
