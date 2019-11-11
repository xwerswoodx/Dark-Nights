import os
import glob
import string
import time
import types
import sys
import re

# Colorama - Begin
# Check: https://pypi.python.org/pypi/colorama#downloads
from colorama import *
init()
# Colorama - End

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

## UID: 121 - Begin
#
#from ID_items import *
#from ID_factions import *
#from ID_quests import *
#from ID_party_templates import *
#from ID_parties import *
#from ID_scenes import *
#from ID_mission_templates import *
#from ID_menus import *
#from ID_particle_systems import *
#from ID_scene_props import *
#from ID_presentations import *
#from ID_sounds import *
#from ID_map_icons import *
#from ID_animations import *
#from ID_tableau_materials import *
#from ID_scripts import *
#from ID_strings import *
#from ID_music import *
from ids.ID_items import *
from ids.ID_factions import *
from ids.ID_quests import *
from ids.ID_party_templates import *
from ids.ID_parties import *
from ids.ID_scenes import *
from ids.ID_mission_templates import *
from ids.ID_menus import *
from ids.ID_particle_systems import *
from ids.ID_scene_props import *
from ids.ID_presentations import *
from ids.ID_sounds import *
from ids.ID_map_icons import *
from ids.ID_animations import *
from ids.ID_tableau_materials import *
from ids.ID_scripts import *
from ids.ID_strings import *
from ids.ID_music import *
#
## UID: 121 - End

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
    pink = Style.BRIGHT + Fore.MAGENTA
    purple = Style.NORMAL + Fore.MAGENTA
    majestic = Style.DIM + Fore.MAGENTA
    lcyan = Style.BRIGHT + Fore.CYAN
    cyan = Style.NORMAL + Fore.CYAN
    dcyan = Style.DIM + Fore.CYAN
    white = Style.NORMAL + Fore.WHITE

num_voice_types = 2
start_time = int(round(time.time() * 1000))
class strs():
    error = colors.dred + "[Error]: " + colors.cyan
    warn = colors.dyellow + "[Warning]: " + colors.cyan
    info = colors.pink + "[Info]: " + colors.cyan

def calcTime():
    _start = start_time
    _end = int(round(time.time() * 1000))
    _diff = (_end - _start) / 1000.0
    return _diff
    
# Global Definitions - Begin
def findObject(tag, obj):
  try:
    item = globals()[tag.lower() + "_" + obj.lower()]
    return item
  except:
    print(strs.error + "Unable to find object " + tag.lower() + "_" + obj.lower())
    return 0

def get_id_value(tag, identifier, tag_uses):
    tag_type = -1
    id_no = -1
    if (tag == "str"):
##        id_no = find_bject(strings,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_string
    elif (tag == "itm"):
##        id_no = find_object(items,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_item
    elif (tag == "trp"):
##        id_no = find_object(troops,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_troop
    elif (tag == "fac"):
##        id_no = find_object(factions,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_faction
    elif (tag == "qst"):
##        id_no = find_object(quests,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_quest
    elif (tag == "pt"):
##        id_no = find_object(party_templates,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_party_tpl
    elif (tag == "p"):
##        id_no = find_object(parties,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_party
    elif (tag == "scn"):
##        id_no = find_object(scenes,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_scene
    elif (tag == "mt"):
##        id_no = find_object(mission_templates,identifier)
        id_no = findObject("mst", identifier)
        tag_type = tag_mission_tpl
    elif (tag == "mnu"):
##        id_no = find_object(game_menus,identifier)
        id_no = findObject("menu", identifier)
        tag_type = tag_menu
    elif (tag == "script"):
##        id_no = find_object(scripts,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_script
    elif (tag == "psys"):
##        id_no = find_object(particle_systems,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_particle_sys
    elif (tag == "spr"):
##        id_no = find_object(scene_props,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_scene_prop
    elif (tag == "prsnt"):
##        id_no = find_object(presentations,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_presentation
    elif (tag == "snd"):
##        id_no = find_object(sounds,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_sound
    elif (tag == "icon"):
##        id_no = find_object(map_icons,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_map_icon
    elif (tag == "skl"):
##        id_no = find_object(skills,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_skill
    elif (tag == "track"):
##        id_no = find_object(tracks,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_track
    elif (tag == "mesh"):
##        id_no = find_object(meshes,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_mesh
    elif (tag == "anim"):
##        id_no = find_object(animations,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_animation
    elif (tag == "tableau"):
##        id_no = find_object(tableaus,identifier)
        id_no = findObject(tag, identifier)
        tag_type = tag_tableau
    return (tag_type, id_no)

def convert_to_identifier(s0):
    s0 = s0.replace(" ", "_")
    s0 = s0.replace("'", "_")
    s0 = s0.replace("`", "_")
    s0 = s0.replace("(", "_")
    s0 = s0.replace(")", "_")
    s0 = s0.replace("-", "_")
    s0 = s0.replace(",", "_")
    s0 = s0.replace("|", "")
    s0 = s0.replace("\t", "_")
    return s0.lower()

def convert_to_identifier_with_no_lowercase(s0):
    s0 = s0.replace(" ", "_")
    s0 = s0.replace("'", "_")
    s0 = s0.replace("`", "_")
    s0 = s0.replace("(", "_")
    s0 = s0.replace(")", "_")
    s0 = s0.replace("-", "_")
    s0 = s0.replace(",", "_")
    s0 = s0.replace("|", "")
    s0 = s0.replace("\t", "_")
    return s0

def replace_spaces(s0):
    s0 = s0.replace("\t", "_")
    s0 = s0.replace(" ", "_")
    return s0

def create_autoid(sentence, auto_ids):
    text = sentence[3]
    token_ipt = convert_to_identifier(sentence[1])
    token_opt = convert_to_identifier(sentence[4])
    done = 0
    auto_id = "dlga_" + token_ipt + ":" + token_opt
    done = 0
    if not auto_id in auto_ids:
    #if not auto_ids.has_key(auto_id):
        done = 1
    else:
        #if auto_ids.has_key(auto_id) and (auto_ids[auto_id] == text):
        if auto_id in auto_ids and (auto_ids[auto_id] == text):
            done = 1

    if not done:
        number = 1
        new_auto_id = auto_id + "." + str(number)
        #while auto_ids.has_key(new_auto_id):
        while new_auto_id in auto_ids:
            number += 1
            new_auto_id = auto_id + "." + str(number)
        auto_id = new_auto_id
    auto_ids[auto_id] = text
    return auto_id

def compile_sentence_tokens(sentences):
    input_tokens = []
    output_tokens = []
    dialog_states = ["start","party_encounter","prisoner_liberated","enemy_defeated","party_relieved","event_triggered","close_window","trade","exchange_members", "trade_prisoners","buy_mercenaries","view_char","training","member_chat","prisoner_chat"]
    dialog_state_usages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for sentence in sentences:
        output_token_id = -1
        output_token = sentence[4]
        found = 0
        for i_t in range(len(dialog_states)):
            if output_token == dialog_states[i_t]:
                output_token_id = i_t
                found = 1
                break
        if not found:
            dialog_states.append(output_token)
            dialog_state_usages.append(0)
            output_token_id = len(dialog_states) - 1
        output_tokens.append(output_token_id)

    for sentence in sentences:
        input_token_id = -1
        input_token = sentence[1]
        found = 0
        for i_t in range(len(dialog_states)):
            if input_token == dialog_states[i_t]:
                input_token_id = i_t
                dialog_state_usages[i_t] = dialog_state_usages[i_t] + 1
                found = 1
                break
        if not found:
            print(strs.error + "Input token " + input_token + " not found.")
        input_tokens.append(input_token_id)
    file = open(export_dir + "dialog_states.txt", "w")
    for dialog_state in dialog_states:
        file.write("%s\n"%dialog_state)
    file.close()
    for i_t in range(len(dialog_states)):
        if dialog_state_usages[i_t] == 0:
            print(strs.error + "Output token " + dialog_states[i_t] + " not found.")
    return (input_tokens, output_tokens)

