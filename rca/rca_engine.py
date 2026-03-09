from llm.bedrock_llm import BedrockLLM
from rag.vector_store import VectorStore
from src.pattern_detector import PatternDetector
from src.correlation_engine import CorrelationEngine

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
        
        pattern_detector = PatternDetector()
        correlation_engine = CorrelationEngine()

        patterns = pattern_detector.detect_new_patterns(logs)
        correlations = correlation_engine.correlate_events(logs)

        results = {
            "anomaly": anomaly_results,
            "patterns": patterns,
            "correlations": correlations,
            "logs": logs,
            "rca_summary": summary
        }
        return self.llm.generate(prompt)
    
       