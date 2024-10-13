# decalre a string
message = "hello, Python is fun"

print(f"{message = }")
print("----------------------")
# 1. len
print(f"{len(message) = }")

# 2. captalize
# first character of the text is capital (upper case), and rest is lower
print(f"{message.capitalize() = }")

# 3. upper
print(f"{message.upper() = }")

# lower
print(f"{message.lower() = }")

# 4. title
print(f"{message.title() = }")

# 5. swapcase
print(f"{message.swapcase() = }")

# 6. casefold
# the same can be done using the lower function as well
my_name = "ALEX"
your_name = "alEx"
print(f"{my_name.casefold() = }")
print(f"{your_name.casefold() = }")