def save_triggers(file,template_name,triggers,variable_list,variable_uses,tag_uses,quick_strings):
    file.write("%d\n"%len(triggers))
    for i in range(len(triggers)):
        trigger = triggers[i]
        file.write("%f %f %f "%(trigger[0],trigger[1],trigger[2]))
        save_statement_block(file, 0, 1, trigger[3], variable_list, variable_uses,tag_uses,quick_strings)
        save_statement_block(file, 0, 1, trigger[4], variable_list, variable_uses,tag_uses,quick_strings)
        file.write("\n")
    file.write("\n")

def save_mission_template_group(file, entry):
    if (len(entry[5]) > 8):
        print(strs.error + "Too many item_overrides.")
    file.write("%d %d %d %d %d %d  "%(entry[0],entry[1],entry[2],entry[3],entry[4], len(entry[5])))
    for item_override in entry[5]:
        file.write("%d "%(item_override))
    file.write("\n")

def save_party_template_troop(file,troop):
    if troop:
        file.write("%d %d %d "%(troop[0],troop[1],troop[2]))
        if (len(troop) > 3):
            file.write("%d "%troop[3])
        else:
            file.write("0 ")
    else:
        file.write("-1 ")

def write_passage(file,scenes,passage):
    scene_no = 0
    found = 0
    while (not found) and (scene_no < len(scenes)):
        if (scenes[scene_no][0] == passage):
            found = 1
        else:
            scene_no += 1
    if (passage == "exit"):
        scene_no = 100000
    elif (passage == ""):
        scene_no = 0
    elif not found:
        print(strs.error + "Passage " + str(passage) + " not found.")
    file.write(" %d "%scene_no)

def save_psys_keys(file, keys1, keys2):
    file.write("%f %f   %f %f\n"%(keys1[0], keys1[1], keys2[0], keys2[1]))
  
def compile_relations():
    relations = []
    for i in range(len(factions)):
        r = [0.0 for j in range(len(factions))]
        relations.append(r)
    for i_faction in range(len(factions)):
        relations[i_faction][i_faction] = factions[i_faction][3]
        rels = factions[i_faction][4]
        for rel in rels:
            rel_name = rel[0]
            other_pos = -1
            for j_f in range(len(factions)):
                if factions[j_f][0] == rel_name:
                    other_pos = j_f
            if other_pos == -1:
                print(strs.error + "Faction not found: " + rel_name)
            else:
                relations[other_pos][i_faction] = rel[1]
                relations[i_faction][other_pos] = rel[1]
    return relations

def write_face_tex(file, tex_set):
    file.write(" %d "%len(tex_set))
    for tex in tex_set:
        color = tex[1]
        hair_mats = tex[2]
        hair_colors = []
        if len(tex) > 3:
            hair_colors = tex[3]
        file.write(" %s %d %d %d "%(tex[0],color, len(hair_mats), len(hair_colors)))
        for hair_mat in hair_mats:
            file.write(" %s "%(replace_spaces(hair_mat)))
        for hair_color in hair_colors:
            file.write(" %d "%(hair_color))
    file.write("\n")

def write_textures(file, tex_set):
    file.write(" %d "%len(tex_set))
    for tex in tex_set:
        file.write(" %s "%tex)
    file.write("\n")

def write_voices(file, voices):
  file.write(" %d "%(len(voices)))
  for voice_rec in voices:
      file.write(" %d %s "%(voice_rec[0],voice_rec[1]))
  file.write("\n")

def compile_sounds(sounds):
    all_sounds = []
    for sound in sounds:
        sound_files = sound[2]
        sound_flags = sound[1]
        for i_sound_file in range(len(sound_files)):
            sound_file = sound_files[i_sound_file]
            if (type(sound_file) != type([])):
                sound_file = [sound_file, 0]
                sound_no = 0
                found = 0

                while (sound_no< (len(all_sounds))) and (not found):
                    if all_sounds[sound_no][0] == sound_file[0]:
                        found = 1
                    else:
                        sound_no += 1
                if not found:
                    all_sounds.append((sound_file[0], sound_flags))
                    sound_no = len(all_sounds) - 1
                sound_files[i_sound_file] = [sound_no, sound_file[1]]
    return all_sounds

def compile_action_sets(actions):
    action_codes = []
    for action in actions:
        index = -1
        for i_action_code in range(len(action_codes)):
            if action_codes[i_action_code] == action[0]:
                index = i_action_code
                break
        if index == -1:
            pos = len(action_codes)
            action_codes.append(action[0])
            action[0] = pos
        else:
            action[0] = index
    return action_codes

def decompile_action_sets(actions, args):
    for i_action in range(len(actions)):
        action = actions[i_action]
        action[0] = args[i_action]
    return actions

def insert_quick_string_with_auto_id(sentence,quick_strings):
  index = 0
  text = convert_to_identifier_with_no_lowercase(sentence)
  sentence = replace_spaces(sentence)
  done = 0
  i = 20
  lt = len(text)
  if (i > lt):
    i  = lt
  auto_id = "qstr_" + text[0:i]
  done = 0
  index = search_quick_string_keys(auto_id, quick_strings)
  if index >= 0 and (quick_strings[index][1] == sentence):
    done = 1
  while (i <= lt) and not done:
    auto_id = "qstr_" + text[0:i]
    index = search_quick_string_keys(auto_id, quick_strings)
    if index >= 0:
      if quick_strings[index][1] == sentence:
        done = 1
      else:
        i += 1
    else:      
      done = 1
      index = len(quick_strings)
      quick_strings.append([auto_id, sentence])
  if not done:
    number = 1
    new_auto_id = auto_id + str(number)
    while quick_strings.has_key(new_auto_id):
      number += 1
      new_auto_id = auto_id + str(number)
    auto_id = new_auto_id
    index = len(quick_strings)
    quick_strings.append([auto_id, sentence])
  return index

def search_quick_string_keys(key, quick_strings):
  index = -1
  for i in range(len(quick_strings)):
    if quick_strings[i][0] == key:
      index = i
  return index

def check_varible_not_defined(variable_string, variables_list):
    for i_t in range(len(variables_list)):
        if variable_string == variables_list[i_t]:
            print(strs.warn + "Variable " + variable_string + "used for both local and global contexts.")
            break

def get_identifier_value(str, tag_uses):
    ##underscore_pos = string.find(str, "_")
    underscore_pos = str.find("_")
    result = -1
    if (underscore_pos > 0):
        tag_str = str[0:underscore_pos]
        id_str  = str[underscore_pos + 1:len(str)]
        (tag_type, id_no) = get_id_value(tag_str,id_str,tag_uses)
        if (tag_type > 0):
            if (id_no < 0):
                print(strs.error + "Unable to find object " + str + ".")
            else:
                result = id_no | (tag_type << op_num_value_bits)
        else:
            print(strs.error + "Unrecognized tag " + tag_str + " in object " + str + ".")
    else:
        print(strs.error + "Invalid object " + str + ". Variables should start with $ sign and references should start with @ sign.")
    return result

def get_variable(variable_string,variables_list,variable_uses):
    found = 0
    result = -1
    var_string = variable_string[1:]
    for i_t in range(len(variables_list)):
        if var_string == variables_list[i_t]:
            found = 1
            result = i_t
            variable_uses[result] = variable_uses[result] + 1
            break
    if not found:
        if (variable_string[0] == '$'):
            variables_list.append(variable_string)
            variable_uses.append(0)
            result = len(variables_list) - 1
