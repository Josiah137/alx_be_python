# daily_reminder.py

# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt the user for the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask the user if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Function to provide the reminder
def task_reminder(task, priority, time_bound):
    reminder = f"'{task}' is a {priority} priority task"

    # Match case statement for priority level
    match priority:
        case "high":
            reminder += " that requires your full focus."
        case "medium":
            reminder += " that should be addressed soon."
        case "low":
            reminder += " that can be done when you have free time."
        case _:
            reminder = "Invalid priority entered."
            return reminder
    
    # Add urgency if the task is time-bound
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder += " It can be done at your convenience."
    else:
        reminder = "Invalid input for time sensitivity."
    
    return reminder

# Print the customized reminder
print(task_reminder(task, priority, time_bound))

