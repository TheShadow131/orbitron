# Development

This guide describes the recommended local workflow to keep the project maintainable over time.

## Table of contents

- [Recommended workflow](#recommended-workflow)
- [Local startup](#local-startup)
- [Pre-commit setup](#pre-commit-setup)
- [Local validations](#local-validations)

## Recommended workflow

1. Create a branch from main for a single, clear objective.
2. Install dependencies if this is your first setup.
3. Implement focused changes.
4. Run local quality checks.
5. Open a pull request with clear context.

## Local startup

```bash
uv run python -m app
```

## Pre-commit setup

Install git hooks once after dependency installation:

```bash
uv run pre-commit install
```

Run all hooks manually at any time:

```bash
uv run pre-commit run --all-files
```

## Local validations

Run these checks before opening a pull request.
These are the same checks executed in CI for the current phase (Ruff and Mypy only):

```bash
uv run pre-commit run --all-files
```

If you need to run the underlying commands directly:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy .
```

If you need to auto-format and apply safe lint fixes before running checks:

```bash
uv run ruff format .
uv run ruff check . --fix
```
