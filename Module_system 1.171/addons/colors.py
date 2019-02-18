# Colorama - Begin
# Check: https://pypi.python.org/pypi/colorama#downloads
from colorama import *
init()
# Colorama - End

class colors():
    reset = Style.RESET_ALL
    lred = Style.BRIGHT + Fore.RED
    red = Style.NORMAL + Fore.RED
    dred = Style.DIM + Fore.RED
    lblue = Style.BRIGHT + Fore.BLUE
    blue = Style.NORMAL + Fore.BLUE
    dblue = Style.DIM + Fore.BLUE
    black = Style.NORMAL + Fore.BLACK
    gray = Style.DIM + Fore.WHITE
    dgray = Style.BRIGHT + Fore.BLACK
    lgreen = Style.BRIGHT + Fore.GREEN
    green = Style.NORMAL + Fore.GREEN
    dgreen = Style.DIM + Fore.GREEN
    lyellow = Style.BRIGHT + Fore.YELLOW
    yellow = Style.NORMAL + Fore.YELLOW
    dyellow = Style.DIM + Fore.YELLOW
    lpink = Style.BRIGHT + Fore.MAGENTA
    pink = Style.NORMAL + Fore.MAGENTA
    dpink = Style.DIM + Fore.MAGENTA
    lcyan = Style.BRIGHT + Fore.CYAN
    cyan = Style.NORMAL + Fore.CYAN
    dcyan = Style.DIM + Fore.CYAN
    white = Style.NORMAL + Fore.WHITE
