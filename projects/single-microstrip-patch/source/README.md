# LaTeX Source

This directory contains the self-contained public portfolio report source for the 915 MHz inset-fed microstrip patch antenna.

## Build

Run from this directory:

```bash
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The source uses the same restrained university-style architecture as the published 5G patch-array and resonant wire-dipole portfolio reports.

The public source intentionally excludes institutional branding, student identification, grading material, the native CST binary, and generated LaTeX auxiliary files.
