# Displaying a welcome message.
print("Choose a number, any number! Should you enter the correct number, the pogram will stop and you will have won!")

user_input = 0                      # Creating an empty variable for user input
averages_list = []                  # And an empty list for collecting user inputs.

# Starting the while loop
while user_input != -1:
    user_input = int(input("\n> "))     # Continues asking for user input.
    if user_input == -1:                # Once desired number chosen, stops loop.
        break
    else:                                   # If not the desired number,
        averages_list.append(user_input)    # Adds input to list.
        print("Nope. Try again!")

# Announcing the end of the game
if user_input == -1:
    print("That's the one! Congrats, you win!\nIt only took you...", len(averages_list), "tries! Good effort!\n")


# Displaying the average of the numbers entered
print("The average of the numbers entered is:\n>", sum(averages_list) / len(averages_list))

print('\033[1m' + "\n\nThank you for using WawTech Software!\n")


# A version without the nested for loop:

# Displaying a welcome message.
print("Choose a number, any number! Should you enter the 'correct' number, the pogram will stop and you will have won!")

user_input = int(input("\n> "))     # Creating a number variable with user input,
averages_list = []                  # and an empty list for collecting user input.

# Starting the while loop
while user_input != -1:
    print("Nope. Try again!")
    averages_list.append(user_input)       # Adds input to list
    user_input = int(input("\n> "))        # Continues asking for input

# Announcing the end of the game
if user_input == -1:
    print("That's the one! Congrats, you win!\nIt only took you...", len(averages_list), "tries! Good effort!\n")


# Displaying the average of the numbers entered
print("The average of the numbers entered is:\n>", sum(averages_list) / len(averages_list))