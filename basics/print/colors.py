#  print colors on python console
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

print(RED + " This isn Red" +RESET)
print(GREEN + " This isn Green" +RESET)
print(YELLOW + " This isn Yellow" +RESET)
print(BLUE + " This isn Blue" +RESET)
print(MAGENTA + " This isn Magenta" +RESET)
print(CYAN + " This isn Cyan" +RESET)
print(WHITE + " This isn White" +RESET)

# format the background
BLACK = "\033[40m"
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
BLUE_BG = "\033[44m"
MAGENTA_BG = "\033[45m"
CYAN_BG = "\033[46m"
WHITE_BG = "\033[47m"

print(BLUE_BG + WHITE + " I am in White " + RESET)