import sys
from Tkinter import Tk

from ids.ID_items import *
from module_items import *

list = sys.argv

def get_item_from_id():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    i = 1
    result = ""
    while i < len(list):
        item = int(list[i])
        itm = items[item]
        print("%d item id is: itm_%s"%(item, itm[0]))
        name = ",itm_%s"%(itm[0])
        result = "%s,itm_%s"%(result, itm[0])
        i = i + 1
    res = result[1:]
    r.clipboard_append(res)
    r.update()
##    r.destroy()

get_item_from_id()
    
