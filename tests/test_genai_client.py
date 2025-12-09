from __future__ import annotations

import logging
from types import SimpleNamespace

import pytest

from agentic_ai_project.config import Settings
from agentic_ai_project.genai_client import GenAIClient


class _DummyResponses:
    def __init__(self, response):
        self._response = response
        self.last_payload = None

    def generate(self, **kwargs):
        self.last_payload = kwargs
        return self._response


class _DummyClient:
    def __init__(self, response):
        self.responses = _DummyResponses(response)


def test_generate_returns_text():
    response = SimpleNamespace(text="hello world", candidates=[])
    client = GenAIClient(
        Settings(api_key="token", model="models/demo"),
        client=_DummyClient(response),
        logger=logging.getLogger("test"),
    )

    result = client.generate("hi")

    assert result == "hello world"


def test_generate_uses_candidate_fallback():
    part = SimpleNamespace(text="fallback text")
    content = SimpleNamespace(parts=[part])
    candidate = SimpleNamespace(content=content)
    response = SimpleNamespace(text="", candidates=[candidate])
    dummy_client = _DummyClient(response)
    client = GenAIClient(
        Settings(api_key="token", model="models/demo"),
        client=dummy_client,
        logger=logging.getLogger("test"),
    )

    result = client.generate("hi")

    assert result == "fallback text"


def test_generate_wraps_errors():
    class _BrokenResponses:
        def generate(self, **kwargs):
            raise ValueError("boom")

    broken_client = SimpleNamespace(responses=_BrokenResponses())
    client = GenAIClient(
        Settings(api_key="token", model="models/demo"),
        client=broken_client,
        logger=logging.getLogger("test"),
    )

    with pytest.raises(RuntimeError):
        client.generate("hi")
