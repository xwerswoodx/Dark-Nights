from module_map_icons import *
from headers.header_parties import *
from module_factions import *
from module_troops import *
from module_info import *

def decode_parties():
    file = open(export_dir + "parties.txt", "r")
    dec = open("decoded_parties.py", "w")
    dec.write("from header_common import *\nfrom header_parties import *\nfrom ID_troops import *\nfrom ID_factions import *\nfrom ID_party_templates import *\nfrom ID_map_icons import *\n\nparties = [\n")
    with file as f:
        for line in f:
            array = line.split(" ")
            if len(array) > 3:
                #print("%s - %s"%(line, array[4]))
                dec.write("  (\"%s\", \"%s\", %s|%s, no_menu, pt_none, fac_%s, %d, %s, %d, (%.2f, %.2f), [%s]"%(array[4][2:], array[5], get_icon(array[6]), get_flags(array[6]), factions[int(array[9])][0], int(array[10]), get_behavior(array[11]), int(array[12]), float(array[15]), float(array[16]), get_troop_list(line)))
            elif len(array) == 1:
                if int(float(line)) > 0:
                    dec.write(", %d),\n"%calculate_bear(line))
                else:
                    dec.write("),\n")
    dec.write("]")
    file.close()
    dec.close()
    print("parties.txt decoded.")

def get_flags(value):
    flags = int(value)
    result = ""
    if pf_disabled&flags:
        result = result + "pf_disabled|"
    if pf_is_ship&flags:
        result = result + "pf_is_ship|"
    if pf_is_static&flags:
        result = result + "pf_is_static|"
    if pf_label_small&flags:
        result = result + "pf_label_small|"
    if pf_label_medium&flags:
        result = result + "pf_label_medium|"
    if pf_label_large&flags:
        result = result + "pf_label_large|"
    if pf_always_visible&flags:
        result = result + "pf_always_visible|"
    if pf_default_behavior&flags:
        result = result + "pf_default_behavior|"
    if pf_auto_remove_in_town&flags:
        result = result + "pf_auto_remove_in_town|"
    if pf_quest_party&flags:
        result = result + "pf_quest_party|"
    if pf_no_label&flags:
        result = result + "pf_no_label|"
    if pf_limit_members&flags:
        result = result + "pf_limit_members|"
    if pf_hide_defenders&flags:
        result = result + "pf_hide_defenders|"
    if pf_show_faction&flags:
        result = result + "pf_show_faction|"
    if pf_dont_attack_civilians&flags:
        result = result + "pf_dont_attack_civilians|"
    if pf_civilian&flags:
        result = result + "pf_civilian|"
    return result[:-1]

def get_flags_as_int(value):
    flags = int(value)
    result = 0
    if pf_disabled&flags:
        result = result + pf_disabled
    if pf_is_ship&flags:
        result = result + pf_is_ship
    if pf_is_static&flags:
        result = result + pf_is_static
    if pf_label_small&flags:
        result = result + pf_label_small
    if pf_label_medium&flags:
        result = result + pf_label_medium
    if pf_label_large&flags:
        result = result + pf_label_large
    if pf_always_visible&flags:
        result = result + pf_always_visible
    if pf_default_behavior&flags:
        result = result + pf_default_behavior
    if pf_auto_remove_in_town&flags:
        result = result + pf_auto_remove_in_town
    if pf_quest_party&flags:
        result = result + pf_quest_party
    if pf_no_label&flags:
        result = result + pf_no_label
    if pf_limit_members&flags:
        result = result + pf_limit_members
    if pf_hide_defenders&flags:
        result = result + pf_hide_defenders
    if pf_show_faction&flags:
        result = result + pf_show_faction
    if pf_dont_attack_civilians&flags:
        result = result + pf_dont_attack_civilians
    if pf_civilian&flags:
        result = result + pf_civilian
    return result

def get_icon(value):
    icon = get_icon_as_int(value)
    return "icon_" + map_icons[icon][0]
    

def get_icon_as_int(value):
    flags = get_flags_as_int(value)
    return int(value) - flags

def get_behavior(value):
    ai = int(value)
    if ai == 0:
        return "ai_bhvr_hold"
    elif ai == 1:
        return "ai_bhvr_travel_to_party"
    elif ai == 2:
        return "ai_bhvr_patrol_location"
    elif ai == 3:
        return "ai_bhvr_patrol_party"
    elif ai == 4:
        return "ai_bhvr_attack_party"
    elif ai == 5:
        return "ai_bhvr_avoid_party"
    elif ai == 6:
        return "ai_bhvr_travel_to_point"
    elif ai == 7:
        return "ai_bhvr_negotiate_party"
    elif ai == 8:
        return "ai_bhvr_in_town"
    elif ai == 9:
        return "ai_bhvr_travel_to_ship"
    elif ai == 10:
        return "ai_bhvr_escort_party"
    elif ai == 11:
        return "ai_bhvr_driven_by_party"
    else:
        return "ai_bhvr_hold"

def get_troop_list(ln):
    sep = ln.split(" ")
    loop = int(sep[22])
    i = 0
    result = ""
    while i < loop:
        index = i * 4
        index += 23
        result = "(trp_" + troops[int(sep[index])][0] + ", " + sep[index + 1] + ", " + sep[index + 3] + "),"
        i += 1
    return result[:-1];

def calculate_bear(value):
    bear_result = int(float(value))
    static = 3.1415926 / 180.0
    bear_result = bear_result / static
    return int(bear_result)

decode_parties()
