# Normal-Incidence Plane-Wave Reflection from a Dielectric Slab

## Project status

**Public project package available**

This project studies a lossless air--dielectric--air slab at normal incidence using a
transmission-line model and CST frequency-domain simulation. The slab thickness is
approximately one free-space wavelength at 1 GHz, and relative permittivity is swept
from 1 to 10 in 0.25 increments.

## Key results

| Metric | Result |
|---|---:|
| Evaluation frequency | 1.000 GHz |
| Analytical free-space wavelength | 299.792 mm |
| CST slab thickness | 299.79 mm |
| Permittivity sweep | 1.00 to 10.00 in 0.25 steps |
| Predicted matched values | 1.00, 2.25, 4.00, 6.25, 9.00 |
| CST minimum locations | Same five sweep values |
| CST \|S11\| at eps_r = 4 | 0.0104206 |
| Equivalent value at eps_r = 4 | -39.64 dB |
| Field-validation case | eps_r = 4 at 1 GHz |

## Evidence classification

- **Analytical:** transmission-line input impedance, reflection coefficient,
  half-wavelength matching condition, regenerated magnitude and phase curves.
- **Simulated:** CST geometry, boundaries, ports, parameter sweep, S-parameter curves,
  result table, and E/H field screenshots.
- **Measured:** no experimental or material-measurement evidence is claimed.

## Important qualifications

The principal validation metric is the location of the reflection minima, not their
exact depth. The public source archive does not include the native CST model, raw
complex S-parameter export, mesh statistics, solver log, or formal port/mesh
convergence record. A higher-order port-mode accuracy warning was reported. The model
uses finite transverse dimensions and electric/magnetic side walls to approximate a
TEM-like environment rather than an infinite free-space plane wave.

## Package contents

- `report/` - compiled portfolio-report PDF
- `source/` - complete LaTeX source
- `code/` - analytical verification script
- `figures/cst-results/` - preserved CST evidence
- `figures/analytical/` - regenerated analytical plots
- `results/` - human- and machine-readable results
- `simulation-notes/` - model-access and numerical-reliability notes
- `CHECKSUMS.sha256` - integrity record
