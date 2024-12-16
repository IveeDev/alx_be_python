task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
in_time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if in_time == "yes":
            print(f"Reminder: '{
                  task}' is a high priority task that requires immediate attention today!")
        else:
            print(
                f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if in_time == "yes":
            print(f"Reminder: '{
                  task}' is a medium priority task!")
        else:
            print(f"Note '{
                  task}' is a low priority task. Consider completing it when you have free time..")

    case "low":
        if in_time == "yes":
            print(f"{task} is a low task")
        else:
            print(f"Note: '{
                  task}' is a low priority task. is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority!")
