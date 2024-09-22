# daily_reminder.py

# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt the user for the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes/no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a Match Case statement for the task's priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority entered."

# Check if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += " that can be done at your convenience."
else:
    reminder = "Invalid input for time sensitivity."

# Print the final reminder
print(reminder)

