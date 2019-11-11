## UID: 85 - Begin
#
#from header_skins import *
#
## UID: 85 - End
## UID: 121 - Begin
#
#from ID_particle_systems import *
from ids.ID_particle_systems import *
#
## UID: 121 - End

## UID: 85 - Begin
#
voice_die        = 0
voice_hit        = 1
voice_grunt      = 2
voice_grunt_long = 3
voice_yell       = 4
voice_warcry     = 5
voice_victory    = 6
voice_stun       = 7

skf_use_morph_key_10 = 0x00000001
skf_use_morph_key_20 = 0x00000002
skf_use_morph_key_30 = 0x00000003
skf_use_morph_key_40 = 0x00000004
skf_use_morph_key_50 = 0x00000005
skf_use_morph_key_60 = 0x00000006
skf_use_morph_key_70 = 0x00000007
#
## UID: 85 - End

####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
    (240, 0, -0.4, 0.3, "Chin Size"),
    (230, 0, -0.4, 0.8, "Chin Shape"),
    (250, 0, -0.3, 0.6, "Chin Forward"),
    (130, 0, -0.5, 1.0, "Jaw Width"),
    (120, 0, -0.5, 0.6, "Lower Lip"),
    (110, 0, -0.2, 0.6, "Upper Lip"),
    (100, 0, 0.2, -0.2, "Mouth-Nose Distance"),
    (90, 0, 0.6, -0.6, "Mouth Width"),
    (30, 0, -0.3, 0.3, "Nostril Size"),
    (60, 0, 0.3, -0.3, "Nose Height"),
    (40, 0, -0.2, 0.3, "Nose Width"),
    (70, 0, -0.3, 0.4, "Nose Size"),
    (50, 0, 0.2, -0.3, "Nose Shape"),
    (80, 0, -0.3, 0.7, "Nose Bridge"),
    (160, 0, -0.2, 0.3, "Eye Width"),
    (190, 0, -0.3, 0.1, "Eye to Eye Dist"),
    (170, 0, -0.8, 0.8, "Eye Shape"),
    (200, 0, -0.3, 0.7, "Eye Depth"),
    (180, 0, -1.5, 1.5, "Eyelids"),
    (20, 0, 0.6, -0.3, "Cheeks"),
    (260, 0, -0.6, 0.5, "Cheek Bones"),
    (220, 0, 0.8, -0.8, "Eyebrow Height"),
    (210, 0, -0.8, 0.8, "Eyebrow Shape"),
    (10, 0, -0.6, 0.5, "Temple Width"),
    (270, 0, -0.3, 1.0, "Face Depth"),
    (150, 0, -0.3, 0.5, "Face Ratio"),
    (140, 0, -0.4, 0.5, "Face Width"),
    (280, 0, 1.0, 1.0, "Post-Edit"),
]

woman_face_keys = [
    (230, 0, 0.5, -0.8, "Chin Size"),
    (220, 0, -0.7, 0.5, "Chin Shape"),
    (10, 0, -0.7, 0.7, "Chin Forward"),
    (20, 0, -0.7, 0.7, "Jaw Width"),
    (40, 0, -1.0, 0.5, "Jaw Position"),
    (90, 0, -0.7, 0.7, "Jaw Neck"),
    (50, 0, -0.7, 0.7, "Cheeks"),
    (100, 0, -0.7, 0.7, "Cheek Bones"),
    (270, 0, 0.5, -0.3, "Mouth-Nose Distance"),
    (30, 0, -0.7, 0.5, "Mouth Width"),
    (160, 0, 0.7, -0.5, "Lips Position"),
    (60, 0, 0.5, -0.5, "Nose Height"),
    (70, 0, -0.5, 0.7, "Nose Width"),
    (80, 0, 1.0, -1.0, "Nose Size"),
    (240, 0, 0.4, -0.4, "Nose Shape"),
    (150, 0, -0.5, 0.5, "Eye Width"),
    (110, 0, 0.5, -0.5, "Eye to Eye Dist"),
    (120, 0, 0.9, -0.9, "Eye Shape"),
    (130, 0, -0.7, 0.7, "Eye Position"),
    (140, 0, -1.0, 1.5, "Eyelids"),
    (170, 0, -0.9, 0.7, "Eyebrow Height"),
    (180, 0, -0.5, 1.0, "Eyebrow Shape"),
    (260, 0, 0.5, -0.5, "Temple Width"),
    (200, 0, 0.7, -0.7, "Face tall-short"),
    (210, 0, -0.7, 0.7, "Face Depth"),
    (250, 0, -0.4, 0.4, "Face Ratio"),
    (190, 0, -0.9, 0.7, "Face Width"),
    (280, 0, 0.0, 1.0, "Post-Edit"),
]

undead_face_keys = []
chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26
comp_less_than = -1;
comp_greater_than = 1;

