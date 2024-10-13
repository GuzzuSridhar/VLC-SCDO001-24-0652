# Declaration of strings

# write a string using
# double quote
# single quotes
# docstrings
# fstrings (same as backtics in JS)

# using double quotes
greting = "Hello"
msg = "Alex's house is near by"
print(msg)
# using single quotes
greting = 'Hello'
quote ='is is said that "Python is Fun"'
print(quote)

# using the fstring
name = "Alex"
age = 25
# default print stmt
print("Hello,", name)
# using fstrings
print(f"Hello, {name}")
message = f'Hello, {name}'
print(message)

# using multiple datatypes (concat)
print("Hello "+name+ " you are "+ str(age) + " years old.")

# fstring does implicit type conversion
print(f"Hello, {name}, you are {age} years old")

# docstring
# use triple quotes
# used for documenting
# can be used using the help() function
# does not have any effect on the code
'''
This is a file used to demostrate the usage of strings
'''
