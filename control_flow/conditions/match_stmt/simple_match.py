#  same as the switch statement in other programming languages
#  used to test against multiple constants
#  can be be used with expressions but not advised (as the code gets a bit complex to read)

dow = int(input("Enter a Day of the Week[1-7]: "))

match dow:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid day of the week")

        

