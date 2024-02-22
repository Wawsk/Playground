# text_variables.py

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
SEARCH_SUB = f"""{TILDE}
What type of an item are you looking for?
Select one of the categories:
{TILDE}"""