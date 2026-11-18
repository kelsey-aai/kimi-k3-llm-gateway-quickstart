# Kimi K3 API quickstart (AssemblyAI LLM Gateway)

Call Moonshot AI's Kimi K3 (`kimi-k3`) through AssemblyAI's OpenAI-compatible LLM Gateway, in Python, JavaScript and curl. Companion code for the blog post [How to use the Kimi K3 API](https://www.assemblyai.com/blog/kimi-k3-api).

## What's here

| File | What it does |
| --- | --- |
| `quickstart.py` | One chat completion with the OpenAI Python SDK |
| `quickstart.mjs` | The same request with the OpenAI Node SDK |
| `quickstart.sh` | The same request with curl |
| `summarize_call.py` | Summarizes a call transcript, with a fallback model and global routing |
| `sample_transcript.txt` | A short support-call transcript to try it on |

## Setup

1. Get an AssemblyAI API key from the [dashboard](https://www.assemblyai.com/dashboard).
2. Copy `.env.example` to `.env` and fill in `ASSEMBLYAI_API_KEY`, or export it in your shell.

### Python

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ASSEMBLYAI_API_KEY=your_key
python quickstart.py
python summarize_call.py sample_transcript.txt
```

### JavaScript (Node 18+)

```bash
npm install
export ASSEMBLYAI_API_KEY=your_key
node quickstart.mjs
```

### curl

```bash
export ASSEMBLYAI_API_KEY=your_key
./quickstart.sh
```

## Notes

- Base URL: `https://llm-gateway.assemblyai.com/v1`. Kimi K3 runs in the US region or through global routing (`"model_region": "global"`). It is not on the EU endpoint.
- Supported parameters for `kimi-k3`: `max_tokens`, `tools`, `tool_choice`, `response_format`, `stream`, `reasoning_effort`. `temperature` is not in the list, so the samples leave it out.
- Kimi K3 always reasons before it answers, so leave headroom in `max_tokens`. If you don't set it, the gateway reserves 8,000 output tokens against your rate limit.
- Default provider is AWS Bedrock (on by default). Fireworks AI also serves the model and is opt-in under Data Controls in the dashboard.
- Current price, context window and benchmark data: `GET https://llm-gateway.assemblyai.com/v1/models` (public, no key) or the [model catalog](https://www.assemblyai.com/products/llm-gateway/models).

## License

MIT
