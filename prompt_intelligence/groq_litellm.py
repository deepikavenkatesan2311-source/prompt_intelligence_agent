"""Groq-compatible LiteLLM wrapper.

Groq's chat API rejects assistant messages that include reasoning fields
(`reasoning_content`, `reasoning`, `thinking_blocks`) on later turns, but
ADK's LiteLLM adapter preserves them in session history after tool calls.
"""

from __future__ import annotations

from typing import Any

from google.adk.models.lite_llm import LiteLlm
from google.adk.models.lite_llm import LiteLLMClient

_GROQ_UNSUPPORTED_ASSISTANT_KEYS = frozenset({
    "reasoning_content",
    "reasoning",
    "thinking_blocks",
})


def _strip_groq_unsupported_fields(
    messages: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    cleaned: list[dict[str, Any]] = []
    for message in messages:
        msg = dict(message)
        if msg.get("role") == "assistant":
            for key in _GROQ_UNSUPPORTED_ASSISTANT_KEYS:
                msg.pop(key, None)
        cleaned.append(msg)
    return cleaned


class _GroqLiteLLMClient(LiteLLMClient):
    async def acompletion(self, model, messages, tools, **kwargs):
        cleaned_messages = _strip_groq_unsupported_fields(messages)
        return await super().acompletion(
            model, cleaned_messages, tools, **kwargs
        )


class GroqLiteLlm(LiteLlm):
    """LiteLlm configured for Groq multi-turn tool + skill sessions."""

    def __init__(self, model: str, **kwargs):
        super().__init__(model=model, **kwargs)
        self.llm_client = _GroqLiteLLMClient()
