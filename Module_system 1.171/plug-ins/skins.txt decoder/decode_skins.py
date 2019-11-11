import re, string
from module_info import *

def decode_skins():
    slots = ['chin_size', 'chin_shape', 'chin_forward', 'jaw_width', 'jaw_position', 'mouth_nose_distance', 'mouth_width', 'cheeks', 'nose_height', 'nose_width', 'nose_size', 'nose_shape', 'nose_bridge', 'cheek_bones', 'eye_width', 'eye_to_eye_dist', 'eye_shape', 'eye_depth', 'eyelids', 'eyebrow_position', 'eyebrow_height', 'eyebrow_depth', 'eyebrow_shape', 'temple_width', 'face_depth', 'face_ratio', 'face_width']
    
    file = open(export_dir + "skins.txt", "r")
    dec = open("decoded_skins.py", "w")
    dec.write('from ids.ID_particle_systems import *')
    dec.write('\n\nvoice_die        = 0\nvoice_hit        = 1\nvoice_grunt      = 2\nvoice_grunt_long = 3\nvoice_yell       = 4\nvoice_warcry     = 5\nvoice_victory    = 6\nvoice_stun       = 7')
    dec.write('\n\nskf_use_morph_key_10 = 0x00000001\nskf_use_morph_key_20 = 0x00000002\nskf_use_morph_key_30 = 0x00000003\nskf_use_morph_key_40 = 0x00000004\nskf_use_morph_key_50 = 0x00000005\nskf_use_morph_key_60 = 0x00000006\nskf_use_morph_key_70 = 0x00000007\n')
    dec.write('\n####################################################################################################################')
    dec.write('\n#  Each skin record contains the following fields:')
    dec.write('\n#  1) Skin id: used for referencing skins.')
    dec.write('\n#  2) Skin flags. Not used yet. Should be 0.')
    dec.write('\n#  3) Body mesh.')
    dec.write('\n#  4) Calf mesh (left one).')
    dec.write('\n#  5) Hand mesh (left one).')
    dec.write('\n#  6) Head mesh.')
    dec.write('\n#  7) Face keys (list)')
    dec.write('\n#  8) List of hair meshes.')
    dec.write('\n#  9) List of beard meshes.')
    dec.write('\n# 10) List of hair textures.')
    dec.write('\n# 11) List of beard textures.')
    dec.write('\n# 12) List of face textures.')
    dec.write('\n# 13) List of voices.')
    dec.write('\n# 14) Skeleton name')
    dec.write('\n# 15) Scale (doesn\'t fully work yet)')
    dec.write('\n# 16) Blood particles 1 (do not add this if you wish to use the default particles)')
    dec.write('\n# 17) Blood particles 2 (do not add this if you wish to use the default particles)')
    dec.write('\n# 18) Face key constraints (do not add this if you do not wish to use it)')
    dec.write('\n####################################################################################################################\n\n')
    
    start = 0
    with file as f:
        for line in f:
            array = line.split(" ")
            if re.match(r"^[a-z]+$",array[0]):
                cur = array[0].rstrip()
                start = 1
            if start == 1:
                start = start + 1
            elif start == 2:
                start = start + 1
            elif start == 3:
                dec.write('%s_face_keys = [\n'%(cur))
                keys = int(array[2])
                i = 0
                while i < keys:
                    spoint = (i * 6) + 4
                    dec.write('    (%s, %s, %s, %s, "%s"),\n'%(array[spoint].rstrip(), array[spoint + 1].rstrip(), floatFix(array[spoint + 2].rstrip()), floatFix(array[spoint + 3].rstrip()), string.replace(array[spoint + 4].rstrip(), "_", " ")))
                    i = i + 1
                dec.write(']\n\n')
                start = start + 1

    file.close()

    i = 0
    while i < len(slots):
        dec.write('%s = %d\n'%(slots[i], i))
        i = i + 1
    dec.write('comp_less_than = -1;\ncomp_greater_than = 1;\n\n')

    file = open(export_dir + "skins.txt", "r")
    start = 0
    dec.write("skins = [")
    with file as f:
        for line in f:
            array = line.split(" ")
            print('-' + line)
            if re.match(r"^[a-z]+$",array[0]):
                dec.write('\n    ("%s", %s, '%(array[0].rstrip(), getKey(array[1].rstrip())))
                cur = array[0].rstrip()
                start = 1
            if start == 1:
                start = start + 1
            elif start == 2:
                dec.write(' "%s", "%s", "%s", '%(array[1], array[2], array[3].rstrip()))
                start = start + 1
            elif start == 3:
                dec.write('"%s", %s_face_keys,\n'%(array[1].rstrip(), cur))
                start = start + 1
            elif start == 4:
                hairs = int(array[0].rstrip())
                start = start + 1
            elif start == 5:
                dec.write('     [')
                if hairs > 0:
                    i = 1
                    p = 1
                    while i <= hairs:
                        if p == 1:
                            dec.write('"%s"'%(array[p].rstrip()))
                        else:
                            dec.write(', "%s"'%(array[p].rstrip()))
                        p = p + 2
                        i = i + 1
                dec.write('],\n')
                beard = -1
                start = start + 1
            elif start == 6 and beard == -1:
                dec.write('     [')
                beard = int(array[1].rstrip())
                if beard < 1:
                    start = start + 1
            elif start == 6 and beard > 0:
                beard = beard - 1
                if beard:
                    dec.write('"%s", '%(array[2].rstrip()))
                else:
                    dec.write('"%s"'%(array[2].rstrip()))
                    start = start + 1
            elif start == 7:
                dec.write('],\n')
                start = start + 1
            elif start == 8:
                dec.write('     [')
                ht = int(array[1].rstrip())
                if ht > 0:
                    i = 1
                    while i <= ht:
                        s = (i * 2) + 1
                        if i == 1:
                            dec.write('"%s"'%(array[s].rstrip()))
                        else:
                            dec.write(', "%s"'%(array[s].rstrip()))
                        i = i + 1
                dec.write('],\n')
                start = start + 1
            elif start == 9:
                dec.write('     [')
                ht = int(array[1].rstrip())
                if ht > 0:
                    i = 1
                    while i <= ht:
                        s = (i * 2) + 1
                        if i == 1:
                            dec.write('"%s"'%(array[s].rstrip()))
                        else:
                            dec.write(', "%s"'%(array[s].rstrip()))
                        i = i + 1
                dec.write('],\n')
                start = start + 1
            elif start == 10:
                dec.write('     [')
                mesh = int(array[1].rstrip())
                i = 1
                s = 3
                while i <= mesh:
                    dec.write('\n         ("%s", %s, '%(array[s].rstrip(), convertHex(array[s + 1].rstrip())))
                    hc = int(array[s + 2].rstrip())
                    hh = int(array[s + 3].rstrip())
                    hh = hh + hh
                    a = s + 5
                    dec.write('[')
                    while a < s + 5 + hc:
                        if a == s + 5:
                            dec.write('"%s"'%(array[a].rstrip()))
                        else:
                            dec.write('", %s"'%(array[a].rstrip()))
                        a = a + 1
                    a = a + 1
                    dec.write('], [')
                    b = a;
                    while a < b + hh:
                        if a == b:
                            dec.write('%s'%(convertHex(array[a].rstrip())))
                        else:
                            dec.write(', %s'%(convertHex(array[a].rstrip())))
                        a = a + 2
                    dec.write(']),')
                    s = a
                    i = i + 1
                dec.write('\n        ], ')
                start = start + 1
            elif start == 11:
                dec.write(' [\n')
                voices = int(array[1].rstrip())
                i = 1
                while i <= voices:
                    s = i * 3
                    dec.write('            (%s, "%s"),\n'%(getVoiceKey(array[s].rstrip()), array[s + 1].rstrip()))
                    i = i + 1
                dec.write('        ], ')
                start = start + 1
            elif start == 12:
                dec.write('"%s", %s, '%(array[1].rstrip(), floatFix(array[2].rstrip())))
                start = start + 1
            elif start == 13:
                i = 0
                while i < len(array):
                    dec.write('%s, '%(getPsysKey(array[i].rstrip())))
                    i = i + 1
                start = start + 1
            elif start == 14:
                ext = int(array[0].rstrip())
                if ext < 1:
                    dec.write('\n    ),\n')
                    start = -1
                else:
                    dec.write('[\n')
                    start = start + 1
            elif start == 15:
                start = start + 1
            elif start >= 16 and start < (16 + ext):
                dec.write('            [%s, %s'%(floatFix(array[0].rstrip()), comps(array[1].rstrip())))
                arr = int(array[2].rstrip())
                if arr > 0:
                    i = 1
                    while i <= arr:
                        a = (i * 2) + 2
                        dec.write(', (%s, %s)'%(floatFix(array[a].rstrip()), slots[int(array[a + 1].rstrip())]))
                        i = i + 1
                dec.write('],\n')
                if start == (15 + ext):
                    dec.write('        ]),\n')
                    start = -1
                start = start + 1
    file.close()
    dec.write(']')
    dec.close()
    print("skins.txt decoded.")

