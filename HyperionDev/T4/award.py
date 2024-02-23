# Displaying a welcome message.
print("""Hello! This program will help determine your qualification time. 
Simply enter your times in the following prompts:""")

# Creating variables for swimming, cycling and running times from taking user input, 
# and converting them to an integer.
swimming_time = int(input("Enter the time it took you to finish the swimming event.\n> "))
cycling_time = int(input("Enter the time it took you to finish the cycling event.\n> "))
running_time = int(input("Enter the time it took you to finish the running event.\n> "))

# Combining the variables into total time
total_time = swimming_time + cycling_time + running_time

# Displaying the total for user reference
print("The total amount of time it took you to complete the triathlon is", total_time, "minutes.")

if (total_time >= 111):
    print("It's more than 10 minutes off from the qualifying time. No award.")
elif (total_time > 105):
    print("It's within 10 minutes of the qualifying time. Provincial Scroll award.")
elif (total_time > 100):
    print("It's within 5 minutes of the qualifying time. Provincial Half Colours award.")
else:
    print("It's within the qualifying time. Provincial Colours award.")
