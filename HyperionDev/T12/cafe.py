import re

# Designing the very varied menu.
menu = ["Toastie", "Grilled Cheese", "Croque Monsieur", "Jaffle", "Panini"]

# Taking stock of menu items from input, creating a dict based of "menu" list.
stock = {i: float(input(f"Enter the amount of \"{i}\" we have in stock:\n>")) for i in menu}
print("\n", stock, "\n")

# Taking price of each menu item from input, creating a second dict based of "menu" list.
# Using strip method to clean up input.
price = {i: float(re.sub(r'[^0-9.]', "", (input(f"Enter the price of \"{i}\":\n>").strip()))) for i in menu}
print("\n", price, "\n")

# Calculating the total value of the entire stock,
total_stock = round(sum(stock[val] * price[val] for val in stock), 2)
print(total_stock)
