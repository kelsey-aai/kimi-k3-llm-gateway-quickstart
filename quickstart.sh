#!/usr/bin/env bash
set -euo pipefail

curl -s "${LLM_GATEWAY_BASE_URL:-https://llm-gateway.assemblyai.com/v1}/chat/completions" \
  -H "Authorization: $ASSEMBLYAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k3",
    "messages": [
      {"role": "user", "content": "In two sentences, explain what a context window is."}
    ],
    "max_tokens": 4000
  }'
