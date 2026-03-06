import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)

    def train(self, features):
        """
        Train anomaly detection model
        """
        self.model.fit(features)

    def detect(self, features):
        """
        Detect anomalies
        Returns:
        -1 = anomaly
         1 = normal
        """
        predictions = self.model.predict(features)

        results = []
        for i, pred in enumerate(predictions):
            results.append({
                "index": i,
                "status": "ANOMALY" if pred == -1 else "NORMAL"
            })

        return results