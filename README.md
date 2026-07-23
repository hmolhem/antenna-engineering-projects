# Antenna Engineering Projects

A public engineering portfolio by **Hossein Molhem** focused on antenna design, applied electromagnetics, full-wave simulation, arrays, mutual coupling, and beam steering.

This repository presents project-level engineering work rather than chapter-by-chapter study notes. Each project is organized to show the design objective, analytical baseline, simulation method, quantitative results, validation evidence, numerical limitations, and engineering conclusions.

> **Evidence classification:** Unless a project explicitly states otherwise, the results in this repository are analytical or simulated. Fabrication and measurement results will be identified separately and will not be implied from simulation data.

## Featured Project

### 5G Microstrip Patch Array with Beam Steering

**Status:** Public project package in preparation

The first featured project develops a single inset-fed microstrip patch and extends it to a two-element array for a nominal **2.50 GHz** operating frequency.

Current verified simulation highlights include:

- Tuned single-patch resonance near **2.491 GHz**
- Minimum simulated reflection coefficient of approximately **-30.7 dB**
- Two-port **2 x 1** array implementation
- S-parameter and mutual-coupling evaluation
- Broadside excitation and relative phase cases of **+90 degrees** and **-90 degrees**
- Far-field, directivity, gain, and efficiency analysis
- Explicit documentation of solver, mesh-cell, material-model, and array-detuning limitations

See [`projects/5g-patch-array/`](projects/5g-patch-array/) for the current project record.

## Project Portfolio

| Project | Engineering focus | Status |
|---|---|---|
| [5G Microstrip Patch Array](projects/5g-patch-array/) | Patch tuning, two-port array modeling, coupling, far field, beam steering | In preparation |
| Wearable Half-Wave Dipole | Multilayer body loading, detuning, efficiency, gain, retuning | Planned |
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
│   └── pull_request_template.md
├── assets/
│   └── README.md
├── docs/
│   ├── WORKFLOW.md
│   ├── PROJECT_STANDARD.md
│   ├── HANDOFF_INDEX.md
│   └── handoffs/
└── projects/
    ├── README.md
    └── 5g-patch-array/
        └── README.md
```

Each mature project is expected to include a project README, selected figures, quantitative results, a public report, reproducibility notes, and an explicit limitations section. Large proprietary or tool-specific binary models may be distributed separately rather than stored directly in Git history.

## Tools and Technical Areas

- **Electromagnetics:** antenna theory, radiation, polarization, arrays, waveguides
- **Simulation:** CST Studio Suite
- **Analysis:** Python, MATLAB
- **Documentation:** LaTeX, Markdown
- **Engineering workflow:** Git and GitHub

## Related Repositories

- [Engineering LaTeX Templates](https://github.com/hmolhem/engineering-latex-templates) — reusable report, presentation, IEEE-paper, and technical-carousel documentation system
- [Antenna Theory, Radar, and DSP Portfolio](https://github.com/hmolhem/antenna-theory-radar-dsp-portfolio) — educational notes, derivations, and numerical studies

## Collaboration

I am interested in research and engineering collaboration involving antenna design, antenna arrays, beamforming, applied electromagnetics, full-wave simulation, RF systems, and technical validation.

## Attribution and Academic Integrity

This is an independent educational and professional portfolio. It is not an official Kennesaw State University repository and does not imply endorsement by the university, an instructor, CST Studio Suite, or any third party.

Copyrighted textbooks, scanned pages, instructor solution manuals, and restricted course materials are not included. Project reports and figures are original unless a source is explicitly credited.

See [`LICENSE.md`](LICENSE.md) for the repository's content and code terms.