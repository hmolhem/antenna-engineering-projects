"""Analytical verification utilities for the wearable half-wave dipole study."""

from math import sqrt

C0 = 3.0e8
F0_HZ = 1.120e9
INITIAL_DIAMETER_MM = 1.81
INITIAL_LENGTH_MM = 133.93
FREE_SPACE_INITIAL_MIN_GHZ = 1.0200
FREE_SPACE_TUNED_LENGTH_MM = 122.0
BODY_5MM_MIN_GHZ = 0.9792
BODY_RETUNED_LENGTH_MM = 106.6
SEPARATIONS_MM = (10.0, 5.0, 0.1)


def db_to_percent(value_db: float) -> float:
    return 100.0 * 10.0 ** (value_db / 10.0)


def main() -> None:
    wavelength_mm = C0 / F0_HZ * 1000.0
    half_wave_mm = wavelength_mm / 2.0
    radius_mm = INITIAL_DIAMETER_MM / 2.0
    free_space_estimate_mm = INITIAL_LENGTH_MM * FREE_SPACE_INITIAL_MIN_GHZ / (F0_HZ / 1e9)
    body_estimate_mm = FREE_SPACE_TUNED_LENGTH_MM * BODY_5MM_MIN_GHZ / (F0_HZ / 1e9)
    reactive_near_field_mm = 0.62 * sqrt(FREE_SPACE_TUNED_LENGTH_MM**3 / wavelength_mm)
    far_field_mm = 2.0 * FREE_SPACE_TUNED_LENGTH_MM**2 / wavelength_mm

    print("Wearable Half-Wave Dipole Verification")
    print("======================================")
    print(f"Design frequency                 : {F0_HZ/1e9:.3f} GHz")
    print(f"Free-space wavelength            : {wavelength_mm:.2f} mm")
    print(f"Theoretical half-wave length     : {half_wave_mm:.2f} mm")
    print(f"Specified wire radius            : {radius_mm:.3f} mm")
    print(f"Free-space scaling estimate      : {free_space_estimate_mm:.2f} mm")
    print(f"Selected free-space tuned length : {FREE_SPACE_TUNED_LENGTH_MM:.1f} mm")
    print(f"5 mm body scaling estimate       : {body_estimate_mm:.2f} mm")
    print(f"Selected body-retuned length     : {BODY_RETUNED_LENGTH_MM:.1f} mm")
    print()
    print("Normalized separations")
    for value in SEPARATIONS_MM:
        print(f"  {value:4.1f} mm = {value/wavelength_mm:.6f} lambda0")
    print(f"Reactive near-field estimate     : {reactive_near_field_mm:.2f} mm")
    print(f"2D^2/lambda far-field estimate   : {far_field_mm:.2f} mm")
    print()
    print("Efficiency conversion from CST dB values")
    cases = {
        "10 mm radiation": -3.410,
        "10 mm total": -4.190,
        "5 mm radiation": -3.837,
        "5 mm total": -5.126,
        "0.1 mm radiation": -10.52,
        "0.1 mm total": -11.50,
    }
    for name, value_db in cases.items():
        print(f"  {name:18s}: {value_db:7.3f} dB = {db_to_percent(value_db):6.2f} %")


if __name__ == "__main__":
    main()
