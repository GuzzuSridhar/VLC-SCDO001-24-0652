#  used to execute when all the if and elif conditions fail
#  there can be 0 or 1 else block


season = input("Enter the season: ")

if season == "winter":
    print("wear woolen clothes")
    print("stay indoors")
elif season == "summer":
    print("wear cotton clothes")
    print("use air conditioner")
elif season == "rainy":
    print("carry umbrella")
else:
    print("Invalid Season")