# club multiple conditions
# using elif
# there can be 0 or more elif blocks following the if statement
# cannot exist without an if statement
# if one of the conditions is met the rest of the conditions are not evaluated

season = input("Enter the season: ")

if season == "winter":
    print("wear woolen clothes")
    print("stay indoors")
elif season == "summer":
    print("wear cotton clothes")
    print("use air conditioner")
elif season == "rainy":
    print("carry umbrella")

