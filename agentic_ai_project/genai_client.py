from __future__ import annotations

import logging
from typing import Optional

from google import genai

from .config import Settings
from .validation import validate_non_empty_string


class GenAIClient:
    def __init__(
        self,
        settings: Settings,
        *,
        client: Optional[genai.Client] = None,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        self._settings = settings
        self._logger = logger or logging.getLogger("agentic_ai_project.genai")
        self._client = client or genai.Client(api_key=settings.api_key)

    def generate(
        self,
        prompt: str,
        *,
        model: Optional[str] = None,
        system_instruction: Optional[str] = None,
    ) -> str:
        validated_prompt = validate_non_empty_string(prompt, "prompt")
        model_name = model or self._settings.model
        try:
            response = self._client.responses.generate(
                model=model_name,
                contents=[{"role": "user", "parts": [validated_prompt]}],
                system_instruction=system_instruction,
            )
        except Exception as exc:
            self._logger.error("GenAI generate failed", exc_info=True)
            raise RuntimeError(f"GenAI request failed: {exc}") from exc

        text = getattr(response, "text", "")
        if not text:
            candidate_text = _first_candidate_text(response)
            if candidate_text:
                text = candidate_text

        return text.strip()


def _first_candidate_text(response: object) -> str:
    try:
        candidates = getattr(response, "candidates", None)
        if not candidates:
            return ""
        candidate = candidates[0]
        content = getattr(candidate, "content", None)
        if not content or not getattr(content, "parts", None):
            return ""
        part = content.parts[0]
        return getattr(part, "text", "") or ""
    except Exception:
        return ""
