import sys, os, subprocess, msvcrt

from colors import *

def start():
    print(colors.dgreen + "Which add-on would you like to use?")
    print(colors.dred + "0" + colors.cyan + " - Restart")
    print(colors.dred + "1" + colors.cyan + " - Start Item ID Compiler")
    print(colors.dred + "exit" + colors.cyan + " - Exit")

args = sys.argv
def addons():
    if (i == 0):
        os.system('cls')
        start()
    elif (i == 1):
        print(colors.dred + "itemIDCompiler> " + colors.dgreen + "Please specify an item ID:")
        array = raw_input(colors.dred + "itemIDCompiler> " + colors.cyan)
        plugin = subprocess.check_call("python -m addons.get_item_from_id " + array, shell=True)
        start()

try:
    i = int(args[1])
    
    if (i < 0):
        start()
    elif (i >= 0):
        addons()
except:
    pass
