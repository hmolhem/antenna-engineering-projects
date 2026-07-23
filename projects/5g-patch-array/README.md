# 5G Microstrip Patch Array with Beam Steering

## Project Status

**Public package in preparation.** This page establishes the verified engineering record that will be expanded in a dedicated feature branch.

## Objective

Design and tune an inset-fed rectangular microstrip patch near **2.50 GHz**, extend the element to a two-port **2 x 1** array, evaluate matching and mutual coupling, and study broadside and phase-shifted excitation cases.

## Current Verified Simulation Record

| Quantity | Current result |
|---|---:|
| Nominal design frequency | 2.50 GHz |
| Tuned single-patch resonance | approximately 2.491 GHz |
| Tuned single-patch minimum S11 | approximately -30.7 dB |
| Tuned patch length | approximately 38.40 mm |
| Inset position | approximately 14.11 mm |
| Inset gap | 1.00 mm |
| Array configuration | Two-element, two-port linear array |
| Excitation cases | Broadside, +90-degree relative phase, -90-degree relative phase |

## Engineering Scope

The final public package is expected to cover:

- Analytical patch-dimension estimates
- Single-element geometry and inset-feed tuning
- S-parameter evaluation
- Two-element array construction and port definition
- Mutual coupling and resonance detuning
- Broadside excitation
- Relative phase excitation and beam-steering interpretation
- Three-dimensional far-field patterns and principal-plane cuts
- Directivity, gain, radiation efficiency, and total efficiency
- Solver warnings, mesh restrictions, and model limitations

## Important Modeling Limitation

The initial single-patch model used a DiClad 880 IM substrate and copper metallization. Due to CST Learning Edition mesh-cell constraints, the successful tuned model used PEC for metallic parts while retaining dielectric substrate loss. This simplification must be considered when interpreting conductor-loss-dependent quantities.

The array also exhibited coupling and resonance changes relative to the isolated element. Ideal array-factor steering predictions therefore provide a reference, not a substitute for the simulated coupled-array result.

## Evidence Classification

All results currently listed here are **simulated**. No fabrication or measurement validation is claimed.

## Planned Public Files

```text
5g-patch-array/
├── README.md
├── report/
├── figures/
├── results/
├── code/
└── simulation-notes/
```

Large CST binary models will not be added to ordinary Git history until an appropriate distribution method and file-size policy are selected.
