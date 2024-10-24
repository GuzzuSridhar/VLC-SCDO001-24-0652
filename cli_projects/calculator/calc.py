def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def main():
    while True:
        print("Select an operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Enter your Choice: "))

        if choice in (1,2,3,4):
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter Second number: "))
            if choice == 1:
                print(str(n1) + " + " + str(n2) + " = " + str(add(n1,n2)))
            elif choice == 2:
                print(str(n1) + " - " + str(n2) + " = " + str(subtract(n1,n2)))
            elif choice == 3:
                print(str(n1) + " x " + str(n2) + " = " + str(multiply(n1,n2)))
            elif choice == 4:
                print(str(n1) + " / " + str(n2) + " = " + str(divide(n1,n2)))
        elif choice == 5:
           print("Exiting........")
           break
        else:
            print("Invalid Choice please select a valid operation")

if __name__ == "__main__":
    main()