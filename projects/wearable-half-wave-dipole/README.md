# Wearable Half-Wave Dipole Antenna

## Project status

**Public engineering package available**

This project studies a center-fed cylindrical half-wave dipole at **1.120 GHz** near a finite multilayer skin-fat-muscle model. The workflow establishes a tuned free-space baseline, quantifies body-induced detuning and loss at three separation distances, and evaluates first-order retuning for the 5 mm case.

## Engineering questions

- How does a lossy high-permittivity body model change dipole input matching?
- How strongly do antenna-body spacing, mismatch, and tissue absorption affect efficiency and gain?
- Can length-only retuning recover the design-frequency match near the body?
- Which conclusions are reliable under CST Learning Edition mesh and boundary constraints?

## Key results

| Configuration | Dominant matching minimum | S11 at 1.120 GHz | Gain at 1.120 GHz |
|---|---:|---:|---:|
| Tuned free space, L = 122.0 mm | 1.1168 GHz | -15.48433 dB | Baseline |
| Body at 10 mm | 1.0312 GHz | -7.839072 dB | 0.7515 dBi |
| Body at 5 mm | 0.9792 GHz | -5.903831 dB | 0.3534 dBi |
| Body at 0.1 mm | 1.3976 GHz* | -6.951098 dB | -5.261 dBi |
| Retuned body at 5 mm, L = 106.6 mm | 1.0928 GHz | -8.000936 dB | Not used as a validated comparison metric |

\*The 0.1 mm non-monotonic matching-minimum displacement was not verified through mesh or boundary convergence and is reported as a fixed-model observation.

## Evidence classification

- Analytical design calculations
- CST full-wave simulation
- No fabricated prototype or measured validation
- No SAR or regulatory-compliance claim

## Numerical limitations

The CST Learning Edition 100,000-cell limit required a finite body patch and reduced open-boundary spacing. A formal mesh- and boundary-convergence campaign was not completed. These limitations are documented explicitly in [numerical-reliability.md](simulation-notes/numerical-reliability.md).

## Package contents

- [Engineering report PDF](report/wearable-half-wave-dipole-engineering-report.pdf)
- [Reproducible LaTeX source](source/)
- [Analytical verification script](code/wearable_dipole_verification.py)
- [Key results](results/key-results.md)
- [Curated figures](figures/)
- [Numerical reliability notes](simulation-notes/numerical-reliability.md)
- [Native model access notes](simulation-notes/model-access.md)

## Tools

CST Studio Suite Learning Edition, Python, LaTeX, Git, and GitHub.
