from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.documents = []
        self._load_logs()
    
    def search(self, query, k=3):
        docs = self.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]

    def _load_logs(self):
        with open("data/logs.txt", "r") as f:
            logs = f.readlines()

        embeddings = self.model.encode(logs)
        self.index.add(np.array(embeddings))
        self.documents = logs

    def retrieve(self, query, k=3):
        query_embedding = self.model.encode([query])
        _, indices = self.index.search(np.array(query_embedding), k)

        return "\n".join([self.documents[i] for i in indices[0]])