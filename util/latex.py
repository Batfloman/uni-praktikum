import numpy as np;
import re;

latex_patterns = {
    r'([A-Za-z])_(\d+)': r'$\1_{\2}$',  # Replace I_1 with $I_1$
    r'\bphi\b': r'$\varphi$',         # Replace 'phi' with $\varphi$
}

def replace_latex_patterns(input_string, replacements = latex_patterns):
    """
    Replace specified patterns in the input string with corresponding LaTeX syntax.

    Args:
        input_string (str): The string to process.
        replacements (dict): A dictionary where keys are regex patterns and 
                             values are replacement strings.

    Returns:
        str: The processed string with LaTeX replacements.
    """
    for pattern, replacement in replacements.items():
        input_string = re.sub(pattern, replacement, input_string)
    return input_string

def save_table(arr, filename: str):
    """
    Save a 2D NumPy array as a LaTeX table into a .tex file.
    Overwrites the file if it exists.
    
    Parameters:
        arr (numpy.ndarray): 2D array to be converted into a table.
        filename (str): Name of the .tex file to save.
    """
    if not filename.endswith(".tex"):
        filename = filename + ".tex";

    if isinstance(arr, np.ndarray):
        rows, cols = arr.shape

    with open(filename, 'w') as f:
        f.write("\\begin{tabular}{" + "c" * cols + "}\n")
        f.write("\\hline\n")
        
        for row in arr:
            processed_row = [
                replace_latex_patterns(str(value)) for value in row
            ]
            f.write(" & ".join(processed_row) + " \\\\\n")
        
        f.write("\\hline\n")
        f.write("\\end{tabular}\n")