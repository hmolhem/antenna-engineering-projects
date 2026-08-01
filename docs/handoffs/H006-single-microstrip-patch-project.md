# H006 - Inset-Fed Single Microstrip Patch Public Package

- **Handoff ID:** H006
- **Date:** 2026-08-01
- **Branch:** `feature/single-microstrip-patch-project`
- **Pull request:** [#10](https://github.com/hmolhem/antenna-engineering-projects/pull/10)
- **Status:** Merged
- **Head commit:** `55f82bcfe7b163c66c0c295152b0263b859231a9`
- **Merge commit:** `ac5664ee5b2174ec24ba84dcf891e78531da8154`

## Purpose

Publish the fifth complete engineering project package in the antenna portfolio: analytical synthesis, CST tuning, input-match interpretation, field visualization, and radiation-pattern validation for a 915 MHz inset-fed rectangular microstrip patch on Rogers RT/duroid 5880.

## Implemented

- Added a 26-page public engineering report.
- Added sanitized and reproducible LaTeX source based on the `portfolio-report-template` architecture.
- Matched the cover, front matter, page geometry, headers, chapter hierarchy, and restrained academic visual language of the published 5G patch-array, waveguide, and resonant wire-dipole reports.
- Removed the Kennesaw State University logo, student ID, instructor, course number, grading strategy, rubric-compliance material, and administrative submission language.
- Reframed the 915 MHz operating frequency and inset feed as public engineering specifications rather than exposing the original student-ID selection rule.
- Added Portfolio Context and Evidence, Abstract, and Project Objective as separate plain-text front-matter pages.
- Added analytical verification for wavelength, patch width, effective dielectric constant, fringing extension, physical patch length, inset-depth estimate, reflection magnitude, VSWR, and frequency error.
- Added curated CST geometry, reflection-coefficient, E-field, H-field, 3D-pattern, and principal-plane pattern figures.
- Corrected terminology by separating negative reflection coefficient from positive return loss.
- Distinguished the 0.9186 GHz matching-minimum marker from the 0.915 GHz field and far-field monitors.
- Documented PEC metallization, dielectric loss, missing raw exports, missing native CST files, absent convergence studies, and the slightly positive displayed radiation-efficiency value in dB.
- Added Markdown and CSV key-result summaries, an analytical Python script, captured analytical output, numerical-reliability notes, and native-model-access notes.
- Added an Engineering Verification Matrix mapping principal claims to evidence, outcomes, dispositions, and next validation actions.
- Updated the root README, project portfolio index, changelog, and handoff index.

## Verified Results

### Analytical baseline

- Design frequency: 0.915 GHz
- Free-space wavelength: 327.64 mm
- Rogers RT/duroid 5880 substrate: relative permittivity 2.20 and thickness 1.575 mm
- Analytical patch width: 129.51 mm
- Effective dielectric constant: 2.1605
- Fringing extension: 0.834 mm
- Effective patch length: 111.45 mm
- Analytical physical patch length: 109.79 mm
- Analytical inset-depth estimate: 38.13 mm

### CST tuning and final result

- Final CST patch width: 129.5 mm
- Final CST patch length: 108.2 mm
- Final inset depth: 38.2 mm
- Exact displayed matching-minimum frequency: 0.9186 GHz
- Exact displayed reflection-coefficient marker: -22.14379 dB
- Equivalent positive return loss: 22.14379 dB
- Derived reflection magnitude: 0.0781
- Derived VSWR: 1.170
- Frequency error from the 0.915 GHz target: 3.6 MHz or 0.393%
- Displayed peak directivity at 0.915 GHz: 7.01 dBi
- Displayed Phi=0 HPBW: 82.3 degrees
- Displayed Phi=90 HPBW: 90.8 degrees

## Evidence Classification

- Analytical and simulated evidence only.
- No fabricated prototype, VNA measurement, gain measurement, field-probe measurement, or antenna-range validation is claimed.
- Exact numerical claims are limited to displayed CST markers or independently regenerated analytical values.
- Derived matching quantities are identified separately from direct CST outputs.
- The field and far-field screenshots are recorded at 0.915 GHz, while the matching minimum occurs at 0.9186 GHz.
- Native CST binary models are not included in ordinary Git history.

## Numerical Reliability

- No raw CST S-parameter or far-field export is included.
- No formal mesh-convergence or boundary-distance convergence study is available.
- Solver settings, boundary settings, and mesh statistics are not fully preserved in the public evidence set.
- The patch and ground are modeled as PEC, so finite-conductivity copper loss is not represented.
- Dielectric loss is retained through the stated substrate loss tangent.
- The slightly positive displayed radiation efficiency in dB corresponds to a value marginally above unity and is treated as a numerical-display anomaly rather than a validated KPI.
- The report does not establish fabrication tolerance, connector effects, feed-launch effects, or measured performance.

## Validation Performed

- LaTeX source compiled successfully with the documented PDFLaTeX and Biber sequence.
- Final PDF contains 26 A4 pages and all pages were rendered for visual inspection.
- Pages 1-4 were compared against the established portfolio-report architecture.
- No unresolved citations or cross-references remain.
- No overfull boxes were reported in the final build log.
- Analytical geometry and matching quantities were regenerated with the included Python script.
- Values were synchronized across the report, README, key-result files, project index, root README, and this handoff.
- SHA-256 integrity records are included for the public package files.
- No `.cst` file, student ID, grading record, university logo, or restricted course material is included.

## Limitations and Follow-Up

Future validation should export raw S-parameter and far-field data, preserve solver and mesh records, complete mesh and boundary convergence studies, model finite-conductivity copper, quantify bandwidth and realized gain, include connector and fabrication tolerances, fabricate a prototype, and perform VNA and radiation-pattern measurements.

## Rollback

Revert merge commit `ac5664ee5b2174ec24ba84dcf891e78531da8154` to remove the single-patch project package without rewriting repository history.
