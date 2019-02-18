## UID: 121 - Begin
#
#from header_common import *
#from header_parties import *
#from ID_troops import *
#from ID_factions import *
#from ID_map_icons import *
from headers.header_common import *
from headers.header_parties import *
from ids.ID_troops import *
from ids.ID_factions import *
from ids.ID_map_icons import *
#
## UID: 121 - End

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END

  ## UID: 122 - Begin
  #
  #("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_slaver_chief,1,1),(trp_slave_crusher,2,4),(trp_slave_hunter,9,12),(trp_slave_driver,9,12),(trp_manhunter,9,12)]),
  #
  ## UID: 122 - End
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ## UID: 137 - Begin
  #
  #("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,2,38),(trp_bandit,2,20)]),
  #("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,2,38),(trp_bandit,2,20)]),
  #("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,2,38),(trp_bandit,2,20)]),
  #("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,2,32),(trp_bandit,2,20)]),
  #("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,2,40),(trp_bandit,2,20)]),
  #("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,3,30),(trp_bandit,2,20)]),
  ("steppe_bandits", "Steppe Bandits", icon_khergit|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit_2,1,2), (trp_steppe_bandit,2,38), (trp_bandit,2,20)]),
  ("taiga_bandits", "Tundra Bandits", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit_2,1,2), (trp_taiga_bandit,2,38), (trp_bandit,2,20)]),
  ("desert_bandits", "Desert Bandits", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_desert_guard,1,2), (trp_desert_bandit,2,38), (trp_bandit,2,20)]),
  ("forest_bandits", "Forest Bandits", icon_axeman|carries_goods(2), 0, fac_forest_bandits, bandit_personality, [(trp_forest_bandit_2,1,2), (trp_forest_bandit,2,32), (trp_bandit,2,20)]),
  ("mountain_bandits", "Mountain Bandits", icon_axeman|carries_goods(2), 0, fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit_2,1,2), (trp_mountain_bandit,2,40), (trp_bandit,2,20)]),
  ("sea_raiders", "Sea Raiders", icon_axeman|carries_goods(2), 0, fac_outlaws,bandit_personality,[(trp_sea_raider_2,1,2), (trp_sea_raider,3,30), (trp_bandit,2,20)]),
  ## UID: 10 - Begin
  #
  #("sea_raiders_ships","Sea Raiders",icon_ship|pf_is_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,6,60),(trp_bandit,2,20)]),
  ("sea_raiders_ships", "Sea Raiders", icon_ship|pf_is_ship|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_sea_raider_2,1,2), (trp_sea_raider,6,60), (trp_bandit,2,20)]),
  #
  ## UID: 10 - End
  #
  ## UID: 137 - End

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
  ## UID: 12 - Begin
  #
  ## UID: 122 - Begin
  #
  #("dark_hunters","Dark Hunters",icon_dedal_map_swadia_king_b,0,fac_dark_knights,soldier_personality,[(trp_dark_knight,8,32),(trp_dark_hunter,6,24),(trp_dark_pikeman,8,32)]),
  ("dark_hunters","Dark Hunters",icon_dedal_map_swadia_king_b,0,fac_dark_knights,soldier_personality,[(trp_dark_lord,1,5),(trp_dark_knight_2,7,11),(trp_dark_cavalary,6,10),(trp_master_dark_crossbowman,6,11),(trp_dark_lord_archer,3,9),(trp_dark_pikeman,4,9)]),
  #
  ## UID: 122 - End
  ## UID: 95 - Begin
  #
  #("desert_cavalry", "Desert Cavalry", icon_dedal_map_swadia_lord_a, 0, fac_desert_cavalry, soldier_personality, [(trp_desert_cavalry, 10, 50)]),
  ("desert_cavalry", "Desert Cavalry", icon_dedal_map_swadia_lord_a, 0, fac_desert_cavalry, soldier_personality, [(trp_desert_cavalry, 5, 35),(trp_desert_archer, 5, 15),(trp_desert_guard, 2, 5)]),
  #
  ## UID: 95 - End
  #
  ## UID: 12 - End
  
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ## UID: 79 - Begin
  #
  ("sea_traders", "Royal Traders", icon_ship|pf_is_ship|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  #
  ## UID: 79 - End
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ## UID: 62 - Begin
  #
  ("supporters_reinforcements_a", "{!}supporters_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_supporters_recruit,5,10),(trp_supporters_militia,2,4)]),
  ("supporters_reinforcements_b", "{!}supporters_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_supporters_footman,3,6),(trp_supporters_skirmisher,2,4)]),
  ("supporters_reinforcements_c", "{!}supporters_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_supporters_man_at_arms,2,4),(trp_supporters_crossbowman,1,2)]),
  #
  ## UID: 62 - End

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,2,4)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,6),(trp_swadian_skirmisher,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,2,4),(trp_swadian_crossbowman,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,2,4)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_skirmisher,2,4),(trp_vaegir_footman,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,2,3),(trp_vaegir_infantry,1,2)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_skirmisher,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,2,3),(trp_nord_footman,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,5)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),

  ## UID: 24 - Begin
  #
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_umalelithian_recruit,5,10),(trp_umalelithian_infantry,2,4)]),
  ## UID: 122 - Begin
  #
  #("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_umalelithian_veteran,2,4),(trp_umalelithian_warrior,2,3),(trp_umalelithian_archer,1,3)]),
  #("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_umalelithian_guard,3,5)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_umalelithian_bear_warrior,2,4),(trp_umalelithian_skirmisher,2,3),(trp_umalelithian_wolf_rider,1,3)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_umalelithian_bear_berserker,1,2),(trp_umalelithian_archer_2,1,2)]),
  #
  ## UID: 122 - End

  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kielian_tribeswoman,5,10), (trp_kielian_spearwoman,2,4)]),
  ## UID: 137 - Begin
  #
  #("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kielian_archer,2,4),(trp_kielian_trained_spearwoman,2,3),(trp_kielian_veteran_spearwoman,1,3)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kielian_archer,2,4), (trp_kielian_assassin_woman,2,3), (trp_kielian_horsewoman,1,3)]),
  #
  ## UID: 137 - End
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kielian_swordswoman,3,5)]),
  #
  ## UID: 24 - End
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

  ## UID: 62 - Begin
  #
  ("kingdom_0_patrol", "Player Kingdom Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_player_supporters_faction, soldier_personality, [(trp_supporters_footman, 12, 36),(trp_supporters_knight, 10, 30),(trp_supporters_infantry, 12, 36)]),
  #
  ## UID: 62 - End
  ## UID: 21 - Begin
  #
  ("kingdom_1_patrol", "Swadian Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_1, soldier_personality, [(trp_swadian_footman, 12, 36),(trp_swadian_knight, 10, 30),(trp_swadian_infantry, 12, 36)]),
  ("kingdom_2_patrol", "Vaegir Patrol Party", icon_vaegir_knight|pf_show_faction, 0, fac_kingdom_2, soldier_personality, [(trp_vaegir_veteran, 12, 36),(trp_vaegir_knight, 10, 30),(trp_vaegir_infantry, 12, 36)]),
  ("kingdom_3_patrol", "Khergit Patrol Party", icon_khergit|pf_show_faction, 0, fac_kingdom_3, soldier_personality, [(trp_khergit_horseman, 12, 34),(trp_khergit_veteran_horse_archer, 10, 30),(trp_khergit_horse_archer, 12, 36)]),
  ("kingdom_4_patrol", "Nord Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_4, soldier_personality, [(trp_nord_trained_footman, 12, 36),(trp_nord_veteran, 10, 30),(trp_nord_warrior, 12, 36)]),
  ("kingdom_5_patrol", "Rhodok Patrol Party", icon_vaegir_knight|pf_show_faction, 0, fac_kingdom_5, soldier_personality, [(trp_rhodok_trained_spearman, 12, 36),(trp_rhodok_sergeant, 10, 30),(trp_rhodok_veteran_spearman, 12, 36)]),
  ("kingdom_6_patrol", "Sarranid Patrol Party", icon_khergit|pf_show_faction, 0, fac_kingdom_6, soldier_personality, [(trp_sarranid_archer, 12, 36),(trp_sarranid_mamluke, 10, 30),(trp_sarranid_horseman, 12, 36)]),
  ## UID: 24 - Begin
  #
  ## UID: 122 - Begin
  #
  #("kingdom_7_patrol", "Umalelithian Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_7, soldier_personality, [(trp_umalelithian_warrior, 12, 36),(trp_umalelithian_leader, 10, 30),(trp_umalelithian_trained_archer, 12, 36)]),
  ("kingdom_7_patrol", "Umalelithian Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_7, soldier_personality, [(trp_umalelithian_bear_berserker, 12, 36),(trp_umalelithian_archer_2, 10, 30),(trp_umalelithian_wolf_rider, 12, 36)]),
  #
  ## UID: 122 - End
  ## UID: 137 - Begin
  #
  #("kingdom_8_patrol", "Kielian Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_8, soldier_personality, [(trp_kielian_master_archer, 12, 36),(trp_kielian_sergeant, 10, 30),(trp_kielian_horsewoman, 12, 36)]),
  ("kingdom_8_patrol", "Kielian Patrol Party", icon_gray_knight|pf_show_faction, 0, fac_kingdom_8, soldier_personality, [(trp_kielian_master_archer, 12, 36),(trp_kielian_assassin_woman, 10, 30),(trp_kielian_horsewoman, 12, 36)]),
  #
  ## UID: 137 - End
  #
  ## UID: 24 - End
  #
  ## UID: 21 - End

  ## UID: 60 - Begin
  #
  ("watch_tower", "Watch Tower", icon_dedal_map_watchtower|pf_is_static|pf_hide_defenders|pf_label_small, 0, fac_neutral, merchant_personality, []),
  ("messenger_post", "Messenger Post", icon_dedal_map_messenger_post|pf_is_static|pf_hide_defenders|pf_label_small, 0, fac_neutral, merchant_personality, []),
  ("windmill", "Wind Mill", icon_dedal_map_windmill|pf_is_static|pf_hide_defenders|pf_label_small, 0, fac_neutral, merchant_personality, []),
  #
  ## UID: 60 - End

  ## UID: 80 - Begin
  #
  ("deer_herd", "Deer Herd", icon_deer|carries_goods(10), 0, fac_wild_animals, merchant_personality, [(trp_deer,3,15)]),
  ("boar_herd", "Boar Herd", icon_boar|carries_goods(10), 0, fac_wild_animals, merchant_personality, [(trp_boar,2,7)]),
  #
  ## UID: 80 - End
]
