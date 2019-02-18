import sys, subprocess
from Tkinter import Tk

from ids.ID_items import *
from module_items import *
from colors import *

list = sys.argv

def get_item_from_id():
    i = 0
    while i < len(list):
        if not list[i].isdigit():
            print(colors.dred + "itemIDCompiler> " + colors.cyan + str(list[i]) + colors.white + " is not valid id. (ID's can include numbers only.)")
        else:
            item = int(list[i])
            if len(items) < item:
                print(colors.dred + "itemIDCompiler> " + colors.cyan + str(item) + colors.white + " is not valid id. (ID number is out of range.)")
            else:
                itm = items[item]
                print(colors.dred + "itemIDCompiler> " + colors.cyan + str(item) + colors.dgreen + " item id is:" + colors.cyan + " itm_" + itm[0] + colors.dgreen + ".")
        i = i + 1

try:
    list = list[1:]
    while len(list) > 0:
        get_item_from_id()
        print("")
        print(colors.dred + "itemIDCompiler> " + colors.dgreen + "Please specify an item ID:")
        list = raw_input(colors.dred + "itemIDCompiler> " + colors.cyan).split()
except:
    print("")
    pass
    
