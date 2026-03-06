from pattern_detector import PatternDetector

logs = [
    "ERROR gateway restart",
    "ERROR gateway restart",
    "WARNING CPU spike",
    "CRITICAL memory overflow detected"
]

detector = PatternDetector()

anomalies = detector.detect_new_patterns(logs)

print("Detected anomalies:")
print(anomalies)