city = None
print(type(city))

if city is None:
    print("no value is assigned")

city = input("Enter the city:")
print(type(city))
if city is not None:
    print("value has been assigned")

