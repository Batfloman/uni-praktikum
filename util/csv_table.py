import numpy as np;
import csv

def save(data_array, filename):
    """
    Save the 2D NumPy array to a CSV file.

    Parameters:
    filename (str): The name of the file to save the data to.
    data_array (numpy.ndarray): The 2D NumPy array containing the data.
    """
    if not filename.endswith('.csv'):
        filename += '.csv'

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_array)

    return

import csv

def read(filename):
    if not filename.endswith('.csv'):
        filename += '.csv'

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Read the data into a numpy array
        data = np.array([row for row in reader])

    return data