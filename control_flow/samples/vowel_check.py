#count number of vowels in a string
in_str = input("Enter a string: ")
vowel_count = 0
idx = 0
while idx < len(in_str):
    if in_str[idx] in "aeiouAEIOU":
        vowel_count += 1
    idx += 1
print(f"There are {vowel_count} vowels in {in_str}")

# in_str = input("Enter a string: ")
new_str= ""
idx = 0
while idx < len(in_str):
    if in_str[idx] not in "aeiouAEIOU":
        new_str += in_str[idx]
    idx += 1
print(f"There are {len(in_str)-len(new_str)} vowels in {in_str}")

# is_str = input("Enter your is_str: ")
x = 0
is_Vowel = False
vowels = ["a", "e", "i", "o", "u"]
while x < len(in_str):
    if in_str[x] in vowels:
        is_Vowel = True
    x += 1

if is_Vowel:
    print(f"{in_str} contains vowel")
else:
    print(f"{in_str} does not contains vowel")

# is_str = input("Enter your is_str: ")
x = 0
is_Vowel = False
vowels = [97, 101, 105, 111 , 117]
while x < len(in_str):
    if ord(in_str[x]) in vowels:
        is_Vowel = True
    x += 1

if is_Vowel:
    print(f"{in_str} contains vowel")
else:
    print(f"{in_str} does not contains vowel")