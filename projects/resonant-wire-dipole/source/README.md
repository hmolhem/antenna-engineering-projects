# Resonant Wire Dipole Portfolio Report Source

This folder is a project-specific instance of the public `portfolio-report-template`.
Its visual hierarchy is aligned with the published 5G patch-array engineering report:
a restrained academic cover, plain front matter, one principal report chapter, standard
black section headings, and maroon chapter titles.

The folder contains the LaTeX report source, analytical verification script, CST evidence
figures, run manifest, and recorded console output.

## Build

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Temporary build files and root-level `main.pdf` are not publication artifacts. The
reviewed PDF is stored in the project-level `report/` folder.
