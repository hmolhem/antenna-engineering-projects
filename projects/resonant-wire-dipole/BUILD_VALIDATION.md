# Build and Visual Validation Record

## Report

- Title: Resonant Wire Dipole Design and CST Validation
- Template basis: `portfolio-report-template`
- Visual reference: published `5g-patch-array` engineering report
- Paper size: A4
- Final page count: 25

## Build sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Validation completed

- PDF opens successfully with PyMuPDF.
- All 25 pages rendered successfully for visual inspection.
- Pages 1-4 were specifically checked against the 5G report source architecture.
- The cover uses the same restrained two-rule composition as the 5G report.
- Portfolio Context, Abstract, and Project Objective use plain academic text without colored evidence boxes.
- The main report uses one principal chapter with standard black section and subsection headings.
- Colored analytical, simulated, measured, limitation, and engineering-decision boxes were removed.
- No unresolved citations or cross-references remain.
- No overfull boxes were reported in the final LaTeX log.
- Figures, tables, appendices, and bibliography were visually reviewed.

## Evidence limitation

The report remains based on analytical calculations and preserved CST screenshots. It
does not claim measured hardware performance or completed mesh/boundary convergence.
