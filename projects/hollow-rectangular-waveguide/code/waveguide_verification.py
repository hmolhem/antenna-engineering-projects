"""Verify the analytical modal quantities for the public waveguide project."""

from __future__ import annotations

import math
from dataclasses import dataclass

C0 = 299_792_458.0
ETA0 = 376.730313668
F0 = 10.0e9

A = 20.0e-3
B = 20.0e-3
LENGTH = 90.0e-3

CST_PORT1_GHZ = (7.490707, 7.491242, 10.5935)
CST_PORT2_GHZ = (7.49031, 7.49064, 10.5931)


@dataclass(frozen=True)
class Mode:
    name: str
    m: int
    n: int


MODES = (
    Mode("TE10", 1, 0),
    Mode("TE01", 0, 1),
    Mode("(1,1) family", 1, 1),
    Mode("TE20", 2, 0),
    Mode("TE02", 0, 2),
)


def cutoff_frequency(mode: Mode) -> float:
    return (C0 / 2.0) * math.sqrt((mode.m / A) ** 2 + (mode.n / B) ** 2)


def guide_wavelength(frequency: float, cutoff: float) -> float | None:
    if frequency <= cutoff:
        return None
    lambda0 = C0 / frequency
    return lambda0 / math.sqrt(1.0 - (cutoff / frequency) ** 2)


def te_impedance(frequency: float, cutoff: float) -> float | None:
    if frequency <= cutoff:
        return None
    return ETA0 / math.sqrt(1.0 - (cutoff / frequency) ** 2)


def relative_error_percent(numerical: float, analytical: float) -> float:
    return 100.0 * (numerical - analytical) / analytical


def main() -> None:
    print("Hollow Square Waveguide Analytical Verification")
    print("=" * 88)
    print(f"Geometry: a = {A * 1e3:.3f} mm, b = {B * 1e3:.3f} mm, "
          f"length = {LENGTH * 1e3:.3f} mm")
    print(f"Observation frequency: {F0 / 1e9:.3f} GHz")
    print()

    print("Low-order analytical modes")
    print("-" * 88)
    print(f"{'Mode':<18}{'fc (GHz)':>12}{'Status at 10 GHz':>24}"
          f"{'lambda_g (mm)':>18}{'Z_TE (ohm)':>16}")
    print("-" * 88)

    for mode in MODES:
        fc = cutoff_frequency(mode)
        lambda_g = guide_wavelength(F0, fc)
        z_te = te_impedance(F0, fc)
        status = "propagating" if F0 > fc else "evanescent"
        lambda_text = f"{lambda_g * 1e3:.3f}" if lambda_g else "N/A"
        impedance_text = f"{z_te:.3f}" if z_te else "N/A"
        print(
            f"{mode.name:<18}{fc / 1e9:>12.6f}{status:>24}"
            f"{lambda_text:>18}{impedance_text:>16}"
        )

    fc10 = cutoff_frequency(MODES[0])
    lambda_g10 = guide_wavelength(F0, fc10)
    z_te10 = te_impedance(F0, fc10)
    assert lambda_g10 is not None
    assert z_te10 is not None

    print()
    print("Lowest-order detailed quantities")
    print("-" * 88)
    print(f"Free-space wavelength: {C0 / F0 * 1e3:.6f} mm")
    print(f"Guide wavelength: {lambda_g10 * 1e3:.6f} mm")
    print(f"TE wave impedance: {z_te10:.6f} ohm")
    print(f"Electrical length: {LENGTH / lambda_g10:.6f} guide wavelengths")

    analytical_ghz = (
        cutoff_frequency(MODES[0]) / 1e9,
        cutoff_frequency(MODES[1]) / 1e9,
        cutoff_frequency(MODES[2]) / 1e9,
    )

    print()
    print("CST cutoff comparison")
    print("-" * 88)
    print(f"{'Mode':<10}{'Theory':>14}{'Port 1':>14}{'Error P1':>14}"
          f"{'Port 2':>14}{'Error P2':>14}")
    print("-" * 88)

    for index, theory in enumerate(analytical_ghz, start=1):
        p1 = CST_PORT1_GHZ[index - 1]
        p2 = CST_PORT2_GHZ[index - 1]
        print(
            f"{index:<10}{theory:>14.6f}{p1:>14.6f}"
            f"{relative_error_percent(p1, theory):>13.4f}%"
            f"{p2:>14.6f}{relative_error_percent(p2, theory):>13.4f}%"
        )


if __name__ == "__main__":
    main()
