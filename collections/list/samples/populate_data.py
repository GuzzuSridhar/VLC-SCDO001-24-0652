get_data = []

# print(get_data)

while True:
    name = input("Enter name: ")
    age = int(input("Enter Age: "))
    city = input("Enter city: ")
    get_data.append([name,age,city])
    add_more = bool(int(input("Enter another record? (0/1): ")))
    if(not add_more):
        break

print(get_data)
