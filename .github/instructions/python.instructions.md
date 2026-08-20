---
applyTo: "app/**/*.py"
---

# Python Instructions

- Keep changes small, localized, and easy to validate.
- Respect the existing structure and style before introducing new abstractions.
- Follow the repository's code quality rules as closely as possible.
- Avoid broad refactors, extra configuration layers, or speculative patterns unless they are required by the task.
- If the task affects the main application flow, keep in mind that the project entry point is `app/__main__.py`.
- Reuse utilities, modules, and patterns that already exist in the repository before creating new ones.
- Do not add new dependencies or change project tooling unless there is a direct task-driven reason.
- Add comments only when they clarify a decision or a non-obvious code block.
- When a change affects behavior or code quality, prioritize validations close to the change and run project checks when relevant, for example `uv run ruff format --check .`, `uv run ruff check .`, and `uv run mypy .`.
- If something cannot be validated locally, state it clearly and explain why.
