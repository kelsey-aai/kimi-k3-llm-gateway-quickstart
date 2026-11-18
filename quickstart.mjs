import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env.LLM_GATEWAY_BASE_URL ?? "https://llm-gateway.assemblyai.com/v1",
  apiKey: process.env.ASSEMBLYAI_API_KEY,
});

const response = await client.chat.completions.create({
  model: "kimi-k3",
  messages: [
    { role: "user", content: "In two sentences, explain what a context window is." },
  ],
  max_tokens: 4000,
});

console.log(response.choices[0].message.content);
console.log(response.usage);
