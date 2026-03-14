"""
Benchmark script for the Log Anomaly Detector.
Run with: python benchmark.py

This script:
1. Generates 100,000 synthetic log lines
2. Feeds them through the detector
3. Measures throughput (lines/sec)
4. Verifies that expected alerts are triggered

TODO: This script will fail to run until you implement detector.py.
      Implement the detector first, then run this to check performance.
"""

import time
import random
from detector import AnomalyDetector

# ---------------------------------------------------------------------------
# Log line generator
# ---------------------------------------------------------------------------

NORMAL_IPS = [f"10.0.{i}.{j}" for i in range(10) for j in range(10)]
ABUSIVE_IP = "192.168.99.99"

PATHS = ["/api/users", "/api/posts", "/api/comments", "/api/login", "/health"]
METHODS = ["GET", "POST", "PUT", "DELETE"]


def generate_log_line(ip: str, timestamp: float, status: int = 200) -> str:
    """Generate a synthetic Apache log line."""
    from datetime import datetime, timezone
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    ts_str = dt.strftime("%d/%b/%Y:%H:%M:%S +0000")
    method = random.choice(METHODS)
    path = random.choice(PATHS)
    size = random.randint(128, 4096)
    return f'{ip} - - [{ts_str}] "{method} {path} HTTP/1.1" {status} {size}'


def generate_normal_traffic(n: int, base_ts: float) -> list[str]:
    """Generate n lines of normal traffic (200 responses, varied IPs)."""
    lines = []
    for i in range(n):
        ip = random.choice(NORMAL_IPS)
        ts = base_ts + i * 0.01  # 100 lines/second
        lines.append(generate_log_line(ip, ts, status=200))
    return lines


def generate_error_spike(n: int, base_ts: float) -> list[str]:
    """Generate n 500-error lines from varied IPs within a short window."""
    lines = []
    for i in range(n):
        ip = random.choice(NORMAL_IPS)
        ts = base_ts + i * 0.5  # spread over n/2 seconds
        lines.append(generate_log_line(ip, ts, status=500))
    return lines


def generate_ip_abuse(n: int, base_ts: float, abusive_ip: str) -> list[str]:
    """Generate n lines from a single abusive IP."""
    lines = []
    for i in range(n):
        ts = base_ts + i * 0.3
        lines.append(generate_log_line(abusive_ip, ts, status=200))
    return lines


# ---------------------------------------------------------------------------
# Benchmark
# ---------------------------------------------------------------------------

def run_benchmark():
    print("=" * 60)
    print("Log Anomaly Detector — Benchmark")
    print("=" * 60)

    # Build a 100k-line dataset with embedded anomalies
    base_ts = 1_700_000_000.0  # arbitrary Unix timestamp
    lines = []

    # 80k lines of normal traffic
    lines += generate_normal_traffic(80_000, base_ts)

    # 15 error-spike lines within a 60s window (triggers alert at threshold=10)
    lines += generate_error_spike(15, base_ts + 10)

    # 150 requests from a single abusive IP within 60s (triggers alert at threshold=100)
    lines += generate_ip_abuse(150, base_ts + 20, ABUSIVE_IP)

    # Shuffle to simulate real stream ordering
    random.shuffle(lines)

    total_lines = len(lines)
    print(f"Dataset: {total_lines:,} log lines")
    print()

    detector = AnomalyDetector()
    alerts = []

    start = time.perf_counter()
    for line in lines:
        emitted = detector.process_line(line)
        alerts.extend(emitted)
    elapsed = time.perf_counter() - start

    throughput = total_lines / elapsed
    print(f"Processed {total_lines:,} lines in {elapsed:.3f} seconds")
    print(f"Throughput: {throughput:,.0f} lines/sec")
    print(f"Alerts emitted: {len(alerts)}")
    print()

    # Validate correctness
    passed = True

    if throughput < 50_000:
        print("FAIL: Throughput below 50,000 lines/sec target")
        passed = False
    else:
        print(f"PASS: Throughput {throughput:,.0f} >= 50,000 lines/sec")

    if len(alerts) == 0:
        print("FAIL: No alerts were emitted — check your threshold logic")
        passed = False
    else:
        print(f"PASS: At least one alert emitted")

    print()
    if passed:
        print("All benchmarks passed.")
    else:
        print("One or more benchmarks failed. See above.")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmark()
