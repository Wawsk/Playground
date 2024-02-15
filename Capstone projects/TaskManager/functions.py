"""
Functions for Task Manager Application

This module contains various functions used in the Task Manager application.
These functions include task manipulation, user interaction, and file handling.

Functions:
- add_task(): Creates a new task.
- edit_task(selected_task): Edits the selected task.
- view_and_edit_tasks(): Displays and edits tasks assigned to the user.
- print_task(task, task_number): Prints a task.
- generate_reports(): Generates and displays task reports.
- count_tasks(tasks): Counts completed, uncompleted, and overdue tasks.
- print_tasks_assigned_to_user(tasks, username): Prints tasks assigned to a user.
- display_statistics(): Displays statistics from task_overview.txt and user_overview.txt.
"""
import os
import datetime

def main_menu():
    """Display main menu options."""
    # Clear the screen
    os.system('cls')

    # Main menu options
    menu = ["-" * 50, "Welcome to the Task Manager!", "Select an option:",
            "r - Register a user", "a - Add a new task",
            "va - View all tasks", "vm - View my tasks",
            "gr - Generate reports", "ds - Display statistics",
            "e - exit", "", "Enter -1 at any time to cancel current process",
            "-" * 50]
    # Print menu
    print('\n'.join(menu))


def reg_user():
    """Registers a new user."""
    while True:
        # Prompt user for a username
        username = input("Enter a username: ")

        # Check if user wants to cancel
        if username == '-1':
            break
        # Check if username already exists
        elif is_username_taken(username):
            print(f"Error: the username '{username}' is already taken.")
        else:
            # Add username to the users.txt file
            with open('users.txt', 'a', encoding='utf-8') as file:
                file.write(f"{username}\n")
            # Confirmation message
            print(f"User '{username}' has been registered successfully!")
            input("\nPress Enter to continue...")
            break


def is_username_taken(username):
    """Check if username is already taken."""
    # Open users.txt file and check if username exists
    with open('users.txt', 'r', encoding='utf-8') as file:
        return username in file.read().splitlines()


def add_task():
    """Creates a new task."""
    # Open tasks.txt file to add a new task
    with open("tasks.txt", "a", encoding='utf-8') as file:
        file.write("\n")

        # Gather task information
        task_info = {
            "Task name": get_input('Task name', not_empty=True),
            "Assigned to": get_input('Assigned to', not_empty=True, username=True),
            "Date assigned": get_input('Date assigned (DD-MM-YYYY)', not_empty=True, date=True),
            "Due date": get_input('Due date (DD-MM-YYYY)', not_empty=True, date=True),
            "Task Complete? [Yes/No]": get_input('Task Complete? [Yes/No]', not_empty=True, \
                                                                            yes_no=True),
            "Task description": input('Task description: ').strip()
        }

        # Write task information to tasks.txt file
        file.write('\n'.join([f"{key}: {value}" for key, value in task_info.items()]))


def get_input(prompt, not_empty=False, username=False, date=False, yes_no=False):
    """Get input from user with optional validation."""
    while True:
        # Prompt the user for input
        user_input = input(prompt + ": ").strip()
        # Check if user wants to cancel
        if user_input == '-1':
            print("Task creation cancelled.")
            return ""
        # Check if input is empty, validation for not_empty flag
        if not user_input:
            if not_empty:
                print(f"Error: {prompt.lower()} cannot be empty.")
                continue
            return user_input
        # Check if input is a valid username, validation for username flag
        if username and not is_username_taken(user_input):
            print("Error: User does not exist. Please enter an existing user.")
            continue
        # Check if input is a valid date, validation for date flag
        if date:
            try:
                datetime.datetime.strptime(user_input, "%d-%m-%Y")
            except ValueError:
                print("Error: Invalid date format. Please enter date in DD-MM-YYYY format.")
                continue
        # Check if input is 'Yes' or 'No', validation for yes_no flag
        if yes_no and user_input.lower() not in ['yes', 'no']:
            print("Error: Please enter 'Yes' or 'No'.")
            continue
        return user_input


def view_all():
    """Display all tasks."""
    # Open tasks.txt file and display all tasks
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')
    for i, task in enumerate(tasks, start=1):
        # Print task details
        print_task(task, i)
    input("\nEnter -1 to go back to the previous menu: ")


