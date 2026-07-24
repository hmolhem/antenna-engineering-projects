# Reproducible Report Source

This directory contains the sanitized LaTeX source for the wearable half-wave dipole engineering report.

## Build

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

The build requires a LaTeX distribution with `biber`, `biblatex`, `listings`, and the standard AMS packages.

## Evidence classification

The report contains analytical calculations and CST simulation results. It does not claim fabrication, measured validation, or SAR compliance. The 0.1 mm non-monotonic matching-minimum displacement is explicitly classified as a fixed-model result because formal mesh and boundary convergence were not completed.

## Native CST model

Native `.cst` files are intentionally excluded from the public Git history. See `../simulation-notes/model-access.md` in the project package.
