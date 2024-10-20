data = [['name',"age","city"],["Alex",35,"New York"], ["David", 45, "Singapore"],["Sara", 30,"KL"]]

# print(len(data))
# print(len(data[0]))
# print(len(data[1]))
# print(len(data[2]))
# print(len(data[3]))

for x in range(len(data)):
    for y in range(len(data[x])):
        print(f"{data[x][y]:<10}",end="| ")
    print()
    if x == 0:
        print('-'*35)