# Numerical Reliability

## Strongest evidence

The analytical and CST cutoff frequencies agree within 0.061% for all three reported modes at both ports. The two port solutions are also mutually consistent.

## Important limitations

- No formal mesh-density or adaptive-convergence record is included.
- No systematic port-polarization or eigenbasis sensitivity study was performed.
- The model uses vacuum and PEC, so conductor and dielectric loss are absent.
- Raw S-parameter exports are unavailable; non-marker values are visual estimates.
- Only the first three solved port modes are documented.
- The square guide has a degenerate modal subspace, so mode index is not a unique physical polarization label.
- The native CST model is not included in ordinary Git history.
- No horn flare, transition, manufacturing tolerance, or measured validation is included.

## Interpretation rule

For the degenerate lowest-order pair, interpret transmitted power across the full two-mode subspace. Do not treat one same-index S-parameter as the total transmission.

## Future validation

A stronger engineering validation campaign should include:

1. Mesh and port-eigenmode convergence.
2. Controlled polarization lines or a slightly rectangular cross section.
3. Finite-conductivity copper walls.
4. Raw Touchstone or CSV data export.
5. Horn transition and flare modeling.
6. Prototype and VNA or field measurement.
