## UID: 121 - Begin
#
#from header_common import *
from headers.header_common import *
#
## UID: 121 - End

ff_always_hide_label = 0x00000001
ff_max_rating_bits = 8
ff_max_rating_mask = 0x0000ff00

def max_player_rating(rating):
  r = 100 - rating
  return (r << ff_max_rating_bits) & ff_max_rating_mask

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights", "Dark Knights", 0, 0.5, [("innocents",-0.9), ("player_supporters_faction", -0.4), ("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1", -0.1),("kingdom_2", -0.1),("kingdom_3", -0.1),("kingdom_4", -0.1),("kingdom_5", -0.1),("kingdom_6", -0.1),("kingdom_7", -0.1),("kingdom_8", -0.1)], [], 0x000000),
  ("desert_cavalry", "Desert Cavalry", 0, 0.5, [("kingdom_6", -0.5), ("player_supporters_faction", -0.4), ("innocents", -0.9), ("outlaws", -0.05), ("peasant_rebels", -0.1), ("deserters", -0.02), ("mountain_bandits", -0.05), ("forest_bandits", -0.05),("kingdom_1", -0.1),("kingdom_2", -0.1),("kingdom_3", -0.1),("kingdom_4", -0.1),("kingdom_5", -0.1),("kingdom_6", -0.1),("kingdom_7", -0.1),("kingdom_8", -0.1)], [], 0xF0E68C),

  ("culture_0", "{!}culture_0", 0, 0.0, [], []),
  ("culture_1", "{!}culture_1", 0, 0.9, [], []),
  ("culture_2", "{!}culture_2", 0, 0.9, [], []),
  ("culture_3", "{!}culture_3", 0, 0.9, [], []),
  ("culture_4", "{!}culture_4", 0, 0.9, [], []),
  ("culture_5", "{!}culture_5", 0, 0.9, [], []),
  ("culture_6", "{!}culture_6", 0, 0.9, [], []),
  ## UID: 24 - Begin
  #
  ("culture_7",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_8",  "{!}culture_6", 0, 0.9, [], []),
  #
  ## UID: 24 - End

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [("player_supporters_faction",1.00)], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.4),("desert_cavalry", -0.1)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Kingdom of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0xEE7744),
  ("kingdom_2",  "Kingdom of Vaegirs",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0xCCBB99),
  ("kingdom_3",  "Khergit Khanate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0xCC99FF),
  ("kingdom_4",  "Kingdom of Nords",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0x33DDDD),
  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0x33DD33),
  ("kingdom_6",  "Sarranid Sultanate",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0xDDDD33),
  ## UID: 24 - Begin
  #
  ("kingdom_7",  "Kingdom of Umalelith", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0x996600),
  ("kingdom_8",  "Kielian Sultanate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("dark_knights", -0.1),("desert_cavalry", -0.1)], [], 0x0066cc),
  #
  ## UID: 24 - End

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
#INVASION MODE START
  ("ccoop_all_stars","All Stars", 0, 0.5,[], []),
#INVASION MODE END

  ## UID: 80 - Begin
  #
  ("wild_animals", "Wild Animals",0, 0.1, [("player_faction",-0.15)], [], 0xFFFFFF),
  #
  ## UID: 80 - End
]
