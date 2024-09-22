# Prompt the user for the task description  
task = input("Enter your task: ")  

# Validate priority input  
while True:  
    priority = input("Priority (high/medium/low): ").lower()  
    if priority in ["high", "medium", "low"]:  
        break  
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")  

# Validate time-bound input  
while True:  
    time_bound = input("Is it time-bound? (yes/no): ").lower()  
    if time_bound in ["yes", "no"]:  
        break  
    print("Invalid input. Please enter 'yes' or 'no'.")  

# Initialize the reminder variable  
reminder = ""  

# Use a Match Case statement for the task's priority  
match priority:  
    case "high":  
        reminder = f"'{task}' is a high priority task"  
    case "medium":  
        reminder = f"'{task}' is a medium priority task"  
    case "low":  
        reminder = f"'{task}' is a low priority task."  

# Check if the task is time-bound  
if time_bound == "yes":  
    reminder += " that requires immediate attention today!"  
elif time_bound == "no":  
    reminder += " Consider completing it when you have free time."  

# Print the final reminder  
print(f"Reminder: {reminder}")
