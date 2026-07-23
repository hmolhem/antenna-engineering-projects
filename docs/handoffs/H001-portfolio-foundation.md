# H001 — Portfolio Foundation

## Scope

Establish the initial public architecture for `antenna-engineering-projects` without yet importing the complete CST project packages.

## Branch

```text
feature/portfolio-foundation
```

## Pull Request

Pending at handoff creation.

## Files Added or Updated

- `README.md`
- `CHANGELOG.md`
- `LICENSE.md`
- `.gitignore`
- `.github/pull_request_template.md`
- `assets/README.md`
- `docs/WORKFLOW.md`
- `docs/PROJECT_STANDARD.md`
- `docs/HANDOFF_INDEX.md`
- `docs/handoffs/H001-portfolio-foundation.md`
- `projects/README.md`
- `projects/5g-patch-array/README.md`

## Engineering Decisions

- Separate project evidence from the chapter-oriented educational repository.
- Use the 5G patch array as the first featured project.
- Distinguish analytical, simulated, and measured evidence explicitly.
- Keep large CST binary models out of ordinary Git history.
- Preserve reports and figures under retained copyright while allowing code to use explicit file- or folder-level MIT licensing.
- Require numerical-reliability and limitations discussions for anomalous or constrained simulations.

## Validation

- Confirmed public repository creation and `main` default branch.
- Created all changes on `feature/portfolio-foundation`.
- Checked internal Markdown paths and planned project locations for consistency.
- Used only previously verified project results in the landing-page summary.

## Known Limitations

- The full report, figures, code, and CST model are not yet included.
- The featured-project page is an initial project record, not the final public package.
- No measured antenna data are claimed.
- Repository automation and CI are not yet configured.

## Follow-On Work

The next feature should build the complete public package for the 5G microstrip patch array, including selected figures, the final report, result tables, simulation limitations, and model-access guidance.

## Rollback

Because the foundation is isolated on a feature branch, rollback before merge consists of closing the pull request and deleting `feature/portfolio-foundation`. After merge, revert the squash commit associated with the foundation PR.
