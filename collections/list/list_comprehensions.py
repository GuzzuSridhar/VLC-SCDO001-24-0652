#  allows the developers to create list and populate the filtered data 
# syntax
#  [expression for item in iterable if condition]

nums = [i for i in range(10)]
print(nums)

squares = [x**2 for x in range(1,6)]
print(squares)

# list with even numbers from 1 tp 100
even_nums = [e for e in range(1,101) if e%2 ==0]
print(even_nums)