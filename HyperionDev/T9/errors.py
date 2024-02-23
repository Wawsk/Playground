# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")  ### Syntax error, missing parenthesis
print ("\n")    ### Syntax error, missing parenthesis
                ### Logical error, incorrect indentation

                ### For the above print functions, can reduce it to a single line of code:
                ### print ("Welcome to the error program\n\n") # for the same effect

# Variables declaring the user's age, casting the str to an int, and printing the result
    ### Block of code indented unnecessarily, Logical error
age_str = "24"          ### Syntax error, incorrect symbol used to declare a variable
                        ### Not an error, but lowercase_Uppercase used to name string instead of lowercase_underscore
age = int(age_str)      ### Cannot convert to an integer, "years old" removed from age_str, Runtime error

### Above block overly complex, could DRY it by using:
### age = 24
### As it automatically becomes an integer

print("I'm", age,"years old.") ### Runtime error, cannot use + symbol to print an integer. Can use , or fstring

# Variables declaring additional years and printing the total years of age
years_from_now = 3    ### Logical error, variable value is a string instead of integer
total_years = age + years_from_now

print ("The total number of years: ", total_years)    ### Syntax error, missing parenthesis
                                                            ### Logical error, "answer_years" in quotes, wrong variable
                                                            ### Also use comma instead of +

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6     ### Runtime error, variable total not defined, likely meant to be total_years
                                        ### Logical error, missing the addition of 6 months stated in the final print statement
print ("In 3 years and 6 months, I'll be ", total_months, " months old")  ### Syntax error, missing parenthesis

#HINT, 330 months is the correct answer

