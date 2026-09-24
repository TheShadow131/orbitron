# Contributing

This guide defines the collaboration rules for the repository.

## Table of contents

- [Rules](#rules)
- [Branch pattern](#branch-pattern)
- [Commit pattern](#commit-pattern)
- [Issues](#issues)
- [Pull request (PR)](#pull-request-pr)
- [Style and validations](#style-and-validations)

## Rules

- Open an issue before coding whenever possible.
- Keep communication clear, direct, and respectful.
- Keep each change focused and limited in scope.
- Do not push changes directly to main.
- Every change must be merged through a pull request.
- If behavior or documentation changes, update documentation in the same PR.
- Run lint and type checks before opening a PR.

## Branch pattern

Follow a GitHub Flow style branching model.

| Type | Pattern | Example | Use case |
| --- | --- | --- | --- |
| feat | feat/issue-id-short-description | feat/12-add-api-client | New feature |
| fix | fix/issue-id-short-description | fix/34-handle-empty-input | Bug fix |
| ci | ci/issue-id-short-description | ci/45-update-workflow | CI changes |
| hotfix | hotfix/issue-id-short-description | hotfix/52-fix-production-error | Urgent production fix |
| release | release/version | release/1.2.0 | Release preparation |
| docs | docs/issue-id-short-description | docs/61-update-installation-guide | Documentation changes |
| refactor | refactor/issue-id-short-description | refactor/73-clean-service-layer | Refactor without behavior changes |
| chore | chore/issue-id-short-description | chore/88-update-dev-tools | Maintenance |

Use lowercase names with hyphens. Include the issue id in branch names except for release branches.

## Commit pattern

Use short and consistent commit messages:

| Type | Pattern | Example |
| --- | --- | --- |
| feat | feat: short description | feat: add user profile endpoint |
| fix | fix: short description | fix: handle null payload |
| ci | ci: short description | ci: cache uv dependencies |
| docs | docs: short description | docs: improve installation steps |
| refactor | refactor: short description | refactor: simplify startup flow |
| chore | chore: short description | chore: update lint settings |
| revert | revert: short description | revert: rollback env loading change |

Keep commit messages in imperative mood and present tense.

## Issues

Before creating an issue, search for duplicates.

Use repository issue templates when available:

- [Bug report template](../.github/ISSUE_TEMPLATE/bug_report.yml) for reproducible errors.
- [Feature request template](../.github/ISSUE_TEMPLATE/feature_request.yml) for improvements.
- [Task template](../.github/ISSUE_TEMPLATE/task.yml) for planned work items.

## Pull request (PR)

Before opening a PR:

1. Confirm that the branch scope is clear.
2. Link the related issue when applicable.
3. Summarize the main changes.
4. Explain how you validated the change.
5. Confirm local checks passed.

Pull request template:

- [Pull request template](../.github/PULL_REQUEST_TEMPLATE.md)

## Style and validations

Run these commands before submitting changes.
This repository currently enforces these checks in CI (Ruff and Mypy only):

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy .
```
