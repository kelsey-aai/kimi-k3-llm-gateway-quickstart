import os

from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("LLM_GATEWAY_BASE_URL", "https://llm-gateway.assemblyai.com/v1"),
    api_key=os.environ["ASSEMBLYAI_API_KEY"],
)

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {"role": "user", "content": "In two sentences, explain what a context window is."}
    ],
    max_tokens=4000,
)

print(response.choices[0].message.content)
print(response.usage)
