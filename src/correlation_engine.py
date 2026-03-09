class CorrelationEngine:

    def correlate_events(self, logs):
        correlations = []

        for i in range(len(logs) - 1):
            current_log = logs[i].lower()
            next_log = logs[i + 1].lower()

            # Example correlation rules
            if "cpu" in current_log and "memory" in next_log:
                correlations.append("CPU spike likely caused memory pressure")

            if "memory" in current_log and "restart" in next_log:
                correlations.append("Memory overflow likely caused service restart")

            if "Network timeout triggered retry mechanism" not in correlations:
                correlations.append("Network timeout triggered retry mechanism")

        return correlations