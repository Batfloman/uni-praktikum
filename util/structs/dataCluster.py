import numpy as np
import copy
import pandas as pd
from typing import List, Optional, Tuple, Union
import re

from util.structs import Dataset, Measurement, CopyManager
from util import excel_table;
from util import latex;

def _column_has_measurement(array):
    return any(isinstance(obj, Measurement) for obj in array);

def _get_error_index_str(index):
    return f"Δ{index}" 

def _get_values_array(column):
    values = []
    for item in column:
        value = item.value if isinstance(item, Measurement) else item;
        values.append(value);
    return values;

def _get_errors_array(column):
    values = []
    for item in column:
        value = item.error if isinstance(item, Measurement) else "-";
        values.append(value);
    return values;    

class DataCluster:
    def __init__(self, data: List[Dataset] = np.array([])):
        self.data = data
        self.save = _Save_Manager(self);
        self.copy = CopyManager(self);
    
    def to_np_array(self, with_header = True):
        indicies = self.get_indicies();
    
        # needed for np.column_stack...
        length = len(self) + 1 if with_header else len(self);
        arr = np.zeros((length, 0))

        for index in indicies:
            column = self.column(index)

            # values
            values = _get_values_array(column);
            if with_header:
                values.insert(0, index);
            arr = np.column_stack((arr, values))

            # uncertaintys only if there is atleast one Measurement in the current column, otherwise unnecessary
            if _column_has_measurement(column):
                errors = _get_errors_array(column);
                if with_header:
                    errors.insert(0, _get_error_index_str(index));
                arr = np.column_stack((arr, errors))

        return arr;

    def add(self, dataset: Dataset):
        """
        Add a new dataset to the data collection.
        """
        self.data = np.append(self.data, copy.deepcopy(dataset))

    def sort(self, *keys: str) -> 'DataCluster':
        """
        Sort the datasets based on the specified keys.

        Parameters:
        keys (str): Indices to sort the datasets by.

        Returns:
        Data: A new Data object with sorted datasets.
        """
        if not keys:
            return self

        def sort_function(dataset: Dataset) -> Tuple:
            return tuple(dataset[key].value for key in keys if key in dataset)

        sorted_data = sorted(self.data, key=sort_function)
        return DataCluster(np.array(sorted_data))

    def remove(self, to_remove: Union['DataCluster', Dataset]):
        """
        Remove datasets from the data collection.

        Parameters:
        to_remove (Data or Dataset): The datasets to remove.
        """
        if isinstance(to_remove, DataCluster):
            for dataset in to_remove:
                self.remove(dataset)
        elif isinstance(to_remove, Dataset):
            if to_remove not in self.data:
                print(f"tried removing not exsisting {to_remove}");
                return;
            self.data.remove(to_remove)
        else:
            raise ValueError(f"Unsupported type for removal: {type(to_remove)}")

    def values(self, index: str) -> np.ndarray:
        """
        Get the values for a specific index from all datasets.

        Parameters:
        index (str): The index to extract values from.

        Returns:
        np.ndarray: An array of values.
        """
        return np.array([dataset[index].value for dataset in self.data if index in dataset])

    def errors(self, index: str) -> np.ndarray:
        """
        Get the errors for a specific index from all datasets.

        Parameters:
        index (str): The index to extract errors from.

        Returns:
        np.ndarray: An array of errors.
        """
        return np.array([dataset[index].error for dataset in self.data if index in dataset])

    def column(self, index: str) -> np.ndarray:
        """
        Get the measurements for a specific index from all datasets.

        Parameters:
        index (str): The index to extract measurements from.

        Returns:
        np.ndarray: An array of measurements.
        """
        return np.array([dataset[index] if index in dataset else None for dataset in self.data])

    def data_mean(self) -> Dataset:
        """
        Calculate the mean value and error for each index across all datasets.

        Returns:
        Dataset: A new Dataset containing the mean values and errors.
        """
        indices = self.get_indicies();

        mean_dataset = Dataset();

        for index in indices:
            values = [];
            errors = [];
            for d in self.data:
                if index not in d:
                    continue;
                if isinstance(d[index], Measurement):
                    values.append(d[index].value);
                    errors.append(d[index].error);
                if isinstance(d[index], int) or isinstance(d[index], float):
                    values.append(d[index]);
                    errors.append(0)
                
            values = np.array(values)
            errors = np.array(errors)

            N = len(values)
            mean_val = np.mean(values)
            mean_err = np.sqrt(np.sum(errors**2)) / N
            mean_dataset[index] = Measurement(mean_val, mean_err)
        
        return mean_dataset
    
    def copy_remove_index(self, index):
        new_data = DataCluster()

        for d in self.data:
            new_set = d.copy_remove_index(index);
            new_data.add(new_set)
            
        return new_data

    def filter_null(self, index_to_check: Optional[List[str]] = None) -> 'DataCluster':
        """
        Filter out datasets with null values for specific indices.

        Parameters:
        index_to_check (List[str], optional): Indices to check for null values. If None, check all indices.

        Returns:
        Data: A new Data object without datasets containing null values for the specified indices.
        """
        surviving = []
        
        for dataset in self.data:
            valid = True
            indices_to_check = index_to_check if index_to_check else dataset.measurements.keys()
            
            for index in indices_to_check:
                if index in dataset:
                    value = dataset[index]
                    valid_measurement = isinstance(value, Measurement) and not np.isnan(value.value);
                    valid_num = isinstance(value, int) or isinstance(value, float);
                    valid_string = isinstance(value, str) and bool(value.strip())
                    if not (valid_measurement or valid_num or valid_string):
                        valid = False
                        break
                else:
                    valid = False
                    break
            
            if valid:
                surviving.append(dataset)
        
        return DataCluster(np.array(surviving))

    def filter(self, index: str, value: float) -> 'DataCluster':
        """
        Filter datasets based on a specific value for a given index.

        Parameters:
        index (str): The index to filter by.
        value (float): The value to filter by.

        Returns:
        Data: A new Data object containing datasets with the specified value for the index.
        """
        surviving = [];
        for d in self.data:
            if isinstance(d, Measurement) and d[index].value == value:
                surviving.append(d);
            elif d[index] == value:
                surviving.append(d)
        return DataCluster(np.array(surviving))
    
    def round_index(self, index: str, additional_digits: int = 0):
        for dataset in self.data:
            if index in dataset:
                dataset[index].round(additional_digits);
    
    def get_indicies(self):
        all_indices = set()
        for dataset in self.data:
            all_indices.update(dataset.measurements.keys())
        
        # Sort indices for consistent column ordering
        return sorted(all_indices)

    def get_all_indicies_with_error(self):
        all_indices = self.get_indicies();

        all_indices_error = [None]*(len(all_indices)*2)
        all_indices_error[0::2] = all_indices;
        all_indices_error[1::2] = [f"Δ{index}" for index in all_indices];
        return all_indices_error;

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        return self.data[key]

    def __str__(self) -> str:
        table_data = self.to_np_array_measurements(); 
        header = table_data[0]
        data = table_data[1:]

        return create_table(header, data);
    
    def to_np_array_measurements(self, include_header = True):
        indicies = self.get_indicies();
        data_array = []

        for dataset in self.data:
            row = []
            for index in indicies:
                if not index in dataset:
                # if not index in dataset or not isinstance(dataset[index], Measurement):
                    row.append("NaN")
                    continue;
                measurement = dataset[index]
                row.append(str(measurement));
            data_array.append(row)
        
        # Create header row with unique indices (avoid duplicates)
        if include_header:
            header_row = indicies
            data_array = np.vstack([header_row, data_array])
        
        return data_array;
    
    def save_to_excel_measurements(self, filename: str) -> None:
        """
        """
        as_array = self.to_np_array_measurements(include_header=True)
        excel_table.save(as_array, filename)
        excel_table.add_column_border(filename);
        excel_table.change_column_width(filename, column_width=16)

        return;
    
