INFO = """
This program will help you create a document to register
students at the exam venue. Please enter how many
students will attend the exam first (You will be able
to add additional students by running the program again).
Enter each student's ID number afterwards.
"""

print(INFO)

# Argument type check before iterating.
while True:
    student_count = input("Number of students registering for the event:\n> ")

    if student_count.isnumeric():
        student_count = int(student_count)
        break
    else:
        print("Enter a numeric value")

# Creating and editing the text file. Using append mode
# to allow additional entries.
with open("reg_form.txt", "a+", encoding="utf-8") as file:
    for i in range(student_count):
        student_id = input("Enter student ID:\n> ")
        file.write(student_id + "\t" + 30*"." + "\n\n")
