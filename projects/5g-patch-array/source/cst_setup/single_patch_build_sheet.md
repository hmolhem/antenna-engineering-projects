# CST Single-Patch Build Sheet

This file records the geometry and solver setup actually used for the inset-fed single-patch model.

## Coordinate convention

- Patch width and later array axis: **x-axis**
- Patch length and feed direction: **y-axis**
- Substrate thickness: **z-axis**
- Feed enters from the **negative-y** side
- Waveguide Port 1 is located at `y = feedYmin` and points in the positive-y direction

## Units

```text
Geometry: mm
Frequency: GHz
Time: ns
Temperature: K
Voltage: V
Current: A
Impedance: ohm
Conductance: S
Inductance: nH
Capacitance: pF
```

## Main CST parameters

```text
f0          = 2.501 GHz
fmin        = 2.0 GHz
fmax        = 3.0 GHz
epsr        = 2.20
lossTan     = 0.0009
h           = 1.524 mm
copperT     = 0.035 mm
copperSigma = 5.87e7 S/m
patchW      = 47.382 mm
patchL      = 39.657 mm initially; 38.40 mm final single patch
feedW       = 4.735 mm
feedL       = 15.000 mm
insetY      = 14.520 mm initially; 14.11 mm final single patch
insetGap    = 1.000 mm
gndW        = 56.526 mm
gndL        = 63.801 mm
arrayD      = 59.935 mm
portW       = 3*feedW = 14.205 mm
portH       = 5*h = 7.620 mm
```

## Layer stack

```text
Ground metal:  z = 0 to copperT
Substrate:      z = copperT to copperT + h
Top metal:      z = copperT + h to copperT + h + copperT
```

Numerical values:

```text
zTopSub   = 1.559 mm
zTopMetal = 1.594 mm
```

## Top-metal brick construction

The inset-fed patch is built using four connected rectangular bricks:

| Object | x range | y range | z range |
|---|---|---|---|
| Feed line | `-halfFeedW` to `halfFeedW` | `feedYmin` to `insetYend` | `zTopSub` to `zTopMetal` |
| Patch main | `-halfPatchW` to `halfPatchW` | `insetYend` to `patchYmax` | `zTopSub` to `zTopMetal` |
| Patch left arm | `-halfPatchW` to `-slotHalfW` | `patchYmin` to `insetYend` | `zTopSub` to `zTopMetal` |
| Patch right arm | `slotHalfW` to `halfPatchW` | `patchYmin` to `insetYend` | `zTopSub` to `zTopMetal` |

Derived coordinates:

```text
halfGndW  = gndW/2
halfGndL  = gndL/2
halfPatchW= patchW/2
halfFeedW = feedW/2
slotHalfW = halfFeedW + insetGap
feedYmin  = -halfGndL
patchYmin = -halfGndL + feedL
patchYmax = patchYmin + patchL
insetYend = patchYmin + insetY
feedYmax  = insetYend
```

## Port definition

```text
Port name: 1
Normal: Y
Orientation: Positive
Coordinates: Free
Xmin: -portW/2
Xmax:  portW/2
Ypos:  feedYmin
Zmin:  0
Zmax:  portH
Number of modes: 1
```

## Boundary and solver

```text
Solver: Frequency Domain, General Purpose
Mesh: Tetrahedral
Source type: All Ports
Frequency range: 2.0 to 3.0 GHz
S-parameter normalization: 50 ohm
Boundaries: Open (add space) on all six sides
Farfield monitor: 2.501 GHz
Solver accuracy used for tuning: 1e-3
Adaptive tetrahedral refinement: Off for Learning Edition mesh limit
```

The initial volumetric copper run exceeded the Learning Edition cell limit. The final tuned runs used PEC metallization while retaining the dielectric loss of DiClad 880-IM.

## Geometry documentation exported

The following CST geometry images are included in the report package:

```text
figures/5g_patch_array/single_patch/single_patch_top_view_geometry.png
figures/5g_patch_array/single_patch/single_patch_cross_section_geometry.png
```

The corresponding final-dimension and layer-stack tables are included in the LaTeX report.
