#  used to compare  values or variables
# the result of applying a comparison operator is always boolean (true or false)

#  types of comparison operators are
# == -- equality check (used with numbers and strings)
# != -- inequality check (used with numbers and strings)
# > -- greater than (used with numbers and strings)
# >= -- greater than equals (used with numbers and strings)
# < -- lesser than (used with numbers and strings)
# <= -- lesser than equals (used with numbers and strings)

# ------------equals operator------------------
# can be used with strings and numbers

# with strings (case sensitive comparision)
# use string methods to do a case insensitive comparision
str1 = "Hello"
str2 = "hello"
print(str1 == str2)
print(str1.casefold() == str2.casefold())

# with numbers
x = 10
y = 20
print (x == y)
#  print (f"{x == y}")

# ------------inequals operator------------------
# can be used with  numbers and strings
# with strings (case sensitive comparision)
print (x != y)
str1 = "Hello"
str2 = "Hello"
print(str1 != str2)
print(str1 == str2)
# with numbers
print (x != y)

# ------------greater operator------------------
# can be used with  numbers and strings
# compare lexicographically
str1 = "ABC"
str2 = "DEF"
print(str1 > str2)

print(x > y)
print(y > x)

# ------------greater than equals operator------------------
# can be used with  numbers and strings
# compare lexicographically
str1 = "ABC"
str2 = "DEF"
print(str1 >= str2)

print(x >= y)
print(y >= x)

# ------------Lesser than  operator------------------
# can be used with  numbers and strings
# compare lexicographically
str1 = "ABC"
str2 = "DEF"
print(str1 < str2)

print(x < y)
print(y < x)

# ------------lesser than equals operator------------------
# can be used with  numbers and strings
# compare lexicographically
str1 = "ABC"
str2 = "DEF"
print(str1 <= str2)

print(x <= y)
print(y <= x)







