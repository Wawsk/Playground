# This program uses static numbers in order to represent the exact pattern presented in the Practical Task description.

# Start the for loop.
# Range determines the number of rows.
for number_of_rows in range(1, 10):
    # Using the min function to find the smallest value and choose between (number_of_rows) and (10 - number_of_rows)
    number_of_stars = "*" * min(number_of_rows, 10 - number_of_rows)
    # at number_of_rows = 6, (10 - number_of_rows) becomes the smaller value
    print(number_of_stars)


# I have been looking through the built in functions in python and thought of using this method to print this pattern.
# I hope this is okay!
# Thanks!