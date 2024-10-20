# break
#  exit the loop when encountered

# simple number print
x = 1
while x <= 10:
    print(x)
    if x == 5:
        break
    x += 1


print("--------------------------")
#  continue statement
#  skip the current iteration
x = 1
while x <= 10:
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1

print("--------------------------")


# # example of break with vowel find
in_str = input("Enter a string: ")
x = 0
is_Vowel = False
vowels = ["a", "e", "i", "o", "u"]
while x < len(in_str):
    if in_str[x] in vowels:
        is_Vowel = True
        break
    x += 1

if is_Vowel:
    print(f"{in_str} contains vowel")
else:
    print(f"{in_str} does not contains vowel")