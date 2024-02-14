import os
import datetime

def main_menu():
    """sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
    os.system('cls')
    print("Welcome to the Task Manager!")
    print("Select an option:")
    print("r - Register a user")
    print("a - Add a new task")
    print("va - View all tasks")
    print("vm - View my tasks")
    print("gr - Generate reports")
    print("ds - Display statistics")
    print("q - Quit")

def reg_user():
    """Registers a new user.

    Prompts the user to enter a username and checks if the username is
    already taken. If not taken, creates a new user within 'users.txt' file.

    Return: None
    """

    while True:
        # Prompt the user to enter a username
        username = input("Enter a username: ")

        # Check if the username is already taken
        if is_username_taken(username):
            print(f"Error: the username '{username}' is already taken.")
            continue

        # Append the username to the 'users.txt' file
        with open('users.txt', 'a', encoding='utf-8') as file:
            file.write(f"{username}\n")
        
        # Print a success message
        print(f"User '{username}' has been registered successfully!")
        break  # Exit the loop once registration is successful


def is_username_taken(username):
    with open('users.txt', 'r', encoding='utf-8') as file:
        users = file.readlines()

    for user in users:
        if user.strip() == username:
            return True

    return False


def add_task():
    with open("tasks.txt", "a", encoding='utf-8') as file:
        file.write("\n")  # Add empty line to separate tasks
        task_number = get_next_task_number()  # Get the next task number
        file.write(f"Task number: {task_number}\n")
        file.write(f"Task name: {input('Task name: ')}\n")
        file.write(f"Assigned to: {input('Assigned to: ')}\n")
        file.write(f"Date assigned: {input('Date assigned (DD-MM-YYYY): ')}\n")
        file.write(f"Due date: {input('Due date (DD-MM-YYYY): ')}\n")
        file.write(f"Task Complete? [Yes/No]: {input('Task Complete? [Yes/No]: ')}\n")
        file.write(f"Task description: {input('Task description: ')}\n")

def get_next_task_number():
    try:
        with open("tasks.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        if lines:  # Check if there are any lines in the file
            last_line = lines[-1].strip()
            if last_line.startswith("Task number: "):
                return int(last_line.split(": ")[1]) + 1
            else:
                return 1
        else:
            return 1  # If the file is empty, start from task number 1
    except FileNotFoundError:
        return 1


def view_all():
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    # Print each task with tabulated values for each header
    for task in tasks:
        lines = task.split('\n')
        for line in lines:
            header, value = line.split(": ")
            print(f"{header:<25} {value}")
        print("_" * 50)  # Long line between tasks

        #add a way to exit viewing the result to accomodate os - cls
    


def view_mine():
    username = input("Enter your username: ")
    if not is_username_taken(username):
        print(f"Error: the username '{username}' does not exist.")
        return

    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    # Display tasks assigned to the current user
    for idx, task in enumerate(tasks, start=1):
        if f"Assigned to: {username}" in task:
            print(f"\nTask {idx}:")
            print(task)

    # Allow the user to select a task or return to main menu
    while True:
        task_choice = input("Enter the number of the task to select, or enter '-1' to return to the main menu: ")
        if task_choice == '-1':
            break
        elif not task_choice.isdigit() or int(task_choice) < 1 or int(task_choice) > len(tasks):
            print("Invalid input. Please enter a valid task number.")
        else:
            task_idx = int(task_choice) - 1
            selected_task = tasks[task_idx]
            print(f"\nSelected Task {task_choice}:")
            print(selected_task)

            # Provide options to mark the task as complete or edit the task
            task_complete = [line.split(": ")[1] for line in selected_task.split("\n") if line.startswith("Task Complete?")]
            if task_complete and task_complete[0].lower() == "no":
                action = input("Choose an action (mark/ edit): ").lower()
                if action == "mark":
                    tasks[task_idx] = selected_task.replace("No", "Yes", 1)
                    with open("tasks.txt", "w", encoding='utf-8') as file:
                        file.write('\n\n'.join(tasks))
                    print("Task marked as complete.")
                elif action == "edit":
                    edit_task(selected_task)
                else:
                    print("Invalid action.")
            else:
                print("Task is already completed.")

def edit_task(selected_task):
    # Load tasks from file
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    # Extract the task details
    lines = selected_task.split("\n")
    task_info = {}
    for line in lines:
        header, value = line.split(": ")
        task_info[header] = value

    # Allow the user to edit the assigned user or the due date
    print("Editing Task:")
    print(selected_task)
    while True:
        edit_choice = input("Enter the field to edit (assigned/due), or enter '-1' to return to task selection: ").lower()
        if edit_choice == '-1':
            break
        elif edit_choice == 'assigned':
            new_assigned_to = input("Enter new assigned to: ")
            task_info['Assigned to'] = new_assigned_to
            print("Assigned to updated.")
        elif edit_choice == 'due':
            new_due_date = input("Enter new due date (DD-MM-YYYY): ")
            task_info['Due date'] = new_due_date
            print("Due date updated.")
        else:
            print("Invalid choice. Please enter 'assigned' or 'due'.")

    # Update the task in the tasks list and write it back to the file
    updated_task = "\n".join([f"{header}: {value}" for header, value in task_info.items()])
    tasks[tasks.index(selected_task)] = updated_task
    with open("tasks.txt", "w", encoding='utf-8') as file:
        file.write('\n\n'.join(tasks))


def generate_reports():
    # Read tasks from file
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    total_tasks = len(tasks)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    # Count completed, uncompleted, and overdue tasks
    for task in tasks:
        task_info = dict(line.split(": ", 1) for line in task.split("\n"))
        if task_info["Task Complete? [Yes/No]"].lower() == "yes":
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            due_date = task_info["Due date"]
            if due_date:
                try:
                    today = datetime.date.today()
                    due_date_parsed = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
                    if today > due_date_parsed:
                        overdue_tasks += 1
                except ValueError:
                    print(f"Warning: Invalid due date format for task: {task}")

    # Calculate percentages
    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    percentage_overdue = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

    # Write to task_overview.txt
    with open("task_overview.txt", "w", encoding='utf-8') as file:
        file.write("Task Overview\n")
        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed_tasks}\n")
        file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue tasks: {overdue_tasks}\n")
        file.write(f"Percentage incomplete: {percentage_incomplete:.2f}%\n")
        file.write(f"Percentage overdue: {percentage_overdue:.2f}%\n")
    
    # Read users from file
    with open("users.txt", "r", encoding='utf-8') as file:
        users = file.read().strip().split('\n')  # Split users by newline

    # Calculate user-specific statistics
    with open("user_overview.txt", "w", encoding='utf-8') as file:
        file.write("User Overview\n")
        file.write(f"Total users: {len(users)}\n")
        file.write(f"Total tasks: {total_tasks}\n")
        file.write("\n")
        for user in users:
            user_tasks = [task for task in tasks if f"Assigned to: {user}" in task]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = 0
            uncompleted_user_tasks = 0
            overdue_user_tasks = 0
            
            for task in user_tasks:  # This loop calculates statistics for each user's tasks
                task_info = dict(line.split(": ", 1) for line in task.split("\n"))
                if task_info["Task Complete? [Yes/No]"].lower() == "yes":
                    completed_user_tasks += 1
                else:
                    uncompleted_user_tasks += 1
                    due_date = task_info["Due date"]
                    if due_date:
                        try:
                            today = datetime.date.today()
                            due_date_parsed = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
                            if today > due_date_parsed:
                                overdue_user_tasks += 1
                        except ValueError:
                            print(f"Warning: Invalid due date format for task: {task}")

            percentage_user_assigned = (total_user_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            percentage_user_completed = (completed_user_tasks / total_user_tasks) * 100 if total_user_tasks > 0 else 0
            percentage_user_uncompleted = (uncompleted_user_tasks / total_user_tasks) * 100 if total_user_tasks > 0 else 0
            percentage_user_overdue = (overdue_user_tasks / uncompleted_user_tasks) * 100 if uncompleted_user_tasks > 0 else 0

            file.write(f"User: {user}\n")
            file.write(f"Total tasks assigned: {total_user_tasks}\n")
            file.write(f"Percentage of total tasks: {percentage_user_assigned:.2f}%\n")
            file.write(f"Percentage completed: {percentage_user_completed:.2f}%\n")
            file.write(f"Percentage to be completed: {percentage_user_uncompleted:.2f}%\n")
            file.write(f"Percentage overdue: {percentage_user_overdue:.2f}%\n\n")

            print(f"completed {completed_user_tasks}")
            print(f"incomplete {uncompleted_user_tasks}")
            print(f"overdue {overdue_user_tasks}")