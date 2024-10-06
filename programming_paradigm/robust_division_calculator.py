# robust_division_calculator.py  

def safe_divide(numerator, denominator):  
    """Performs division and handles division by zero and non-numeric inputs."""  
    try:  
        num = float(numerator)  # Attempt to convert numerator to float  
        denom = float(denominator)  # Attempt to convert denominator to float  
    except ValueError:  
        return "Error: Please enter numeric values only."  # Handle non-numeric input  

    try:  
        result = num / denom  # Attempt division  
    except ZeroDivisionError:  
        return "Error: Cannot divide by zero."  # Handle division by zero  

    return f"The result of the division is {result}"  # Return successful result
