from .measurement import Measurement

class Dataset:
    def __init__(self, measurements: dict = {}):
        self.measurements = measurements;

    def copy_remove_index(self, index):
        if not index in self.measurements:
            return Dataset(self.measurements)
        new_measurements = {k: v for k, v in self.measurements.items() if k != index}
        return Dataset(new_measurements)

    def __getitem__(self, index) -> Measurement:
        return self.measurements[index];

    def __setitem__(self, index, value):
        self.measurements[index] = value;
    
    def __contains__(self, key):
        return key in self.measurements;

    def __str__(self):
        strings = [];
        for key, value in self.measurements.items():
            strings.append(f"{key}: {value}")
        return f'{", ".join(strings)}'