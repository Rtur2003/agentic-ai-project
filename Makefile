.PHONY: help install test lint format type-check security clean dev

help:
	@echo "Agentic AI Project - Development Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install       Install project with dev dependencies"
	@echo "  make dev           Install pre-commit hooks"
	@echo ""
	@echo "Quality & Testing:"
	@echo "  make test          Run test suite"
	@echo "  make lint          Run linting checks"
	@echo "  make format        Auto-format code"
	@echo "  make type-check    Run type checking"
	@echo "  make security      Run security scans"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean         Remove build artifacts"

install:
	pip install -e .[dev]

dev: install
	pre-commit install

test:
	python -m pytest -v

lint:
	ruff check .

format:
	ruff format .
	ruff check --fix .

type-check:
	mypy agentic_ai_project

security:
	bandit -r agentic_ai_project

clean:
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
