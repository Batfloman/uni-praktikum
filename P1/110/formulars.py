from util import graph
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from util import graph_fit
from dataset import Dataset

import numpy as np;

from util.structs import Measurement

def calc_C_Kal(masse_wasser, masse_messing):
    c_W = Measurement(4.185e3, 0)
    c_M = Measurement(0.377e3, 0)

    value = c_W.value * masse_wasser.value + c_M.value * masse_messing.value;

    C_Kal_after_m_W = c_W.value * masse_wasser.error
    C_Kal_after_m_M = c_M.value * masse_messing.error
    error = np.sqrt(C_Kal_after_m_W**2 + C_Kal_after_m_M**2)

    return Measurement(value, error);

def calc_C(C_Kal: Measurement, T_hot: Measurement, T_equal: Measurement, T_cold: Measurement):
    value = C_Kal.value * (T_equal.value - T_cold.value) / (T_hot.value - T_equal.value);

    after_C_Kal = (T_equal.value - T_cold.value) / (T_hot.value - T_equal.value) * C_Kal.error;
    after_T_hot = -C_Kal.value * (T_equal.value - T_cold.value) / (T_hot.value - T_equal.value)**2;
    after_T_equal = C_Kal.value * (T_hot.value - T_cold.value) / (T_hot.value - T_equal.value)**2;
    after_T_cold = -C_Kal.value  / (T_hot.value - T_equal.value);
    error = np.sqrt(after_C_Kal**2 + after_T_hot**2 + after_T_equal**2 + after_T_cold**2);

    return Measurement(value, error);

def calc_c_specific(C: Measurement, mass: Measurement):
    value = 1/mass.value * C.value;

    after_m = -1/mass.value**2 * C.value * mass.error;
    after_C = 1/mass.value * C.error;
    error = np.sqrt(after_m**2 + after_C**2);

    return Measurement(value, error);

def calc_c_molar(C: Measurement, amount_of_substance: Measurement):
    value = 1/amount_of_substance.value * C.value;

    after_m = -1/amount_of_substance.value**2 * C.value * amount_of_substance.error;
    after_C = 1/amount_of_substance.value * C.error;
    error = np.sqrt(after_m**2 + after_C**2);

    return Measurement(value, error);

def calc_n(total_mass: Measurement, molar_mass: Measurement):
    value = total_mass.value / molar_mass.value;

    after_m = total_mass.error / molar_mass.value;
    after_M = -total_mass.value / molar_mass.value**2 * molar_mass.error;
    error = np.sqrt(after_m**2 + after_M**2)

    return Measurement(value, error)


def evaluate(vorkurve, mitte, nachkurve):
    p = plt.subplots(figsize=(12, 10));
    fig, ax = p;
    ax.grid(alpha=.33)

    # Adjust x-axis ticks
    ax.xaxis.set_major_locator(plt.MaxNLocator(nbins=10))  # Adjust the number of major ticks
    ax.xaxis.set_minor_locator(AutoMinorLocator())         # Add minor ticks

    # Adjust y-axis ticks
    ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=10))  # Adjust the number of major ticks
    ax.yaxis.set_minor_locator(AutoMinorLocator())         # Add minor ticks

    # ---------------
    # scatter points    

    graph.scatter(vorkurve.t, vorkurve.T, yerr=vorkurve.T_err, p=p)
    graph.scatter(mitte.t, mitte.T, yerr=mitte.T_err, p=p)
    graph.scatter(nachkurve.t, nachkurve.T, yerr=nachkurve.T_err, p=p)

    # ---------------
    # graphs

    m, dm, _, _, sp = graph_fit.fit(vorkurve.t, vorkurve.T, yerr=vorkurve.T_err)
    graph.lineplot_around_sp(m, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    # graph.lineplot_around_sp(m+dm, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    # graph.lineplot_around_sp(m-dm, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    print(f"Vorkurve:\n\tm: {m:.2e}\n\tdm: {dm:.2e}")
    print(sp)

    m, dm, _, _, sp = graph_fit.fit(nachkurve.t, nachkurve.T, yerr=nachkurve.T_err)
    graph.lineplot_around_sp(m, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    # graph.lineplot_around_sp(m+dm, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    # graph.lineplot_around_sp(m-dm, sp, min(vorkurve.t), max(nachkurve.t), p=p)
    print(f"Nachkurve:\n\tm: {m:.2e}\n\tdm: {dm:.2e}")
    print(sp)

    return p;

def gen_datasets_from(data, len_vorkurve, len_nachkurve, time_column_index = 0, temp_column_index = 1, temp_err_column_index = 2):
    vorkurve = Dataset(
        data[:len_vorkurve, time_column_index], 
        data[:len_vorkurve, temp_column_index], 
        data[:len_vorkurve, temp_err_column_index]
    )
    mitte = Dataset(
        data[len_vorkurve:-len_nachkurve, time_column_index], 
        data[len_vorkurve:-len_nachkurve, temp_column_index], 
        data[len_vorkurve:-len_nachkurve, temp_err_column_index]
    )
    nachkurve = Dataset(
        data[-len_nachkurve:, time_column_index], 
        data[-len_nachkurve:, temp_column_index], 
        data[-len_nachkurve:, temp_err_column_index]
    )
    return vorkurve, mitte, nachkurve