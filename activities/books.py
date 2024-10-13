# CLI to capture the users name and his fav book
# print the details on console

# constants for colors
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# create a variable to hold the users name
user_name = ""
# create a variable to hold the fav book of the user
fav_book = ""

# accept the users input to the variables created above
print(YELLOW)
user_name = input("Whats your Name please? ")
fav_book = input("Whats your fav book? ")
print(RESET)

#  format and print the details to console

# simple print
# print(user_name)
# print(fav_book)

# constants for colors
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# formatted print
print(f"{GREEN} Hello {user_name.capitalize()}!, Your fav book is {fav_book.capitalize()} ")
