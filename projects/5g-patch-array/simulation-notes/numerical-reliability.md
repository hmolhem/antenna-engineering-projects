# Numerical Reliability and Modeling Limitations

## Solver environment

The models were developed with CST Studio Suite Learning Edition using a frequency-domain tetrahedral workflow. The limited mesh-cell allowance constrained adaptive refinement and finite-conductivity modeling.

## Metallization decision

The successfully tuned baseline single-patch and array simulations used PEC metallization while retaining DiClad 880-IM dielectric loss. PEC therefore preserves the dominant resonance, matching, directivity, and normalized pattern behavior, but omits copper ohmic loss.

A supplementary fixed-mesh lossy-metal copper simulation was completed for the final single-patch geometry. It produced nearly unchanged resonance, matching, directivity, and normalized pattern shape, while radiation efficiency decreased from approximately 96.3% to 92.46% and total efficiency decreased from approximately 96.2% to 92.38%.

## Convergence status

A formal mesh-convergence study was not completed. An adaptive finite-conductivity run exceeded the Learning Edition cell limit before convergence and its incomplete results were not used. A formal open-boundary convergence study was also not completed.

The results should therefore be interpreted as engineering-level simulation evidence, not as fully converged production-level prediction or measured antenna performance.

## Recommended future validation

Future work should compare progressively refined local meshes and increased open-boundary spacing using resonant frequency, S-parameters, mutual coupling, directivity, efficiencies, and steering angle as convergence metrics. Fabrication and vector-network-analyzer/anechoic-chamber measurements would be required for experimental validation.
