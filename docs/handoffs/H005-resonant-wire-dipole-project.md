# H005 - Resonant Wire Dipole Public Package

- **Handoff ID:** H005
- **Date:** 2026-08-01
- **Branch:** `feature/resonant-wire-dipole-project`
- **Pull request:** Pending
- **Status:** Ready for review

## Purpose

Publish the fourth complete engineering project package in the antenna portfolio: analytical sizing, CST length tuning, input-match interpretation, and radiation-pattern validation for a finite-radius center-fed wire dipole near 1 GHz.

## Implemented

- Added a 25-page public engineering report.
- Added sanitized and reproducible LaTeX source based on the `portfolio-report-template` architecture.
- Matched the cover, front matter, page geometry, headers, chapter hierarchy, and restrained academic visual language of the published 5G patch-array report.
- Removed student ID, course, instructor, grading, university branding, and administrative material.
- Added Portfolio Context and Evidence, Abstract, and Project Objective as separate plain-text front-matter pages.
- Added analytical verification for the canonical half-wave dipole pattern, directivity, and half-power beamwidth.
- Added curated CST geometry, reflection-coefficient, 2D-pattern, and 3D-pattern figures for the 150 mm, 125 mm, and 135.6 mm cases.
- Distinguished exact CST marker values from plot-derived estimates.
- Corrected terminology by separating negative reflection coefficient from positive return loss.
- Documented the 73-ohm port reference and avoided implying a 50-ohm or broadband qualification.
- Added Markdown and CSV key-result summaries, an analytical Python script, captured analytical output, numerical-reliability notes, and native-model-access notes.
- Added an Engineering Verification Matrix mapping the principal claims to evidence, outcomes, dispositions, and next validation actions.
- Updated the root README, project portfolio index, changelog, and handoff index.

## Verified Results

### Analytical baseline

- Target frequency: 1.000 GHz
- Free-space wavelength: 300.0 mm
- Initial half-wave length: 150.0 mm
- Canonical half-wave dipole directivity: 2.15 dBi
- Analytical half-power beamwidth: 78.08 degrees

### CST tuning and final result

- Preliminary 150 mm resonance: approximately 0.83 GHz, read from the plotted curve
- Preliminary 125 mm resonance: approximately 1.08 GHz, read from the plotted curve
- Final tuned length: 135.6 mm
- Final exact CST resonance marker: 0.99648 GHz
- Final exact CST reflection coefficient marker: -47.01186 dB with a 73-ohm port reference
- Equivalent positive return loss: 47.01186 dB
- Frequency error from the 1.000 GHz target: 3.52 MHz or 0.352%
- Displayed CST directivity: 2.149 dBi
- Displayed CST angular width: approximately 78.4 degrees

## Evidence Classification

- Analytical and simulated evidence only.
- No fabrication, VNA measurement, field-range measurement, or measured efficiency is claimed.
- Exact numerical claims are limited to displayed CST markers or independently regenerated analytical results.
- Preliminary resonances and displayed angular width are explicitly classified as plot-derived estimates.
- Native CST binary models are not included in ordinary Git history.

## Numerical Reliability

- No raw CST S-parameter export is included.
- No formal mesh-convergence or boundary-distance convergence study is available.
- Solver settings and mesh statistics are not fully preserved in the public evidence set.
- The very deep match depends on the 73-ohm reference impedance and should not be generalized to a 50-ohm interface.
- Agreement in directivity and HPBW supports pattern-level consistency but does not establish fabrication tolerance or measured performance.

## Validation Performed

- LaTeX source compiled successfully with the documented `pdflatex` and Biber sequence.
- Final PDF contains 25 A4 pages and all pages were rendered for visual inspection.
- Pages 1-4 were compared against the 5G report architecture.
- Colored evidence and decision boxes were removed in favor of plain academic text and standard headings.
- No unresolved citations or cross-references remain.
- No overfull boxes were reported in the final build log.
- Analytical directivity and HPBW were regenerated with the included Python script.
- Values were synchronized across the report, README, key-result files, project index, root README, and this handoff.
- SHA-256 integrity records are included for the public package files.
- No `.cst` file, student ID, grading record, or restricted course material is included.

## Limitations and Follow-Up

Future validation should export raw S-parameter and far-field data, record solver and mesh settings, complete mesh and boundary convergence studies, evaluate a 50-ohm feed/matching strategy, assess conductor and fabrication tolerances, fabricate a prototype, and perform VNA and radiation-pattern measurements.

## Rollback

Before merge, close the pull request and delete `feature/resonant-wire-dipole-project`. After merge, revert the H005 merge commit to remove the project package and restore the previous indexes without rewriting repository history.
