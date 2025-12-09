from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv

# Load environment variables early so downstream imports see them.
load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str
    log_level: str = "INFO"


def _resolve_log_level(level: Optional[str]) -> int:
    if not level:
        return logging.INFO
    # Tolerate numeric or string levels; avoid over-engineering a mapping table.
    try:
        return int(level)
    except ValueError:
        normalized = level.upper()
        return getattr(logging, normalized, logging.INFO)


def configure_logging(level: Optional[str] = None) -> logging.Logger:
    resolved_level = _resolve_log_level(level or os.getenv("LOG_LEVEL"))
    logging.basicConfig(
        level=resolved_level,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    return logging.getLogger("agentic_ai_project")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        # Fail fast to avoid silent network calls with missing credentials. @Rtur2003
        raise RuntimeError("GENAI_API_KEY is required to contact the GenAI service.")

    model = os.getenv("GENAI_MODEL", "models/gemini-1.5-flash")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    return Settings(api_key=api_key, model=model, log_level=log_level)

