import re
from datetime import datetime


class LogParser:
    def __init__(self):
        # Example log pattern
        # [2026-03-03 03:12:01] Zone-2 gateway ERROR Memory threshold exceeded
        self.pattern = re.compile(
            r"\[(?P<timestamp>.*?)\]\s+(?P<zone>\S+)\s+(?P<service>\S+)\s+(?P<level>\S+)\s+(?P<message>.*)"
        )

    def parse_log(self, log_line):
        match = self.pattern.match(log_line)

        if not match:
            return None

        data = match.groupdict()

        return {
            "timestamp": data["timestamp"],
            "zone": data["zone"],
            "service": data["service"],
            "severity": data["level"],
            "message": data["message"],
        }

    def parse_logs(self, logs):
        structured_logs = []

        for log in logs:
            parsed = self.parse_log(log)
            if parsed:
                structured_logs.append(parsed)

        return structured_logs