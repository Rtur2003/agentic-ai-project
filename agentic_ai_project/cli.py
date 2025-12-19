from __future__ import annotations

import argparse
import sys

from .config import configure_logging, get_settings
from .genai_client import GenAIClient


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a single GenAI prompt and print the response."
    )
    parser.add_argument(
        "prompt", nargs="?", help="Prompt text; falls back to stdin if omitted."
    )
    parser.add_argument("--model", help="Override model name for this request.")
    parser.add_argument("--system", help="Optional system instruction.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    prompt = args.prompt
    if not prompt:
        if sys.stdin.isatty():
            parser.error("prompt is required via argument or piped stdin")
        prompt = sys.stdin.read().strip()

    settings = get_settings()
    logger = configure_logging(settings.log_level)

    client = GenAIClient(settings=settings, logger=logger)
    try:
        result = client.generate(
            prompt, model=args.model, system_instruction=args.system
        )
    except Exception as exc:
        logger.error(str(exc))
        return 1

    sys.stdout.write(result + ("\n" if not result.endswith("\n") else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
