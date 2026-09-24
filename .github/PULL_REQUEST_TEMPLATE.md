# Pull Request

## Brief description
<!-- Provide a concise description of the change and why it is needed. -->

## Related issue
<!-- Reference the related issue (for example, #123), or remove this section if not applicable. -->

## Changes
<!-- Brief list of the key changes included in this PR. -->

## Type of change
- [ ] Bugfix
- [ ] New feature
- [ ] Documentation
- [ ] Chore or maintenance
- [ ] CI or build

## Validation
<!-- Describe how the change was validated (local checks, manual verification, etc.). -->

For code or behavior changes, include the commands you ran and a short result summary. Current baseline quality checks:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy .
```

If a validation item is not applicable, state `N/A` and explain why briefly.

## Verification checklist
### Always
- [ ] I reviewed this template before submitting.
- [ ] The related issue is linked, if applicable.
- [ ] Acceptance criteria from the related issue were covered.
- [ ] The related task or issue was reviewed before submitting.
- [ ] Validation evidence was included (or explicitly marked as not applicable).

### If applicable
- [ ] Code follows project lint and formatting rules (if code files changed).
- [ ] Type checks pass locally (if typed Python code or public interfaces changed).
- [ ] Documentation was updated when needed (if workflow, behavior, setup, or usage changed).
- [ ] CI checks are passing (if workflows or behavior affected by CI changed).

## Notes for reviewers
<!-- Include any context that helps reviewers focus on risk areas or important decisions. -->
