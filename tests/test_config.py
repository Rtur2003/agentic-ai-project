from __future__ import annotations

import pytest

from agentic_ai_project import config


@pytest.fixture(autouse=True)
def clear_config_cache():
    config.get_settings.cache_clear()
    yield
    config.get_settings.cache_clear()


def test_get_settings_requires_api_key(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("GENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        config.get_settings()


def test_get_settings_reads_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("GENAI_API_KEY", "token-123")
    monkeypatch.setenv("GENAI_MODEL", "models/demo")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = config.get_settings()

    assert settings.api_key == "token-123"
    assert settings.model == "models/demo"
    assert settings.log_level == "DEBUG"
