import numpy as np;

from util.structs import Measurement

def calc_E(length: Measurement, height: Measurement, width: Measurement, slope_m: Measurement) -> Measurement:
    E_value = length.value**3 / (height.value**3 * width.value * slope_m.value * 4)

    E_after_l = 3/4 * length.value**2 * length.error / (height.value**3 * width.value * slope_m.value)
    E_after_h = -3/4 * length.value**3 * height.error / (height.value**4 * width.value * slope_m.value)
    E_after_w = -1/4 * length.value**3 * width.error / (height.value**3 * width.value**2 * slope_m.value)
    E_after_m = -1/4 * length.value**3 * slope_m.error / (height.value**3 * width.value * slope_m.value**2)
    E_error = np.sqrt(E_after_l**2 + E_after_h**2 + E_after_w**2 + E_after_m**2)

    return Measurement(E_value, E_error);

def calc_D(slope_m: Measurement, mass_weight: Measurement) -> Measurement:
    D_value = 1/slope_m.value * 8 *  np.pi**2 * mass_weight.value;

    D_after_slope = -1/slope_m.value**2 * 8 * np.pi**2 * mass_weight.value * slope_m.error;
    D_after_mass = -1/slope_m.value * 8 * np.pi**2 * mass_weight.error;
    D_error = np.sqrt(D_after_slope**2 + D_after_mass**2)

    return Measurement(D_value, D_error)