get_data = []

# accept data for multiple people 
while True:
    name = input("Enter name: ")
    age = int(input("Enter Age: "))
    city = input("Enter city: ")
    get_data.append([name,age,city])
    add_more = bool(int(input("Enter another record? (0/1): ")))
    if(not add_more):
        break

# print the header column
print(f"{'Name':<10}",end="| ")
print(f"{'Age':<10}",end="| ")
print(f"{'City':<10}",end="| ")
print()
print('-'*35)

# print the data in a table format
for x in range(len(get_data)):
    for y in range(len(get_data[x])):
        print(f"{get_data[x][y]:<10}",end="| ")
    print()

