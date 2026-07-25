# Hollow Rectangular Waveguide Report Source

This directory contains the reproducible LaTeX source for the public
portfolio edition of the hollow rectangular waveguide modal-analysis
project.

## Portfolio report architecture

The visual language and front-matter sequence follow the public 5G patch-array
portfolio report:

1. minimal cover page;
2. Portfolio Context and Evidence;
3. Abstract;
4. Project Objective;
5. table of contents, list of figures, and list of tables;
6. technical report body, appendix, and references.

The cover intentionally contains only the project title, subtitle, author,
portfolio-edition label, and date. Evidence classification and publication
context are kept on their own page rather than placed on the cover.

## Compilation

```bash
latexmk -pdf main.tex
```

The bibliography uses `biblatex` with Biber. Numbered in-text citations are
hyperlinked in red, internal document links are blue, and URLs are cyan.

## Evidence scope

The report contains analytical and CST-simulated evidence. It does not claim
fabrication, measurement, finite-conductivity validation, or a completed horn
feed.

## Engineering evidence traceability

The report includes a dedicated Engineering Evidence Matrix before the conclusion. It maps each major claim to analytical or simulated evidence, quantitative outcomes, evidence disposition, and the next validation action.
