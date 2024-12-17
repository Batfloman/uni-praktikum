import numpy as np;

from util.structs import Measurement;

def calc_wheel_volume(radius: Measurement, thickness: Measurement):
  value = np.pi * radius.value**2 * thickness.value;
  
  after_radius = 2* np.pi * radius.value * thickness.value * radius.error;
  after_thickness = np.pi * radius.value**2 * thickness.error;
  error = np.sqrt(after_radius**2 + after_thickness**2);

  return Measurement(value, error);

def calc_wheel_mass(volume: Measurement, t: Measurement):
  value = volume.value * t.value;

  after_volume = t.value * volume.error;
  after_t = volume.value * t.error;
  error = np.sqrt(after_volume**2 + after_t**2);

  return Measurement(value, error);

def calc_wheel_moment_of_inertia(mass: Measurement, radius: Measurement):
  value = 1/2 * mass.value * radius.value**2;

  after_mass = 1/2 * radius.value**2 * mass.error;
  after_radius = mass.value * radius.value * radius.error;
  error = np.sqrt(after_mass**2 + after_radius**2);

  return Measurement(value, error);

# def calc_T_1(T_n: Measurement, n: Measurement):
#   value = T_n.value / n.value;

#   after_T_n = (1/n.value) * T_n.error;
#   after_n = -T_n.value/n.value**2 * n.error;
#   error = np.sqrt(after_T_n**2 + after_n**2)

#   return Measurement(value, error);

# def calc_omega(T_1: Measurement):
#   value = 2*np.pi / T_1.value;

#   after_T_1 = -2*np.pi / T_1.value**2 * T_1.error;
#   error = np.sqrt(after_T_1**2)

#   return Measurement(value, error)