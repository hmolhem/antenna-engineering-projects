# Project Documentation Standard

Each project should be understandable to an engineering reviewer without requiring access to the original course prompt or private simulation workspace.

## Minimum Public Record

A mature project should contain:

```text
project-name/
├── README.md
├── report/
├── figures/
├── code/
├── results/
└── simulation-notes/
```

Not every folder must exist in the first commit, but missing evidence should be marked clearly.

## Required README Sections

Each project README should include:

1. Engineering objective
2. Operating frequency or design requirements
3. Analytical baseline
4. Geometry and materials
5. Simulation or measurement method
6. Key quantitative results
7. Validation and numerical-reliability checks
8. Limitations
9. Reproducibility and model-access notes
10. Engineering conclusions

## Result Reporting

Quantitative claims should include units, reference conditions, and evidence source. For example:

```text
Simulated S11 minimum: -30.7 dB at 2.491 GHz
```

Avoid unsupported statements such as "excellent performance" without a metric and comparison basis.

## Figures

Figures should have descriptive names and captions. Preferred examples:

```text
single_patch_s11_tuned.png
array_2x1_geometry_ports.png
array_broadside_farfield_3d.png
beam_steering_minus90_phi0_cut.png
```

Every figure should identify what is plotted, the operating condition, and the relevant excitation or parameter case.

## Simulation Limitations

Document material simplifications, learning-edition limits, solver warnings, mesh restrictions, missing convergence studies, and any differences between ideal array theory and the simulated structure.

## Measurement Claims

Do not describe simulated results as measured. Fabrication, calibration, test setup, instrumentation, and uncertainty should be documented before claiming experimental validation.
