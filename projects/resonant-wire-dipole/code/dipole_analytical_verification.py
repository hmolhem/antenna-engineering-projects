#!/usr/bin/env python3
"""Independent analytical verification for the resonant wire dipole portfolio."""
from __future__ import annotations

from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt

C0 = 3.0e8
DESIGN_FREQUENCY_HZ = 1.0e9
FINAL_LENGTH_MM = 135.6
CST_RESONANCE_GHZ = 0.99648
CST_S11_DB = -47.01186
CST_DIRECTIVITY_DBI = 2.149

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures" / "analytical"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def trapz(y: np.ndarray, x: np.ndarray) -> float:
    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(y, x))
    return float(np.trapz(y, x))


def normalized_pattern(theta: np.ndarray) -> np.ndarray:
    sin_theta = np.sin(theta)
    numerator = np.cos(0.5 * np.pi * np.cos(theta))
    field = np.zeros_like(theta)
    mask = np.abs(sin_theta) > 1.0e-12
    field[mask] = np.abs(numerator[mask] / sin_theta[mask])
    return field / np.max(field)


def half_power_angles(theta: np.ndarray, field: np.ndarray) -> tuple[float, float, float]:
    power = field**2
    peak = int(np.argmax(power))
    left_i = np.where(power[:peak] <= 0.5)[0][-1]
    right_i = np.where(power[peak:] <= 0.5)[0][0] + peak
    left = np.interp(0.5, [power[left_i], power[left_i + 1]], [theta[left_i], theta[left_i + 1]])
    right = np.interp(0.5, [power[right_i], power[right_i - 1]], [theta[right_i], theta[right_i - 1]])
    return math.degrees(left), math.degrees(right), math.degrees(right - left)


def directivity(theta: np.ndarray, field: np.ndarray) -> tuple[float, float]:
    omega_a = 2.0 * np.pi * trapz(field**2 * np.sin(theta), theta)
    d_linear = 4.0 * np.pi / omega_a
    return d_linear, 10.0 * math.log10(d_linear)


def save_plots(theta: np.ndarray, field: np.ndarray, left: float, right: float, hpbw: float) -> None:
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="polar")
    ax.plot(theta, field)
    ax.plot(2.0 * np.pi - theta, field)
    ax.set_title("Analytical Thin Half-Wave Dipole Pattern")
    ax.set_rmax(1.0)
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "analytical_half_wave_dipole_polar.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    field_db = 20.0 * np.log10(np.maximum(field, 1.0e-5))
    fig = plt.figure(figsize=(7.5, 4.8))
    plt.plot(np.degrees(theta), field_db)
    plt.axhline(-3.0, linestyle="--", linewidth=1.0)
    plt.axvline(left, linestyle=":", linewidth=1.0)
    plt.axvline(right, linestyle=":", linewidth=1.0)
    plt.text(90.0, -6.0, f"HPBW = {hpbw:.2f} deg", ha="center")
    plt.xlim(0, 180)
    plt.ylim(-40, 1)
    plt.xlabel("theta (degrees)")
    plt.ylabel("Normalized field magnitude (dB)")
    plt.title("Analytical Thin Half-Wave Dipole Pattern")
    plt.grid(True)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "analytical_half_wave_dipole_pattern_db.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    wavelength_m = C0 / DESIGN_FREQUENCY_HZ
    theta = np.linspace(0.0, np.pi, 20001)
    field = normalized_pattern(theta)
    left, right, hpbw = half_power_angles(theta, field)
    d_linear, d_dbi = directivity(theta, field)
    error_mhz = abs(1.0 - CST_RESONANCE_GHZ) * 1000.0
    error_pct = abs(1.0 - CST_RESONANCE_GHZ) * 100.0
    save_plots(theta, field, left, right, hpbw)

    print("Resonant Wire Dipole Analytical Verification")
    print(f"Design frequency: {DESIGN_FREQUENCY_HZ/1e9:.3f} GHz")
    print(f"Wavelength: {wavelength_m*1000:.3f} mm")
    print(f"First-order half-wave length: {wavelength_m*500:.3f} mm")
    print(f"Final CST length: {FINAL_LENGTH_MM:.1f} mm")
    print(f"Analytical half-power angles: {left:.2f} deg, {right:.2f} deg")
    print(f"Analytical HPBW: {hpbw:.2f} deg")
    print(f"Analytical directivity: {d_linear:.4f} = {d_dbi:.2f} dBi")
    print(f"Final CST resonance: {CST_RESONANCE_GHZ:.5f} GHz")
    print(f"Final CST S11: {CST_S11_DB:.5f} dB")
    print(f"Equivalent return loss: {-CST_S11_DB:.5f} dB")
    print(f"Final CST directivity: {CST_DIRECTIVITY_DBI:.3f} dBi")
    print(f"Frequency error: {error_mhz:.2f} MHz = {error_pct:.3f} percent")


if __name__ == "__main__":
    main()
