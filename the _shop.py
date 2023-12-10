import time

# Dictionary containing inventory in The Shop
inventory = {
    "Swords": {"Mithril": 325, 
               "Steel": 85, 
               "Iron": 38, 
               "Wooden": 12
},
    "Bows": {"Stick": 25, 
             "Oak": 90, 
             "Elvish": 130, 
             "World Tree": 2020
},
}
# Defining functions:
# Converts inventory items value from copper coins to silver and gold.
def coin_conversion():
    for key, value in items.items():
        if value > 100:
            value /= 100
            print(f"\n{key} {sub_choice}, {value} Gold coins")
        elif 10 < value < 100:
            value /= 10
            print(f"\n{key} {sub_choice}, {value} Silver coins")
        else:
            print(f"\n{key} {sub_choice}, {value} Copper coins")


# Texts:
# Welcome message
MAIN_MENU = f"""{50 * "~ "}
Welcome to The Shop!

We are supplying all manner of adventuring goods, please browse at your leisure. 
You can use this enchanted tome to perform a variety of functions. Just write down
a number or one of the following options and the tome will take you to the next page."""

# Interaction with the global while loop
MAIN_MENU_OPTIONS ="""
    1. Search (Searches categories, not individual items)
    2. Browse
    3. Basket WIP
    4. Requests WIP
    5. Information WIP"""

# Repeating browsing message
BROWSING = "\nHere is what we have for sale...\n"



# Main menu while loop
print(MAIN_MENU)
while True:
    print(MAIN_MENU_OPTIONS)
    time.sleep(1)
    menu_choice = input("\n\t> ").lower()
    time.sleep(1)

    # Allows searching specific items
    if menu_choice == "1" or menu_choice == "search":
        print("\nWhat are you looking for?\n  -Swords\n  -Bows\n")
        sub_choice = input("> ").capitalize()
        time.sleep(1)
        if sub_choice in inventory:
            print("\nWe offer:\n")
            time.sleep(1)
            for item in inventory[sub_choice].keys():
                print(f"- {item} Swords")
        elif sub_choice not in inventory:
            print("Not in the inventory")
            time.sleep(1)





    # Allows browsing the inventory dictionary
    elif menu_choice == "2" or menu_choice == "browse":
        sub_choice = input("""\nWhat item are you looking for?
                            
We offer a range of Swords, Bows etc...
Write it down to continue.
                           
    > """).capitalize()
        time.sleep(2)
        while True:
            if "Sword" in sub_choice:
                items = inventory["Swords"]
                print(BROWSING)
                coin_conversion()
                time.sleep(1)
                item_choice = input("\nWrite down what you would like to add:\n> ").capitalize()
                if item_choice in items:
                    print("yay") # This is where adding a item to basket goes.
                break
            elif "Bow" in sub_choice:
                items = inventory["Bows"]
                print(BROWSING)
                coin_conversion()
                time.sleep(1)
                item_choice = input("\nWrite down what you would like to add:\n> ").capitalize()
                if item_choice in items:
                    print("yay") # This is where adding a item to basket goes.
                break
            else:
                print("We don't have that in stock, try again...")
                sub_choice = input("""\nWhat item are you looking for?
        Write it down to continue or write exit to go back.
        > """)






# elif menu_choice == "3" or menu_choice == "browse":
#     print("yay for 3")
# elif menu_choice == "4" or menu_choice == "requsts":
#     print("yay for 4")
# elif menu_choice == "5" or menu_choice == "":
#     print("yay for 5")
# else:
#     print("Wrong choice! Try again...")




