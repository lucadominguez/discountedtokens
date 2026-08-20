# DiscountedTokens — Cheap GPT-5.x API

[![Live](https://img.shields.io/badge/live-discountedtokens.com-blue)](https://discountedtokens.com)
[![Stripe](https://img.shields.io/badge/payments-Stripe-green)](https://discountedtokens.com/guest)
[![Harnesses](https://img.shields.io/badge/OpenAI%20%2B%20Anthropic%20%2B%20Responses-compatible-purple)](https://discountedtokens.com/docs)

**Frontier GPT-5.x models at up to 84% under OpenRouter list — one key for every harness. Instant credits, no signup for agents.**

Buy credits by card (Stripe) or crypto (USDT/USDC). OpenAI-compatible, Anthropic-compatible, and Responses (Codex/JCode) endpoints from a single base URL.

Market reference = **real OpenRouter published list price** (fetched 2026-08-20), so every savings figure is verifiable dollars against a real published price — not a tuned comparison.

## Quick start (60 seconds)

```bash
# 1. Buy credits — https://discountedtokens.com/guest (no account needed)
# 2. Use any OpenAI-compatible client:
curl https://discountedtokens.com/v1/chat/completions \
  -H "Authorization: Bearer **your-key**" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","messages":[{"role":"user","content":"hello"}]}'
```

Or point your existing harness at it:
```python
from openai import OpenAI
client = OpenAI(base_url="https://discountedtokens.com/v1", api_key="<<redacted:sk-…>>")
```

## Model catalogue

The site serves a full catalogue page at https://discountedtokens.com/models — the **complete OpenRouter catalogue (416 models)** browsed side by side with the models we actually discount. The discounted models are featured up top with their real list-price comparison; the rest are searchable and filterable by provider. Snapshot is bundled at deploy.

## Pricing (USD per 1M tokens — vs real OpenRouter list)

| Model | You pay in | You pay out | OpenRouter list | You save |
|---|---|---|---|---|
| GPT-5.6 | $0.80 | $4.80 | $2.50 / $15.00 | 68% |
| GPT-5.6 Sol | $0.80 | $4.80 | $2.50 / $15.00 | 68% |
| GPT-5.6 Terra | $0.32 | $1.92 | $2.00 / $12.00 | 84% |
| GPT-5.5 | $0.80 | $4.80 | $5.00 / $30.00 | 84% |
| GPT-5.4 | $0.40 | $2.40 | $2.50 / $15.00 | 84% |
| GPT-5.4 (2026-03-05) | $0.40 | $2.40 | $2.50 / $15.00 | 84% |
| GPT-5.4 Mini | $0.12 | $0.72 | $0.75 / $4.50 | 84% |

Price history: the site auto-snapshots our rates + the OpenRouter list every 5h into a visible history table (first-recorded date, snapshot count, current rates, delta since first). See https://discountedtokens.com/pricing

Pricing updates when we add verified models — see https://discountedtokens.com/pricing

## Harness compatibility

| Harness | Endpoint |
|---|---|
| OpenAI SDK (Python/Node) | `POST /v1/chat/completions` |
| Codex / JCode | `POST /v1/responses` |
| Claude Code | `POST /v1/messages` (x-api-key) |
| Cursor, LangChain, LibreChat, OpenWebUI | `base_url` swap |

## Features

- ⚡ 99.99% uptime on Cloudflare edge — 36 regions
- 🤖 Agent-ready: instant credits, no KYC, `llms.txt` discovery, guest checkout
- 💳 Card (Stripe) + crypto (USDT/USDC)
- 📊 Dashboard with per-model usage, spend, token counts
- 🔗 One key for every harness
- 🖤 Light "Slate & Violet" UI (Attentify design language): Space Grotesk + Inter + JetBrains Mono, aurora + dot grid texture, featured discount cards, rotating announcement banner, live pricing ticker

## Links

- Site: https://discountedtokens.com
- Pricing: https://discountedtokens.com/pricing
- Model catalogue: https://discountedtokens.com/models
- Free LLM tiers: https://discountedtokens.com/free
- Docs: https://discountedtokens.com/docs
- Cost guide: https://discountedtokens.com/guide
- Agent discovery: https://discountedtokens.com/llms.txt

## Disclaimer

Discount resale of model capacity from a verified upstream pool. Model identity is probed before listing. Only models that serve a real chat completion are catalogued (the upstream advertises image/realtime/audio variants that are NOT listed here because they don't serve chat). Use at your own discretion for production workloads.