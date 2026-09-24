---
applyTo: ".github/**/*.md,.github/**/*.yml,.github/**/*.yaml"
---

# GitHub Instructions

- Treat files under `.github/` as repository configuration and metadata; change them only when the task directly requires it.
- Respect existing templates, workflows, and conventions before proposing new structure.
- Do not modify CI workflows, automations, or templates unless the change is clearly justified by the task and can be explained clearly.
- When a task involves preparing or drafting pull request content, review and follow `.github/PULL_REQUEST_TEMPLATE.md`.
- When a task involves preparing or drafting issue or task content, review the templates available in `.github/ISSUE_TEMPLATE/` and adapt to the most appropriate one.
- When drafting PRs or issues, do not invent validations, links, acceptance criteria, or technical context not supported by the actual changes or by the user's request.
- If a template section does not apply, state it explicitly rather than leaving ambiguous information.
- If the task affects validation or quality, reflect in PR content which commands were run and include a brief summary of the result, following the repository template.
