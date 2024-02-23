 # Importing the math module.
import math

# Displaying the welcome message and description.
print('''investment\t- to calculate the amount of interest you'll earn on your investment.
bond\t\t- to calculate the amount you'll have to pay on a home loan.

Enter either 'investment' or 'bond' from the menu above to proceed''')

# User determines which part of the code to execute.
# Changing the variable to lowercase to accomodate user capitalization.
user_selection = input(">").lower()

# Start of the if statements.
if user_selection not in ("investment", "bond"):    # Incorrect input error handling.
    print("\nNot a valid option selected, please try again.\n")

# Executes this part of the code if the user input states "investment".
elif user_selection == "investment":
    # Taking details from the user, tripping potential special characters
    # and converting strings to floats to accomodate decimal number input.
    deposit_amount = (input("\nEnter the amount you would like to deposit:\n> ").strip("£$¥€,"))
    deposit_amount = float(deposit_amount)
    interest_rate = (input("\nEnter the interest rate:\n> ").strip("%"))
    interest_rate = float(interest_rate) / 100  # Dividing by 100 to make use in calculations
    deposit_length = (input("\nEnter the number of years you plan on investing:\n> ").lower().strip("years"))
    deposit_length = float(deposit_length)

    # User determines calculation type.
    # Changing the variable to lowercase to accomodate user capitalization.
    interest = input("\nIs it a 'simple' or 'compound' interest rate?\n> ").lower() 

    # Continuing the "investment" part of the code within a nested if statement.
    if interest == "simple":    # Executes this part of the code if the user input states "simple".
        # Calculating and rounding displaying the interest and total amount of investment.
        total_amount = deposit_amount * (1 + interest_rate * deposit_length)
        print(f"\nThe amount you will have at the end of your {int(deposit_length)} year(s) will be: {round(total_amount, 2)}")

    elif interest == "compound":    # Executes this part of the code if the user input states "compound".
        # Calculating, rounding and displaying the interest and total amount of investment. 
        total_amount = deposit_amount * math.pow((1 + interest_rate), deposit_length)
        print(f"\nThe amount you will have at the end of your {int(deposit_length)} year(s) will be: {round(total_amount, 2)}")

# Executes this part of the code if the user input states "bond".
elif user_selection == "bond":
    # Taking details from the user, stripping potential special characters,
    # and converting strings to floats to accomodate decimal number input.
    house_vaule = (input("\nEnter the present value of the house:\n> ").strip("£$¥€,"))
    house_vaule = float(house_vaule)
    interest_rate = (input("\nEnter the interest rate:\n> ").strip("%"))
    interest_rate = float(interest_rate) / 100  # Dividing by 100 to make use in calculations
    bond_length = (input("\nEnter the number of months to repay the bond:\n> ").lower().strip("months"))
    bond_length = int(bond_length)

    # Calculating and displaying monthly repayment value
    repayment = ((interest_rate / 12) * house_vaule) / (1 - (1 + interest_rate/12) ** (- bond_length))
    print(f"\nThe monthly payments you can expect to pay are: {round(repayment, 2)}")


print('\033[1m' + "\n\nThank you for using WawTech Software!\n")
