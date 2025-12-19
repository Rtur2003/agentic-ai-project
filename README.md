# Agentic AI Project

[![Test Suite](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/test.yml/badge.svg)](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/test.yml)
[![Code Quality](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/lint.yml/badge.svg)](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/lint.yml)
[![Security Scan](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/security.yml/badge.svg)](https://github.com/Rtur2003/agentic-ai-project/actions/workflows/security.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

Lightweight CLI wrapper around Google GenAI. Provides fast env-driven configuration, defensive error handling, and comprehensive testing that avoids live network calls.

## Features

- **Fast Configuration**: Environment-driven setup with validation
- **Type Safety**: Full type hints with mypy strict mode
- **Defensive**: Explicit validation guards and error handling
- **Well-Tested**: Comprehensive test coverage with mocked dependencies
- **CI/CD Ready**: Pre-configured GitHub Actions workflows
- **Developer Friendly**: Pre-commit hooks, linting, and formatting

## Quick Start

### Installation

```bash
# Install with development tools
make install

# Or using pip directly
pip install -e .[dev]
```

### Configuration

Copy `.env.example` to `.env` and configure:

```bash
GENAI_API_KEY=your-api-key-here
GENAI_MODEL=models/gemini-1.5-flash  # optional
LOG_LEVEL=INFO                        # optional
```

### Usage

**Run a prompt:**
```bash
python -m agentic_ai_project.cli "Write a haiku about resilience"
```

**Override model:**
```bash
python -m agentic_ai_project.cli --model models/gemini-1.5-pro "Summarize quantum computing"
```

**Pipe from stdin:**
```bash
echo "Plan a 3-day trip to Paris" | python -m agentic_ai_project.cli
```

**With system instruction:**
```bash
python -m agentic_ai_project.cli --system "Be concise" "Explain Python decorators"
```

## Development

### Setup Development Environment

```bash
make dev  # Installs dependencies and pre-commit hooks
```

### Common Tasks

```bash
make test         # Run test suite
make lint         # Run linting checks
make format       # Auto-format code
make type-check   # Run type checking
make security     # Run security scans
make clean        # Remove build artifacts
```

### Project Structure

```
agentic_ai_project/
├── config.py          # Environment configuration and logging
├── validation.py      # Input validation guards
├── genai_client.py    # GenAI API wrapper
├── cli.py             # Command-line interface
└── py.typed           # Type checking marker

tests/
├── test_config.py     # Configuration tests
└── test_genai_client.py  # Client tests
```

### Code Quality

The project maintains high code quality standards:

- **Linting**: Ruff with comprehensive rule set
- **Type Checking**: mypy in strict mode
- **Formatting**: Ruff auto-formatting
- **Pre-commit**: Automated quality gates
- **CI/CD**: GitHub Actions for tests, linting, and security

## Configuration Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GENAI_API_KEY` | Yes | - | Google GenAI API key |
| `GENAI_MODEL` | No | `models/gemini-1.5-flash` | Model identifier |
| `LOG_LEVEL` | No | `INFO` | Logging verbosity |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

This project is provided as-is for educational and development purposes.