##            file = open("./variables.txt", "a")
##            file.write("\n" + var_string)
##            file.close()
            print(strs.warn + "Usage of unassigned global variable: " + variable_string) #+ " automatically added to variables.txt"
        else:
            print(strs.warn + "Usage of unassigned local variable: " + variable_string)
    return result

def process_param(param,global_vars_list,global_var_uses, local_vars_list, local_var_uses, tag_uses, quick_strings):
    result = 0
    if (type(param) is str):
        if (param[0] == '$'):
            check_varible_not_defined(param[1:], local_vars_list)
            result = get_variable(param, global_vars_list,global_var_uses)
            result |= opmask_variable
        elif (param[0] == ':'):
            check_varible_not_defined(param[1:], global_vars_list)
            result = get_variable(param, local_vars_list,local_var_uses)
            result |= opmask_local_variable
        elif (param[0] == '@'):
            result = insert_quick_string_with_auto_id(param[1:], quick_strings)
            result |= opmask_quick_string
        else:
            result = get_identifier_value(param.lower(), tag_uses)
            if (result < 0):
                print(strs.error + "Illegal Identifier " + str(param))
    else:
        result = param
    return result

def save_statement(file, opcode, no_variables, statement, variable_list, variable_uses, local_vars_list, local_var_uses, tag_uses, quick_strings):
    if no_variables == 0:
        lenstatement = len(statement) - 1
        if (is_lhs_operation(opcode) == 1):
            if (lenstatement > 0):
                param = statement[1]
                if (type(param) is str):
                    if (param[0] == ':'):
                        add_variable(param[1:], local_vars_list, local_var_uses)
    else:
        lenstatement = 0
    file.write("%d %d "%(opcode, lenstatement))
    for i in range(lenstatement):
        operand = process_param(statement[i + 1],variable_list,variable_uses,local_vars_list,local_var_uses,tag_uses,quick_strings)
        file.write("%d "%operand)

def save_statement_block(file, statement_name, can_fail_statement, statement_block, variable_list, variable_uses, tag_uses, quick_strings):
    local_vars = []
    local_var_uses = []
    file.write(" %d "%(len(statement_block)))

    store_script_param_1_uses = 0
    store_script_param_2_uses = 0
    current_depth = 0
    can_fail = 0
    for i in range(len(statement_block)):
        statement = statement_block[i]

        if ((type(statement) is not list) and (type(statement) is not tuple)):
            opcode = statement
            no_variables = 1
        else:
            opcode = statement[0]
            no_variables = 0

        if (opcode in [
            try_begin,
            try_for_range,
            try_for_range_backwards,
            try_for_parties,
            try_for_agents,
        ]):
            current_depth = current_depth + 1
        elif (opcode == try_end):
            current_depth = current_depth - 1
        elif (opcode == store_script_param_1 or (opcode == store_script_param and statement[2] == 1)):
            store_script_param_1_uses = store_script_param_1_uses + 1
        elif (opcode == store_script_param_2 or (opcode == store_script_param and statement[2] == 2)):
            store_script_param_2_uses = store_script_param_2_uses + 1
        elif (can_fail_statement == 0 and current_depth == 0 and (is_can_fail_operation(opcode) or ((opcode == call_script) and (statement[1].startswith("cf_", 7)))) and (not statement_name.startswith("cf_"))):
            print(strs.error + "Script can fail at operation #" + str(i) + ". Use cf_ at the beginning of its name: " + statement_name)
        save_statement(file, opcode, no_variables, statement, variable_list, variable_uses, local_vars, local_var_uses, tag_uses, quick_strings)

    if (store_script_param_1_uses > 1):
        print(strs.error + "The operation store_script_param_1 is used more than once: " + colors.lred + str(statement_name))
    if (store_script_param_2_uses > 1):
        print(strs.error + "The operation store_script_param_2 is used more than once: " + colors.lred + str(statement_name))
    if (current_depth > 0):
        print(strs.error + "Not enough try_end operation used on script: " + colors.lred + str(statement_name))

    i = 0
    while (i < len(local_vars)):
        if (local_var_uses[i] == 0 and not(local_vars[i].startswith("unused"))):
            print(strs.warn + "Local variable never used: " + local_vars[i] + ", at: " + colors.lred + str(statement_name))
        i += 1

    if (len(local_vars) > 128):
        print(strs.warn + "Script uses more than 128 (" + str(len(local_vars)) + ") local wariables: " + colors.lred + str(statement_name))

def save_simple_triggers(file, temps, variable_list, variable_uses, tag_uses, quick_strings):
  file.write("%d\n"%len(temps))
  for temp in temps:
    file.write("%f "%(temp[0]))
    save_statement_block(file, 0, 1, temp[1], variable_list, variable_uses, tag_uses, quick_strings)
    file.write("\n")
  file.write("\n")

def clear_module():
##    files = [file for file in glob.glob("*.pyc")]
##    for file in files:
##        os.remove(file)
    if os.path.exists("./__pycache__"):
        os.system("rm -rf ./__pycache__")
    if os.path.exists("./ids/__pycache__"):
        os.system("rm -rf ./ids/__pycache__")
    if os.path.exists("./headers/__pycache__"):
        os.system("rm -rf ./headers/__pycache__")

def is_lhs_operation(op_code):
  found = 0
  if op_code in lhs_operations:
      return 1
  return 0

def is_lhs_operation_for_global_vars(op_code):
  found = 0
  if op_code in lhs_operations:
      return 1
  if op_code in global_lhs_operations:
      return 1
  return 0

def is_can_fail_operation(op_code):
  found = 0
  if op_code in can_fail_operations:
      return 1
  return 0

def add_variable(variable_string, variables_list, variable_uses):
  found = 0
  for i_t in range(len(variables_list)):
    if variable_string == variables_list[i_t]:
      found = 1
      variable_uses[i_t] = variable_uses[i_t] - 1
      break
  if not found:
    variables_list.append(variable_string)
    variable_uses.append(-1)

def compile_global_vars_in_statement(statement, variable_list, variable_uses):
  opcode = 0
  if ((type(statement) is not list) and (type(statement) is not tuple)):
    opcode = statement
  else:
    opcode = statement[0]
    if (is_lhs_operation_for_global_vars(opcode) == 1):
      if (len(statement) > 1):
        param = statement[1]
        if (type(param) is str):
          if (statement[1][0] == '$'):
            add_variable(statement[1][1:], variable_list, variable_uses)

def compile_global_vars(statement_block, variable_list, variable_uses):
  for statement in statement_block:
    compile_global_vars_in_statement(statement, variable_list, variable_uses)

def save_variables(variables_list, variable_uses):
  file = open(export_dir + "variables.txt", "w")
  for i in range(len(variables_list)):
    file.write("%s\n"%variables_list[i])
  file.close()
  file = open(export_dir + "variable_uses.txt","w")
  for i in range(len(variables_list)):
    file.write("%d\n"%variable_uses[i])
  file.close()

def save_quick_strings(quick_strings):
    file = open(export_dir + "quick_strings.txt", "w")
    langFile = open(language_dir + "quick_strings.csv", "w")

    file.write("%d\n"%len(quick_strings))
    for i in range(len(quick_strings)):
        langFile.write("%s|%s\n"%(quick_strings[i][0], quick_strings[i][1].replace("_"," ")))
        file.write("%s %s\n"%(quick_strings[i][0],replace_spaces(quick_strings[i][1])))
    file.close()
    langFile.close()

def save_tag_uses(tag_uses):
    file = open(export_dir + "tag_uses.txt","w")
    for i in range(len(tag_uses)):
        for j in range(len(tag_uses[i])):
            file.write("%d %d %d;" % (i, j, tag_uses[i][j]))
        file.write("\n")
    file.close()
