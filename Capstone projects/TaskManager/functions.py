import os
import datetime

def main_menu():
    """
"""
    os.system('cls')
    print("-" * 50)
    print("Welcome to the Task Manager!")
    print("Select an option:")
    print("r - Register a user")
    print("a - Add a new task")
    print("va - View all tasks")
    print("vm - View my tasks")
    print("gr - Generate reports")
    print("ds - Display statistics")
    print("e - exit\n")
    print("Enter -1 at any time to cancel current process")
    print("-" * 50)

def reg_user():
    """Registers a new user.

    Prompts the user to enter a username and checks if the username is
    already taken. If not taken, creates a new user within 'users.txt' file.

    Return: None
    """

    while True:
        # Prompt the user to enter a username
        username = input("Enter a username: ")

        # Check if the user wants to cancel registration
        if username == '-1':
            return

        # Check if the username is already taken
        elif is_username_taken(username):
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
    """Creates a new task.

    Prompts the user to enter a task details and writes them to tasks.txt file
    Error handling for no user in

    """
    with open("tasks.txt", "a", encoding='utf-8') as file:
        file.write("\n")  # Add empty line to separate tasks

        while True:
            user_input = input('Task name: ')
            if user_input == '-1':
                print("Task creation cancelled.")
                return
            else:
                if user_input:
                    file.write(f"Task name: {user_input}\n")
                    break
                else:
                    print("Error: Task name cannot be empty.")

        while True:
            user_input = input('Assigned to: ').strip()
            if user_input == '-1':
                print("Task creation cancelled.")
                return
            if is_username_taken(user_input):
                file.write(f"Assigned to: {user_input}\n")
                break
            else:
                print("Error: User does not exist. Please enter an existing user.")

        while True:
            date_format_error = False
            user_input = input('Date assigned (DD-MM-YYYY): ')
            if user_input == '-1':
                print("Task creation cancelled.")
                return
            if user_input:
                try:
                    datetime.datetime.strptime(user_input, "%d-%m-%Y")
                    file.write(f"Date assigned: {user_input}\n")
                    break
                except ValueError:
                    print("Error: Invalid date format. Please enter date in DD-MM-YYYY format.")
                    date_format_error = True
            if not date_format_error:
                print("You entered an invalid date format, please enter a new date assigned.")

        while True:
            date_format_error = False
            user_input = input('Due date (DD-MM-YYYY): ')
            if user_input == '-1':
                print("Task creation cancelled.")
                return
            if user_input:
                try:
                    datetime.datetime.strptime(user_input, "%d-%m-%Y")
                    file.write(f"Due date: {user_input}\n")
                    break
                except ValueError:
                    print("Error: Invalid date format. Please enter date in DD-MM-YYYY format.")
                    date_format_error = True
            if not date_format_error:
                print("You entered an invalid date format, please enter a new due date.")

        while True:
            user_input = input('Task Complete? [Yes/No]: ').strip().lower()
            if user_input == 'yes' or user_input == 'no':
                file.write(f"Task Complete? [Yes/No]: {user_input}\n")
                break
            elif user_input == '-1':
                print("Task creation cancelled.")
                return
            else:
                print("Error: Please enter 'Yes' or 'No'.")

        while True:
            user_input = input('Task description: ')
            if user_input == '-1':
                print("Task creation cancelled.")
                return
            else:
                if user_input:
                    file.write(f"Task description: {user_input}\n")
                    break
                else:
                    print("Error: Task description cannot be empty.")


def get_next_task_number():
    """Support function.

    Checks tasks.txt for number of tasks and assigns
    a number to each task

    Return: None
    """
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
    task_number = 1
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    while True:
        print("\nView all tasks:")
        for task in tasks:
            print(f"\nTask {task_number}:")
            for line in task.split('\n'):
                try:
                    header, value = line.split(": ")
                    print(f"{header:<25} {value}")
                except ValueError:
                    print(f"Missing parameter: {line}")
            print("_" * 50)  # Long line between tasks
            task_number += 1

        # Ask the user to go back or continue
        choice = input("\nEnter -1 to go back to the previous menu: ")
        if choice == "-1":
            break


def view_mine():
    username = input("Enter your username: ")
    if not is_username_taken(username):
        print(f"Error: the username '{username}' does not exist.")
        return
    os.system('cls')

    while True:
        with open("tasks.txt", "r", encoding='utf-8') as file:
            tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

        # Display task names assigned to the current user
        print("Enter -1 at any time to cancel current process")
        print("-" * 50)
        print(f"Tasks belonging to {username}:\n")
        task_numbers = []
        for idx, task in enumerate(tasks, start=1):
            if f"Assigned to: {username}" in task:
                task_numbers.append(idx)
                print(f"Task {idx}: {get_task_name(task)}")

        # Allow the user to select a task or go back
        choice = input("Enter the number of the task to select and edit: ")
        if choice.isdigit() and int(choice) in task_numbers:
            task_idx = int(choice) - 1
            selected_task = tasks[task_idx]
            display_task_details(selected_task)
            edit_choice = input("Do you want to edit this task? (yes/no): ").lower()
            if edit_choice == 'yes':
                edit_task(selected_task)
            os.system('cls')  # Clear screen for a tidy interface when a task is selected
        elif choice == '-1':
            break
        else:
            print("Invalid input. Please enter a valid task number or 'back' to return to the main menu.")

def get_task_name(task):
    # Extract and return the task name
    lines = task.split("\n")
    for line in lines:
        if line.startswith("Task name"):
            return line.split(": ")[1]
    return ""

def display_task_details(task):
    # Display all task details with numbers on the left
    lines = task.split("\n")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}. {line}")

def edit_task(selected_task):
    # Extract the task details
    task_info = {}
    lines = selected_task.split("\n")
    for line in lines:
        header, value = line.split(": ")
        task_info[header] = value

    # Allow the user to edit the task
    print("Editing Task:")
    while True:
        edit_choice = input("Enter the number of the field to edit, or enter '-1' to return to task selection: ")
        if edit_choice == '-1':
            print("Returning to task selection.")
            break
        elif edit_choice.isdigit() and int(edit_choice) in range(1, len(lines) + 1):
            field_number = int(edit_choice) - 1
            header, _ = lines[field_number].split(": ", 1)
            new_value = input(f"Enter new value for {header}: ")
            task_info[header] = new_value
            print(f"{header} updated.")
        else:
            print("Invalid input. Please enter a valid field number.")

    # Update the task in the tasks list and write it back to the file
    updated_task = "\n".join([f"{header}: {value}" for header, value in task_info.items()])
    tasks = []
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline
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