import os
import string
import glob
import time
import traceback
import sys

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
print(colors.lred + "Dark Nights new compiling system. (v0.2.5)")

class strs():
    error = colors.dred + "[Error]: " + colors.cyan
    warn = colors.dyellow + "[Warning]: " + colors.cyan
    info = colors.pink + "[Info]: " + colors.cyan
    traceback = colors.dred + "[Traceback]: " + colors.cyan

eCount = 0
try:
    from module_info import *
    from module_item_modifiers import *
    from module_sounds import *
    from module_map_icons import *
    from module_strings import *
    from module_skills import *
    from module_music import *
    from module_meshes import *
    from module_skins import *
    from module_factions import *
    from module_triggers import *
    from module_dialogs import *
    from module_simple_triggers import *
    from module_presentations import *
    from module_variables import *
    from module_scene_props import *
    from module_game_menus import *
    from module_mission_templates import *
    from module_scripts import *
    from module_items import *
    from module_scenes import *
    from module_troops import *
    from module_particle_systems import *
    from module_tableau_materials import *
    from module_party_templates import *
    from module_parties import *
    from module_quests import *
    from module_info_pages import *
    from module_scripts import *
    from module_postfx import *
    from module_animations import *

    from headers.header_operations import *
    from headers.header_items import *
    from headers.header_troops import *
    from headers.header_scene_props import *
    from headers.header_common import *
except Exception as e:
    eCount = 1
    args = traceback.format_exc().splitlines()
    cFile = str(args[2].split()[1])
    cLine = str(args[3].split('"')[2].split()[2][0:-1])
    cError = str(args[4])
    cDesc = ' '.join(str(args[5]).split()[2:])
    print(strs.traceback)
    traceback.print_exc()
##    print(strs.traceback + cDesc + ". (" + cFile + ", " + cLine + ")")
##    print(colors.dpink + "         " + cError)
    
def clear_module():
    files = [file for file in glob.glob("ID_*.pyc")]
    for file in files:
        os.remove(file)

def convert_to_identifier(s0):
  s1 = string.replace(s0," ","_")
  s2 = string.replace(s1,"'","_")
  s3 = string.replace(s2,"`","_")
  s4 = string.replace(s3,"(","_")
  s5 = string.replace(s4,")","_")
  s6 = string.replace(s5,"-","_")
  s7 = string.replace(s6,",","")
  s8 = string.replace(s7,"|","")
  s9 = string.replace(s8,"\t","_")
  s10 = string.lower(s9)
  return s10

