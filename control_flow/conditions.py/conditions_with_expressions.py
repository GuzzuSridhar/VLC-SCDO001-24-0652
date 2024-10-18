#  using expressions in conditions

salary = float(input("Enter your salary: "))
comm = float(input("Enter your commission: "))

if salary+comm >= 10_000:
    print("Excellent earning")
elif salary+comm < 10_000 and salary+comm >= 5000:
    print("Good Earning")
elif salary+comm >= 2000 and salary+comm < 5000:
    print("Average Earning")
else:
    print("Below par Earning")