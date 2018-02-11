import string

from process_common import *
from module_item_modifiers import *

def save_python_header():
  file = open("./header_item_modifiers.py","w")
  for imod in xrange(len(imods)):
    file.write("imod_%s = %d\n"%(convert_to_identifier(imods[imod][0]),imod))

  file.write("\n")
  x = 1
  for imodbit in xrange(len(imods)):
    file.write("imodbit_%s = %d\n"%(convert_to_identifier(imods[imodbit][0]),x))
    x = x * 2
  file.close()

## UID: 6 - Begin
#
def write_imods(variable_list,variable_uses,tag_uses,quick_strings):
  langFile = open(language_dir + "item_modifiers.csv", "w")
  for imod in imods:
    if (len(imod) > 2):
      langFile.write("imod_%s|%s\n"%(convert_to_identifier(imod[0]),imod[2].replace("%n", imod[1])))
    else:
      langFile.write("imod_%s|%s\n"%(convert_to_identifier(imod[0]),imod[1] + " %s"))
  langFile.close()
#
## UID: 6 - End

print "Exporting item modifier data..."
save_python_header()

from module_info import *

from process_common import *
from process_operations import *

variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
## UID: 6 - Begin
#
write_imods(variables,variable_uses,tag_uses,quick_strings)
#
## UID: 6 - End
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
