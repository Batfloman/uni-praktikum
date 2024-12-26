import sympy as sp;
from inspect import signature
import re
from IPython.display import Markdown, display
from typing import Callable, Union

def display_equation(input_data: Union[str, Callable, sp.Basic]):
    """
    Processes the input and displays a LaTeX-rendered equation in a Jupyter Notebook.
    
    Parameters:
    - input_data (Union[str, Callable, Basic]): 
        - str: Path to a LaTeX file.
        - Callable: A Python function to be converted to a sympy expression.
        - Basic: A sympy symbol/expression.
    """
    if isinstance(input_data, str):
        # Handle file path
        try:
            with open(input_data, 'r', encoding='utf-8') as f:
                latex_content = f.read()
            
            # Validate and clean LaTeX content
            cleaned_content = re.sub(r"\\label\{[^}]*\}", "", latex_content)
            display(Markdown(f"$$ {cleaned_content} $$"))
        except FileNotFoundError:
            raise ValueError(f"The file at path '{input_data}' was not found.")
        except Exception as e:
            raise ValueError(f"Error reading the file: {e}")
    
    elif callable(input_data):
        # Handle function
        try:
            sympy_expr = to_sympy(input_data)
            latex_expr = sp.latex(sympy_expr)
            display(Markdown(f"$$ {latex_expr} $$"))
        except Exception as e:
            raise ValueError(f"Error converting function to sympy expression: {e}")
    
    elif isinstance(input_data, sp.Basic):
        # Handle sympy expression
        latex_expr = sp.latex(input_data)
        display(Markdown(f"$$ {latex_expr} $$"))
    
    else:
        raise TypeError("Input must be a file path (str), a callable function, or a sympy expression.")

def export_as_latex(func, filename: str, **symbol_overrides):
    """
    Converts a function or SymPy expression into a LaTeX representation and saves it to a file.

    Parameters:
    - func: Python function or SymPy expression to convert.
    - filename: Output filename for the LaTeX file.
    - symbol_overrides: Optional overrides for argument symbols.

    Raises:
    - ValueError: If `func` is not a valid Python function or SymPy expression.
    """
    # Ensure the function is a SymPy expression
    if not isinstance(func, sp.Basic):
        try:
            func = to_sympy(func, **symbol_overrides)
        except Exception as e:
            raise ValueError("Invalid input: unable to convert to SymPy.") from e

    # Add .tex extension if not provided
    if not filename.endswith(".tex"):
        filename += ".tex"

    # Write the LaTeX string to a file
    try:
        with open(filename, 'w') as f:
            f.write(sp.latex(func))
        print(f"LaTeX exported successfully to {filename}")
    except IOError as e:
        raise IOError(f"Failed to write LaTeX to file: {filename}") from e

def to_sympy(func, **symbol_overrides):
    """
    Converts a Python function into a symbolic representation using SymPy.

    If the input is already a SymPy expression, it applies only the symbol overrides.

    Parameters:
    - func: Python function or SymPy expression.
    - (optional) symbol_overrides: overrides for argument symbols.

    Returns:
    - SymPy expression.
    """
    if isinstance(func, sp.Basic):
        # Apply overrides to the existing SymPy expression
        return _override_symbols(func, symbol_overrides)

    # Extract argument names from the Python function
    arg_names = signature(func).parameters.keys()

    # Create symbols for each argument
    symbols_dict = _create_symbols(arg_names, symbol_overrides)

    # Call the function with symbolic arguments
    sympy_expr = func(**symbols_dict)

    # Apply overrides (if any) to the resulting SymPy expression
    return _override_symbols(sympy_expr, symbol_overrides)
    
def get_derivative(func, var):
    """
    Computes the derivative of a Python function or SymPy expression.

    Parameters:
    - func: Python function or SymPy expression to differentiate.
    - var: Variable with respect to which the derivative is taken. Can be a string or a SymPy symbol.
    - symbol_overrides: Optional overrides for argument symbols.

    Returns:
    - The derivative as a SymPy expression.
    """
    # Ensure `func` is a SymPy expression
    if not isinstance(func, sp.Basic):
        func = to_sympy(func)

    # Ensure `var` is a SymPy symbol
    if isinstance(var, str):
        var = sp.symbols(var)

    # Compute the derivative
    return sp.diff(func, var)

def gaussian_error_propagation(func, exclude=None, **symbol_overrides):
    """
    Computes the general form of Gaussian error propagation symbolically.

    Parameters:
    - func: Python function or SymPy expression for which uncertainty is propagated.
    - exclude: Optional set of symbols to exclude from propagation.
    - symbol_overrides: Optional overrides for argument symbols.

    Returns:
    - The general form of the propagated uncertainty as a SymPy expression.
    """
    # Ensure the function is a SymPy expression
    if not isinstance(func, sp.Basic):
        func = to_sympy(func, **symbol_overrides)

    # Determine free symbols in the function
    variables = func.free_symbols

    # Apply exclusions if provided
    if exclude is not None:
        if not isinstance(exclude, set):
            exclude = set(exclude)
        exclude = {sp.symbols(sym) if isinstance(sym, str) else sym for sym in exclude}
        variables = variables - exclude

    # General form of propagated uncertainty
    propagated = 0
    for symbol in variables:
        sigma = sp.symbols(f"\\sigma_{{{symbol}}}")  # Symbolic uncertainty for each variable
        derivative = sp.diff(func, symbol)
        propagated += (derivative * sigma) ** 2

    return sp.sqrt(propagated)

def _create_symbols(arg_names, symbol_overrides):
    """
    Creates a dictionary mapping argument names to SymPy symbols or overrides.

    Parameters:
    - arg_names: List of argument names (strings).
    - symbol_overrides: Dictionary of symbol overrides.

    Returns:
    - Dictionary mapping argument names to SymPy symbols or overrides.
    """
    symbols_dict = {}
    for name in arg_names:
        override = symbol_overrides.get(name)
        if override is None:
            # Default to a SymPy symbol
            symbols_dict[name] = sp.symbols(name)
        elif isinstance(override, str):
            # Interpret strings as custom symbol names
            symbols_dict[name] = sp.symbols(override)
        elif isinstance(override, sp.Basic):
            # Use the provided SymPy symbol or function as-is
            symbols_dict[name] = override
        elif isinstance(override, type(sp.Function('f'))):  # Ensure SymPy-compatible callable
            symbols_dict[name] = override
        else:
            raise ValueError(f"Invalid override for {name}: {override}")
    return symbols_dict

def _override_symbols(expr, symbol_overrides):
    """
    Applies symbol overrides to a SymPy expression.

    Parameters:
    - expr: SymPy expression.
    - symbol_overrides: Dictionary of symbol overrides.

    Returns:
    - SymPy expression with overridden symbols.
    """
    # Map existing symbols to their overrides
    replacements = {
        sym: _create_symbols([str(sym)], symbol_overrides).get(str(sym))
        for sym in expr.free_symbols
    }
    return expr.subs(replacements)