def print_task(task, task_number):
    """Print task details."""
    # Print task number and details
    print(f"\nTask {task_number}:")
    for line in task.split('\n'):
        try:
            header, value = line.split(": ")
            print(f"{header:<25} {value}")
        except ValueError:
            print(f"Missing parameter: {line}")
    print("_" * 50)


def view_mine():
    """Display tasks assigned to the user."""
    # Prompt user for username
    username = input("Enter your username: ")
    # Check if username exists
    if not is_username_taken(username):
        print(f"Error: the username '{username}' does not exist.")
        return
    # Open tasks.txt file and display tasks assigned to the user
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')
    while True:
        # Print tasks assigned to the user
        print_tasks_assigned_to_user(tasks, username)
        # Prompt user for task selection
        choice = input("\nEnter the number of the task to select and edit: ")
        if choice.isdigit() and 1 <= int(choice) <= len(tasks):
            # Edit selected task
            edit_task(tasks[int(choice) - 1])
        elif choice == '-1':
            break
        else:
            input("Invalid input. Press Enter to continue...")


def print_tasks_assigned_to_user(tasks, username):
    """Print tasks assigned to the user."""
    # Clear screen
    os.system('cls')
    print("Enter -1 at any time to cancel current process")
    print("-" * 50)
    print(f"Tasks belonging to {username}:")
    for i, task in enumerate(tasks, start=1):
        if f"Assigned to: {username}" in task:
            # Print task details
            print_task(task, i)



def edit_task(selected_task):
    """
    Allow the user to edit the details of a selected task.

    Args:
        selected_task (str): The task to be edited, represented as a string.

    """
    # Extract the task details
    task_info = {}
    lines = selected_task.split("\n")
    for idx, line in enumerate(lines, start=1):
        header, value = line.split(": ")
        task_info[header] = value
        # Display each task detail with a corresponding number for selection
        print(f"{idx}. {line}")

    # Allow the user to edit the task
    print("Enter -1 at any time to cancel current process")
    print("-" * 50)
    print("Editing Task:")
    while True:
        # Prompt user to choose a field to edit
        edit_choice = input("Enter the number of the field to edit: ")
        if edit_choice == '-1':
            # Return to task selection if user cancels
            print("Returning to task selection.")
            break
        elif edit_choice.isdigit() and int(edit_choice) in range(1, len(lines) + 1):
            # Validate user input and update selected field with a new value
            field_number = int(edit_choice) - 1
            header, _ = lines[field_number].split(": ", 1)
            new_value = input(f"Enter new value for {header}: ")

            # Validations for specific fields
            if header == "Assigned to":
                if not is_username_taken(new_value):
                    # Ensure selected username exists
                    print("Error: User does not exist. Please enter an existing user.\n")
                    continue
            elif header in ["Date assigned", "Due date"]:
                try:
                    # Ensure entered date is in correct format
                    datetime.datetime.strptime(new_value, "%d-%m-%Y")
                except ValueError:
                    print("Error: Invalid date format. Please enter date in DD-MM-YYYY format.\n")
                    continue
            elif header == "Task Complete? [Yes/No]":
                # Ensure input is either 'Yes' or 'No'
                if new_value.lower() not in ['yes', 'no']:
                    print("Error: Please enter 'Yes' or 'No'.\n")
                    continue
            elif not new_value.strip():  # Empty field validation
                print(f"Error: {header} cannot be empty.\n")
                continue

            # Update task information with new value
            task_info[header] = new_value
            print(f"{header} updated.")
        else:
            print("Invalid input. Please enter a valid field number.\n")

    # Update the task in the tasks list and write it back to the file
    updated_task = "\n".join([f"{header}: {value}" for header, value in task_info.items()])
    tasks = []
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline
    tasks[tasks.index(selected_task)] = updated_task
    with open("tasks.txt", "w", encoding='utf-8') as file:
        file.write('\n\n'.join(tasks))


