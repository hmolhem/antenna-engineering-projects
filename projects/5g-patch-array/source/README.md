# 5G Microstrip Patch Array Design and Beam Steering

This source package contains the public portfolio edition of an antenna-engineering report covering
analytical patch synthesis, CST full-wave simulation, two-port array characterization, mutual
coupling, and phase-controlled beam steering.

## Evidence classification

- **Analytical:** closed-form patch, feed-line, wavelength, array-spacing, and phase-shift calculations.
- **Simulated:** CST geometry, scattering parameters, directivity patterns, efficiencies, and beam steering.
- **Measured:** no fabricated prototype or measurement campaign is claimed.

## Key simulated results

### Single patch

- Design frequency: 2.501 GHz
- Final simulated resonance: 2.50507 GHz
- Minimum \(S_{11}\): approximately -39.87 dB
- Peak directivity: approximately 7.226 dBi
- PEC-baseline radiation efficiency: approximately 96.3%
- PEC-baseline total efficiency: approximately 96.2%
- Fixed-mesh copper sensitivity result: approximately 92.46% radiation efficiency and 92.38% total efficiency

### Two-element array

- Topology: two-port \(2\times1\) linear patch array
- Center-to-center spacing: 59.935 mm
- \(S_{11}\): approximately -11.93 dB near 2.498 GHz
- \(S_{22}\): approximately -15.20 dB near 2.497 GHz
- Mutual coupling: approximately -15 dB

### Beam steering

- Broadside: equal amplitude and 0-degree relative phase
- Steered cases: -90-degree and +90-degree relative phase
- CST-observed scan displacement: approximately 20 degrees in opposite half-planes
- Ideal two-element array-factor prediction: 30-degree magnitude

## Numerical limitations

The principal tuned models used PEC metallization while retaining dielectric loss because the CST
Studio Suite Learning Edition mesh-cell limit prevented a fully refined finite-conductivity workflow.
A supplementary fixed-mesh copper model was completed for the single patch. Formal mesh-convergence
and boundary-convergence studies were not completed, and the report states these limitations explicitly.

## Build

A TeX Live installation with `latexmk`, `pdflatex`, and `biber` is recommended.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

To remove generated build files:

```bash
latexmk -C
```

## Package structure

```text
appendices/       Python verification appendices and console outputs
codes/            Analytical Python scripts
content/          Main technical report sections
cst_setup/        Parameter and coordinate records
figures/          Curated CST geometry and result figures
frontmatter/      Cover, context, abstract, and project objective
setup/            LaTeX packages, layout, theme, and macros
main.tex          Report entry point
references.bib    Public technical references
```

Native CST project files are not included in this ordinary source archive because of file-size and
distribution considerations. Institutional branding, student-identification data, grading material,
and course-administration content have been removed from the public edition.