def compile_ids():
    start_time = int(round(time.time() * 1000))
    if (eCount > 0):
        end_time = int(round(time.time() * 1000))
        diff_time = str((end_time - start_time) / 1000.0)
        print(colors.lred + "Compiling failed in " + colors.dcyan + diff_time + colors.lred + " milliseconds.")
        return 0
    
    print(colors.dgreen + "Initializing module...")
    file = open("./ids/ID_map_icons.py", "w")
    for i in xrange(len(map_icons)):
        file.write("icon_%s = %d\n"%(convert_to_identifier(map_icons[i][0]), i))
    file.close()
    file = open("./ids/ID_strings.py", "w")
    for i in xrange(len(strings)):
        file.write("str_%s = %d\n"%(convert_to_identifier(strings[i][0]), i))
    file.close()
    file = open("./ids/ID_skills.py", "w")
    for i in xrange(len(skills)):
        file.write("skl_%s = %d\n"%(convert_to_identifier(skills[i][0]), i))
    file.write("\n")
    x = 1
    for i in xrange(len(skills)):
        max = skills[i][3]
        if max > 15:
            print(strs.error + "Max level cannot be more than 15, it was automatically dropped to 15 for skill " + skills[i][0] + ".")
            max = 15
        for l in xrange(max):
            file.write("knows_" + skills[i][0] + "_" + str(l + 1) + " = " + str(x * (l + 1)) + "\n")
        x *= 16
    file.close()
    file = open("./ids/ID_musics.py", "w")
    for i in xrange(len(tracks)):
      file.write("track_%s = %d\n"%(convert_to_identifier(tracks[i][0]), i))
    file.close()
    file = open("./ids/ID_animations.py", "w")
    for i in xrange(len(animations)):
      file.write("anim_%s = %d\n"%(convert_to_identifier(animations[i][0]), i))
    file.close()
    file = open("./ids/ID_meshes.py", "w")
    for i in xrange(len(meshes)):
      file.write("mesh_%s = %d\n"%(convert_to_identifier(meshes[i][0]), i))
    file.close()
    file = open("./ids/ID_sounds.py", "w")
    for i in xrange(len(sounds)):
      file.write("snd_%s = %d\n"%(convert_to_identifier(sounds[i][0]), i))
    file.close()
    file = open("./ids/ID_factions.py", "w")
    for i in xrange(len(factions)):
      file.write("fac_%s = %d\n"%(convert_to_identifier(factions[i][0]), i))
    file.close()
    file = open("./ids/ID_items.py", "w")
    for i in xrange(len(items)):
      file.write("itm_%s = %d\n"%(convert_to_identifier(items[i][0]), i))
    file.close()
    file = open("./ids/ID_scenes.py", "w")
    for i in xrange(len(scenes)):
      file.write("scn_%s = %d\n"%(convert_to_identifier(scenes[i][0]), i))
    file.close()
    file = open("./ids/ID_troops.py", "w")
    for i in xrange(len(troops)):
      file.write("trp_%s = %d\n"%(convert_to_identifier(troops[i][0]), i))
    file.close()
    file = open("./ids/ID_particle_systems.py", "w")
    for i in xrange(len(particle_systems)):
      file.write("psys_%s = %d\n"%(convert_to_identifier(particle_systems[i][0]), i))
    file.close()
    file = open("./ids/ID_scene_props.py", "w")
    for i in xrange(len(scene_props)):
      file.write("spr_%s = %d\n"%(convert_to_identifier(scene_props[i][0]), i))
    file.close()
    file = open("./ids/ID_tableau_materials.py", "w")
    for i in xrange(len(tableaus)):
      file.write("tableau_%s = %d\n"%(convert_to_identifier(tableaus[i][0]), i))
    file.close()
    file = open("./ids/ID_presentations.py", "w")
    for i in xrange(len(presentations)):
      file.write("prsnt_%s = %d\n"%(convert_to_identifier(presentations[i][0]), i))
    file.close()
    file = open("./ids/ID_party_templates.py", "w")
    for i in xrange(len(party_templates)):
      file.write("pt_%s = %d\n"%(convert_to_identifier(party_templates[i][0]), i))
    file.close()
    file = open("./ids/ID_parties.py", "w")
    for i in xrange(len(parties)):
      file.write("p_%s = %d\n"%(convert_to_identifier(parties[i][0]), i))
    file.close()
    file = open("./ids/ID_quests.py", "w")
    for i in xrange(len(quests)):
      file.write("qst_%s = %d\n"%(convert_to_identifier(quests[i][0]), i))
      file.write("qsttag_%s = %d\n\n"%(quests[i][0], opmask_quest_index|i))
    file.close()
    file = open("./ids/ID_info_pages.py", "w")
    for i in xrange(len(info_pages)):
      file.write("ip_%s = %d\n"%(convert_to_identifier(info_pages[i][0]), i))
    file.close()
    file = open("./ids/ID_scripts.py", "w")
    for i in xrange(len(scripts)):
      file.write("script_%s = %d\n"%(convert_to_identifier(scripts[i][0]), i))
    file.close()
    file = open("./ids/ID_mission_templates.py", "w")
    for i in xrange(len(mission_templates)):
      file.write("mst_%s = %d\n"%(convert_to_identifier(mission_templates[i][0]), i))
    file.close()
    file = open("./ids/ID_menus.py", "w")
    for i in xrange(len(game_menus)):
      file.write("menu_%s = %d\n"%(convert_to_identifier(game_menus[i][0]), i))
    file.close()
    file = open("./ids/ID_postfx_params.py", "w")
    for i in xrange(len(postfx_params)):
      file.write("pfx_%s = %d\n"%(convert_to_identifier(postfx_params[i][0]), i))
    file.close()
    end_time = int(round(time.time() * 1000))
    diff_time = str((end_time - start_time) / 1000.0)
    clear_module() #Clean the module system at the end...
    print(colors.dgreen + "Initialization completed in " + colors.dcyan + diff_time + colors.dgreen + " milliseconds.")
    os.system("compile.py 1")

compile_ids()