def count_tasks(task_list):
    """
    Count the number of completed, uncompleted, and
    overdue tasks in the given task list.

    Args:
        task_list (list): A list of task strings.

    Returns:
        tuple: A tuple containing the counts of completed, uncompleted, and overdue tasks.

    """
    completed = 0
    uncompleted = 0
    overdue = 0

    for task in task_list:
        task_info = {}
        for line in task.split("\n"):
            parts = line.split(": ", 1)
            if len(parts) == 2:  # Ensure it's a valid key-value pair
                key, value = parts
                task_info[key] = value
            else:
                print(f"Skipping invalid line in task: {line}")

        if task_info.get("Task Complete? [Yes/No]", "").lower() == "yes":
            completed += 1
        else:
            uncompleted += 1
            due_date = task_info.get("Due date")
            if due_date:
                try:
                    today = datetime.date.today()
                    due_date_parsed = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
                    if today > due_date_parsed:
                        overdue += 1
                except ValueError:
                    print(f"Warning: Invalid due date format for task: {task}")

    return completed, uncompleted, overdue



def generate_reports():
    """
    Generate task and user overview reports based on the tasks and users stored in files.

    Reads tasks and users from files, counts completed, uncompleted, and overdue tasks,
    calculates various statistics, and writes them into 'task_overview.txt' and
    'user_overview.txt' files.
    """
    # Read tasks from file
    with open("tasks.txt", "r", encoding='utf-8') as file:
        tasks = file.read().strip().split('\n\n')  # Split tasks by double newline

    # Count completed, uncompleted, and overdue tasks
    completed_tasks, uncompleted_tasks, overdue_tasks = count_tasks(tasks)

    # Calculate total tasks
    total_tasks = completed_tasks + uncompleted_tasks

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
            completed_user_tasks, uncompleted_user_tasks, overdue_user_tasks = \
            count_tasks(user_tasks)

            percentage_user_assigned = (total_user_tasks / total_tasks) * 100 \
            if total_tasks > 0 else 0
            percentage_user_completed = (completed_user_tasks / total_user_tasks) * 100 \
            if total_user_tasks > 0 else 0
            percentage_user_uncompleted = (uncompleted_user_tasks / total_user_tasks) * 100 \
            if total_user_tasks > 0 else 0
            percentage_user_overdue = (overdue_user_tasks / uncompleted_user_tasks) * 100 \
            if uncompleted_user_tasks > 0 else 0

            file.write(f"User: {user}\n")
            file.write(f"Total tasks assigned: {total_user_tasks}\n")
            file.write(f"Percentage of total tasks: {percentage_user_assigned:.2f}%\n")
            file.write(f"Percentage completed: {percentage_user_completed:.2f}%\n")
            file.write(f"Percentage to be completed: {percentage_user_uncompleted:.2f}%\n")
            file.write(f"Percentage overdue: {percentage_user_overdue:.2f}%\n\n")


def display_statistics():
    """
    Display statistics from task_overview.txt and user_overview.txt files.

    Reads statistics from the 'task_overview.txt' and 'user_overview.txt' files, and displays them
    to the user.
    If the files are not found, prompts the user to generate the statistics files.

    The user must provide their username to access the statistics. Only users with the username
    'admin' are allowed to view the statistics.
    """
    while True:
        os.system('cls')  # Clear screen before continuing
        print("Enter -1 at any time to cancel current process")
        print("-" * 50)
        print("")
        # Check if the user is admin
        username = input("Enter your username: ").strip()
        if username == "-1":
            break
        elif username != "admin":
            print("Access denied. You must be the admin to view statistics.")
            input("Press Enter to continue...")
            continue

        # Display task_overview.txt
        task_file_path = "task_overview.txt"
        user_file_path = "user_overview.txt"

        try:
            with open(task_file_path, "r", encoding='utf-8') as task_overview_file:
                print("\nTask Overview\n-------------\n")
                print(task_overview_file.read())
        except FileNotFoundError:
            print(f"Error: {task_file_path} not found.")
            generate = input("Do you want to generate the statistics files now? (yes/no): ").lower()
            if generate == "yes":
                generate_reports()
                input("Press Enter to continue...")
                continue  # Restart the function
            else:
                input("Press Enter to continue...")

        # Display user_overview.txt
        try:
            with open(user_file_path, "r", encoding='utf-8') as user_overview_file:
                print("\nUser Overview\n------------\n")
                print(user_overview_file.read())
        except FileNotFoundError:
            print(f"Error: {user_file_path} not found.")
            generate = input("Do you want to generate the statistics files now? (yes/no): ").lower()
            if generate == "yes":
                generate_reports()
                input("Press Enter to continue...")
                continue  # Restart the function
            else:
                input("Press Enter to continue...")

        input("Press Enter to continue...")
        break
