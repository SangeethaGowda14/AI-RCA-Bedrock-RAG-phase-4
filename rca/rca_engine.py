from llm.bedrock_llm import BedrockLLM
from rag.vector_store import VectorStore

class RCAEngine:
    def __init__(self):
        self.vector_store = VectorStore()
        self.llm = BedrockLLM()

    def analyze(self, log_text: str):
        context = self.vector_store.retrieve(log_text)

        prompt = f"""
You are an AI system performing Root Cause Analysis.

Logs:
{context}

Task:
Explain the root cause of the issue in simple technical language.
Provide causes and suggested fixes.
"""

        return self.llm.generate(prompt)