# H002 - 5G Patch-Array Public Package

- **Handoff ID:** H002
- **Date:** 2026-07-23
- **Branch:** `feature/5g-patch-array-project`
- **Pull request:** [#2](https://github.com/hmolhem/antenna-engineering-projects/pull/2)
- **Status:** Merged
- **Head commit:** `5d564ffa91eb80357dc70f94f3b7a240a3bd8074`
- **Merge commit:** `332675692321df14eab4de47adb2d1be6476eb65`

## Purpose

Publish the first complete engineering project package in the antenna portfolio: analytical design, CST full-wave simulation, two-port array characterization, conductor-loss sensitivity, and phase-controlled beam steering for a 5G microstrip patch array.

## Implemented

- Updated repository and project landing pages with final verified results.
- Added the public 61-page engineering report PDF.
- Added the sanitized and reproducible LaTeX report source.
- Added analytical Python design and beam-steering scripts.
- Added selected single-patch, array, and beam-steering figures for rapid GitHub review.
- Added human-readable and CSV key-result summaries.
- Added numerical-reliability and model-access notes.
- Updated `CHANGELOG.md`, the project index, and the handoff index.

## Verified Results

### Single patch

- Design frequency: 2.501 GHz
- Final simulated resonance: 2.50507 GHz
- Minimum S11: approximately -39.87 dB
- Peak directivity: approximately 7.226 dBi
- PEC radiation and total efficiencies: approximately 96.3% and 96.2%
- Fixed-mesh copper radiation and total efficiencies: approximately 92.46% and 92.38%

### Two-port array

- Element spacing: 59.935 mm
- S11: approximately -11.93 dB near 2.498 GHz
- S22: approximately -15.20 dB near 2.497 GHz
- S12/S21 coupling: approximately -15.19/-14.57 dB
- Broadside displayed peak directivity: approximately 9.655 dBi

### Beam steering

- Relative phase cases: 0, -90, and +90 degrees
- CST-observed phase-shifted scan displacement: approximately 20 degrees in opposite half-planes

## Evidence Classification

- Analytical and simulated evidence only.
- No fabrication or measurement validation is claimed.
- Combined-result gain and efficiency values flagged by CST as unreliable are not presented as validated results.

## Numerical Reliability

- Baseline tuned models used PEC metallization while retaining dielectric loss.
- A fixed-mesh copper sensitivity run was completed for the single patch.
- Formal mesh- and boundary-convergence studies were not completed because of CST Learning Edition limits.
- Native `.cst` binaries are intentionally excluded from ordinary Git history.

## Validation Performed

- Public PDF and expanded source package checked for student-identification, grading, D2L, and restricted-course remnants.
- Scientific citations retained for Rogers material properties, Stutzman-Thiele antenna theory, and CST post-processing documentation.
- Final PDF compiled from the sanitized source package.
- Selected figure paths and Markdown links checked within the package.
- Project result values synchronized across the root README, project README, result summaries, and handoff.
- PR #2 was merged and the remote feature branch was deleted.

## Limitations and Follow-Up

- No experimental prototype or measured validation is included.
- The full two-element array was not validated with adaptive finite-conductivity convergence.
- Native CST files require a separate reviewed distribution path.
- A future revision may add automated LaTeX compilation and link checks through GitHub Actions.

## Rollback

Revert merge commit `332675692321df14eab4de47adb2d1be6476eb65` to remove the H002 package without rewriting repository history.
