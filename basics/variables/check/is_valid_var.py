# The isidentifier only looks for a valid naming syntax and not for a keyword
print("my_var".isidentifier())
print("myvar".isidentifier())
print("MYVAR".isidentifier())


print("1my_var".isidentifier())
print("my@var".isidentifier())
# does not check for a keywords
print("class".isidentifier())


