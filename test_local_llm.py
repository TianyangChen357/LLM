from openai import OpenAI

# Use local SGLang endpoint (OpenAI-compatible)
client = OpenAI(
    api_key="not-needed",  # Local doesn't require API key
    base_url="http://localhost:8000/v1"  # Your local SGLang server
)

response = client.chat.completions.create(
    model="Qwen/Qwen3-14B",  # Your local model
    messages=[
        {"role": "user", "content": "hello"}
    ],
    max_tokens=100
)
print(response.choices[0].message.content)