latex_to_unicode = {
    r"\alpha": "α",
    r"\beta": "β",
    r"\theta": "θ",
    r"\omega": "ω",
    r"\Omega": "Ω",
    r"\sum": "∑",
    r"\times": "×",
    r"\varphi": "φ",
}

def _latex_to_unicode_converter(text):
    # Match all LaTeX expressions inside $...$
    def replace_latex(match):
        latex_content = match.group(1).strip()  # Extract content inside $...$
        for latex, unicode_char in latex_to_unicode.items():
            latex_content = latex_content.replace(latex, unicode_char)
        return latex_content

    return re.sub(r'\$(.*?)\$', replace_latex, text)

class _Save_Manager:
    def __init__(self, super: DataCluster):
        self._super = super;
    
    def _create_dataframe(self):
        """Create a DataFrame from the object's table."""
        table = self._super.to_np_array(with_header=True);
        header = table[0]
        table_data = table[1:]

        data = {index: table_data[:, i] for i, index in enumerate(header)}
        df = pd.DataFrame(data)

        # Replace LaTeX in headers with Unicode equivalents
        processed_header = [_latex_to_unicode_converter(col) for col in header]
        df.columns = processed_header

        return df
    
    def as_excel(self, filename):
        """Save the DataFrame to an Excel file."""
        df = self._create_dataframe()
        excel_table.save(df, filename);
    
    def as_latex(self, filename):
        data = self._super.to_np_array_measurements();
        latex.save_table(data, filename)

def create_table(columns, data):
    """
    Create a table-like string with columns.

    Parameters:
    columns (list): List of column names.
    data (list of lists): List of rows, where each row is a list of values corresponding to the columns.

    Returns:
    str: A string representing the table.
    """
    # Ensure columns are strings
    columns = [str(col) for col in columns]

    # Calculate the maximum width for each header
    header_widths = [len(col) for col in columns]

    # Calculate the maximum width for each column considering both headers and data rows
    column_widths = [max(header_widths[i], max(len(str(row[i])) for row in data)) for i in range(len(columns))]

    # Create the table header
    table = " | ".join(f"{column:{width}}" for column, width in zip(columns, column_widths)) + "\n"

    # Add a separator line
    table += "-+-".join("-" * width for width in column_widths) + "\n"

    # Add the data rows
    for row in data:
        table += " | ".join(f"{value:{width}}" for value, width in zip(row, column_widths)) + "\n"

    return table