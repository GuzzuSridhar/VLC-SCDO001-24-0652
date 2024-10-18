#  calculator using conditions

#  declare variables for holding numbers


num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

opr = input("Select an operation ([a]dd [s]ubtract [m]ultiply [d]ivide):")

result = 0

if opr.lower() == 'a':
    result = num1+num2
elif opr.lower() == 's':
    result = num1-num2
elif opr.lower() == 'm':
    result = num1*num2
elif opr.lower() == 'd':
    result = num1/num2
else:
    result = "invalid operation"

print(f"{result = }")
