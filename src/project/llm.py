"""Single entry point for LLM calls: every call is traced in Langfuse and routable by model name.

Frontier and open models both go through OpenRouter's OpenAI-compatible API so that
A/B comparisons in evals are a one-line change.
"""

from __future__ import annotations

from langfuse.decorators import observe
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from project.settings import settings

_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=settings.openrouter_api_key)


@observe()
def complete(prompt: str, *, model: str | None = None, system: str = "", **kwargs) -> str:
    model = model or settings.frontier_model
    messages: list[ChatCompletionMessageParam] = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    resp = _client.chat.completions.create(model=model, messages=messages, **kwargs)
    return resp.choices[0].message.content or ""
