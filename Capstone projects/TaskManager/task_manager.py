"""Main program for task_manager.
Displaying the menu and handling menu options."""

from functions import (
    main_menu,
    reg_user,
    add_task,
    view_all,
    view_mine,
    generate_reports,
    display_statistics
)

while True:
    main_menu()
    user_input = input("Enter your selection: ").lower()
    options = {
        'r': reg_user, 'a': add_task, 'va': view_all,
        'vm': view_mine, 'gr': generate_reports, 'ds': display_statistics
        }
    if user_input in options:
        options[user_input]()
    elif user_input == 'e':
        break
    else: 
        print("Invalid selection. Please try again.")
