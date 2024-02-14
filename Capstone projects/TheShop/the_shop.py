
from inventory import weapons
import time

# Defining classes:
class ItemSearch:
    def __init__(self, inventory):
        self.inventory = inventory

    def browse_items(self, category):
        items = self.inventory.get(category, [])
        if not items:
            print("We don't have that in stock. Try again?")
            return

        print(f"Browsing items in {category}..."
              f"\n{category} made out of what material?\n{TILDE}\n")
        item_choice = input(">>> ")

        if any(item_choice == item["name"] for item in items):
            selected_item = next(item for item in items if item["name"] == item_choice)
            self.display_item_stats(selected_item)
            time.sleep(2)
        else:
            print("Item not found in the inventory.")

    def display_item_stats(self, item):
        print("\nItem Stats:")
        for key, value in item.items():
            if key == "cost":
                value = coin_conversion(item)
                continue
            print(f"{key.capitalize()}: {value}")

# Reuse the ItemSearch class
searching = ItemSearch(weapons)

# Defining functions:
def coin_conversion(item):
    # Converts item value to coins
    value = item["cost"]
    gold = value // 100
    silver = (value % 100) // 10
    copper = value % 10

    result = []
    if gold > 0:
        result.append(f"{gold} Gold")
    if silver > 0:
        result.append(f"{silver} Silver")
    if copper > 0:
        result.append(f"{copper} Copper")
    
    print("Cost:", ", ".join(result))

def coin_rev_conversion ():
    # Converts coins into total value
    gold = int(input("Enter Gold value:\n>>> "))
    silver = int(input("Enter Silver value:\n>>> "))
    copper = int(input("Enter Copper value:\n>>> "))
    cost = (gold * 100 + silver * 10 + copper)


# Texts:
# Separator
TILDE = '~ ' * 35

# Welcome message
MAIN_MENU = f"""{TILDE}
Welcome to The Shop!

  We are supplying all manner of adventuring goods, please browse
at your leisure. You can use this enchanted tome to perform a
variety of functions. Just write down a number or one of the
following options and the tome will take you to the relevant page."""

# Interaction with the global while loop
MAIN_MENU_OPTIONS =f"""
  1. Inventory (View our stock)
  2. Search (Search for a specific item)
  3. Basket WIP
  4. Requests WIP
  5. Information WIP
  6. Wallet / Conversion WIP
 {TILDE}"""

# Repeating browsing message
BROWSING = "\nHere is what we have for sale...\n"
SEARCH_SUB = f"""\nWhat type of an item are you looking for?
Select one of the categories:
  - Swords
  - Bows
  - Axes
or
  - Exit to go back to the previous page
{TILDE}"""


# Main menu while loop
print(MAIN_MENU)
while True:
    print(MAIN_MENU_OPTIONS)
    menu_choice = input(">>> ").lower()

    # Allows searching specific items
    while menu_choice == "1" or menu_choice == "inventory":
        print(SEARCH_SUB)
        sub_choice = input(">>> ").capitalize()
        
        if sub_choice == "Exit":
            break
        elif sub_choice not in weapons:
            print("We don't sell that... Select one of the provided options")
        elif sub_choice in weapons:
            category_name = sub_choice
            print("\nWe offer:\n")
            for item in weapons[sub_choice]:
                print(f"- {item['name']} {sub_choice}")
            print("\n", TILDE)
            time.sleep(1)



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