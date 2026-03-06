import numpy as np
from anomaly_detector import AnomalyDetector

# Example log features
features = np.array([
    [10, 0.1],
    [12, 0.2],
    [11, 0.15],
    [200, 3.5]   # anomaly
])

detector = AnomalyDetector()

detector.train(features)

results = detector.detect(features)

for r in results:
    print(r)