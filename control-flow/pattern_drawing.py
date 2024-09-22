# pattern_drawing.py

# Ask the user to input a positive integer for the pattern size
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Initialize the row counter for the while loop
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print the asterisks for each column in the row
    for col in range(size):
        print("*", end="")
    # Print a newline after each row is complete
    print()
    
    # Move to the next row
    row += 1

