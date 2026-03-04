from log_parser import LogParser

logs = [
    "[2026-03-03 03:10:00] Zone-2 gateway INFO Service started",
    "[2026-03-03 03:11:10] Zone-2 gateway WARNING Memory usage high",
    "[2026-03-03 03:12:01] Zone-2 gateway ERROR Memory threshold exceeded"
]

parser = LogParser()

structured = parser.parse_logs(logs)

for log in structured:
    print(log)