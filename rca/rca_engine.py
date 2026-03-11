import boto3
import json
from llm.bedrock_llm import BedrockLLM
from rag.vector_store import VectorStore
from src.pattern_detector import PatternDetector
from src.correlation_engine import CorrelationEngine

class RCAEngine:

    def __init__(self):

        self.bedrock_client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )

    def generate_ai_explanation(self, context):

        prompt = f"""
    You are a Site Reliability Engineer.

    Analyze the log evidence and produce a SHORT RCA report.

    Log Evidence:
    {context}

    Return ONLY plain text in the following format:

    Root Cause:
    (one sentence)

    Impact:
    (one sentence)

    Fix:
    • step
    • step
    • step

    Rules:
    Do NOT return code.
    Do NOT return Python variables.
    """

        response = self.bedrock_client.invoke_model(
            modelId="meta.llama3-8b-instruct-v1:0",
            body=json.dumps({
                "prompt": prompt,
                "max_gen_len": 120,
                "temperature": 0.2
            })
        )

        response_body = json.loads(response["body"].read())

        result = response_body["generation"]

        # Clean unwanted text
        result = result.replace("root_cause =", "")
        result = result.replace("impact =", "")
        result = result.replace("fix =", "")
        result = result.replace("#", "")
        result = result.replace("(", "")
        result = result.replace(")", "")
        result = result.replace('"', "")
        result = result.replace("return", "")
        result = result.strip()

        return result


    def generate_mitigation(self, context):

        prompt = f"""
        You are a Site Reliability Engineer.

        Based on the RCA context below, suggest mitigation steps.

        Context:
        {context}

        Return ONLY 3 mitigation steps in bullet format.

        Example format:

        • Step 1
        • Step 2
        • Step 3

        Rules:
        - Do NOT write code
        - Do NOT use variables
        - Do NOT return JSON
        - Only return bullet points
        """

        response = self.bedrock_client.invoke_model(
            modelId="meta.llama3-8b-instruct-v1:0",
            body=json.dumps({
                "prompt": prompt,
                "max_gen_len": 80,
                "temperature": 0.2
            })
        )

        # Convert Bedrock response
        response_body = json.loads(response["body"].read())

        result = response_body["generation"]

        # Split into lines
        lines = result.split("\n")

        # Keep only bullet points
        clean_lines = [line.strip() for line in lines if line.strip().startswith("•")]

        return "\n".join(clean_lines)

    def analyze(self, log_query):

       # Load logs from data file
        log_file = "data/logs.txt"

        logs = []
        with open(log_file, "r") as f:
            logs = f.readlines()

        # Extract only error logs
        error_lines = [log.strip() for log in logs if "ERROR" in log]
        
        # Basic log statistics
        log_stats = {
            "file_count": 2,
            "total_errors": len(error_lines)
        }
        
        # Pattern detection
        pattern_detector = PatternDetector()
        patterns = pattern_detector.detect_new_patterns(error_lines)

        # Event correlation
        correlation_engine = CorrelationEngine()
        correlations = correlation_engine.correlate_events(error_lines)

        # Default solutions based on error codes
        solutions = []

        for err in error_lines:

            if "NETWORK_DOWN" in err:
                solutions.append({
                    "error": "E_NETWORK_DOWN",
                    "solution": "Ping internal and external endpoints, verify firewall rules, check DNS resolution, test alternate network routes, and contact network operations if required."
                })

            elif "DB_FAIL" in err:
                solutions.append({
                    "error": "E_DB_FAIL",
                    "solution": "Check database connection pool usage, review recent schema changes, terminate long running queries, and verify database permissions."
                })

            elif "CONFIG_MISMATCH" in err:
                solutions.append({
                    "error": "E_CONFIG_MISMATCH",
                    "solution": "Compare configuration files across environments, validate environment variables, verify service discovery settings, and rollback recent configuration changes."
                })

        from datetime import datetime

        summary_text = f"""

        # 🔍 RCA SUMMARY

        ## ❓ Query
        {log_query}

        ## 📊 Findings
        Total Errors: {len(error_lines)}
        Log Files: {log_stats.get("file_count", "N/A")}

        ## 🚨 Errors
        """

        for i, err in enumerate(error_lines[:3], 1):
            summary_text += f"{i}. {err}\n"

        summary_text += "\n## 🛠 Recommended Fix\n"

        for sol in solutions[:5]:
            error_code = sol.get("error", "Unknown")
            solution_text = sol.get("solution", "No solution available")

            summary_text += f"\n**{error_code}**\n- {solution_text}\n"

        summary_text += f"\n---\nGenerated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        results = {
            "rca_summary": summary_text,
            "error_lines": error_lines,
            "patterns": patterns,
            "correlations": correlations,
            "solutions": solutions,
            "log_stats": log_stats
        }

        return results
                
                