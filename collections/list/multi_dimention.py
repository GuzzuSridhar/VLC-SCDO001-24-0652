matrix = [[1,2,3],[4,5,6]]

# access elements
print("------------- using indexes -----------------------")
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])

print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])

print("------------- using loops -----------------------")
# using loops

for rows in matrix:
    for element in rows:
        print(element, end=" ")
    print()

# ---------------------------------------

