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

# Aligning strings without using fstring
print("Name".center(30),"Age".center(5),"City".center(15))
print("Alex".center(30),"45".center(5),"Kl".center(15))
print("David".center(30),"35".center(5),"Singapore".center(15))

# Aligning strings  using fstring
print(f"{'name':<30} | {'age':<5} | {'City':<20} |")
print(f"{'name':>30} {'age':>5} {'City':>20}")
print(f"{'name':^30} {'age':^5} {'City':^20}")

# using custom character to fill spaces
print(f"{'name':-^30} {'age':-^5} {'City':-^20}")
print(f"{'name':*^30} {'age':*^5} {'City':*^20}")





