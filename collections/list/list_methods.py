#  a list to learn methods on
print("-------------Original List--------------------")
fruits = ['apple','banana']
print(fruits, end= '\n\n')

print("-------------Append List--------------------")
# append list element
fruits.append('orange')
print(fruits)

print("-------------Extend List--------------------")
#  extend is used to add a new list to the current one
fruits.extend(['goa','mango'])
print(fruits)

print("-------------Insert List element--------------------")
# inserts an element at the given index and pushes the current elements forward
fruits.insert(0,'grapes')
print(fruits)

print("-------------Remove List element--------------------")
# removes an element 
fruits.remove('banana')
print(fruits)

print("-------------Remove List element at a given index--------------------")
# pop() removes the element at given index, if no idex removes last elements
# returns the removed element

# fruits.pop(3)
# print(fruits)
print(fruits.pop(3), "has been removed")

print("-------------Index --------------------")
# index method return index of the element
print(fruits.index('apple'))

print("-------------count --------------------")
# count returns tyhe #times of a elements presence
print(fruits.count('apple'))
fruits.append("apple")
print(fruits.count('apple'))

print("-------------reverse --------------------")
fruits.reverse()
print(fruits)

print("-------------sort --------------------")
#  ascending sort
fruits.sort()
print(fruits)
# descending sort
fruits.sort(reverse=True)
print(fruits)

print("-------------copy a list --------------------")
new_fruits = fruits.copy()
print(new_fruits)

print("-------------Length of list --------------------")
# len is used to get the # elements
print(len(fruits)) 

print("-------------clear List --------------------")
# clear() removes all emenets
fruits.clear()
print(fruits)

print("-------------sum of elements in a  List --------------------")
# int list
nums = [1,2,3,4,5]
print(sum(nums))



