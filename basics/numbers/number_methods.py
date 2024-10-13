# number methods
import math
import random
# abs
# ensures that the output is always positive
print(f"{abs(-7) = }")

earnings = 1000
deductions = 250
# net = earnings- deductions
net = deductions -earnings 
print(abs(net))

# int
price = 7.71
print(int(price))

# float
qty = 9
print(float(qty))

# round
#  Rounds a number to the nearest integer or to a given number of decimal places.
# rounds to the nearest integer, with .5 rounding to the nearest even integer.
print(round(4.6))         # Output: 5
print(round(4.5))         # Output: 4 (rounds to nearest even number)
print(round(4.567, 2))    # Output: 4.57 (rounds to 2 decimal places)

# ceil
# Rounds a number up to the nearest integer (always up).
print(math.ceil(4.1))     # Output: 5
print(math.ceil(4.9))     # Output: 5

# floor
# Rounds a number down to the nearest integer (always down).
print(math.floor(4.1))    # Output: 4
print(math.floor(4.9))    # Output: 4

# random number
# random int  between 0 and 1
print(f"{random.random() = }")
# random float
print(f"{random.uniform(1.3,4.5) = } ")
# random int
print(f"{random.randint(1,100) = }")



