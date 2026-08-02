# Numerical Reliability

- The model has finite transverse dimensions and electric/magnetic side walls; it is a
  TEM-like finite model, not a literal infinite plane wave in unbounded free space.
- The native CST project, raw complex S-parameter export, solver log, and mesh
  statistics were not supplied.
- No mesh-convergence, boundary-size, port-length, or requested-mode convergence study
  is preserved.
- The source report records a Port 2 warning involving higher-order mode accuracy and a
  non-standard mode.
- Agreement of the fundamental-mode minimum locations with analytical theory supports
  the intended physical interpretation but does not independently validate higher-order
  modal behavior.
- Exact null depth is treated as a fixed-model numerical output. The minimum locations
  are the principal validation metric.
- The slab is modeled as lossless and nonmagnetic; material dispersion, dielectric loss,
  fabrication tolerance, and experimental measurement are outside the evidence set.
