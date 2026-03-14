"""
Real-time Log Anomaly Detector
Phase 1, Week 3 — Industrial Project 1

Starter skeleton — implement each section marked with TODO.
Do not modify the function signatures unless AXIOM approves the change.
"""


# ---------------------------------------------------------------------------
# parser.py (inline for simplicity — extract to parser.py if you prefer)
# ---------------------------------------------------------------------------

def parse_log_line(line: str) -> dict | None:
    """
    Parse a single Apache Common Log Format line into a dict.

    Expected format:
        IP - USER [TIMESTAMP] "METHOD PATH PROTOCOL" STATUS SIZE

    Returns a dict with keys:
        ip, user, timestamp_str, method, path, protocol, status, size

    Returns None if the line cannot be parsed.

    TODO: Implement this parser using string splitting or regex.
          Do NOT use a CSV or log-parsing library.
    """
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# sliding_window.py (inline) — implement your own deque-based sliding window
# ---------------------------------------------------------------------------

class SlidingWindow:
    """
    A time-based sliding window that tracks event timestamps.

    Maintains a window of the last `window_seconds` seconds.
    When an event arrives, old events outside the window are evicted.

    DSA: This uses a deque (double-ended queue) for O(1) amortized
         append at the back and pop at the front.

    You may NOT use collections.deque — implement your own
    using a Python list with head/tail pointers (circular buffer).
    """

    def __init__(self, window_seconds: int):
        """
        TODO: Initialize internal storage.
              Consider: what is a reasonable initial capacity?
        """
        self.window_seconds = window_seconds
        # TODO: implement internal storage
        raise NotImplementedError

    def add(self, timestamp: float) -> None:
        """
        Add a new event timestamp to the window.
        Evict all timestamps older than (timestamp - window_seconds).

        TODO: implement
        """
        raise NotImplementedError

    def count(self) -> int:
        """
        Return the number of events in the current window.

        TODO: implement — this should be O(1)
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# ip_tracker.py (inline)
# ---------------------------------------------------------------------------

class IPTracker:
    """
    Tracks request frequency per IP using a sliding window per IP.

    DSA: hashmap of {ip_string: SlidingWindow}
    """

    def __init__(self, window_seconds: int, threshold: int):
        """
        TODO: Initialize the hashmap and config.
        """
        self.window_seconds = window_seconds
        self.threshold = threshold
        # TODO: implement
        raise NotImplementedError

    def record(self, ip: str, timestamp: float) -> bool:
        """
        Record a request from `ip` at `timestamp`.
        Returns True if this IP has exceeded the threshold in the window.

        TODO: implement
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# detector.py — main detection logic
# ---------------------------------------------------------------------------

ERROR_THRESHOLD = 10      # max 5xx errors in the window before alert
IP_THRESHOLD = 100        # max requests per IP in the window before alert
WINDOW_SECONDS = 60       # sliding window size in seconds


class AnomalyDetector:
    """
    Main detector class. Processes log lines and emits alerts.
    """

    def __init__(
        self,
        error_threshold: int = ERROR_THRESHOLD,
        ip_threshold: int = IP_THRESHOLD,
        window_seconds: int = WINDOW_SECONDS,
    ):
        """
        TODO: Initialize the error sliding window and IP tracker.
        """
        # TODO: implement
        raise NotImplementedError

    def process_line(self, line: str) -> list[str]:
        """
        Process a single log line.
        Returns a list of alert strings (may be empty).

        TODO:
          1. Parse the line.
          2. Record the request in the IP tracker.
          3. If status code >= 500, record it in the error window.
          4. Check thresholds and return alerts.
        """
        raise NotImplementedError

    def run(self, stream) -> None:
        """
        Read log lines from `stream` (e.g., sys.stdin or a file object).
        Print each alert to stdout.

        TODO: implement the main loop.
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    detector = AnomalyDetector()
    detector.run(sys.stdin)
