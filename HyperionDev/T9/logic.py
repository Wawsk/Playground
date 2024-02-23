# Use this code to find the highest number within a list

# Defining variables
numbers = [2, 7, 3, 25, 13, 11]
max_num = 0
i = 0

# Loop comparing each number from list to the current highest number
while i < len(numbers):
    if numbers[i] > max_num:
        max_num += numbers[i]
    i += 1

# Displays the result
print(f"The maximum value is: {max_num}")




# Did you spot the error? :)
# It's located on line 11.
