from sklearn.cluster import DBSCAN
from sentence_transformers import SentenceTransformer

class PatternDetector:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def detect_new_patterns(self, logs):

        embeddings = self.model.encode(logs)

        clustering = DBSCAN(eps=0.5, min_samples=2).fit(embeddings)

        labels = clustering.labels_

        anomalies = []

        for i, label in enumerate(labels):
            if label == -1:
                anomalies.append(logs[i])

        return anomalies