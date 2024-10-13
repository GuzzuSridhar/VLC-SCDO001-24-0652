#  Accepting the information about the user.
name = input("Whats your name? ")
age = int(input("Whats your age? "))

# print the details using fstring
print(f'Hello {name}!, you are {age} years old')

# using multiple fstrings
# using fstring to create a string (text)
greetings = f"Hello {name}!," f"you are {age} years old"
print(greetings)

# debugging using fstring
# usual code written as in other programming languages
print("Age: ", age)
print("Name: ", name)

# using fstring to print such debug statements
print(f"{age = }")
print(f"{age+10 = }")
print(f"{name = }")
