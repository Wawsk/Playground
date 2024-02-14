"""This is the main program for task_manager.
Displaying the menu and handling menu options."""

from functions import (
    main_menu,
    reg_user,
    add_task,
    view_all,
    view_mine,
    generate_reports
)

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
