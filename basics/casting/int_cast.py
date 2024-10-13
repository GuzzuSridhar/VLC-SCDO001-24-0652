# int(x): Converts x to an integer. If x is a float, it truncates the decimal part.
# Only works on valid numbers or strings that represent integers; otherwise, it raises an error.

# float to int
int_val = int(6.55)
print(int_val)

# string to int
# the string should be a valid number representation
int_val = int("67")
print(type(int_val))
print(int_val)

# boolean to int
int_val = int(True)
print(int_val)
int_val = int(False)
print(int_val)

