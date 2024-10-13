# static value to the variable

# value of the variable dynamic
# use the input function input()
name = ""
name= input("What is your name? ")
print("Hello",name)

city = input("Which city do you live in? ")
print("Hello",name,"From",city)

# the input captured is always a string
#  to work with other types use casting
age = int(input("How old are you? "))
# age = input("How old are you? ")
print(type(age))
print("You will be ", age+1 , "years, next year" )
# print("You will be ", int(age)+1 , "years, next year" )

