# Global Conversion Factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

# Function to convert Fahrenheit to Celsius  
def convert_to_celsius(fahrenheit):  
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  

# Function to convert Celsius to Fahrenheit  
def convert_to_fahrenheit(celsius):  
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  

def main():  
    # Prompt the user for input  
    try:  
        temp_input = float(input("Enter the temperature to convert: "))  
    except ValueError:  
        print("Invalid temperature. Please enter a numeric value.")  
        return  

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  

    if unit == 'C':  
        converted_temp = convert_to_fahrenheit(temp_input)  
        print(f"{temp_input}°C is {converted_temp:.2f}°F")  
    elif unit == 'F':  
        converted_temp = convert_to_celsius(temp_input)  
        print(f"{temp_input}°F is {converted_temp:.2f}°C")  
    else:  
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  

if __name__ == "__main__":  
    main()
