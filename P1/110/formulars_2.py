import numpy as np;

from util.structs import Measurement;

def calc_p_0(p_L: Measurement, mass: Measurement, radius: Measurement):
  value = p_L.value + mass.value * 9.81 / (np.pi * radius.value**2);

  after_p_L = 1 * p_L.error;
  after_mass = 9.81 / (np.pi * radius.value**2) * mass.error;
  after_radius = -2 * mass.value * 9.81 / (np.pi * radius.value**3) * radius.error;

  error = np.sqrt(after_p_L**2 + after_mass**2 + after_radius**2);

  return Measurement(value, error)

def calc_kappa(period_time: Measurement, mass: Measurement, radius: Measurement, Volume_0: Measurement, pressure_0: Measurement):
  value = 4 * mass.value * Volume_0.value / (period_time.value**2 * radius.value**4 * pressure_0.value)
  
  after_period = -2 * 4 * mass.value * Volume_0.value / (period_time.value**3 * radius.value**4 * pressure_0.value) * period_time.error;
  after_mass = 4 * Volume_0.value / (period_time.value**3 * radius.value**4 * pressure_0.value) * period_time.error * mass.error;
  after_V_0 = 4 * mass.value / (period_time.value**2 * radius.value**4 * pressure_0.value) * Volume_0.error;
  after_radius = -4 * 4 * mass.value * Volume_0.value / (period_time.value**2 * radius.value**5 * pressure_0.value) * radius.error;
  after_pressure = -1 * 4 * mass.value * Volume_0.value / (period_time.value**2 * radius.value**4 * pressure_0.value**2) * pressure_0.error; 

  error = np.sqrt(after_period**2 + after_mass**2 + after_V_0**2 + after_radius**2 + after_pressure**2);

  return Measurement(value, error);