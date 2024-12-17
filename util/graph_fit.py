import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from warnings import warn
from collections import namedtuple

from util.structs import DataCluster, Dataset, Measurement

FitResult = namedtuple('FitResult', ['func', 'params', 'value_func', 'min_func', 'max_func'])

def perform_generic_fit(x, y, model, initial_guess, yerr = None, param_names=None):
    """
    Perform a generic fit to the data with uncertainties using a specified model.

    Parameters:
    x (array): Independent variable data.
    y (array): Dependent variable data.
    yerr (array): Uncertainties in the dependent variable data.
    model (callable): The model function to fit.
    initial_guess (array): Initial guess for the parameters.
    param_names (list, optional): List of parameter names. Defaults to None.

    Returns:
    fit_func (callable): The fitted model function with specific parameters.
    params (Dataset): Dataset containing the fit parameters and their uncertainties.
    """
    if yerr is not None:
        # Check for zero or negative errors and raise a warning or error
        if np.any(yerr <= 0):
            raise ValueError("Error values in 'yerr' must be positive and non-zero for meaningful fitting.")
        sigma = yerr
        absolute_sigma = True
    else:
        # If yerr is not provided, curve_fit uses equal weights
        sigma = None
        absolute_sigma = False

    # Perform curve fitting
    popt, pcov = curve_fit(model, x, y, sigma=sigma, absolute_sigma=absolute_sigma, p0=initial_guess, bounds=(-np.inf, np.inf))
    perr = np.sqrt(np.diag(pcov))

    # Create a function that represents the fitted model
    # fit_func = lambda x_val: model(x_val, *popt)
    # Create min and max parameter sets
    # popt_min = popt - perr
    # popt_max = popt + perr
    # # Create functions for min and max models
    # min_func = lambda x_val: model(x_val, *popt_min)
    # max_func = lambda x_val: model(x_val, *popt_max)

    # If no names or not enough names are given, default to "param_i"
    if param_names is None:
        param_names = [f"param_{i}" for i in range(len(popt))]
    elif len(param_names) < len(popt):
        param_names += [f"param_{i}" for i in range(len(param_names), len(popt))]

    # Create a Dataset object to hold the fit parameters and their uncertainties
    params = Dataset({
        name: Measurement(popt[i], perr[i]) for i, name in enumerate(param_names)
    })

    def value_func(x_value):
        return model(x_value, *popt)

    def fit_func(x_val):
        return model(x_val, *[params[name] for name in param_names])

    # # Define min and max functions based on the `fit_func` uncertainty
    def min_func(x_val):
        results = fit_func(x_val);
        if isinstance(results, Measurement):
            return results.value - results.error
        return [res.value - res.error for res in results]

    def max_func(x_val):
        results = fit_func(x_val);
        if isinstance(results, Measurement):
            return results.value + results.error
        return [res.value + res.error for res in results]
    
    # return FitResult(func=fit_func, params=params, value_func=value_func, min_func=min_func, max_func=max_func)
    return FitResult(func=fit_func, params=params, value_func=value_func, min_func=min_func, max_func=max_func)

class Linear:
    def model(x, a, b):
        """Linear model: y = a * x + b"""
        return a * x + b

    @staticmethod
    def perform_fit(x, y, yerr = None):
        return perform_generic_fit(x, y, Linear.model, None, yerr=yerr, param_names=["m", "n"])
    
    @staticmethod
    def on_data(data: DataCluster, x_index, y_index):
        x_values = data.values(x_index)
        y_values = data.values(y_index)
        y_errors = data.errors(y_index)

        return Linear.perform_fit(x_values, y_values, y_errors)
        
class InverseSquare:
    @staticmethod
    def model(x, a, x0, b, c):
        """Modified inverse-square model: y = a / ((x - x0)^2 + b) + c"""
        return a / ((x - x0)**2 + b) + c

    @staticmethod
    def perform_fit(x, y, yerr = None):
        return perform_generic_fit(x, y, InverseSquare.model, [max(y), np.mean(x), 1, min(y)], yerr=yerr, param_names=["a", "x0", "b", "c"])
    
    @staticmethod
    def on_data(data: DataCluster, x_index, y_index):
        x_values = data.values(x_index)
        y_values = data.values(y_index)
        y_errors = data.errors(y_index)

        return InverseSquare.perform_fit(x_values, y_values, y_errors)
    
class ResonanceCurve:
    @staticmethod
    def model(x, a, x0, beta):
        """Model for the resonance curve. omega is here x"""
        denom = ((x0**2 - x**2)**2 + (2 * beta * x)**2)**0.5
        return a / denom 

    @staticmethod
    def perform_fit(x, y, yerr=None):
        # Provide an initial guess for parameters: [a, x0, zeta, c]
        initial_guess = [max(y), x[np.argmax(y)], 0.1]
        return perform_generic_fit(x, y, ResonanceCurve.model, initial_guess, yerr=yerr, param_names=["a", "x0", "beta"])

    @staticmethod
    def on_data(data: DataCluster, x_index, y_index):
        x_values = data.values(x_index)
        y_values = data.values(y_index)
        y_errors = data.errors(y_index)
        return ResonanceCurve.perform_fit(x_values, y_values, y_errors)