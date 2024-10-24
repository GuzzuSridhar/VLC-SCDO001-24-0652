# immutable collection that is ordered
#  hetrogenous collections

# example
my_tuple = (1,2,3,4,5)
mixed_data = ("Hello",True,1,1.3,[])

# create a tuple that has only one element in it
# age = (5)
age = (5,)
print(id(age))
age = (5,9)
print(id(age))

print(type(my_tuple))
print(type(age))

# create a tuple from a list
my_list = [1,3,5,7,9]
tup = tuple(my_list)
print(type(tup))

