"""
Initial rectangular microstrip patch design calculations.

This script verifies the analytical starting dimensions used in the
public engineering report. The selected design frequency is 2.501 GHz.
The substrate is DiClad 880-IM with h = 0.060 in = 1.524 mm.
"""

from __future__ import annotations

from math import acos, log, pi, sqrt

C0 = 299_792_458.0  # Speed of light in vacuum, m/s
F0_HZ = 2.501e9

# Nominal Rogers DiClad 880 design values.
EPS_R = 2.20
TAN_DELTA = 0.0009
H_M = 1.524e-3

# Inset-feed engineering starting assumptions.
Z0_TARGET = 50.0
EDGE_RESISTANCE_ESTIMATE = 300.0
INSET_GAP_M = 1.000e-3
FEED_EXTENSION_M = 15.000e-3


def microstrip_effective_eps(width_over_h: float, eps_r: float) -> float:
    """Return the quasi-static effective permittivity of a microstrip line."""
    return (
        (eps_r + 1.0) / 2.0
        + (eps_r - 1.0) / 2.0
        * (1.0 + 12.0 / width_over_h) ** (-0.5)
    )


def microstrip_z0_from_u(width_over_h: float, eps_r: float) -> float:
    """Return the characteristic impedance for a given width ratio W/h."""
    u = width_over_h
    eps_eff = microstrip_effective_eps(u, eps_r)

    if u <= 1.0:
        return 60.0 / sqrt(eps_eff) * log(8.0 / u + 0.25 * u)

    return 120.0 * pi / (
        sqrt(eps_eff) * (u + 1.393 + 0.667 * log(u + 1.444))
    )


def solve_microstrip_width_for_z0(
    z0_target: float,
    eps_r: float,
    h_m: float,
) -> tuple[float, float, float]:
    """Solve for microstrip width using bisection on the ratio W/h."""
    lo = 0.01
    hi = 20.0

    for _ in range(100):
        mid = 0.5 * (lo + hi)
        z_mid = microstrip_z0_from_u(mid, eps_r)

        if z_mid > z0_target:
            lo = mid
        else:
            hi = mid

    u = 0.5 * (lo + hi)
    width_m = u * h_m
    eps_eff_feed = microstrip_effective_eps(u, eps_r)
    return width_m, u, eps_eff_feed


lambda0_m = C0 / F0_HZ
patch_width_m = C0 / (2.0 * F0_HZ) * sqrt(2.0 / (EPS_R + 1.0))
eps_eff = (
    (EPS_R + 1.0) / 2.0
    + (EPS_R - 1.0) / 2.0
    * (1.0 + 12.0 * H_M / patch_width_m) ** (-0.5)
)
delta_l_m = (
    0.412
    * H_M
    * ((eps_eff + 0.3) * (patch_width_m / H_M + 0.264))
    / ((eps_eff - 0.258) * (patch_width_m / H_M + 0.8))
)
effective_length_m = C0 / (2.0 * F0_HZ * sqrt(eps_eff))
patch_length_m = effective_length_m - 2.0 * delta_l_m

# Finite ground-plane and substrate starting dimensions.
ground_width_m = patch_width_m + 6.0 * H_M
minimum_ground_length_m = patch_length_m + 6.0 * H_M
ground_length_with_feed_m = patch_length_m + FEED_EXTENSION_M + 6.0 * H_M
element_spacing_m = lambda0_m / 2.0

feed_width_m, feed_width_over_h, eps_eff_feed = (
    solve_microstrip_width_for_z0(Z0_TARGET, EPS_R, H_M)
)
feed_z0_check = microstrip_z0_from_u(feed_width_over_h, EPS_R)
inset_depth_m = (
    patch_length_m
    / pi
    * acos(sqrt(Z0_TARGET / EDGE_RESISTANCE_ESTIMATE))
)

print("Initial Microstrip Patch Design Verification")
print("=" * 72)
print(f"Selected f0: {F0_HZ / 1e9:.6f} GHz")
print("Selected substrate: DiClad 880-IM")
print(f"Working eps_r: {EPS_R:.4f}")
print(f"Working tan_delta: {TAN_DELTA:.5f}")
print(f"Substrate thickness h: {H_M * 1e3:.3f} mm")
print("-" * 72)
print("Rectangular patch starting dimensions")
print(f"lambda0: {lambda0_m * 1e3:.3f} mm")
print(f"Patch width W: {patch_width_m * 1e3:.3f} mm")
print(f"Effective permittivity eps_eff: {eps_eff:.4f}")
print(f"Length extension DeltaL: {delta_l_m * 1e3:.3f} mm")
print(f"Effective length L_eff: {effective_length_m * 1e3:.3f} mm")
print(f"Patch length L: {patch_length_m * 1e3:.3f} mm")
print("-" * 72)
print("Finite ground/substrate starting dimensions")
print(f"Minimum ground width Wg = W + 6h: {ground_width_m * 1e3:.3f} mm")
print(
    "Minimum ground length Lg_min = L + 6h: "
    f"{minimum_ground_length_m * 1e3:.3f} mm"
)
print(f"Feed extension Lf: {FEED_EXTENSION_M * 1e3:.3f} mm")
print(
    "Inset-fed model ground length Lg = L + Lf + 6h: "
    f"{ground_length_with_feed_m * 1e3:.3f} mm"
)
print("-" * 72)
print("Inset-fed microstrip matching starting values")
print(f"Target feed-line impedance Z0: {Z0_TARGET:.1f} ohm")
print(f"Feed width ratio Wf/h: {feed_width_over_h:.4f}")
print(f"Feed-line effective permittivity eps_eff_feed: {eps_eff_feed:.4f}")
print(f"Feed-line width Wf: {feed_width_m * 1e3:.3f} mm")
print(f"Feed-line Z0 verification: {feed_z0_check:.3f} ohm")
print(f"Assumed patch edge resistance: {EDGE_RESISTANCE_ESTIMATE:.1f} ohm")
print(f"Initial inset depth y0: {inset_depth_m * 1e3:.3f} mm")
print(f"Initial inset gap gi: {INSET_GAP_M * 1e3:.3f} mm")
print("-" * 72)
print("Array starting value")
print(f"Initial array spacing d=lambda0/2: {element_spacing_m * 1e3:.3f} mm")
