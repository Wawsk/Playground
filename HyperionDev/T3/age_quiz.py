# Creating a variable from user input and converting it to an integer
age = int(input("Please enter your age.\n> "))

# Creating the if statements
if (age > 100):       # If age over 100
    print("Sorry, you're dead.")
elif (age >= 65):       # If age equal or over 65
    print("Enjoy your retirement!")
elif (age >= 40):   # If age between 40 and 64
    print("You're over the hill.")
elif (age == 21):       # If age equal to 21
    print("Congrats on your 21st!")
elif (age < 13):        # If age under 13
    print("You qualify for the kiddie discount.")
else:                   # Any other input
    print("Age is but a number.")