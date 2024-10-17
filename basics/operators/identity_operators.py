#  used to check the object literal types not the content
myname = "Alex"
yourname = myname
hisname = "Alex"

# check for the equality of values
print(myname == yourname)
print(myname == hisname)
print(yourname == hisname)

# identity operator
# two identity operators
# is
# is not
myname = "Alex"
yourname = myname
hisname = "David"
# the memory location of myname is resued for hisname also
print(id(myname))
print(id(yourname))
print(id(hisname))

print(myname is yourname)
print(myname is hisname)
print(yourname is hisname)

l1 = [1,2,3]
l2 = l1
l3 = [1,2,3]

print(id(l1))
print(id(l2))
print(id(l3))

print(l1 is l2)
print(l1 is l3)

print(l1 is not l3)




