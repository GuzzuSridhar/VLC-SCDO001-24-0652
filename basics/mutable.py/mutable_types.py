# Immutable type: String
string1 = "Hello"
print(id(string1))

string1 += " World"
print(id(string1))

# Mutable type: List
list1 = [1, 2, 3]
print(id(list1))

list1.append(4)
print(id(list1))