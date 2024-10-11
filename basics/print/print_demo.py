name = "Alex"
age = 35

#  printing individual variables (there is a \n infused towards the end)
print(name) 
#  print(name\n) implicitly
print(age)

#  to print the name and age in one line
print(name, end=" ")
print(age)

print(name, end=" - ")
print(age)

# default functionality
print(name, end="\n")
print(age)

# using the + operator
print(name + " " + str(age))
#  simpler way of pythons concat (default seperator is space)
print(name,age) 

#  seperate the values with a custom seperator
print(name,age, sep="|") 
print(name,age, sep=" - ") 
print(name,age, sep="-") 

