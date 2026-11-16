# LLMTR

**Author:** knowhycodata
**Type:** model provider
**Source:** https://github.com/knowhycodata/dify-plugin-llmtr

## Overview

[LLMTR](https://llmtr.com) is an OpenAI-compatible AI gateway. One API key reaches Turkey-hosted open models and global providers such as OpenAI, Anthropic, Google, DeepSeek, and MiniMax through `https://llmtr.com/v1`.

What LLMTR adds on top of plain proxying:

- **Per-key limits and metering:** each API key can have its own rate limit and monthly token or spend ceiling, with usage records per key and per model (model, token counts, cost; no prompt text).
- **Data locality:** models under the `llmtr/` prefix run on LLMTR infrastructure in Turkey, for workloads that must keep data in the country.
- **One bill for many providers:** switching between providers is a model ID change on the same key, so a primary and a fallback model can be set up without a second integration.

## Setup

1. Create an account at [llmtr.com](https://llmtr.com), add credit, and create an API key.
2. In Dify, go to **Settings → Model Provider**, find **LLMTR**, and click **Install** (or install it from the Marketplace).
3. Paste your API key and save. The key is checked with a short request to `openai/gpt-5.4-mini`.

## Usage

The plugin ships these predefined chat models:

| Model ID | Notes |
| --- | --- |
| `openai/gpt-5.4-mini` | Tool calling, vision |
| `anthropic/claude-sonnet-4.6` | Tool calling, vision, 1M context |
| `anthropic/claude-haiku-4.5` | Tool calling, vision |
| `google/gemini-3.5-flash` | Tool calling, vision, 1M context |
| `deepseek/deepseek-v4-pro` | Tool calling, 1M context |
| `minimax/minimax-m3.1-flash` | Tool calling, vision, 1M context |
| `llmtr/qwen3-8-27b` | Turkey-hosted, tool calling |
| `llmtr/gemma-4` | Turkey-hosted, tool calling, vision |

Prices in the model cards are in USD per 1M tokens and come from LLMTR's public model list (`GET https://llmtr.com/v1/models`). Check [llmtr.com/models](https://llmtr.com/models) for current prices.

To use any other model from the catalog, choose **Add Model**, enter the full model ID (for example `qwen/qwen3.7-max`), and set the context size, max tokens, tool calling, and vision options for that model.

## Requirements

- An LLMTR API key with available credit.
- Outbound HTTPS access from the Dify plugin daemon to `llmtr.com`.
- Only the Chat Completions API is used. Models that LLMTR serves only through the Responses API are not supported by this plugin.

## Privacy

See [PRIVACY.md](PRIVACY.md).
