#  clubbing multiple cases in a match

dow = input("Enter a day of the week(ex: Monday):  ")
match dow.lower():
    case "monday" | "tuesday" | "wednesday" |"thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