# Global Definitions - End

def compile_init():
    ## Initialization:
    start_time = int(round(time.time() * 1000))
    print(colors.dgreen + "Compiling module...")
    if (os.path.isfile(export_dir + "tag_uses.txt")):
        os.remove(export_dir + "tag_uses.txt")

    if (os.path.isfile(export_dir + "quick_strings.txt")):
        os.remove(export_dir + "quick_strings.txt")

    if (os.path.isfile(export_dir + "variables.txt")):
        os.remove(export_dir + "variables.txt")

    if (os.path.isfile(export_dir + "variable_uses.txt")):
        os.remove(export_dir + "variable_uses.txt")

    variables = []
    variable_uses = []
    if (os.path.isfile("variables.txt")):
        file = open("variables.txt", "r")
        var_list = file.readlines()
        file.close()
        for variable in var_list:
            #var = string.strip(variable)
            var = variable.strip()
            if var:
                variables.append(var)
                variable_uses.append(int(1))
        save_variables(variables, variable_uses)
    else:
        print(strs.error + "variables.txt not found in your module system, creating a new one...")

    tag_uses = []
    for i in range(tags_end):
        sub_tag_uses = []
        tag_uses.append(sub_tag_uses)

    if (os.path.isfile(export_dir + "tag_uses.txt")):
        file = open(export_dir + "tag_uses.txt", "r")
        var_list = file.readlines()
        file.close()
        for variable in var_list:
            ##var = string.strip(variable).split(';')
            var = variable.strip().split(';')
            if var:
                for v1 in var:
                    v2 = v1.split(' ')
                    if len(v2) >= 3:
                        if len(tag_uses[int(v2[0])]) <= int(v2[1]):
                            num_to_add = int(v2[1]) + 1 - len(tag_uses[int(v2[0])])
                            for i in range(num_to_add):
                                tag_uses[int(v2[0])].append(0)
                        tag_uses[int(v2[0])][int(v2[1])] = int(v2[2])

    quick_strings = []
    if (os.path.isfile(export_dir + "quick_strings.txt")):
        file = open(export_dir + "quick_strings.txt", "r")
        str_list = file.readlines()
        file.close()

        for arg in str_list:
            ##arg = string.strip(arg)
            arg = arg.strip()
            if arg:
                args = arg.split(' ')
                if len(args) == 2:
                    quick_strings.append(args)

    ## Global Variables:
    temp = []
    temp_type = type(temp)
    for var in reserved_variables:
        try:
            add_variable(var, variables, variable_uses)
        except:
            print(strs.error + "Error in reserved variable %s."%var)

    for trigger in triggers:
        try:
            compile_global_vars(trigger[3], variables, variable_uses)
            compile_global_vars(trigger[4], variables, variable_uses)
        except:
            print(strs.error + "Error in trigger " + str(trigger))

    for scene_prop in scene_props:
        try:
            sp_triggers = scene_prop[4]
            for sp_trigger in sp_triggers:
                compile_global_vars(sp_trigger[1], variables, variable_uses)
        except:
            print(strs.error + "Error in scene prop " + str(scene_prop))

    for sentence in dialogs:
        try:
            compile_global_vars(sentence[2], variables, variable_uses)
            compile_global_vars(sentence[5], variables, variable_uses)
        except:
            print(strs.error + "Error in dialog " + str(sentence))

    for game_menu in game_menus:
        try:
            compile_global_vars(game_menu[4], variables, variable_uses)
            menu_items = game_menu[5]
            for menu_item in menu_items:
                compile_global_vars(menu_item[1], variables, variable_uses)
                compile_global_vars(menu_item[3], variables, variable_uses)
        except:
            print(strs.error + "Error in game menu " + str(game_menu))

    for mission_template in mission_templates:
        try:
            mt_triggers = mission_template[5]
            for mt_trigger in mt_triggers:
                compile_global_vars(mt_trigger[3], variables, variable_uses)
                compile_global_vars(mt_trigger[4], variables, variable_uses)
        except:
            print(strs.error + "Error in mission template " + str(mission_template))

    for presentation in presentations:
        try:
            prsnt_triggers = presentation[3]
            for prsnt_trigger in prsnt_triggers:
                compile_global_vars(prsnt_trigger[1], variables, variable_uses)
        except:
            print(strs.error + "Error in presentation " + str(presentation))

    for i_script in range(len(scripts)):
        try:
            func = scripts[i_script]
            if (type(func[1]) == temp_type):
                compile_global_vars(func[1], variables, variable_uses)
            else:
                compile_global_vars(func[2], variables, variable_uses)
        except:
            print(strs.error + "Error in script " + str(func))

    for simple_trigger in simple_triggers:
        try:
            compile_global_vars(simple_trigger[1], variables, variable_uses)
        except:
            print(strs.error + "Error in simple trigger " + str(simple_trigger))

    try:
        save_variables(variables, variable_uses)
    except:
        print(strs.error + "An error occured while saving variables.")
    
    #Item Modifiers:
    langFile = open(language_dir + "item_modifiers.csv", "w")
    file = open(data_dir + "item_modifiers.txt", "w")
    for imod in imods:
        if (len(imod) > 4):
            file.write("imod_%s %s %.6f %.6f\n"%(convert_to_identifier(imod[0]), replace_spaces(imod[4].replace("%n", imod[1])), imod[2], imod[3]))
            langFile.write("imod_%s|%s\n"%(convert_to_identifier(imod[0]), imod[4].replace("%n", imod[1])))
        else:
            file.write("imod_%s %s %.6f %.6f\n"%(convert_to_identifier(imod[0]), replace_spaces(imod[1]) + "_%s", imod[2], imod[3]))
            langFile.write("imod_%s|%s\n"%(convert_to_identifier(imod[0]), imod[1] + " %s"))
    file.close()
    langFile.close()

    #Map Icons:
    file = open(export_dir + "map_icons.txt", "w")
##    ifile = open("./ID_map_icons.py", "w")
    file.write("map_icons_file version 1\n")
    file.write("%d\n"%len(map_icons))
    for i_map_icon in range(len(map_icons)):
        map_icon = map_icons[i_map_icon]
        temp = []
        if (len(map_icon) >= 8):
            file.write("%s %d %s %f %d %f %f %f "%(map_icon[0],map_icon[1],map_icon[2],map_icon[3],map_icon[4],map_icon[5],map_icon[6],map_icon[7]))
            if (len(map_icon) == 9):
                temp = map_icon[8]
        else:
            file.write("%s %d %s %f %d 0 0 0 "%(map_icon[0],map_icon[1],map_icon[2],map_icon[3],map_icon[4]))
            if (len(map_icon) == 6):
                temp = map_icon[5]
