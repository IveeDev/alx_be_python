# # Prompt for task input
# task = input("Enter your task: ")
# # Ensure priority is in lowercase
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# # Match case for task priority
# match priority:
#     case "high":
#         reminder = f"Reminder: '{task}' is a high priority task"
#     case "medium":
#         reminder = f"Note :'{task}' is a medium priority task"
#     case "low":
#         reminder = f"Note: '{task}' is a low priority task"
#     case _:
#         reminder = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."

# # Modify the reminder based on whether the task is time-bound
# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# else:
#     reminder += ". Consider completing it when you have free time."

# # Print the final reminder
# print(reminder)


# Prompt for task input
task = input("Enter your task: ")
# Ensure priority is in lowercase
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for task priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."

# Modify the reminder based on whether the task is time-bound
if priority in ["high", "medium", "low"]:  # Only add if a valid priority was entered
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

# Print the final reminder
print(message)
