# the_shop_functions.py

import time
from inventory import *
from text_variables import *

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