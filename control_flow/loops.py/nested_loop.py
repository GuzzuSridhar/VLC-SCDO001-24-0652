
num = int(input("Enter a number: "))

for outer in range(1,num+1):
    for inner in range(1,11):
       print(outer , "x" , inner , "=" , outer*inner)
    print("--------------------")