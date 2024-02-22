# the_shop.py
import os
import time
from inventory import weapons
from text_variables import *
from the_shop_functions import *

# Main menu while loop
os.system("cls")
while True:
    print(MAIN_MENU)
    print(MAIN_MENU_OPTIONS)
    menu_choice = input(">>> ").lower()

    # Allows searching specific items
    while menu_choice == "1" or menu_choice == "inventory":
        os.system("cls")
        print(SEARCH_SUB)
        for index, category in enumerate(weapons.keys(), start=1):
            print(f"  {index}. {category}")
        print("  0. Exit")
        print(TILDE)
        category_choice = input("What type of an item are you looking for?\n>>> ")
        
        if category_choice == "0":
            os.system("cls")
            break
        try:
            category_index = int(category_choice) - 1
            categories = list(weapons.keys())
            sub_choice = categories[category_index]
            category_name = sub_choice
            print(f"{TILDE}\nWe offer:\n")
            for index, item in enumerate(weapons[sub_choice], start=1):
                print(f"  {index}. {item['name']} {sub_choice}")
            print("\n", TILDE)
            while True:
                try:
                    item_choice = int(input("Enter the number of the item for more details (or 0 to go back):\n>>> "))
                    if item_choice == 0:
                        break
                    selected_item = weapons[sub_choice][item_choice - 1]
                    searching.display_item_stats(selected_item)
                except (ValueError, IndexError):
                    print("We don't sell that here... Select one of the provided options.")
                time.sleep(2)
        except (ValueError, IndexError):
            print("We don't sell that here... Select one of the provided options.")



    # Allows browsing the inventory dictionary
    while menu_choice == "2" or menu_choice == "search":
        sub_choice = input(f"{SEARCH_SUB} \n>>> ").capitalize()
        while True:
            if sub_choice == "Exit":
                break
            elif sub_choice in weapons:
                searching.browse_items("Swords")
                print("\n", TILDE)
                break
        break





# elif menu_choice == "3" or menu_choice == "browse":
#     print("yay for 3")
# elif menu_choice == "4" or menu_choice == "requsts":
#     print("yay for 4")
# elif menu_choice == "5" or menu_choice == "":
#     print("yay for 5")
# else:
#     print("Wrong choice! Try again...")




""" To-Do 

Change "Search" option to what's in option 1 code.
Let Browse show all dictionaries to display all the inventory
Finish inventory
Add being able to add to a basket


"""