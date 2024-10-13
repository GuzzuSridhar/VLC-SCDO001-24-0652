# decalre a string
message = "hello, Python is fun"

print(f"{message = }")
print("----------------------")
# 1. len function which is built in and can be used for other types as well
print(f"{len(message) = }")

# 2. captalize methods
# first character of the text is capital (upper case), and rest is lower
print(f"{message.capitalize() = }")

# 3. upper methods
print(f"{message.upper() = }")

# lower methods
print(f"{message.lower() = }")

# 4. title methods
print(f"{message.title() = }")

# 5. swapcase methods
print(f"{message.swapcase() = }")

# 6. casefold methods
# the same can be done using the lower function as well
my_name = "ALEX"
your_name = "alEx"
print(f"{my_name.casefold() = }")
print(f"{your_name.casefold() = }")

# 7. strip
#  remove white spaces (leading and trailing)
message = "        hello            "
print(f"{len(message) = }")
# nesting of methods and functions
print(f"{len(message.strip()) = }")

# 8. split
# returns a list of all words in the text
message = "hello, Python is fun"
print(f"{message.split() = }")

# 9. isdigit
temp = "test"
print(f"{temp.isdigit() = }")
temp = "123"
print(f"{temp.isdigit() = }")

# example
age = input("Whats your age: ")
print(f"{age.isdigit() = }")

# 10. isalnum
# check for alphanumeric data
test = "abcefg77!!"
print(f"{test.isalnum() = }")

# center
test = "Hello"
print(test.center(50))
print(test.center(20))

# character index in a string
test = "Hello"
# to access a specific character using the index
# the first character
print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])

# using negative index
print(test[-1])
print(test[-2])
print(test[-3])
print(test[-4])
print(test[-5])

# using sep
print(test[0], test[1],test[2],test[3],test[4], sep="")

# using end
print(test[0], end="")
print(test[1], end="")
print(test[2],end="")
print(test[3],end="")
print(test[4])

# string methods with index
# find returns the index of the search text
# when no match return -1
test = "Hello World"
print(f"{test.find("Hello") = }") 
print(f"{test.find("World") = }") 
print(f"{test.find("world") = }") 
print(f"{test.lower().find("world") = }") 

# index returns the index of the search text 
# when no match return a Value error
print(f"{test.index("Hello") = }") 
print(f"{test.index("World") = }") 
# print(f"{test.index("world") = }") 

# replace
msg = test.replace("Hello", "Bye")
print(msg)







