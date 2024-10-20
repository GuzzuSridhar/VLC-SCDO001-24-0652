in_str = input("Enter a String: ")

# get the reverse string
rev_str = ""
idx = len(in_str) -1
while idx >= 0:
    rev_str += in_str[idx]
    idx -= 1
if in_str.casefold() == rev_str.casefold():
    print(f"{in_str = } is a palindrome")
else:
    print(f"{in_str = } is not a palindrome")




