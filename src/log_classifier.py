import re

class LogClassifier:

    def classify(self, log_line):

        log_line = log_line.lower()

        if "critical" in log_line:
            return "CRITICAL"

        elif "error" in log_line:
            return "ERROR"

        elif "warning" in log_line:
            return "WARNING"

        else:
            return "INFO"