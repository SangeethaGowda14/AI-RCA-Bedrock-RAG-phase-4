import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

response = client.invoke_model(
    modelId="nvidia.nemotron-nano-12b-v2",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Explain artificial intelligence in simple words"}
                ]
            }
        ],
        "max_tokens": 200,
        "temperature": 0.3
    })
)

result = json.loads(response["body"].read())
print(result)