def getKey(num):
    if num == "0":
        return "0"
    else:
        return "skf_use_morph_key_" + num + "0"

def convertHex(value):
    return hex(int(value)).rstrip("L")

def getVoiceKey(num):
    if num == "0":
        return "voice_die"
    elif num == "1":
        return "voice_hit"
    elif num == "2":
        return "voice_grunt"
    elif num == "3":
        return "voice_grunt_long"
    elif num == "4":
        return "voice_yell"
    elif num == "5":
        return "voice_warcry"
    elif num == "6":
        return "voice_victory"
    elif num == "7":
        return "voice_stun"

def getPsysKey(num):
    num = int(num)
    if num < 10:
        lst = ['psys_game_rain', 'psys_game_snow', 'psys_game_blood', 'psys_game_blood_2', 'psys_game_hoof_dust', 'psys_game_hoof_dust_snow', 'psys_game_hoof_dust_mud', 'psys_game_water_splash_1', 'psys_game_water_splash_2', 'psys_game_water_splash_3']
        return lst[num];
    elif num < 20:
        num = num - 10
        lst = ['psys_torch_fire', 'psys_fire_glow_1', 'psys_fire_glow_fixed', 'psys_torch_smoke', 'psys_flue_smoke_short', 'psys_flue_smoke_tall', 'psys_war_smoke_tall', 'psys_ladder_dust_6m', 'psys_ladder_dust_8m', 'psys_ladder_dust_10m']
        return lst[num];
    elif num < 30:
        num = num - 20
        lst = ['psys_ladder_dust_12m', 'psys_ladder_dust_14m', 'psys_ladder_straw_6m', 'psys_ladder_straw_8m', 'psys_ladder_straw_10m', 'psys_ladder_straw_12m', 'psys_ladder_straw_14m', 'psys_torch_fire_sparks', 'psys_fire_sparks_1', 'psys_pistol_smoke']
        return lst[num]
    elif num < 40:
        num = num - 30
        lst = ['psys_brazier_fire_1', 'psys_cooking_fire_1', 'psys_cooking_smoke', 'psys_food_steam', 'psys_candle_light', 'psys_candle_light_small', 'psys_lamp_fire', 'psys_dummy_smoke', 'psys_dummy_straw', 'psys_dummy_smoke_big']
        return lst[num]
    elif num < 50:
        num = num - 40
        lst = ['psys_dummy_straw_big', 'psys_gourd_smoke', 'psys_gourd_piece_1', 'psys_gourd_piece_2', 'psys_fire_fly_1', 'psys_bug_fly_1', 'psys_moon_beam_1', 'psys_moon_beam_paricle_1', 'psys_night_smoke_1', 'psys_fireplace_fire_small']
        return lst[num]
    else:
        num = num - 50
        lst = ['psys_fireplace_fire_big', 'psys_village_fire_big', 'psys_village_fire_smoke_big', 'psys_map_village_fire', 'psys_map_village_fire_smoke', 'psys_map_village_looted_smoke', 'psys_dungeon_water_drops', 'psys_wedding_rose', 'psys_sea_foam_a', 'psys_fall_leafs_a']
        return lst[num]
    return str(num)

def comps(num):
    if num == "-1":
        return "comp_less_than"
    else:
        return "comp_greater_than"

def floatFix(num):
    return str(round(float(num),1))
    
decode_skins()
