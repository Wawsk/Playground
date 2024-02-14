
from functions import *

def main_menu():
    print("Welcome to the Task Manager!")
    print("Select an option:")
    print("r - Register a user")
    print("a - Add a new task")
    print("va - View all tasks")
    print("vm - View my tasks")
    print("gr - Generate reports")
    print("ds - Display statistics")
    print("q - Quit")

while True:
    main_menu()
    user_input = input("Enter your selection: ").lower()
    if user_input == 'r':
        reg_user()
    elif user_input == 'a':
        add_task()
    elif user_input == 'va':
        view_all()
    elif user_input == 'vm':
        view_mine()
    elif user_input == 'gr':
        generate_reports()
    # elif user_input == 'ds':
    #     display_statistics()
    elif user_input == 'e':
        break
    else:
        print("Invalid selection. Please try again.")