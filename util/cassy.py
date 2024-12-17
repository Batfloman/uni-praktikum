import numpy as np

def read(filepath, with_header=False):
    if not filepath.endswith('.txt'):
        filepath += '.txt'

    with open(filepath, 'r') as file:
        lines = file.readlines()
        
    # Locate header and data start
    data_start_index = 0
    header = None
    for i, line in enumerate(lines):
        if "DEF=" in line:
            header = line.strip().replace('"', '').replace("DEF=", "").split("\t")
            data_start_index = i + 1  # Data starts after the header line
    
    # Process data from the data start index
    data = []
    for line in lines[data_start_index:]:
        values = line.replace(",", ".").strip().split("\t")
        data.append([float(v) if v != "NAN" else np.nan for v in values])  # Convert to float, handle "NAN" as np.nan
        
    # Convert to numpy array
    data_array = np.array(data, dtype=float)  # Explicitly set dtype to float
    
    # Include header if requested
    if with_header and header:
        return [header] + data_array.tolist()  # Return header as a list with data array
    else:
        return data_array