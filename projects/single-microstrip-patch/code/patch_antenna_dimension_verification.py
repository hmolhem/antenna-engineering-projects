"""Analytical verification for the 915 MHz inset-fed microstrip patch portfolio report."""

import math

C0 = 299_792_458.0
F0_HZ = 915e6
EPS_R = 2.20
H_M = 1.575e-3
TARGET_Z_OHM = 50.0
EDGE_RESISTANCE_OHM = 250.0

FINAL_LENGTH_MM = 108.2
FINAL_WIDTH_MM = 129.5
DOCUMENTED_FEED_WIDTH_MM = 4.89
NOTCH_GAP_MM = 1.0
FINAL_RESONANCE_GHZ = 0.9186
FINAL_S11_DB = -22.14379

lambda0_m = C0 / F0_HZ
width_m = C0 / (2.0 * F0_HZ) * math.sqrt(2.0 / (EPS_R + 1.0))
eps_eff = (
    (EPS_R + 1.0) / 2.0
    + (EPS_R - 1.0) / 2.0 * (1.0 + 12.0 * H_M / width_m) ** -0.5
)
delta_l_m = (
    0.412
    * H_M
    * ((eps_eff + 0.3) * (width_m / H_M + 0.264))
    / ((eps_eff - 0.258) * (width_m / H_M + 0.8))
)
effective_length_m = C0 / (2.0 * F0_HZ * math.sqrt(eps_eff))
physical_length_m = effective_length_m - 2.0 * delta_l_m

inset_depth_mm = (
    FINAL_LENGTH_MM
    / math.pi
    * math.acos(math.sqrt(TARGET_Z_OHM / EDGE_RESISTANCE_OHM))
)
notch_width_mm = DOCUMENTED_FEED_WIDTH_MM + 2.0 * NOTCH_GAP_MM
frequency_error_mhz = FINAL_RESONANCE_GHZ * 1000.0 - F0_HZ / 1e6
frequency_error_percent = frequency_error_mhz / (F0_HZ / 1e6) * 100.0
return_loss_db = -FINAL_S11_DB
gamma_mag = 10.0 ** (FINAL_S11_DB / 20.0)
vswr = (1.0 + gamma_mag) / (1.0 - gamma_mag)
length_adjustment_mm = FINAL_LENGTH_MM - physical_length_m * 1e3
length_adjustment_percent = length_adjustment_mm / (physical_length_m * 1e3) * 100.0

print("Inset-Fed Microstrip Patch Analytical Verification")
print("=" * 72)
print(f"Design frequency: {F0_HZ / 1e9:.3f} GHz")
print(f"Relative permittivity: {EPS_R:.2f}")
print(f"Substrate thickness: {H_M * 1e3:.3f} mm")
print()
print("Analytical starting dimensions")
print(f"Free-space wavelength: {lambda0_m * 1e3:.2f} mm")
print(f"Patch width: {width_m * 1e3:.2f} mm")
print(f"Effective dielectric constant: {eps_eff:.4f}")
print(f"Fringing extension: {delta_l_m * 1e3:.3f} mm")
print(f"Effective patch length: {effective_length_m * 1e3:.2f} mm")
print(f"Physical patch length: {physical_length_m * 1e3:.2f} mm")
print()
print("Final documented geometry")
print(f"Patch width: {FINAL_WIDTH_MM:.1f} mm")
print(f"Patch length: {FINAL_LENGTH_MM:.1f} mm")
print(f"Documented feed width: {DOCUMENTED_FEED_WIDTH_MM:.2f} mm")
print(f"Inset-notch width: {notch_width_mm:.2f} mm")
print(f"Analytical inset-depth estimate: {inset_depth_mm:.2f} mm")
print(f"Length adjustment from analytical value: {length_adjustment_mm:.2f} mm ({length_adjustment_percent:.2f}%)")
print()
print("Final CST marker and derived quantities")
print(f"Matching-minimum frequency: {FINAL_RESONANCE_GHZ:.4f} GHz")
print(f"Minimum S11: {FINAL_S11_DB:.5f} dB")
print(f"Positive return loss: {return_loss_db:.5f} dB")
print(f"Reflection magnitude: {gamma_mag:.4f}")
print(f"VSWR: {vswr:.3f}")
print(f"Frequency error: {frequency_error_mhz:.1f} MHz ({frequency_error_percent:.3f}%)")
