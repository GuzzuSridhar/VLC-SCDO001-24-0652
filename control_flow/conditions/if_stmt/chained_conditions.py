year = 1899

# check if the year is in a range of 1900 and 2100

# use tradional compound conditions
if year > 1900 and year < 2100:
    print("within valid range")
else:
    print("not in range")

# chained conditions
if 1900 <= year <= 2100:
    print("within valid range")
else:
    print("not in range")
