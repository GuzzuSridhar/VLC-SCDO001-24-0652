#  used to execute when all the if and elif conditions fail
#  there can be 0 or 1 else block


season = input("Enter the season: ")

if season.casefold() == "winter":
    print(f"Welcome to {season}")
    print("wear woolen clothes")
    print("stay indoors")
elif season.casefold() == "summer":
    print(f"Welcome to {season}")
    print("wear cotton clothes")
    print("use air conditioner")
elif season.casefold() == "rainy":
    print(f"Welcome to {season}")
    print("carry umbrella")
else:
    print("Invalid Season")

