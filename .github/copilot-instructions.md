# Copilot Instructions

This repository contains Python projects. Keep changes minimal, focused, and easy to validate.

## Working Style

- Prefer the smallest change that solves the request.
- Avoid speculative abstractions, extra configuration, or broad refactors.
- Match the existing project style and keep edits localized.
- If the request is unclear, state the assumption before changing code.

## Project Context

- Prefer the project layout already in place instead of introducing new structure.
- The main entry point is `app/__main__.py`.
- Project documentation lives in `docs/` and `README.md` files.
- GitHub workflow and templates live in `.github/`.
- Repository-level agent guidance lives in `.github/AGENTS.md`.
- If the repo already defines its own conventions, follow them over these defaults.

## Validation

When changing code, prefer validating with the lightest relevant checks first.

- Use the project quality checks from the PR template when they apply.
- Run the narrowest command that can confirm the change.
- If a change affects behavior, include the command you used and a short result summary.

## Communication

- Be direct about tradeoffs and risks.
- Do not introduce unrelated cleanups.
- If validation cannot be run, say why briefly.
