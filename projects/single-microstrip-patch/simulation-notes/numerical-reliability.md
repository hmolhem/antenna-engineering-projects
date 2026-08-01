# Numerical Reliability

- The supplied public source contains exported CST screenshots, not the native `.cst` model or raw numerical exports.
- The exact matching minimum is supported by the marker `(0.9186 GHz, -22.14379 dB)`.
- E-field, H-field, and far-field monitors are shown at 0.915 GHz, not at the 0.9186 GHz matching minimum.
- Patch and ground metallization are PEC; the 0.035 mm thickness is geometrical and conductor loss is omitted.
- No mesh-convergence or boundary-distance convergence study was supplied.
- Solver logs, mesh statistics, and stopping-criterion records were not preserved in the uploaded archive.
- The 3D far-field panel displays radiation efficiency of +0.03436 dB, which is marginally above 100% when converted to linear efficiency. It is treated as a numerical-display anomaly and not used as a verified KPI.
- No fabrication, connector transition, material-tolerance study, VNA measurement, gain measurement, or radiation-range validation is claimed.
