"""Summarize a call transcript with Kimi K3 on AssemblyAI's LLM Gateway.

Usage: python summarize_call.py transcript.txt
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("LLM_GATEWAY_BASE_URL", "https://llm-gateway.assemblyai.com/v1"),
    api_key=os.environ["ASSEMBLYAI_API_KEY"],
)

SYSTEM_PROMPT = (
    "You summarize customer calls. Return three sections: Summary (3 sentences), "
    "Action items (bullets with an owner), and Open questions (bullets). "
    "Use only facts stated in the transcript."
)


def summarize(transcript: str) -> str:
    response = client.chat.completions.create(
        model="kimi-k3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript},
        ],
        max_tokens=4000,
        extra_body={
            # Retry on another model if Kimi K3 fails.
            "fallbacks": [{"model": "claude-sonnet-5-5"}],
            # Route to the provider's global endpoint at global pricing.
            # Remove this line to keep processing in the US region.
            "model_region": "global",
        },
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python summarize_call.py transcript.txt")
    with open(sys.argv[1], encoding="utf-8") as f:
        print(summarize(f.read()))
