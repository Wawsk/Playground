# This program is intended to succesfully fail to divide a number 50 by a range of numbers

counter = 0 
while counter < 9  # Compilation, Syntax error, "while" statement is missing a colon.
print("This program will successfully fail") # Compilation Indentation error, missing indentation after "while" statement.

    for number in range(0, 10): 
        result = 50 / number # Runtime, Zero Division Error due to the range starting at 0, cannot divide numbers by 0!
        print(f"{number} divided by 2 is {round(number, 1)}") # Logical error, used "number" instead of "result"
        counter += 1

