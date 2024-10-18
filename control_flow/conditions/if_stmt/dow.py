dow = input("Enter a day of the week(ex: Monday):  ")

if dow.lower() == "monday" or dow.lower() == "tuesday" or dow.lower() == "wednesday" or dow.lower() == "thursday" or dow.lower() == "friday":
    print("Weekday")
elif dow.lower() == "saturday" or dow.lower() == "sunday":
    print("Weekend")

