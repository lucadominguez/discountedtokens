# DiscountedTokens — Cheap GPT-5.x API

[![Live](https://img.shields.io/badge/live-discountedtokens.com-blue)](https://discountedtokens.com)
[![Stripe](https://img.shields.io/badge/payments-Stripe-green)](https://discountedtokens.com/guest)
[![Harnesses](https://img.shields.io/badge/OpenAI%20%2B%20Anthropic%20%2B%20Responses-compatible-purple)](https://discountedtokens.com/docs)

**Frontier GPT-5.x models at ~80% below retail — one key for every harness. Instant credits, no signup for agents.**

Buy credits by card (Stripe) or crypto (USDT/USDC). OpenAI-compatible, Anthropic-compatible, and Responses (Codex/JCode) endpoints from a single base URL.

## Quick start (60 seconds)

```bash
# 1. Buy credits — https://discountedtokens.com/guest (no account needed)
# 2. Use any OpenAI-compatible client:
curl https://discountedtokens.com/v1/chat/completions \
  -H "Authorization: Bearer sk-res-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","messages":[{"role":"user","content":"hello"}]}'
```

Or point your existing harness at it:
```python
from openai import OpenAI
client = OpenAI(base_url="https://discountedtokens.com/v1", api_key="sk-res-YOUR_KEY")
```

## Pricing (USD per 1M tokens — live from the site)

| Model | Input | Output | Retail ref | You save |
|---|---|---|---|---|
| GPT-5.6 | $0.80 | $4.80 | $2.00 / $10.00 | ~60% |
| GPT-5.6 Sol | $0.80 | $4.80 | $2.00 / $10.00 | ~60% |
| GPT-5.6 Terra | $0.32 | $1.92 | $0.80 / $4.00 | ~60% |
| GPT-5.5 | $0.80 | $4.80 | $2.00 / $10.00 | ~60% |
| GPT-5.4 | $0.40 | $2.40 | $1.00 / $6.00 | ~60% |
| GPT-5.4 Mini | $0.12 | $0.72 | $0.30 / $1.80 | ~60% |

Pricing updates live — see https://discountedtokens.com/pricing

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

## Links

- Site: https://discountedtokens.com
- Pricing: https://discountedtokens.com/pricing
- Docs: https://discountedtokens.com/docs
- Cost guide: https://discountedtokens.com/guide
- Agent discovery: https://discountedtokens.com/llms.txt

## Disclaimer

Discount resale of model capacity from a verified upstream pool. Model identity is probed/verified before listing. Use at your own discretion for production workloads.