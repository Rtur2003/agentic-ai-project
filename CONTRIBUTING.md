# Contributing to Agentic AI Project

## Setup

1. Clone the repository
2. Install dependencies: `make install`
3. Install pre-commit hooks: `make dev`

## Development Workflow

### Before Making Changes

- Ensure tests pass: `make test`
- Ensure code quality: `make lint`

### Making Changes

- Follow Python conventions (PEP 8)
- Add tests for new functionality
- Keep commits atomic and focused
- Use descriptive commit messages

### Code Quality Standards

Run these commands before committing:

```bash
make format      # Auto-format code
make lint        # Check linting
make type-check  # Verify types
make test        # Run tests
```

Or let pre-commit handle it automatically:

```bash
git commit -m "your message"
```

## Commit Message Format

Use conventional commit style:

- `feat:` new feature
- `fix:` bug fix
- `refactor:` code restructuring
- `test:` test additions or changes
- `docs:` documentation changes
- `chore:` maintenance tasks

## Testing

- Write tests for all new code
- Ensure coverage doesn't decrease
- Use mocks to avoid external dependencies

## Pull Requests

- Keep changes focused and atomic
- Include relevant test updates
- Update documentation if needed
- Ensure CI passes before requesting review
