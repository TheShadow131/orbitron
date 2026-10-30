# Contributing to Orbitron

We welcome contributions to Orbitron! Whether it's fixing bugs, adding new features, or improving documentation, your help is greatly appreciated. Please follow the guidelines below to contribute effectively.

## Table of Contents

- [Rules](#rules)
- [Workflow](#workflow)
- [Branch patterns](#branch-patterns)
- [Commit patterns](#commit-patterns)
- [Issues Guidelines](#issues-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Formatting Guidelines](#formatting-guidelines)

## Rules

Follow these rules to ensure a good contribution experience and maintain the quality of the Orbitron project.

- Follow the branch patterns and commit patterns outlined in this guide.
- Ensure your code adheres to the project's coding standards and passes all tests.
- Write clear and concise commit messages.
- Keep pull requests focused and well-documented.
- Review and address feedback promptly.
- Keep the language professional and respectful in all communications.

**Note:** The official language for all contributions and communications within the Orbitron project is English.

## Workflow

The typical workflow for contributing to Orbitron involves the following steps:

1. Fork the Orbitron repository to your GitHub account.
2. Clone your forked repository to your local development environment.
3. Create a new branch following the branch patterns outlined above.
4. Make your changes and commit them following the commit patterns.
5. Open a pull request against the `develop` branch on the original Orbitron repository.
6. Address any feedback and make necessary changes.
7. Once approved, your changes will be merged into the `develop` branch.

## Branch patterns

Orbitron follows a specific branching pattern to maintain a clean and organized repository. The main branches are:

| Type | Description | Format | Example |
|--------|-------------|---------|---------|
| `main` | The main branch containing the stable release of Orbitron. | `main` | `main` |
| `develop` | The development branch containing the latest changes and features under development. | `develop` | `develop` |
| `feat/*` | Feature branches created from `develop` for implementing new features. | `feat/<issue-number>-<short-description>` | `feat/1-add-user-login` |
| `bugfix/*` | Bugfix branches created from `develop` for fixing issues. | `bugfix/<issue-number>-<short-description>` | `bugfix/1-fix-login-error` |
| `hotfix/*` | Hotfix branches created from `develop` for urgent fixes that need to be applied to the stable release. | `hotfix/<issue-number>-<short-description>` | `hotfix/1-fix-crash` |
| `release/*` | Release branches created from `develop` for preparing a new release. | `release/<tag>` | `release/v1.0.0` |
| `chore/*` | Chore branches created from `develop` for maintenance tasks that do not affect the functionality of Orbitron. | `chore/<issue-number>-<short-description>` | `chore/1-update-dependencies` |
| `docs/*` | Documentation branches created from `develop` for updating or adding documentation. | `docs/<issue-number>-<short-description>` | `docs/1-update-contributing-guide` |
| `ci/*` | Continuous integration branches created from `develop` for CI/CD pipeline updates. | `ci/<issue-number>-<short-description>` | `ci/1-update-pipeline` |

## Commit patterns

Orbitron follows a conventional commit pattern to ensure clear and consistent commit messages. Each commit message should have a type, an optional scope, and a concise description. The general format is:

| Type | Description | Format | Example |
|------|-------------|---------|---------|
| `feat` | A new feature | `feat: <description>` | `feat: add user login functionality` |
| `fix` | A bug fix | `fix: <description>` | `fix: resolve crash on startup` |
| `chore` | Maintenance tasks | `chore: <description>` | `chore: update dependencies` |
| `docs` | Documentation changes | `docs: <description>` | `docs: update contributing guide` |
| `style` | Code style changes (formatting, linting) | `style: <description>` | `style: apply code formatting` |
| `refactor` | Code refactoring without changing functionality | `refactor: <description>` | `refactor: optimize database queries` |
| `test` | Adding or updating tests | `test: <description>` | `test: add unit tests for login` |

## Issues Guidelines

Follow these guidelines when creating issues for the Orbitron project:

- Use an appropriate issue template when creating a new issue.
- Provide a clear and descriptive title for the issue.
- Include a detailed description of the problem or feature request.
- Link any relevant pull requests, discussions or sub-issues.
- Assign appropriate labels and milestones to the issue.
- Keep issues small and focused, if necessary, create a main issue and break it into sub-issues.

## Pull Request Guidelines

Follow these guidelines when creating pull requests for the Orbitron project:

- Ensure your pull request is based on the latest `develop` or `main` branch.
- Provide a clear and descriptive title for your pull request.
- Include a detailed description of the changes made and the rationale behind them.
- Link any relevant issues or discussions.
- Follow the commit message conventions outlined in this guide.
- Ensure your pull request passes all tests and checks before requesting a review.
- Respond to feedback and make necessary changes promptly.
- Ensure your pull request adheres to the project's coding standards and guidelines.
- Ensure your pull request does not duplicate existing work or open issues.
- Ensure your pull request is written in English, as it is the official language for all contributions and communications within the Orbitron project.

**Note:** Use the pull request template provided by the Orbitron project to ensure all necessary information is included.

## Formatting Guidelines

Orbitron follows a consistent code formatting style to maintain readability and code quality. Adhere to the following guidelines when formatting your code:

- Use 4 spaces for indentation.
- Limit lines to 88 characters.
- Use snake_case for variable and function names.
- Use PascalCase for class names.
- Place imports at the top of the file, grouped by standard library, third-party, and local imports.
- Add a blank line at the end of each file.
- Follow PEP 8 guidelines for Python code style.
- Use linting tools to check for code style violations and maintain consistency.