skins = [
    ("man", 0, "man_body", "man_calf_l", "m_handL", "male_head", man_face_keys,
     ["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4","hairmessy","straightshoulder","ponytail","shortcut","shortlayer"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
     ["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o", "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g"], #beard meshes ,"beard_q"
     ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
     ["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
     [
         ("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
         ("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
         ("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         #("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
         ("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
         ("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
         ("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
         #("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
         ## UID: 149 - Begin
         #
         ("manface_asian1", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_asian2", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_asian3", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_mideast1", 0xffaeb0a6, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_mideast2", 0xffd0c8c1, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_mideast3", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_black1", 0xff87655c, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_black2", 0xff5a342d, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_black3", 0xff634d3e, ["hair_blonde"], [0xff171313, 0xff007080c]),
         ("manface_white1", 0xffe0e8e8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
         ("manface_white2", 0xffe0e8e8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c, 0xff19100c]),
         ("manface_white3", 0xffe0e8e8, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff19100c]),
         #
         ## UID: 149 - End
         ("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
         #("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
        ], [
            (voice_die,"snd_man_die"),
            (voice_hit,"snd_man_hit"),
            (voice_grunt,"snd_man_grunt"),
            (voice_grunt_long,"snd_man_grunt_long"),
            (voice_yell,"snd_man_yell"),
            (voice_stun,"snd_man_stun"),
            (voice_victory,"snd_man_victory"),
        ], "skel_human", 1.0, psys_game_blood, psys_game_blood_2, [
            ## UID: 149 - Begin
            #
            #[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
            #[0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
            #[1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
            #[0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
            #[1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
            #[-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
            #[0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
            #[2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
            [1.6, comp_greater_than, (1.0,eye_to_eye_dist), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
            [0.6, comp_less_than, (1.0,eye_to_eye_dist), (1.0,temple_width)],
            [1.5, comp_greater_than, (1.0,face_ratio), (1.0,mouth_width)],  # face ratio and mouth to nose distance
            [0.6, comp_greater_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
            [-1.0, comp_less_than, (-1.0,nose_width), (1.0,mouth_width)],  # nose height and mouth to nose distance
            #
            ## UID: 149 - End
        ]),

    ("woman", skf_use_morph_key_10, "woman_body",  "woman_calf_l", "f_handL", "female_head", woman_face_keys,
     ["woman_hair_01", "woman_hair_02", "woman_hair_03", "woman_hair_04", "woman_hair_05", "woman_hair_06", "woman_hair_07", "woman_hair_08", "woman_hair_09", "woman_hair_10", "woman_hair_11", "woman_hair_12", "woman_hair_13", "woman_hair_14", "woman_hair_15", "woman_hair_16", "woman_hair_17", "woman_hair_18", "woman_hair_19", "woman_hair_20", "woman_hair_21", "woman_hair_22", "woman_hair_23", "woman_hair_24", "woman_hair_25", "woman_hair_26", "woman_hair_27", "woman_hair_28", "hairmessy", "shortlayer", "shoulderhair", "shortbob", "shortcut", "ponytail", "longshoulder", "longstraight", "straightshoulder", "slickedback", "maidenhair", "courthair"], #woman_hair_meshes
     #["woman_hair_a","woman_hair_b","woman_hair_c","woman_hair_d","woman_hair_e","woman_hair_f","woman_hair_g"], #woman_hair_meshes
     [],
     ["hair_blonde02", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
     [],
     [
         ## UID: 149 - Begin
         #
         #("womanface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         #("womanface_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         #("womanface_a",0xffe8dfe5,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
         #("womanface_brown",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
         #("womanface_african",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
         #("womanface_midage",0xffe5eaf0,["hair_black","hair_brunette","hair_red","hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
         ("womanface_12", 0xffeaf7ff, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
         ("womanface_03", 0xffe4eded, ["hair_blonde02"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_02", 0xffeaf7ff, ["hair_blonde02"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_04", 0xffd5d3b8, ["hair_blonde02"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
         ("womanface_05", 0xff7e7c85, ["hair_blonde02"], [0xff120808, 0xff007080c]),
         ("womanface_06", 0xfff4eeeb, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_07", 0xffeceeeb, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_08", 0xffe6d1b4, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_09", 0xfff9efe8, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_10", 0xfff3efed, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_11", 0xfff6f3f1, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_01", 0xfff3eeea, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_13", 0xffe9e5e5, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_14", 0xffefefee, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_15", 0xffebebed, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_16", 0xfff7ece8, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_17", 0xffedeae5, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_18", 0xfff2f3f2, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_19", 0xffe6e4e5, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_20", 0xffe7eaea, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_21", 0xffeaeae2, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         ("womanface_22", 0xffeeece8, ["hair_blonde02"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c, 0xff0c0d19]),
         #
         ## UID: 149 - End
        ], [
            (voice_die,"snd_woman_die"),
            (voice_hit,"snd_woman_hit"),
            (voice_yell,"snd_woman_yell"),
        ], "skel_human", 1.0, psys_game_blood,psys_game_blood_2,
    ),
  
##  (
##    "undead", 0,
##    "undead_body", "undead_calf_l", "undead_handL",
##    "undead_head", undead_face_keys,
##    [],
##    [],
##    [],
##    [],
##    [("undeadface_a",0xffffffff,[]),
##     ("undeadface_b",0xffcaffc0,[]),
##     ], #undead_face_textures
##    [], #voice sounds
##    "skel_human", 1.0,
##  ),
]

