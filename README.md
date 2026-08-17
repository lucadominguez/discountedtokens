# DiscountedTokens — Cheap GPT-5.x API

[![Live](https://img.shields.io/badge/live-discountedtokens.com-blue)](https://discountedtokens.com)

**Frontier GPT-5.x models at ~80% below retail market rates.** One OpenAI-compatible / Anthropic-compatible / Responses-compatible API key. Buy credits in minutes — no signup required for AI agents.

## Why

Most model APIs charge $2–$10 per million input tokens. DiscountedTokens runs the same GPT-5.x family you already use, from a low-cost verified pool, at a fraction of that. Get GPT-5.5 class models for pennies.

## Quick start (30 seconds)

```bash
# 1. Buy credits (or create an account + dashboard)
#    https://discountedtokens.com/guest

# 2. Use any OpenAI-compatible client
curl https://discountedtokens.com/v1/chat/completions \
  -H "Authorization: Bearer sk-res-YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.5","messages":[{"role":"user","content":"hello"}]}'
```

## Models (USD per 1M tokens)

| Model | In | Out |
|---|---|---|
| GPT-5.6 | $0.80 | $4.80 |
| GPT-5.6 Sol | $0.80 | $4.80 |
| GPT-5.6 Terra | $0.32 | $1.92 |
| GPT-5.5 | $0.80 | $4.80 |
| GPT-5.4 | $0.40 | $2.40 |
| GPT-5.4 Mini | $0.12 | $0.72 |

*Pricing shown after 300% markup on upstream pool (current catalog prices on site may differ).*

## Harness compatibility

Works with any OpenAI, Responses, or Anthropic-compatible harness:

- **OpenAI SDK** (Python/Node), `base_url = https://discountedtokens.com/v1`
- **Codex / JCode** — `POST /v1/responses`
- **Claude Code** — `POST /v1/messages`
- Cursor, LangChain, LibreChat, OpenWebUI

## Features

- ⚡ **99.99% uptime** on Cloudflare edge (36 regions)
- 🤖 **AI-agent ready** — instant credits, no KYC, `llms.txt` for discovery
- 💳 **Pay with card (Stripe) or crypto (USDT/USDC)**
- 📊 **Dashboard** with per-model usage, spend, token counts
- 🔗 One key for every harness

## Links

- Site: https://discountedtokens.com
- Pricing: https://discountedtokens.com/pricing
- Docs: https://discountedtokens.com/docs
- Agent discovery: https://discountedtokens.com/llms.txt
