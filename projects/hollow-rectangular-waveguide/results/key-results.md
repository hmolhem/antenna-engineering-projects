# Key Results

## Model

- Cross section: 20 mm x 20 mm
- Length: 90 mm
- Interior: vacuum
- Walls: PEC
- Frequency sweep: 8-15 GHz
- Principal observation frequency: 10 GHz
- Solver evidence: CST frequency-domain results
- Port solution: three modes per port

## Analytical modal quantities

| Quantity | Value |
|---|---:|
| TE10 cutoff | 7.494811 GHz |
| TE01 cutoff | 7.494811 GHz |
| (1,1)-family cutoff | 10.599264 GHz |
| TE20/TE02 cutoff | 14.989623 GHz |
| Free-space wavelength at 10 GHz | 29.979246 mm |
| Lowest-order guide wavelength at 10 GHz | 45.284113 mm |
| Lowest-order TE impedance at 10 GHz | 569.056941 ohm |
| Electrical length | 1.987452 guide wavelengths |

## CST cutoff values

| Solved mode | Port 1 | Port 2 | Theory | Port 1 error | Port 2 error |
|---|---:|---:|---:|---:|---:|
| Mode 1 | 7.490707 GHz | 7.490310 GHz | 7.494811 GHz | -0.0548% | -0.0601% |
| Mode 2 | 7.491242 GHz | 7.490640 GHz | 7.494811 GHz | -0.0476% | -0.0557% |
| Mode 3 | 10.593500 GHz | 10.593100 GHz | 10.599264 GHz | -0.0544% | -0.0582% |

## Plot-derived observations

- `S1(1),1(1)` remains below approximately -50 dB across the plotted band and is near -85 dB at 10 GHz.
- `S2(2),1(1)` is the dominant transmitted projection and is near -0.02 dB at 10 GHz.
- `S2(3),1(1)` is much smaller than the degenerate-pair transmission term.
- These are visual estimates from CST plots, not raw-data values.

## Reliability statement

The cutoff-frequency agreement is quantitatively strong within the ideal model. Practical horn-feed suitability is not established because finite conductivity, transitions, tolerances, convergence, and measurement are absent.
