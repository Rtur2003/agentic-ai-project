## Agentic AI Project

Lightweight CLI wrapper around Google GenAI. Provides fast env-driven configuration, defensive error handling, and tests that avoid live network calls.

### Setup
- Install deps: `uv sync` (or `pip install -e .[dev]`)
- Configure environment: copy `.env.example` to `.env` and fill `GENAI_API_KEY`.

### Usage
- Run a prompt: `python -m agentic_ai_project.cli "Write a haiku about resilience"`
- Override model: `python -m agentic_ai_project.cli --model models/gemini-1.5-pro "Short summary of the day"`
- Pipe stdin: `echo "Plan a 3-day trip" | python -m agentic_ai_project.cli`

### Configuration
- `GENAI_API_KEY` (required): service key.
- `GENAI_MODEL` (optional): defaults to `models/gemini-1.5-flash`.
- `LOG_LEVEL` (optional): defaults to `INFO`.

### Development
- Run tests: `python -m pytest` (or `uv run pytest`)
- Key modules:
  - `agentic_ai_project/config.py`: env + logging setup
  - `agentic_ai_project/genai_client.py`: GenAI wrapper
  - `agentic_ai_project/cli.py`: single-shot prompt runner
