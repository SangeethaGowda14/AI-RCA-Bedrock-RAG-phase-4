import boto3
import json

class BedrockLLM:
    def __init__(self):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )
        self.model_id = "nvidia.nemotron-nano-12b-v2"

    def generate(self, prompt: str) -> str:
        response = self.client.invoke_model(
            modelId=self.model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt}
                        ]
                    }
                ],
                "max_tokens": 300,
                "temperature": 0.3
            })
        )

        result = json.loads(response["body"].read())
        return result["choices"][0]["message"]["content"]