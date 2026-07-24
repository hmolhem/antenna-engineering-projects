# H003 - Wearable Half-Wave Dipole Public Package

- **Handoff ID:** H003
- **Date:** 2026-07-24
- **Branch:** `feature/wearable-dipole-project`
- **Pull request:** [#4](https://github.com/hmolhem/antenna-engineering-projects/pull/4)
- **Status:** Merged
- **Head commit:** `336eeace5dee5f7acbd2b367be812f8669489faa`
- **Merge commit:** `5ca32e11dc181622997b4a4346aa3c1a88a98e4d`

## Purpose

Publish the second complete engineering project package in the antenna portfolio: analytical initialization, CST free-space tuning, finite multilayer body loading, antenna-body spacing comparison, efficiency and gain assessment, and first-order retuning of a wearable half-wave dipole at 1.120 GHz.

## Implemented

- Added an 80-page public engineering report.
- Added sanitized and reproducible LaTeX source.
- Removed student ID, course, instructor, grading, university-logo, and unrelated template artifacts.
- Replaced the unrelated wire-dipole utility script with a wearable-project verification script.
- Added curated free-space, body-loading, gain, and retuning figures.
- Added Markdown and CSV key-result summaries.
- Added numerical-reliability and native-model-access notes.
- Updated the root README, project portfolio index, changelog, and handoff index.

## Verified Results

### Free-space baseline

- Design frequency: 1.120 GHz
- Theoretical half-wave length: 133.93 mm
- Tuned dipole length: 122.0 mm
- Matching minimum: -15.52702 dB at 1.1168 GHz
- S11 at 1.120 GHz: -15.48433 dB

### Body-loading cases

- 10 mm: matching minimum at 1.0312 GHz; S11 at target -7.839072 dB; gain 0.7515 dBi
- 5 mm: matching minimum at 0.9792 GHz; S11 at target -5.903831 dB; gain 0.3534 dBi
- 0.1 mm: documented dominant minimum at 1.3976 GHz; S11 at target -6.951098 dB; gain -5.261 dBi

### Retuning

- Selected 5 mm retuned length: 106.6 mm
- Matching minimum: 1.0928 GHz
- S11 at target improved to -8.000936 dB
- The -10 dB matching criterion was not fully recovered

## Evidence Classification

- Analytical and simulated evidence only.
- No fabrication, VNA measurement, chamber measurement, or SAR validation is claimed.
- Native CST binaries are not included in ordinary Git history.

## Numerical Reliability

- CST Learning Edition imposed a 100,000-cell limit.
- The body was represented by a finite 150 mm by 60 mm skin-fat-muscle patch.
- Open-boundary spacing was reduced to 10 mm, producing a reduced-PML-layer warning.
- Formal mesh and boundary convergence were not completed.
- The 0.1 mm non-monotonic matching-minimum displacement is classified as a fixed-model observation and is not generalized as a convergence-validated physical trend.

## Validation Performed

- LaTeX source compiled successfully with `latexmk` and `biber`.
- Final PDF contains 80 A4 pages and was rendered for visual inspection.
- Report metadata identifies the public project and author.
- Source and package searches found no student ID, course, instructor, grading, D2L, KSU-logo, or Persian maintenance comments.
- Selected values were synchronized across the report, project README, result summaries, and handoff.
- No `.cst` file or oversized file is included.
- PR #4 was merged and the remote feature branch was deleted.

## Limitations and Follow-Up

- No experimental validation is included.
- The finite body model is not anatomical.
- SAR and regulatory compliance are outside scope.
- Future work should include mesh and boundary convergence, a higher-fidelity body model, impedance-matching optimization, and measured validation.

## Rollback

Revert merge commit `5ca32e11dc181622997b4a4346aa3c1a88a98e4d` to remove the wearable project package without rewriting repository history.
