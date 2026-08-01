# Inset-Fed Microstrip Patch Antenna Design and CST Validation

## Project status

**Public project package available**

This project develops a 915 MHz inset-fed rectangular microstrip patch on Rogers RT/duroid 5880, connects transmission-line synthesis to CST full-wave simulation, and documents the final input match, field distributions, and broadside far-field behavior.

## Key results

| Metric | Result |
|---|---:|
| Design frequency | 0.915 GHz |
| Substrate | Rogers RT/duroid 5880, er = 2.20, h = 1.575 mm |
| Analytical patch width / length | 129.51 mm / 109.79 mm |
| Final CST patch width / length | 129.5 mm / 108.2 mm |
| Final inset depth | 38.2 mm |
| Matching-minimum frequency | 0.9186 GHz |
| Minimum S11 | -22.14379 dB |
| Positive return loss | 22.14379 dB |
| Frequency error | 0.393% |
| Displayed peak directivity at 0.915 GHz | 7.01 dBi |
| Displayed principal-plane HPBW | 82.3 deg and 90.8 deg |

## Evidence classification

- **Analytical:** patch width, effective permittivity, fringing correction, physical length, inset-depth estimate, and derived matching quantities.
- **Simulated:** CST geometry, S-parameter marker, E/H fields, 3D directivity, and principal-plane patterns.
- **Measured:** no fabricated prototype, VNA sweep, or antenna-range measurement is claimed.

## Important qualifications

The public evidence package contains screenshots rather than the native CST model or raw exports. The patch and ground use PEC, so conductor loss is not modeled. No mesh- or boundary-convergence study is available. The slightly positive displayed radiation efficiency in dB is treated as a numerical-display anomaly and is not promoted as a verified KPI.

## Package contents

- `report/` - reviewed engineering report PDF
- `source/` - complete LaTeX source
- `code/` - analytical verification script
- `figures/` - curated CST evidence
- `results/` - human- and machine-readable key results
- `simulation-notes/` - numerical reliability and model-access notes
- `CHECKSUMS.sha256` - integrity record
