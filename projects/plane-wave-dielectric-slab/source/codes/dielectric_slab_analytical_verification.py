"""Analytical verification for normal incidence on a lossless dielectric slab.

The model is air -> dielectric slab -> air at 1 GHz.  The ideal analytical
slab thickness is one exact free-space wavelength.  The script regenerates
reflection magnitude and wrapped phase over eps_r = 1...10 in 0.25 steps,
prints the predicted matching points, and writes analytical figures and CSV.
"""
from __future__ import annotations

from pathlib import Path
import csv
import math

import matplotlib.pyplot as plt
import numpy as np

C0 = 299_792_458.0
ETA0 = 376.730313668
F0_HZ = 1.0e9
LAMBDA0_M = C0 / F0_HZ
D_M = LAMBDA0_M
EPS_VALUES = np.arange(1.0, 10.0 + 0.25, 0.25)


def slab_reflection(eps_r: float) -> complex:
    """Return the ideal input reflection coefficient of an air-slab-air section."""
    if eps_r <= 0:
        raise ValueError("eps_r must be positive")
    eta_d = ETA0 / math.sqrt(eps_r)
    beta_d = 2.0 * math.pi * math.sqrt(eps_r) / LAMBDA0_M
    tangent = math.tan(beta_d * D_M)
    z_in = eta_d * (ETA0 + 1j * eta_d * tangent) / (
        eta_d + 1j * ETA0 * tangent
    )
    return (z_in - ETA0) / (z_in + ETA0)


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "figures" / "analytical"
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = Path(__file__).resolve().parent.parent / "results" / "analytical-sweep.csv"

    gammas = np.array([slab_reflection(float(eps)) for eps in EPS_VALUES])
    magnitudes = np.abs(gammas)
    phases_deg = np.angle(gammas, deg=True)

    predicted = [(m, (m / 2.0) ** 2) for m in range(2, 7)]

    print("Normal-incidence dielectric-slab analytical verification")
    print(f"f0 = {F0_HZ / 1e9:.6f} GHz")
    print(f"lambda0 = {LAMBDA0_M * 1e3:.6f} mm")
    print(f"ideal slab thickness d = lambda0 = {D_M * 1e3:.6f} mm")
    print(f"eta0 = {ETA0:.6f} ohm")
    print("sweep: eps_r = 1.00 to 10.00 in 0.25 steps")
    print()
    print("Predicted half-wave matching points:")
    for m, eps_r in predicted:
        gamma = slab_reflection(eps_r)
        print(
            f"  m={m}: eps_r={eps_r:.2f}, |Gamma|={abs(gamma):.6e}, "
            f"phase={math.degrees(math.atan2(gamma.imag, gamma.real)):.3f} deg"
        )

    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["eps_r", "gamma_real", "gamma_imag", "gamma_mag", "phase_deg"])
        for eps_r, gamma, mag, phase in zip(EPS_VALUES, gammas, magnitudes, phases_deg):
            writer.writerow(
                [
                    f"{eps_r:.2f}",
                    f"{gamma.real:.12e}",
                    f"{gamma.imag:.12e}",
                    f"{mag:.12e}",
                    f"{phase:.9f}",
                ]
            )

    plt.figure(figsize=(8.2, 4.8))
    plt.plot(EPS_VALUES, magnitudes, linewidth=1.8)
    for _, eps_r in predicted:
        plt.axvline(eps_r, linestyle="--", linewidth=0.8)
    plt.xlabel(r"Relative permittivity, $\varepsilon_r$")
    plt.ylabel(r"$|\Gamma_{\mathrm{ana}}|$")
    plt.title(r"Analytical dielectric-slab reflection coefficient, $d=\lambda_0$")
    plt.grid(True, alpha=0.35)
    plt.tight_layout()
    plt.savefig(out_dir / "analytical_gamma_vs_eps.png", dpi=200)
    plt.close()

    plt.figure(figsize=(8.2, 4.8))
    plt.plot(EPS_VALUES, phases_deg, linewidth=1.8)
    for _, eps_r in predicted:
        plt.axvline(eps_r, linestyle="--", linewidth=0.8)
    plt.xlabel(r"Relative permittivity, $\varepsilon_r$")
    plt.ylabel(r"Wrapped phase of $\Gamma_{\mathrm{ana}}$ (deg)")
    plt.title("Analytical wrapped phase response")
    plt.grid(True, alpha=0.35)
    plt.tight_layout()
    plt.savefig(out_dir / "analytical_phase_vs_eps.png", dpi=200)
    plt.close()

    print()
    print(f"Wrote analytical sweep: {csv_path}")
    print(f"Wrote figures: {out_dir}")


if __name__ == "__main__":
    main()
