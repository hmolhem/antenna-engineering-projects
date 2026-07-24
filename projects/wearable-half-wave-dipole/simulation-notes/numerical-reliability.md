# Numerical Reliability and Limitations

- The study uses a finite 150 mm by 60 mm skin-fat-muscle patch rather than an anatomical body model.
- CST Studio Suite Learning Edition imposed a 100,000-cell limit.
- Open-boundary spacing was reduced to 10 mm to keep the body-loaded model within the cell limit; CST issued a reduced-PML-layer warning.
- The time-domain solver completed and reached its steady-state energy criterion, but a formal mesh-convergence and boundary-convergence study was not completed.
- The 0.1 mm case produced a non-monotonic dominant matching-minimum shift to 1.3976 GHz. This value is treated as a fixed-model observation and should not be generalized as a validated physical trend.
- The strongest supported comparative findings are degradation of target-frequency matching, radiation efficiency, total efficiency, and gain as the dipole approaches the lossy body model.
- No fabrication, VNA measurement, chamber measurement, or SAR validation is included.
