import matplotlib.pyplot as plt;
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np;
from collections import namedtuple
from typing import List, Union

from util.structs import DataCluster, Measurement, Point;
from util.graph_fit import FitResult;

# Define a named tuple for the return value
PlotResult = namedtuple('PlotResult', ['line', 'plot', "fill"])

def _extract_value_error(lst: List[Union[float, int, Measurement]]):
    values = []
    errors = []
    
    for item in lst:
        if isinstance(item, np.str_):
            item = float(item) if '.' in item else int(item)

        if isinstance(item, (float, int)):
            values.append(item)
            errors.append(0)
        elif isinstance(item, Measurement):
            values.append(item.value)
            errors.append(item.error)
        else:
            raise ValueError(f"List contains an unsupported type: {item} is type {type(item)}")
    
    return values, errors

def create_plot(**kwargs) -> tuple[Figure, Axes | np.ndarray]:
    return plt.subplots(**kwargs);

def plot_func(fit_func, plot=None, change_viewport=True, with_error = True, **kwargs):
    """
    Plot data with error bars and a fitted model.

    Parameters:
    fit_func (callable): The fitted model function with specific parameters.
    plot (tuple): Tuple containing the figure and axis objects for plotting.
    """
    min_func = None
    max_func = None
    if isinstance(fit_func, FitResult):
        min_func = fit_func.min_func;
        max_func = fit_func.max_func;
        fit_func = fit_func.value_func;
    if not callable(fit_func):
        raise ValueError("`fit_func` must be a callable function.")
    if plot is not None and (not isinstance(plot, tuple) or len(plot) != 2):
        raise ValueError("`plot` must be a tuple containing (fig, ax).")
     
    if plot is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = plot

    # get the plot dimensions
    xmin, xmax = ax.get_xlim();
    ymin, ymax = ax.get_ylim();

    # Generate a smooth line for the model
    x_smooth = np.linspace(xmin, xmax, 10000)
    y_smooth = fit_func(x_smooth)
    line = ax.plot(x_smooth, y_smooth, **kwargs)

    # if min, max parameter are provided color the 1-sigma area
    fill = None
    if with_error and min_func is not None and max_func is not None:
        y_min = min_func(x_smooth)
        y_max = max_func(x_smooth)
        fill = ax.fill_between(x_smooth, y_min, y_max, color=line[0].get_color(), alpha=0.3)

    # keep the same viewport after plotting
    if not change_viewport:
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

    return PlotResult(line=line, plot=(fig, ax), fill=fill);

"""
    p: plt.subplot instance
"""
def scatter(x: List[Measurement], y: List[Measurement], with_error = True, plot=None, **kwargs):
    if len(x) != len(y):
        print(x)
        print(y)
        raise ValueError(f"Different sizes!\nlen(x): {len(x)}\nlen(y): {len(y)}")

    if plot is None:
        plot = plt.subplots()
    _, ax = plot;

    x_values, x_err = _extract_value_error(x)
    y_values, y_err = _extract_value_error(y)

    linestyle = kwargs.get("linestyle", "none");
    kwargs.pop("linestyle", "none");
    
    scatter = ax.scatter(x_values, y_values, **kwargs)
    face_colors = scatter.get_facecolor()

    errorbar = None
    if with_error:
        errorbar = ax.errorbar(x_values, y_values, xerr=x_err, yerr=y_err, linestyle=linestyle, color=face_colors)

    return scatter, errorbar, plot

def scatter_data(data: DataCluster, x_index, y_index, with_error = True, plot=None, **kwargs):
    x = data.column(x_index);
    y = data.column(y_index);
    return scatter(x, y, with_error, plot=plot, **kwargs);


def plot(x: List[float], y: List[float], p=None, color=None, label=None):
    if p is None:
        p = plt.subplotb();
    _, ax = p;

    ax.plot(x, y, label=label, color=color);

    return p;

def lineplot(m, b, start, end, p=None, color=None, label=None):
    x = np.linspace(start, end, 10000);
    y = m * x + b;
    return plot(x, y, p=p, color=color, label=label)

def lineplot_around_sp(m: float, sp: Point, start, end, p=None, color=None, label=None):
    x = np.linspace(start, end, 10000);
    b = calc_b_lineplot(m, sp);
    y = m * x + b;
    return plot(x, y, p=p, color=color, label=label)

def calc_b_lineplot(m, sp):
    return sp.y - m*sp.x