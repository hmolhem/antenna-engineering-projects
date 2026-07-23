# Repository Workflow

All meaningful changes are developed on dedicated branches and reviewed through pull requests before reaching `main`.

## Branches

Use descriptive branch names:

```text
feature/<scope>
fix/<scope>
docs/<scope>
```

Examples:

```text
feature/portfolio-foundation
feature/5g-patch-array
fix/array-result-caption
```

## Pull Requests

Each pull request should:

1. Have one clear engineering purpose.
2. Summarize added or changed evidence.
3. Identify validation performed.
4. State numerical, modeling, licensing, or reproducibility limitations.
5. Include or update a handoff document.
6. Update `CHANGELOG.md` when appropriate.

Squash merge is preferred when the branch contains incremental implementation commits that represent one logical change.

## Handoffs

Each meaningful feature receives a sequential handoff ID:

```text
H001, H002, H003, ...
```

Handoffs are stored under `docs/handoffs/` and indexed in `docs/HANDOFF_INDEX.md`.

A handoff should record:

- Scope
- Branch
- Pull request
- Files changed
- Engineering decisions
- Validation performed
- Known limitations
- Follow-on work
- Rollback guidance

## Evidence Discipline

Repository claims must distinguish among:

- Analytical prediction
- Simulated result
- Measured result
- Inference or engineering expectation

A simulated antenna is not described as fabricated or experimentally validated unless corresponding evidence is included.

## Numerical Reliability

Unexpected, non-monotonic, or unusually favorable simulation behavior should trigger explicit review of mesh, boundaries, solver settings, ports, convergence, and material assumptions. When such checks cannot be completed, the limitation must be stated rather than hidden.

## Large Files

Large CST or other binary models should not be committed casually to Git history. Use curated exports, Git LFS, GitHub Releases, or a documented external-access process when appropriate.
