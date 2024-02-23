# Open the file and add content to variable
with open("DOB.txt", "r") as file:
    persons = file.readlines()

    # Create empty lists to store names and birthdates
    names = []
    dobs = []

    # Split each line into separate parts
    for line in persons:
        parts = line.split()

        # Separate names and birthdates into separate variables
        name = " ".join(parts[:2])
        dob = " ".join(parts[2:])

        # Add each name and birthdate to respective lists
        names.append(name)
        dobs.append(dob)

    # Format each list for presentation
    f_names = "\n".join(names)
    f_dobs = "\n".join(dobs)

    # Display result
    print(f"\nNames:\n{f_names}\n\nBirthdates:\n{f_dobs}")
    