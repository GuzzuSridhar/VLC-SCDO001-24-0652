#  list of numbers
nums = [1,2,3,4,5]

# list of Strings
names = ['Alex',"David","Jane", 'Sara','James']

print("-----------Using positive index-------------")
# access elements using positive index
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print("-----------Using negative index-------------")
# access elements using negative index
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

print("-----------Using while loop-------------")
# using for loop to access all the elements
for x in names:
    print(x)

print("-----------Using while loop-------------")
# using while loop to access all the elements
loop_var = 0
while loop_var < len(names):
    print(names[loop_var])
    loop_var += 1

