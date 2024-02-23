# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"   ### Runtime error, undefined variable.
animal_type = "cub"
number_of_teeth = 16

### Logical error, missing fstring
### Logical error, wrong placement of variables
### Renamed variable to avoid Runtime error in the following print statement
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 


print (full_spec)       ### Syntax error, missing parentheses
                        ### Runtime error, undefined variable full_spec, likely referring to ll_spec from previous step

