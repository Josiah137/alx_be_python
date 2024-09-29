# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
temp = input("Enter the temperature to convert: ")

# Validate if the temperature input is numeric
if not temp.replace('.', '', 1).isdigit() and not temp.replace('-', '', 1).replace('.', '', 1).isdigit():
    raise ValueError("Invalid temperature. Please enter a numeric value.")

temp = float(temp)  # Convert input to float for calculation

# Ask if the temperature is in Celsius or Fahrenheit
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Convert based on the input unit
if unit == 'F':
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
elif unit == 'C':
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

