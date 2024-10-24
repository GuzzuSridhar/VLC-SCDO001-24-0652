employee_info = {
    "name" :"Alice",
    "age": 30,
    "department" : "Sales",
    "city": "Singapore",
    "hobbies": ["reading","running"],
    "address":{
        "street": "Some Street",
        "state" : "Some State",
        "zip" : '0000'
    }
}

# keys()
# returns a list of keys in the dictionary

print(employee_info.keys())

# values()
# returns a list of values in the dictionary

print(employee_info.values())

# get()
# returns the value for a given key
print(employee_info.get("name"))

# setdefault()
# sets the default value for a given key
employee_info.setdefault("doj","today")
print(employee_info)
