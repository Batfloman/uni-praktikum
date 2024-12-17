import numpy as np

class Dataset:
    def __init__(self, times, Temp, temp_error=None):
        if len(times) != len(Temp):
            raise RuntimeError("Times and Temperatures of different size")
        if temp_error is not None and len(Temp) != len(temp_error):
            raise RuntimeError("Temp and Temp error have different sizes")

        self.t = times
        self.T = Temp
        self.T_err = np.zeros(len(self.T)) if temp_error is None else temp_error

    def __str__(self):
        stacked_data = np.column_stack((self.t, self.T, self.T_err))
        return f"Dataset:\n{stacked_data}"