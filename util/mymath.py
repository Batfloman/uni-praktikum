import numpy as np;
from typing import List

def round(x, num_decimals = 0):
    # potenz = 10**num_decimals;
    return np.round(x, num_decimals)

def ceil(x, num_decimals = 0):
    potenz = 10**num_decimals;
    return np.ceil(x * potenz) / potenz;

def floor(x, num_decimals = 0):
    potenz = 10**num_decimals;
    return np.floor(x * potenz) / potenz;

def get_exponent_significant(value):
    """
    Returns the first significant digit exponent 

    examples:
        10 would give 1
        1.1 would give 0
        0.1 would give -1
    """
    value_str = f"{value:.2e}"
    if 'e' not in value_str: 
        return 0
    return int(value_str.split('e')[1])

def get_exponent_closest_3n(value):
    exponent = get_exponent_significant(value);
    print(exponent)
    # Round exponent to multiples of 3
    exponent_rounded = floor(exponent / 3) * 3
    return int(exponent_rounded)

def round_significant(value, additional_digits = 0):
    return round(value, -get_exponent_significant(value) + additional_digits)

def ceil_significant(value, additional_digits = 0):
    return ceil(value, -get_exponent_significant(value) + additional_digits)

def error_weighted_mean(measurements):
    from util.structs import Measurement
    
    values = np.array([m.value for m in measurements])
    errors = np.array([m.error for m in measurements])

    weights = 1 / errors**2;
    weight_sum = np.sum(weights);

    value = np.sum(values * weights) / weight_sum
    error = 1 / weight_sum**0.5
    return Measurement(value, error);

def get_value_from_skt(skt, skt_max, max_value):
    return max_value * (skt/skt_max);
