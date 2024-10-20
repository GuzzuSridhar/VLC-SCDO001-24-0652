
#  simple loop

# declare a loop variable
count = 0

# exit condition (count = 10)
while count < 10:
    # increment the loop variable
    count += 1
    print("Count", count)
# print(f"{count = }") 

print("--------------------------")

# sample 2 (reverse)
while count > 0:
    print(f"{count = }")
    count -= 1


# loops on strings

#  access the characters in a string

# name = "Alex"
name = input("Enter your name: ")
str_idx = 0
while str_idx < len(name):
    print(name[str_idx], end="")
    str_idx += 1

print()

# reverse of a string
str_idx = len(name) -1
while str_idx >= 0:
    print(name[str_idx], end = "")
    str_idx -= 1 

