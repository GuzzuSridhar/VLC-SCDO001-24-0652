# return statement will be the last statement executed in a function
# when a return is encountered, the control will be transferred to the calling method/ function

def add(n,m):
    return n+m

def join(s,t):
    return s+t

print(f"{add(10,20) = }")
result = add(100,768)
print(result)
print(add(2,4))

print(join("Hello","World"))


# return annotation (type hint)
def calc_total(n,m) -> int:
    return n+m