##        ifile.write("icon_%s = %d\n"%(map_icon[0], i_map_icon))
        save_simple_triggers(file, temp, variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
##    ifile.close()

    #Strings:
    file = open(export_dir + "strings.txt", "w")
    langFile = open(language_dir + "game_strings.csv", "w")
##    ifile = open("./ID_strings.py", "w")
    file.write("stringsfile version 1\n")
    file.write("%d\n"%len(strings))
    for i_string in range(len(strings)):
        arg = strings[i_string]
        langFile.write("str_%s|%s\n"%(convert_to_identifier(arg[0]), arg[1]))
        file.write("str_%s %s\n"%(convert_to_identifier(arg[0]), replace_spaces(arg[1])))
##        ifile.write("str_%s = %d\n"%(convert_to_identifier(arg[0]), i_string))
##    ifile.write("\n\n")
    file.close()
    langFile.close()
##    ifile.close()

    #Skills:
    file = open(export_dir + "skills.txt", "w")
##    ifile = open("./ID_skills.py", "w")
    langFile = open(language_dir + "skills.txt", "w")

    file.write("%d\n"%len(skills))
    for i_skill in range(len(skills)):
        skill = skills[i_skill]
        langFile.write("skl_%s|%s\n"%(skill[0], skill[1]))
        langFile.write("skl_%s_desc|%s\n"%(skill[0], skill[4]))
        file.write("skl_%s %s %d %d %s\n"%(skill[0], replace_spaces(skill[1]), skill[2], skill[3], replace_spaces(skill[4])))
##        ifile.write("skl_%s = %d\n"%(skill[0], i_skill))
##    ifile.write("\n\n")
    file.close()
    langFile.close()
##    ifile.close()

    #Musics:
    file = open(export_dir + "music.txt", "w")
##    ifile = open("./ID_music.py", "w")
    file.write("%d\n"%len(tracks))
    for i_track in range(len(tracks)):
        track = tracks[i_track]
        file.write("%s %d %d\n"%(track[1], track[2], (track[2] | track[3])))
##        ifile.write("track_%s = %d\n"%(track[0], i_track))
    file.close()
##    ifile.close()

    #Animations:
    file = open(export_dir + "actions.txt", "w")
##    ifile = open("./ID_animations.py", "w")

    args = compile_action_sets(animations)
##    args = animations
    file.write("%d\n"%len(args))
    for i_action_code in range(len(args)):
##        ifile.write("anim_%s = %d\n"%(args[i_action_code], i_action_code))
        action_found = 0
        for action in animations:
            if action[0] == i_action_code:
                file.write(" %s %d %d  %d\n"%(args[i_action_code], action[1], action[2], len(action) - 3))
                for elem in action[3:]:
                    file.write("  %f %s %d %d %d "%(elem[0], elem[1], elem[2], elem[3], elem[4]))
                    if (len(elem) > 7):
                        file.write("%d %f %f %f  %f \n"%(elem[5], elem[6][0], elem[6][1], elem[6][2], elem[7]))
                    elif (len(elem) > 6):
                        file.write("%d %f %f %f 0.0 \n"%(elem[5], elem[6][0], elem[6][1], elem[6][2]))
                    elif (len(elem) > 5):
                        file.write("%d 0.0 0.0 0.0 0.0 \n"%elem[5])
                    else:
                        file.write("0 0.0 0.0 0.0 0.0 \n")
                action_found = 1
                break
        if not action_found:
            file.write(" none 0 0\n")
##    ifile.write("\n\n")
    file.close()
##    ifile.close()
    args = decompile_action_sets(animations, args)

    #Meshes:
    file = open(export_dir + "meshes.txt", "w")
##    ifile = open("./ID_meshes.py", "w")
    file.write("%d\n"%len(meshes))
    for i_mesh in range(len(meshes)):
        mesh = meshes[i_mesh]
        file.write("mesh_%s %d %s %f %f %f %f %f %f %f %f %f\n"%(mesh[0], mesh[1], replace_spaces(mesh[2]), mesh[3], mesh[4], mesh[5], mesh[6], mesh[7], mesh[8], mesh[9], mesh[10], mesh[11]))
##        ifile.write("mesh_%s = %d\n"%(mesh[0], i_mesh))
##    ifile.write("\n\n")
    file.close()
##    ifile.close()

    #Sounds:
    file = open(export_dir + "sounds.txt", "w")
##    ifile = open("./ID_sounds.py", "w")
    args = compile_sounds(sounds)
    file.write("soundsfile version 3\n")
    file.write("%d\n"%len(args))
    for sound_sample in args:
        file.write(" %s %d\n"%sound_sample)
    file.write("%d\n"%len(sounds))
    for i_sound in range(len(sounds)):
        sound = sounds[i_sound]
##        ifile.write("snd_%s = %d\n"%(sound[0], i_sound))
        file.write("snd_%s %d %d "%(sound[0], sound[1], len(sound[2])))
        sample_list = sound[2]
        for sample in sample_list:
            file.write("%d %d "%(sample[0], sample[1]))
        file.write("\n")
##    ifile.write("\n\n")
    file.close()
##    ifile.close()

    #Skins:
    file = open(export_dir + "skins.txt", "w")
    ifile = open("./ids/ID_skins.py", "w")
    langFile = open(language_dir + "skins.csv", "w")
    file.write("skins_file version 1\n")
    skn = skins
    if (len(skins) > 16):
        skn = skins[0:15]
    file.write("%d\n"%len(skn))
    for i_skin in range(len(skn)):
        skin = skn[i_skin]
        blood_particles_1 = 0
        blood_particles_2 = 0
        constraints = []
        if len(skin) > 15:
            blood_particles_1 = skin[15]
        if len(skin) > 16:
            blood_particles_2 = skin[16]
        if len(skin) > 17:
            constraints = skin[17]

        ifile.write("skin_%s = %d\n"%(skin[0], i_skin))
        file.write("%s %d\n %s %s %s\n %s %d "%(skin[0], skin[1], skin[2], skin[3], skin[4], skin[5], len(skin[6])))
        for face_key in skin[6]:
            file.write("skinkey_%s %d %d %f %f %s "%(convert_to_identifier(face_key[4]), face_key[0], face_key[1], face_key[2], face_key[3], replace_spaces(face_key[4])))
            langFile.write("skinkey_%s|%s\n"%(convert_to_identifier(face_key[4]), face_key[4]))
        file.write("\n%d\n"%len(skin[7]))

        for mesh_name in skin[7]:
            file.write(" %s "%mesh_name)
        file.write("\n %d\n"%len(skin[8]))
        for bnm in skin[8]:
            file.write("  %s\n"%bnm)
        file.write("\n")
        write_textures(file, skin[9])
        write_textures(file, skin[10])
        write_face_tex(file, skin[11])
        write_voices(file, skin[12])
        file.write(" %s %f "%(skin[13], skin[14]))
        file.write("\n%d %d\n"%(blood_particles_1, blood_particles_2))
        file.write("%d\n"%len(constraints))
        for constraint in constraints:
            file.write("\n%f %d %d "%(constraint[0], constraint[1], len(constraint) - 2))
            for i_pair in range(len(constraint)):
                if i_pair > 1:
                    file.write(" %f %d"%(constraint[i_pair][0], constraint[i_pair][1]))
        file.write("\n")
    ifile.write("\n\n")
    file.close()
    ifile.close()
    langFile.close()

    #Factions:
    file = open(export_dir + "factions.txt", "w")
##    ifile = open("./ID_factions.py", "w")
    langFile = open(language_dir + "factions.csv", "w")
    file.write("factionsfile version 1\n")
    file.write("%d\n"%len(factions))
    relations = compile_relations()
    for i_faction in range(len(factions)):
        faction = factions[i_faction]
        fac_color = 0xAAAAAA
        if len(faction) == 7:
            fac_color = faction[6]
##        ifile.write("fac_%s = %d\n"%(convert_to_identifier(faction[0]), i_faction))
        file.write("fac_%s %s %d %d \n"%(convert_to_identifier(faction[0]), replace_spaces(faction[1]), faction[2], fac_color))
        langFile.write("fac_%s|%s\n"%(convert_to_identifier(faction[0]), faction[1]))
        for reln in relations[i_faction]:
            file.write(" %f "%reln)
        file.write("\n")
        ranks = []
        if (len(faction) > 5):
            ranks = faction[5]
        file.write("%d "%len(ranks))
        for rank in ranks:
            file.write(" %s "%replace_spaces(rank))
##    ifile.write("\n\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Items:
    file = open(export_dir + "item_kinds1.txt", "w")
##    ifile = open("./ID_items.py", "w")
    langFile = open(language_dir + "item_kinds.csv", "w")
    file.write("itemsfile version 3\n")
    file.write("%d\n"%len(items))
    for i_item in range(len(items)):
        item = items[i_item]
##        ifile.write("itm_%s = %d\n"%(convert_to_identifier(item[0]), i_item))
        langFile.write("itm_%s|%s\n"%(convert_to_identifier(item[0]), item[1]))
        langFile.write("itm_%s_pl|%s\n"%(convert_to_identifier(item[0]), item[1]))
        file.write(" itm_%s %s %s %d "%(convert_to_identifier(item[0]), replace_spaces(item[1]), replace_spaces(item[1]), len(item[2])))
        variety_list = item[2]
        for variety in variety_list:
            file.write(" %s %d "%(variety[0], variety[1]))
        file.write(" %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n"%(item[3], item[4], item[5], item[7], get_weight(item[6]), get_abundance(item[6]), get_head_armor(item[6]), get_body_armor(item[6]), get_leg_armor(item[6]), get_difficulty(item[6]), get_hit_points(item[6]), get_speed_rating(item[6]), get_missile_speed(item[6]), get_weapon_length(item[6]), get_max_ammo(item[6]), get_thrust_damage(item[6]), get_swing_damage(item[6])))
        if len(item) > 9:
            file.write(" %d\n"%len(item[9]))
            for item_faction in item[9]:
                file.write(" %d"%item_faction)
            file.write("\n")
        else:
            file.write(" 0\n")
        trigger_list = []
        if len(item) > 8:
            trigger_list = item[8]
        save_simple_triggers(file, trigger_list, variables, variable_uses, tag_uses, quick_strings)
    file.close()
##    ifile.close()
    langFile.close()

    #Scenes:
    file = open(export_dir + "scenes.txt", "w")
##    ifile = open("./ID_scenes.py", "w")
    file.write("scenesfile version 1\n")
    file.write(" %d\n"%len(scenes))
    for i_scene in range(len(scenes)):
        scene = scenes[i_scene]
##        ifile.write("scn_%s = %d\n"%(convert_to_identifier(scene[0]), i_scene))
        file.write("scn_%s %s %d %s %s %f %f %f %f %f %s "%(convert_to_identifier(scene[0]), replace_spaces(scene[0]), scene[1], scene[2], scene[3], scene[4][0], scene[4][1], scene[5][0], scene[5][1], scene[6], scene[7]))
        passages = scene[8]
        file.write("\n  %d "%len(passages))
        for passage in passages:
            write_passage(file, scenes, passage)
        chest_troops = scene[9]
        file.write("\n  %d "%len(chest_troops))
        for chest_troop in chest_troops:
            troop_no = find_troop(troops, chest_troop)
            if (troop_no < 0):
                print(strs.error + "Unable to find chest troop: " + str(chest_troop))
                troop_no = 0
            file.write(" %d "%troop_no)
        file.write("\n")
        if (len(scene) > 10):
            file.write(" %s "%scene[10])
        else:
            file.write(" 0 ")
        file.write("\n")
    file.close()
##    ifile.close()

    #Troops:
    file = open(export_dir + "troops.txt", "w")
##    ifile = open("./ID_troops.py", "w")
    langFile = open(language_dir + "troops.csv", "w")
    file.write("troopsfile version 2\n")
    file.write("%d \n"%len(troops))
    for i_troop in range(len(troops)):
        troop = troops[i_troop]
        troop_len = len(troop)
        if troop_len == 11:
            troop[11:11] = [0, 0, 0, 0, 0]
        elif troop_len == 12:
            troop[12:12] = [0, 0, 0, 0]
        elif troop_len == 13:
            troop[13:13] = [0, 0, 0]
        elif troop_len == 14:
            troop[14:14] = [0, 0]
        elif troop_len == 15:
            troop[15:15] = [0]

        langFile.write("trp_%s|%s\n"%(convert_to_identifier(troop[0]), troop[1]))
        langFile.write("trp_%s_pl|%s\n"%(convert_to_identifier(troop[0]), troop[2]))
##        ifile.write("trp_%s = %d\n"%(convert_to_identifier(troop[0]), i_troop))
        file.write("trp_%s %s %s %s %d %d %d %d %d %d\n  "%(convert_to_identifier(troop[0]), replace_spaces(troop[1]), replace_spaces(troop[2]), replace_spaces(str(troop[13])), troop[3], troop[4], troop[5], troop[6], troop[14], troop[15]))
        inventory_list = troop[7]
        for inventory_item in inventory_list:
            if isinstance(inventory_item, list) or isinstance(inventory_item, tuple):
                file.write("%d %d "%(inventory_item[0], inventory_item[1]<<24))
            else:
                file.write("%d 0 "%inventory_item)
        for i in range(64 - len(inventory_list)):
            file.write("-1 0 ")
        file.write("\n ")
        attrib = troop[8]
        strength = (attrib & 0xff)
        agility = ((attrib >> 8) & 0xff)
        intelligence = ((attrib >> 16) & 0xff)
        charisma = ((attrib >> 24) & 0xff)
        starting_level = (attrib >> level_bits) & level_mask
        file.write(" %d %d %d %d %d\n"%(strength, agility, intelligence, charisma, starting_level))
        wp_word = troop[9]
        for wp in range(7):
            wp_level = wp_word & 0x3FF
            file.write(" %d"%wp_level)
            wp_word = wp_word >> 10
        file.write("\n")

        skill_array = troop[10]
        for i in range(6):
            file.write("%d "%((skill_array >> (i * 32)) & 0xffffffff))
        file.write("\n  ")

        face_keys = [troop[11], troop[12]]
        for fckey in (face_keys):
            word_keys = []
            for word_no in range(4):
                word_keys.append((fckey >> (64 * word_no)) & 0xFFFFFFFFFFFFFFFF)
            for word_no in range(4):
                file.write("%d "%(word_keys[3 - word_no]))
        file.write("\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Particles:
    file = open(export_dir + "particle_systems.txt", "w")
##    ifile = open("./ID_particle_systems.py", "w")
    file.write("particle_systemsfile version 1\n")
    file.write("%d\n"%len(particle_systems))
    for i_psys in range(len(particle_systems)):
        psys = particle_systems[i_psys]
##        ifile.write("psys_%s = %d\n"%(psys[0], i_psys))
        file.write("psys_%s %d %s  %d %f %f %f %f %f \n"%(psys[0], psys[1], psys[2], psys[3], psys[4], psys[5], psys[6], psys[7], psys[8]))
        save_psys_keys(file, psys[9], psys[10])
        save_psys_keys(file, psys[11], psys[12])
        save_psys_keys(file, psys[13], psys[14])
        save_psys_keys(file, psys[15], psys[16])
        save_psys_keys(file, psys[17], psys[18])
        file.write("%f %f %f  "%(psys[19][0], psys[19][1], psys[19][2]))
        file.write("%f %f %f  "%(psys[20][0], psys[20][1], psys[20][2]))
        file.write("%f \n"%psys[21])
        if len(psys) >= 23:
            file.write("%f "%psys[22])
        else:
            file.write("0.0 ")
        if len(psys) >= 24:
            file.write("%f "%psys[23])
        else:
            file.write("0.0 ")
        file.write("\n")
    file.close()
##    ifile.close()

    #Scene Props:
    file = open(export_dir + "scene_props.txt", "w")
##    ifile = open("./ID_scene_props.py", "w")
    file.write("scene_propsfile version 1\n")
    file.write(" %d\n"%len(scene_props))
    for i_scene_prop in range(len(scene_props)):
        scene_prop = scene_props[i_scene_prop]
##        ifile.write("spr_%s = %d\n"%(scene_prop[0], i_scene_prop))
        file.write("spr_%s %d %d %s %s "%(scene_prop[0], scene_prop[1], get_spr_hit_points(scene_prop[1]), scene_prop[2], scene_prop[3]))
        save_simple_triggers(file, scene_prop[4], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
##    ifile.close()

    #Tableau Material:
    file = open(export_dir + "tableau_materials.txt", "w")
##    ifile = open("./ID_tableau_materials.py", "w")
    file.write("%d\n"%len(tableaus))
    for i_tableau in range(len(tableaus)):
        tableau = tableaus[i_tableau]
        file.write("tab_%s %d %s %d %d %d %d %d %d"%(tableau[0], tableau[1], tableau[2], tableau[3], tableau[4], tableau[5], tableau[6], tableau[7], tableau[8]))
##        ifile.write("tableau_%s = %d\n"%(tableau[0], i_tableau))
        save_statement_block(file, 0, 1, tableau[9], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
##    ifile.close()

    #Presentations:
    file = open(export_dir + "presentations.txt", "w")
##    ifile = open("./ID_presentations.py", "w")
    file.write("presentationsfile version 1\n")
    file.write(" %d\n"%len(presentations))
    for i_presentation in range(len(presentations)):
        presentation = presentations[i_presentation]
##        ifile.write("prsnt_%s = %d\n"%(presentation[0], i_presentation))
        file.write("prsnt_%s %d %d "%(presentation[0], presentation[1], presentation[2]))
        save_simple_triggers(file, presentation[3], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
##    ifile.close()

    #Party Templates:
    file = open(export_dir + "party_templates.txt", "w")
##    ifile = open("./ID_party_templates.py", "w")
    langFile = open(language_dir + "party_templates.csv", "w")
    file.write("partytemplatesfile version 1\n")
    file.write("%d\n"%len(party_templates))
    for i_party_template in range(len(party_templates)):
        party_template = party_templates[i_party_template]
        langFile.write("pt_%s|%s\n"%(convert_to_identifier(party_template[0]), party_template[1]))
##        ifile.write("pt_%s = %d\n"%(convert_to_identifier(party_template[0]), i_party_template))
        file.write("pt_%s %s %d %d %d %d "%(convert_to_identifier(party_template[0]), replace_spaces(party_template[1]), party_template[2], party_template[3], party_template[4], party_template[5]))
        members = party_template[6]
        if len(members) > 6:
            print(strs.error + "Number of template members exceeds 6 " + party_template[0])
            members = members[0:6]
        for party_template_member in members:
            save_party_template_troop(file, party_template_member)
        for i in range(6 - len(members)):
            save_party_template_troop(file, 0)
        file.write("\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Parties:
    file = open(export_dir + "parties.txt", "w")
##    ifile = open("./ID_parties.py", "w")
    langFile = open(language_dir + "parties.csv", "w")
    file.write("partiesfile version 1\n")
    file.write("%d %d\n"%(len(parties), len(parties)))
    for i_party in range(len(parties)):
        party = parties[i_party]
##        ifile.write("p_%s = %d\n"%(convert_to_identifier(party[0]), i_party))
        langFile.write("p_%s|%s\n"%(convert_to_identifier(party[0]), party[1]))
        file.write(" 1 %d %d "%(i_party, i_party))
        file.write("p_%s %s %d "%(convert_to_identifier(party[0]), replace_spaces(party[1]), party[2]))

        menu_no = 0
        menu_param = party[3]
        if (type(menu_param) is str):
            menu_no = find_object(game_menus, menu_param)
            if menu_no < 0:
                print(strs.error + "Unable to find menu " + menu_param)
        else:
            menu_no = menu_param
        file.write("%d "%menu_no)
        file.write("%d %d %d %d %d "%(party[4], party[5], party[6], party[6], party[7]))

        ai_behavior_object = 0
        ai_param = party[8]
        if (type(ai_param) is str):
            ai_behavior_object = find_object(parties, ai_param)
            if (ai_behavior_object < 0):
                print(strs.error + "Unable to find party " + ai_param)
        else:
            ai_behavior_object = ai_param
        file.write("%d %d "%(ai_behavior_object, ai_behavior_object))
        
        position = party[9]
        file.write("%f %f %f %f %f %f 0.0 "%(position[0], position[1], position[0], position[1], position[0], position[1]))

        member_list = party[10]
        file.write("%d "%len(member_list))
        for member in member_list:
            file.write("%d %d 0 %d "%(member[0], member[1], member[2]))

        bearing = 0.0
        if len(party) > 11:
            bearing = (3.1415926 / 180.0) * party[11]
        file.write("\n%f\n"%bearing)
    file.close()
##    ifile.close()
    langFile.close()

    #Quests:
    file = open(export_dir + "quests.txt", "w")
##    ifile = open("./ID_quests.py", "w")
    langFile = open(language_dir + "quests.csv", "w")
    file.write("questsfile version 1\n")
    file.write("%d\n"%len(quests))
    for i_quest in range(len(quests)):
        quest = quests[i_quest]
        langFile.write("qst_%s|%s\n"%(quest[0], quest[1]))
##        ifile.write("qst_%s = %d\n"%(quest[0], i_quest))
##        ifile.write("qsttag_%s = %d\n\n"%(quest[0], opmask_quest_index|i_quest))
        file.write("qst_%s %s %d %s \n"%(quest[0], replace_spaces(quest[1]), quest[2], replace_spaces(quest[3])))
##    ifile.write("\n\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Info Pages:
    file = open(export_dir + "info_pages.txt", "w")
##    ifile = open("./ID_info_pages.py", "w")
    langFile = open(language_dir + "info_pages.csv", "w")
    file.write("infopagesfile version 1\n")
    file.write("%d\n"%len(info_pages))
    for i_info_page in range(len(info_pages)):
        info_page = info_pages[i_info_page]
        langFile.write("ip_%s|%s\n"%(info_page[0], info_page[1]))
        langFile.write("ip_%s_text|%s\n"%(info_page[0], info_page[2]))
##        ifile.write("ip_%s = %d\n"%(info_page[0], i_info_page))
        file.write("ip_%s %s %s\n"%(info_page[0], replace_spaces(info_page[1]), replace_spaces(info_page[2])))
##    ifile.write("\n\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Scripts:
    file = open(export_dir + "scripts.txt", "w")
##    ifile = open("./ID_scripts.py", "w")
    file.write("scriptsfile version 1\n")
    file.write("%d\n"%len(scripts))
    for i_script in range(len(scripts)):
        func = scripts[i_script]
##        ifile.write("script_%s = %d\n"%(convert_to_identifier(func[0]), i_script))
        if (type(func[1]) == temp_type):
            file.write("%s -1\n"%convert_to_identifier(func[0]))
            save_statement_block(file, convert_to_identifier(func[0]), 0, func[1], variables, variable_uses, tag_uses, quick_strings)
        else:
            file.write("%s %f\n"%(convert_to_identifier(func[0]), func[1]))
            save_statement_block(file, convert_to_identifier(func[0]), 0, func[2], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
##    ifile.write("\n\n")
    file.close()
##    ifile.close()

    #Mission Templates:
    file = open(export_dir + "mission_templates.txt", "w")
##    ifile = open("./ID_mission_templates.py", "w")
    file.write("missionsfile version 1\n")
    file.write(" %d\n"%len(mission_templates))
    for i_mission_template in range(len(mission_templates)):
        mission_template = mission_templates[i_mission_template]
##        ifile.write("mst_%s = %d\n"%(convert_to_identifier(mission_template[0]), i_mission_template))
        file.write("mst_%s %s %d  %d\n"%(convert_to_identifier(mission_template[0]), convert_to_identifier(mission_template[0]), mission_template[1], mission_template[2]))
        file.write("%s \n"%replace_spaces(mission_template[3]))
        file.write("\n%d "%len(mission_template[4]))
        for group in mission_template[4]:
            save_mission_template_group(file, group)
        save_triggers(file, convert_to_identifier(mission_template[0]), mission_template[5], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
##    ifile.close()

    #Game Menus:
    file = open(export_dir + "menus.txt", "w")
##    ifile = open("./ID_menus.py", "w")
    langFile = open(language_dir + "game_menus.csv", "w")
    file.write("menusfile version 1\n")
    file.write(" %d\n"%len(game_menus))
    for i_game_menu in range(len(game_menus)):
        game_menu = game_menus[i_game_menu]
##        ifile.write("menu_%s = %d\n"%(game_menu[0], i_game_menu))
        langFile.write("menu_%s|%s\n"%(game_menu[0], game_menu[2]))
        file.write("menu_%s %d %s %s"%(game_menu[0], game_menu[1], replace_spaces(game_menu[2]), game_menu[3]))
        save_statement_block(file, 0, 1, game_menu[4], variables, variable_uses, tag_uses, quick_strings)
        menu_items = game_menu[5]
        file.write("%d\n"%len(menu_items))
        for menu_item in menu_items:
            file.write(" mno_%s "%menu_item[0])
            langFile.write("mno_%s|%s\n"%(menu_item[0], menu_item[2]))
            save_statement_block(file, 0, 1, menu_item[1], variables, variable_uses, tag_uses, quick_strings)
            file.write(" %s "%replace_spaces(menu_item[2]))
            save_statement_block(file, 0, 1, menu_item[3], variables, variable_uses, tag_uses, quick_strings)
            door_name = "."
            if len(menu_item) > 4:
                door_name = menu_item[4]
            file.write(" %s "%replace_spaces(door_name))
        file.write("\n")
    file.close()
##    ifile.close()
    langFile.close()

    #Simple Triggers:
    file = open(export_dir + "simple_triggers.txt", "w")
    file.write("simple_triggers_file version 1\n")
    file.write("%d\n"%len(simple_triggers))
    for i_simple_trigger in range(len(simple_triggers)):
        simple_trigger = simple_triggers[i_simple_trigger]
        file.write("%f "%simple_trigger[0])
        save_statement_block(file, 0, 1, simple_trigger[1], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()

    #Triggers:
    file = open(export_dir + "triggers.txt", "w")
    file.write("triggersfile version 1\n")
    file.write("%d\n"%len(triggers))
    for i in range(len(triggers)):
        trigger = triggers[i]
        file.write("%f %f %f "%(trigger[0],trigger[1],trigger[2]))
        save_statement_block(file,0,1,trigger[3], variables, variable_uses, tag_uses, quick_strings)
        save_statement_block(file,0,1,trigger[4], variables, variable_uses, tag_uses, quick_strings)
        file.write("\n")
    file.close()
    
    #Dialogs:
    file = open(export_dir + "conversation.txt", "w")
    langFile = open(language_dir + "dialog.csv", "w")
    file.write("dialogsfile version 2\n")
    file.write("%d\n"%len(dialogs))
    (input_states,output_states) = compile_sentence_tokens(dialogs)
    auto_ids = {}
    for i_sentence in range(len(dialogs)):
        sentence = dialogs[i_sentence]
        try:
            dialog_id = create_autoid(sentence, auto_ids)
            file.write("%s %d %d "%(dialog_id, sentence[0], input_states[i_sentence]))
            langFile.write("%s|%s"%(dialog_id, sentence[3]))
            save_statement_block(file, 0, 1, sentence[2], variables, variable_uses, tag_uses, quick_strings)
            file.write("%s "%replace_spaces(sentence[3]))
            if(len(sentence[3]) == 0):
                file.write("NO_TEXT ")
                langFile.write("No Text")
                print(strs.warn + "Dialog " + dialog_id + " has no text.")
            file.write(" %d "%output_states[i_sentence])
            save_statement_block(file, 0, 1, sentence[5], variables, variable_uses, tag_uses, quick_strings)
            if (len(sentence) > 6):
                file.write("%s "%sencente[6])
            else:
                file.write("NO_VOICEOVER ")
                
            file.write("\n")
            langFile.write("\n")
        except:
            print(strs.error + "Error in dialog line " + str(sentence))
    file.close()
    langFile.close()

    #Post fx:
    file = open(export_dir + "postfx.txt", "w")
##    ifile = open("./ID_postfx_params.py", "w")
    file.write("postfx_paramsfile version 1\n")
    file.write("%d\n"%len(postfx_params))
    for i_postfx_param in range(len(postfx_params)):
        postfx_param = postfx_params[i_postfx_param]
##        ifile.write("pfx_%s = %d\n"%(postfx_param[0], i_postfx_param))
        file.write("pfx_%s %d %d"%(postfx_param[0], postfx_param[1], postfx_param[2]))
        params_list1 = postfx_param[3]
        params_list2 = postfx_param[4]
        params_list3 = postfx_param[5]
        file.write("  %f %f %f %f"%(params_list1[0], params_list1[1], params_list1[2], params_list1[3]))
        file.write("  %f %f %f %f"%(params_list2[0], params_list2[1], params_list2[2], params_list2[3]))
        file.write("  %f %f %f %f\n"%(params_list3[0], params_list3[1], params_list3[2], params_list3[3]))
##    ifile.write("\n\n")
    file.close()
##    ifile.close()
    
    #Not used global variables:
    variables = []
    variable_uses = []
    if (os.path.isfile("variables.txt")):
        file = open("variables.txt", "r")
        var_list = file.readlines()
        file.close()
        for variable in var_list:
            ##var = string.strip(variable)
            var = variable.strip()
            if var:
                variables.append(var)
                variable_uses.append(int(1))
        save_variables(variables, variable_uses)
    else:
        print(strs.error + "variables.txt not found in your module system, creating a new one...")
    i = 0
    while (i < len(variables)):
        if (variable_uses[i] == 0):
            print(strs.warn + "Global variable " + variables[i] + " never used.")
        i += 1
    
    #Finish:
    save_variables(variables, variable_uses)
    save_tag_uses(tag_uses)
    save_quick_strings(quick_strings)

    ## UID: 141 - Begin
    #
    file = open("version.txt", 'r')
    cVersion = "0.1"
    cFirst = "1"
    cVercur = "1"
    cVerbool = 0
    while True:
        readn = file.readline()
        if not readn:
            break
        if re.match(r".*\[v[0-9]\.[0-9]+\]", readn):
            cur = readn.split('[')[1].split(']')[0].replace("v", "")
            cVersion = cur
            cVerbool = 1

        if re.match(r"^[1-9][0-9]*\..*", readn):
            cur = readn.split('.')[0]
            if cVerbool:
                cFirst = cur
                cVerbool = 0
            cVercur = cur
    cCur = int(cVercur) - int(cFirst)
    file.close()
    #
    ## UID: 141 - End
    end_time = int(round(time.time() * 1000))
    diff_time = str((end_time - start_time) / 1000.0)
    #clear_module() #Clean the module system at the end...

    ## UID: 141 - Begin
    #
    #print(colors.dgreen + "Compiling completed in " + colors.dcyan + diff_time + colors.dgreen + " milliseconds.")
    print(colors.dgreen + "Compiling version " + colors.dcyan + "v" + cVersion + "." + str(cCur) + colors.dgreen + " completed in " + colors.dcyan + diff_time + colors.dgreen + " milliseconds.")
    #
    ## UID: 141 - End


compile_init()
