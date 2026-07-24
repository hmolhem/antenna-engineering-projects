# Antenna Engineering Projects

A public engineering portfolio by **Hossein Molhem** focused on antenna design, applied electromagnetics, full-wave simulation, arrays, mutual coupling, body loading, and beam steering.

This repository presents project-level engineering work rather than chapter-by-chapter study notes. Each project is organized to show the design objective, analytical baseline, simulation method, quantitative results, validation evidence, numerical limitations, and engineering conclusions.

> **Evidence classification:** Unless a project explicitly states otherwise, the results in this repository are analytical or simulated. Fabrication and measurement results will be identified separately and will not be implied from simulation data.

## Featured Project

### [5G Microstrip Patch Array Design and Beam Steering](projects/5g-patch-array/)

**Status:** Public project package available

The featured project develops an inset-fed microstrip patch at **2.501 GHz**, extends it to a two-port **2 x 1** array, quantifies mutual coupling, and demonstrates phase-controlled beam steering.

Verified simulation highlights include:

- Final single-patch resonance at **2.50507 GHz**
- Minimum simulated reflection coefficient of approximately **-39.87 dB**
- Single-patch peak directivity of approximately **7.226 dBi**
- PEC-baseline radiation and total efficiencies of approximately **96.3%** and **96.2%**
- Fixed-mesh copper sensitivity result with efficiencies of approximately **92.46%** and **92.38%**
- Two-port **2 x 1** array with approximately **-15 dB** mutual coupling
- Broadside excitation and relative phase cases of **+90 degrees** and **-90 degrees**
- Approximately **20-degree** simulated steering displacement in opposite half-planes
- Explicit documentation of mesh-cell, material-model, solver, and convergence limitations

The project package includes the public engineering report, LaTeX source, analytical Python scripts, selected CST figures, key-result tables, reproducibility material, and model-access notes.

## Wearable Antenna Project

### [Wearable Half-Wave Dipole Antenna](projects/wearable-half-wave-dipole/)

**Status:** Public project package available

This project evaluates a **1.120 GHz** center-fed cylindrical dipole above a finite multilayer skin-fat-muscle model. It establishes a tuned free-space baseline, compares three body-separation distances, quantifies efficiency and gain degradation, and performs first-order retuning for the **5 mm** case.

Verified simulation highlights include:

- Tuned free-space length of **122.0 mm** with **S11 = -15.48433 dB** at 1.120 GHz
- Matching-minimum shifts to **1.0312 GHz** at 10 mm and **0.9792 GHz** at 5 mm
- Gain degradation from **0.7515 dBi** at 10 mm to **0.3534 dBi** at 5 mm and **-5.261 dBi** at 0.1 mm
- Retuned 5 mm design using **L = 106.6 mm**, improving target-frequency S11 to **-8.000936 dB**
- Explicit classification of the 0.1 mm non-monotonic matching-minimum displacement as a fixed-model observation because mesh and boundary convergence were not completed
- No fabrication, measurement, or SAR-compliance claim

## Project Portfolio

| Project | Engineering focus | Status |
|---|---|---|
| [5G Microstrip Patch Array](projects/5g-patch-array/) | Patch synthesis and tuning, two-port array modeling, coupling, conductor-loss sensitivity, beam steering | Public package available |
| [Wearable Half-Wave Dipole](projects/wearable-half-wave-dipole/) | Multilayer body loading, detuning, efficiency, gain, numerical reliability, retuning | Public package available |
| Wire Dipole | Analytical design, resonance tuning, radiation pattern, HPBW | Planned |
| Hollow Rectangular Waveguide | Dominant-mode propagation and antenna-feed modeling | Planned |
| Single Microstrip Patch | Analytical dimensions, inset-feed matching, full-wave tuning | Planned |

## Engineering Methods

Projects may include:

- Analytical first estimates and design equations
- Parametric tuning and design-variable logs
- CST Studio Suite full-wave simulation
- Reflection coefficient, impedance, bandwidth, and port-coupling analysis
- Radiation pattern, beamwidth, directivity, gain, and efficiency evaluation
- Array excitation and phase-steering studies
- Mesh, boundary, solver, and numerical-reliability discussion
- Python or MATLAB post-processing
- LaTeX reports and technical presentations
- Git branches, pull requests, changelogs, and implementation handoffs

## Repository Structure

```text
antenna-engineering-projects/
├── README.md
├── LICENSE.md
├── CHANGELOG.md
├── .gitignore
├── .github/
├── assets/
├── docs/
│   ├── WORKFLOW.md
│   ├── PROJECT_STANDARD.md
│   ├── HANDOFF_INDEX.md
│   └── handoffs/
└── projects/
    ├── README.md
    ├── 5g-patch-array/
    │   ├── README.md
    │   ├── report/
    │   ├── source/
    │   ├── figures/
    │   ├── code/
    │   ├── results/
    │   └── simulation-notes/
    └── wearable-half-wave-dipole/
        ├── README.md
        ├── report/
        ├── source/
        ├── figures/
        ├── code/
        ├── results/
        └── simulation-notes/
```

Each mature project includes a project README, selected figures, quantitative results, a public report, reproducibility notes, and an explicit limitations section. Large proprietary or tool-specific binary models may be distributed separately rather than stored directly in Git history.

## Tools and Technical Areas

- **Electromagnetics:** antenna theory, radiation, polarization, arrays, waveguides
- **Simulation:** CST Studio Suite
- **Analysis:** Python, MATLAB
- **Documentation:** LaTeX, Markdown
- **Engineering workflow:** Git and GitHub

## Related Repositories

- [Engineering LaTeX Templates](https://github.com/hmolhem/engineering-latex-templates) - reusable report, presentation, IEEE-paper, and technical-carousel documentation system
- [Antenna Theory, Radar, and DSP Portfolio](https://github.com/hmolhem/antenna-theory-radar-dsp-portfolio) - educational notes, derivations, and numerical studies

## Collaboration

I am interested in research and engineering collaboration involving antenna design, antenna arrays, beamforming, wearable antennas, applied electromagnetics, full-wave simulation, RF systems, and technical validation.

## Attribution and Academic Integrity

This is an independent educational and professional portfolio. It is not an official Kennesaw State University repository and does not imply endorsement by the university, an instructor, CST Studio Suite, or any third party.

Copyrighted textbooks, scanned pages, instructor solution manuals, and restricted course materials are not included. Project reports and figures are original unless a source is explicitly credited.

See [`LICENSE.md`](LICENSE.md) for the repository's content and code terms.
