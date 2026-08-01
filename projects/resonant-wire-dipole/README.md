# Resonant Wire Dipole Design and CST Validation

## Project status

**Public project package available**

This project develops a finite-radius center-fed wire dipole near **1 GHz**, documents
three length-tuning cases, and verifies the final CST radiation behavior against the
canonical thin half-wave dipole pattern.

## Key results

| Metric | Result |
|---|---:|
| Target frequency | 1.000 GHz |
| Initial analytical length | 150.0 mm |
| Final tuned length | 135.6 mm |
| Final resonance | 0.99648 GHz |
| Final S11 | -47.01186 dB at 73-ohm reference |
| Equivalent return loss | 47.01186 dB |
| Frequency error | 0.352% |
| Displayed CST directivity | 2.149 dBi |
| Analytical directivity | 2.15 dBi |
| Analytical / displayed CST HPBW | 78.08 deg / approximately 78.4 deg |

## Evidence classification

- **Analytical:** wavelength, first-order half-wave length, canonical radiation pattern,
  directivity, and HPBW.
- **Simulated:** CST geometry, S-parameter plots, tuning trend, and far-field figures.
- **Measured:** no fabricated prototype or measurement campaign is claimed.

## Important qualifications

The final resonance and minimum S11 are exact displayed CST marker values. The
preliminary 150 mm and 125 mm minima are plot-derived estimates because raw curve data
were not supplied. The deep match applies to a 73-ohm port reference and should not be
presented as a 50-ohm qualification. Formal mesh and boundary convergence records were
not available.

## Package contents

- `report/` - reviewed engineering report PDF
- `source/` - complete LaTeX source based on the public portfolio template
- `code/` - independent analytical verification script
- `figures/` - curated analytical and CST evidence
- `results/` - human- and machine-readable key results
- `simulation-notes/` - numerical reliability and model-access notes
- `CHECKSUMS.sha256` - integrity record for the public package
