"""Beam-steering phase-shift calculations for a two-element patch array."""

from math import sin, asin, radians, degrees, pi

C0 = 299_792_458.0
f0_hz = 2.501e9
lambda0_m = C0 / f0_hz
# The CST-tuned array used arrayD = lambda0/2 from the analytical setup.
d_m = lambda0_m / 2.0
k0 = 2.0 * pi / lambda0_m

print("Two-Element Array Beam-Steering Phase Shifts")
print("=" * 72)
print(f"f0 = {f0_hz/1e9:.6f} GHz")
print(f"lambda0 = {lambda0_m*1e3:.3f} mm")
print(f"d = lambda0/2 = {d_m*1e3:.3f} mm")
print("-" * 72)
print("Desired steering angle -> required phase shift")
print("theta0_deg, Delta_phi_deg")
for theta_deg in [0, 10, 15, 20, 30, 45]:
    delta_phi_rad = -k0 * d_m * sin(radians(theta_deg))
    print(f"{theta_deg:10.1f}, {degrees(delta_phi_rad):14.3f}")

print("-" * 72)
print("Applied CST phase shift -> ideal array-factor beam angle")
print("Delta_phi_deg, theta0_deg")
for delta_phi_deg in [0, -90, +90]:
    delta_phi_rad = radians(delta_phi_deg)
    sin_theta = -delta_phi_rad / (k0 * d_m)
    theta_deg = degrees(asin(sin_theta))
    print(f"{delta_phi_deg:13.1f}, {theta_deg:10.3f}")
