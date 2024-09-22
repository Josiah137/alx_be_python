# match_case_calculator.py

# Function to perform the selected operation
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero."
        case _:
            return "Invalid operation selected."

# Prompt the user to input two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operation)

# Output the result in a user-friendly message
if isinstance(result, float) or isinstance(result, int):
    print(f"The result is {result}.")
else:
    print(result)

