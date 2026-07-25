# Hollow Rectangular Waveguide Modal Analysis

## Project status

**Public engineering package available**

This project analyzes an ideal vacuum-filled, PEC-walled **20 mm x 20 mm x 90 mm** hollow square waveguide over **8-15 GHz**, with detailed interpretation at **10 GHz**. The central engineering issue is modal degeneracy: the equal transverse dimensions make the lowest-order TE10 and TE01 modes share the same cutoff frequency, so the numerical port basis is not unique.

## Engineering questions

- Which low-order modes propagate at 10 GHz?
- How closely do CST port-eigenmode cutoff frequencies agree with closed-form theory?
- Why can the dominant transmitted coefficient appear in a different output mode index?
- Do the electric-field, magnetic-field, and wall-current plots support the predicted modal behavior?
- What prevents the idealized structure from being treated as a production-ready horn feed?

## Key results

| Quantity | Analytical result | CST Port 1 | CST Port 2 |
|---|---:|---:|---:|
| Lowest-order cutoff, Mode 1 | 7.494811 GHz | 7.490707 GHz | 7.490310 GHz |
| Lowest-order cutoff, Mode 2 | 7.494811 GHz | 7.491242 GHz | 7.490640 GHz |
| Third solved cutoff | 10.599264 GHz | 10.593500 GHz | 10.593100 GHz |
| Maximum cutoff difference from theory | - | 0.0548% | 0.0601% |

Additional analytical quantities at 10 GHz:

- Free-space wavelength: **29.979 mm**
- Lowest-order guide wavelength: **45.284 mm**
- Lowest-order TE wave impedance: **569.057 ohm**
- Electrical length: **1.987 guide wavelengths**

Plot-based observations:

- Same-mode input reflection stays below approximately **-50 dB** over the plotted 8-15 GHz band and is near **-85 dB** around 10 GHz.
- The dominant transmitted projection appears in `S2(2),1(1)` and is approximately **-0.02 dB** near 10 GHz.
- These S-parameter values are visual estimates because raw exported data are not included.

## Engineering interpretation

The large `S2(2),1(1)` coefficient does not by itself indicate physical mode conversion. The two lowest-order modes span a degenerate subspace, and CST may choose different orthogonal basis vectors at the two ports. The physically relevant quantity is therefore the transmitted power across the entire degenerate subspace, not only the same-index modal term.

## Evidence classification

- Closed-form rectangular-waveguide calculations
- Python verification
- CST frequency-domain simulation figures
- No fabricated prototype or measured validation
- No finite-conductivity or insertion-loss claim

## Numerical limitations

The public record does not include a mesh-convergence campaign, port-basis sensitivity study, raw S-parameter exports, or the native CST model. The guide uses vacuum filling and PEC walls. The model contains no horn flare, feed transition, or manufacturing tolerances.

See [numerical-reliability.md](simulation-notes/numerical-reliability.md).

## Package contents

- [Engineering report PDF](report/hollow-rectangular-waveguide-engineering-report.pdf)
- Engineering Evidence Matrix in the report, linking claims to evidence, dispositions, and follow-up validation
- [Reproducible LaTeX source](source/)
- [Analytical verification script](code/waveguide_verification.py)
- [Key results](results/key-results.md)
- [Curated figures](figures/)
- [Numerical reliability notes](simulation-notes/numerical-reliability.md)
- [Native model access notes](simulation-notes/model-access.md)

## Tools

CST Studio Suite, Python, LaTeX, Git, and GitHub.
