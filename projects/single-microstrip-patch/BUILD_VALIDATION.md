# Build and Visual Validation

## Source basis

- Uploaded academic source: `Molhem_Hossein_CST_Simulation_3_Patch_Antenna_Report_Source(1).zip`
- Original academic PDF: 25 A4 pages
- Portfolio architecture: restrained `portfolio-report-template` variant aligned with the published 5G patch-array and resonant wire-dipole reports

## Conversion controls

- Removed the Kennesaw State University logo and institutional branding.
- Removed student ID, instructor, course number, grading strategy, rubric-compliance content, and administrative submission language.
- Retained 915 MHz and inset feed as the public engineering specification rather than exposing the original student-ID selection rule.
- Reorganized the report as Portfolio Context and Evidence, Abstract, Project Objective, one main engineering chapter, an Engineering Verification Matrix, and reproducibility appendices.
- Replaced negative "return loss" wording with the correct distinction between \(S_{11}=-22.14379\) dB and positive return loss of 22.14379 dB.
- Added numerical-reliability qualifications for PEC conductors, missing raw exports, missing native CST files, absent convergence studies, and the slightly positive displayed radiation-efficiency value in dB.

## Analytical validation

The included Python script was executed successfully and regenerated:

- free-space wavelength: 327.64 mm
- patch width: 129.51 mm
- effective dielectric constant: 2.1605
- fringing extension: 0.834 mm
- effective patch length: 111.45 mm
- physical patch length: 109.79 mm
- inset-depth estimate: 38.13 mm
- reflection magnitude: 0.0781
- VSWR: 1.170
- frequency error: 3.6 MHz, or 0.393%

## PDF validation

- Final PDF: `single-microstrip-patch-engineering-report.pdf`
- Page size: A4
- Page count: 26
- PDF preflight: passed
- Rendered-page inspection: 26 of 26 pages
- Front-matter comparison: pages 1-4 visually aligned with the prior portfolio reports
- Unresolved references or citations: none
- Overfull boxes: none
- Blank or unintended pages: none observed
- Student ID, KSU name/logo, instructor name, and course number: absent from the public PDF
- PDF SHA-256: `1b27bbff7676930fbe22e29b3a95d7176e116bd67dfcca9964a1fa3e2a999b18`

## Evidence boundary

The final package contains analytical and simulated evidence only. No fabrication, VNA measurement, gain measurement, or radiation-range validation is claimed.
