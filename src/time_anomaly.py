import numpy as np

class TimeSeriesAnomaly:

    def detect_spike(self, error_counts):

        mean = np.mean(error_counts)
        std = np.std(error_counts)

        threshold = mean + 2 * std

        anomalies = []

        for i, value in enumerate(error_counts):
            if value > threshold:
                anomalies.append((i, value))

        return anomalies