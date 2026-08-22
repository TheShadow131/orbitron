# Orbitron

Python project template with clear documentation, reproducible local setup using uv, and baseline quality checks with pre-commit, Ruff, and Mypy.

## Table of contents

- [Documentation](#documentation)
  - [Recommended reading order](#recommended-reading-order)
  - [Documentation index](#documentation-index)
  - [AI instructions index](#ai-instructions-index)

## Documentation

Use the `README.md` and local documentation in the `docs` directory as the primary source of truth.

### Recommended reading order

Use the documentation in this order:

1. Start with this `README.md` to understand the repository purpose.
2. Read [Installation](docs/installation.md) before setting up the repository locally.
3. Read [Development](docs/development.md) before making changes or running local quality checks.
4. Read [Contributing](docs/contributing.md) before opening issues, creating branches, or submitting pull requests.
5. If you're using an AI coding agent, read [Agent Instructions](.github/AGENTS.md) before analyzing or modifying code in this repository.

### Documentation index

<!-- Documentation index maintenance:
Keep this list in alphabetical order.
For each new guide, add one bullet using this format:
- [Name](FileLink): short description.
-->

This section is focused on people working on the repository (contributors, maintainers, and reviewers).

- [Contributing](docs/contributing.md): branch, commit, and pull request conventions.
- [Development](docs/development.md): day-to-day workflow and local validation commands.
- [Installation](docs/installation.md): environment requirements, local setup, and startup.

### AI instructions index

<!-- AI instructions index maintenance:
Keep this list in alphabetical order.
For each new instruction file, add one bullet using this format:
- [Name](FileLink): short description.
-->

This section is focused on AI coding assistants and agent workflows used in this repository.

- [Agent Instructions](.github/AGENTS.md): baseline behavior rules for coding agents.
- [Copilot Repository Instructions](.github/copilot-instructions.md): repository-wide Copilot guidance.
- [Documentation Instructions](.github/instructions/docs.instructions.md): path-specific rules for `docs/**/*.md` and `README.md`.
- [GitHub Instructions](.github/instructions/github.instructions.md): path-specific rules for files under `.github/` (templates, workflows, and repository metadata).
- [Python Instructions](.github/instructions/python.instructions.md): path-specific rules for Python source files under `app/`.
