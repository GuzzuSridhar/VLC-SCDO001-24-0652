# used to assing value to a variable
# Example
# age = 45
# in the case above the assignment operator was "="

# list of assignment operators
# equals -- = (works with all types)
# plus equals -- += (works with numbers and string)
# minus equals -- -= (works with numbers only)
# multiply equals -- *= (works with numbers only)
# divide equals -- /= (works with numbers only)
# modulo equals -- %= (works with numbers only)

# equals
age = 10
name = "Alex"
price = 99.7
is_valid = True

#-------------------- plus equals operator------------------------------
count = 10
# add one to count (11)
count += 1 
print(count)
# add 5 to count
count += 5
print(count)

# with strings
msg = "Hello! "
# using the += on strings
msg += "Alex"
print(msg)

#-------------------- minus equals operator------------------------------
# can be applied only to numbers
count -= 1
print(count)
count -= 5
print(count)

#-------------------- product equals operator------------------------------
# can be applied only to numbers
count *= 10
print(f"{count = }")

#-------------------- division equals operator------------------------------
# can be applied only to numbers
# will return the quotient after the division
print(type(count))
count /= 10 
# converts the int type to float after division operation
print(f"{count = }")
print(type(count))

#-------------------- modulus equals operator------------------------------
# can be applied only to numbers
# will return the reminder after division
x = 5
x %= 2
print(x)




