# bool(x): Converts x to a boolean.
# bool() returns False for None, 0, 0.0, '', [], 
# and other empty values. All other values are considered True.

# int to boolean
bool_val = bool(-100)
print(bool_val)
bool_val = bool(0)
print(bool_val)

# float to boolean
bool_val = bool(10.5)
print(bool_val)
bool_val = bool(0.0)
print(bool_val)

# String to Boolean
bool_val = bool("Something")
print(bool_val)
bool_val = bool("")
print(bool_val)