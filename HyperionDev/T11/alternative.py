# Create initial strings

string_1 = "Hello World"
string_2  = "I am learning to code"


# Capitalising every second character in a string
result1 = ""
for index, character in enumerate(string_1):
    if index % 2 == 0:
        result1 += character.upper()
    else:
        result1 += character
print(f"\nResult with 'enumerate':\n{result1}\n")

# Alternative without enumerate
result2 = ""
for i in range(len(string_1)):
    if i % 2 == 0:
        result2 += string_1[i].upper()
    else:
        result2 += string_1[i]
print(f"\nAlternative method without 'enumerate':\n{result2}\n")

# Alternative using slicing
result3 = string_1[0] + "".join([
character.upper() if index % 2 == 1 else character for index, character in enumerate(string_1[1:])
])
print(f"\nAlternative using slicing:\n{result3}\n")

# Capitalising every second word in a string
result4 = []
split = string_2.split(" ")
for index, word in enumerate(split):
    if index % 2 == 0:
        result4.append(word.upper())
    else:
        result4.append(word)
print("Capitalising every second word in a string:\n"+" ".join(result4))
