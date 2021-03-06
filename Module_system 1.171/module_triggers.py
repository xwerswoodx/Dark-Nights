## UID: 121 - Begin
#
#from header_common import *
#from header_operations import *
#from header_parties import *
#from header_items import *
from headers.header_common import *
from headers.header_operations import *
from headers.header_parties import *
from headers.header_items import *
## UID: 85 - Begin
#
#from header_skills import *
#from ID_skills import *
#
## UID: 85 - End
from ids.ID_skills import *
from headers.header_triggers import *
from headers.header_troops import *
#from header_triggers import *
#from header_troops import *
#
## UID: 121 - End

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:
  (0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),

  # Refresh Merchants
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_center_inventories")]),
  # Refresh Armor sellers
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_center_armories")]),
  # Refresh Weapon sellers
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_center_weaponsmiths")]),
  # Refresh Horse sellers
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_center_stables")]),

  ## UID: 98 - Begin
  #
  # Refresh tavern keepers
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_center_taverns")]),
  #
  ##UID: 98 - End
  
  ## UID: 34 - Begin
  #
  (0.0, 0, 168.0, [], [(call_script, "script_refresh_booksellers")]),
  #
  ## UID: 34 - End

  ## UID: 62 - Begin
  #
  (0.0, 0, 4.0, [
      (eq, "$players_kingdom", "fac_player_supporters_faction"),
      (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
    ], [
        (call_script, "script_set_supporters_name", 0),
        (call_script, "script_set_supporters_name", "fac_player_supporters_faction"),
    ]),
  #
  ## UID: 62 - End

#############

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),    
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    (store_add, ":p_town_22_plus_one", "p_town_22", 1),
    (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
  
  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
		
		
		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),
		
		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),
			
			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			
			
			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),
			
			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [
      (store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
      (party_is_in_any_town,reg(2)),
    ], [
        (store_faction_of_party, ":faction_no", reg(2)),
        (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
        (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
        ## UID: 152 - Begin
        #
        #(party_set_ai_object,reg(2),reg0),
        (call_script, "script_party_set_ai_object", reg(2), reg0),
        #
        ## UID: 152 - End
        (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),

  ## UID: 12 - Begin
  #
  (10.1, 0, 0.0, [
      (store_num_parties_of_template, ":total_dark_knight", "pt_dark_hunters"),
      (store_mul, ":max_dark_knight", 6, "$g_difficulty"),
      (lt, ":total_dark_knight", ":max_dark_knight"),
##      (neq, "$dnm_dark_knights", 1),
    ], [
        (store_random_in_range, ":town_no", towns_begin, towns_end),
        (set_spawn_radius, 1),
        (spawn_around_party, ":town_no", "pt_dark_hunters"),
        (str_store_party_name, s1, reg0),
##        (display_message, "@Party Spawned: {s1}."),
    ]),
  
  (10.1, 0, 0.0, [
      (store_num_parties_of_template, ":total_desert_cavalry", "pt_desert_cavalry"),
      (store_mul, ":max_desert_cavalry", 3, "$g_difficulty"),
      (lt, ":total_desert_cavalry", ":max_desert_cavalry"),
##      (neq, "$dnm_desert_cavalry", 1),
    ], [
        (store_random_in_range, ":town_no", "p_town_18", "p_town_24"),
        (val_add, ":town_no", 1),
        (set_spawn_radius, 1),
        (spawn_around_party, ":town_no", "pt_desert_cavalry"),
    ]),

  ## UID: 143 - Begin
  #
  #(24.0, 0, 0.0, [
  #    (store_num_parties_of_template, ":total_dark_knight", "pt_dark_hunters"),
  #    (store_num_parties_of_template, ":total_desert_cavalry", "pt_desert_cavalry"),
  #    (this_or_next|gt, ":total_dark_knight", 0),
  #    (             gt, ":total_desert_cavalry", 0),
  #  ], [
  #      (try_for_parties, ":party"),
  #        ## UID: 138 - Begin
  #        #
  #        #(store_random_in_range, ":dk", "trp_dark_knight", "trp_desert_cavalry"),
  #        (store_random_in_range, ":dk", "trp_dark_recruit", "trp_desert_cavalry"),
  #        #
  #        ## UID: 138 - End
  #        ## UID: 95 - Begin
  #        #
  #        #(assign, ":dc", "trp_desert_cavalry"),
  #        (store_random_in_range, ":dc", "trp_desert_cavalry", "trp_town_walker_1"),
  #        #
  #        ## UID: 95 - End
  #
  #        (party_get_template_id, ":template", ":party"),
  #        (try_begin),
  #          (eq, ":template", "pt_dark_hunters"),
  #          (party_add_members, ":party", ":dk", 1),
  #        (else_try),
  #          (eq, ":template", "pt_desert_cavalry"),
  #          (party_add_members, ":party", ":dc", 1),
  #        (try_end),
  #      (try_end),
  #  ]), 
  #
  ## UID: 12 - End
  (24.0, 0, 0.0, [], [(call_script, "script_add_troop_for_parties")]),
  #
  ## UID: 143 - End

  ## UID: 78 - Begin
  #
  ## UID: 100 - Begin
  #
  (12.0, 0, 0.0, [
      (assign, ":cont", 0),
      (try_for_range, ":rand", 0, 25),
        (eq, ":cont", 0),
        (store_add, ":item", ":rand", slot_player_order_item),
        (store_add, ":found", ":rand", slot_player_order_found),
        (troop_slot_ge, "trp_player", ":item", 1),
        (troop_slot_lt, "trp_player", ":found", 0),
        (assign, ":cont", 1),
      (try_end),
      (eq, ":cont", 1),
      (map_free, 0),
    ], [
        (try_for_range, ":town", towns_begin, towns_end),
          # Weaponsmith
          (party_get_slot, ":merchant", ":town", slot_town_weaponsmith),
          (try_for_range, ":slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":item", ":merchant", ":slot"),
            (troop_get_inventory_slot_modifier, ":modifier", ":merchant", ":slot"),
            (try_for_range, ":order", 0, 25),
              (store_add, ":order_item", ":order", slot_player_order_item),
              (store_add, ":order_mod", ":order", slot_player_order_modifier),
              (store_add, ":order_found", ":order", slot_player_order_found),
              (store_add, ":order_hours", ":order", slot_player_order_hours),
              (store_add, ":order_slot", ":order", slot_player_order_slot),
              (store_add, ":order_town", ":order", slot_player_order_town),
              (store_add, ":order_reach", ":order", slot_player_order_reach),
              (store_add, ":order_warn", ":order", slot_player_order_warned),
              (troop_get_slot, ":order_town_no", "trp_player", ":order_town"),
              (troop_slot_eq, "trp_player", ":order_slot", slot_town_weaponsmith),
              (troop_slot_lt, "trp_player", ":order_found", 0),
              (troop_slot_eq, "trp_player", ":order_item", ":item"),
              (troop_slot_eq, "trp_player", ":order_mod", ":modifier"),
              (troop_set_slot, "trp_player", ":order_found", ":town"),
              (store_current_hours, ":hour"),
              (troop_set_slot, "trp_player", ":order_hours", ":hour"),
              (store_distance_to_party_from_party, ":dist", ":order_town_no", ":town"),
              (val_mul, ":dist", 2),
              (val_add, ":dist", ":hour"),
              (troop_set_slot, "trp_player", ":order_reach", ":dist"),
              (try_begin),
                (troop_slot_eq, "trp_player", ":order_town", ":town"),
                (troop_set_slot, "trp_player", ":order_reach", ":hour"),
              (try_end),
              (troop_set_inventory_slot, ":merchant", ":slot", -1),
              (troop_sort_inventory, ":merchant"),
              (troop_set_slot, "trp_player", ":order_warn", -1),
              (str_store_party_name, s1, ":order_town_no"),

              (troop_get_slot, ":reach_time", "trp_player", ":order_reach"),
              (troop_get_slot, ":found_time", "trp_player", ":order_hours"),              
              (store_sub, reg0, ":reach_time", ":found_time"),
              (val_div, reg0, 24),
              (store_sub, reg1, reg0, 1),
        
              (str_store_party_name, s2, ":town"),
              (str_store_troop_name, s3, ":merchant"),
              (str_store_item_name, s4, ":item"),
              (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s3}.\
 '{reg0?Your {s4} will be reach within {reg0} {reg1?days:day} to {s1}. But if you close enought to {s2}, you can collect your {s4} from {s3} in a day.\
 Tomorrow, your {s4} will be sent out with a notable merchant. You can come and collect your {s4} anytime you want after {reg0} {reg1?days:day}:Your {s4} is now ready at {s1} you can come and collect it anytime you want.}'"),
            (try_end),
          (try_end),
          # Armorer
          (party_get_slot, ":merchant", ":town", slot_town_armorer),
          (try_for_range, ":slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":item", ":merchant", ":slot"),
            (troop_get_inventory_slot_modifier, ":modifier", ":merchant", ":slot"),
            (try_for_range, ":order", 0, 25),
              (store_add, ":order_item", ":order", slot_player_order_item),
              (store_add, ":order_mod", ":order", slot_player_order_modifier),
              (store_add, ":order_found", ":order", slot_player_order_found),
              (store_add, ":order_hours", ":order", slot_player_order_hours),
              (store_add, ":order_slot", ":order", slot_player_order_slot),
              (store_add, ":order_town", ":order", slot_player_order_town),
              (store_add, ":order_reach", ":order", slot_player_order_reach),
              (store_add, ":order_warn", ":order", slot_player_order_warned),
              (troop_get_slot, ":order_town_no", "trp_player", ":order_town"),
              (troop_slot_eq, "trp_player", ":order_slot", slot_town_armorer),
              (troop_slot_lt, "trp_player", ":order_found", 0),
              (troop_slot_eq, "trp_player", ":order_item", ":item"),
              (troop_slot_eq, "trp_player", ":order_mod", ":modifier"),
              (troop_set_slot, "trp_player", ":order_found", ":town"),
              (store_current_hours, ":hour"),
              (troop_set_slot, "trp_player", ":order_hours", ":hour"),
              (store_distance_to_party_from_party, ":dist", ":order_town_no", ":town"),
              (val_mul, ":dist", 2),
              (val_add, ":dist", ":hour"),
              (troop_set_slot, "trp_player", ":order_reach", ":dist"),
              (try_begin),
                (troop_slot_eq, "trp_player", ":order_town", ":town"),
                (troop_set_slot, "trp_player", ":order_reach", ":hour"),
              (try_end),
              (troop_set_inventory_slot, ":merchant", ":slot", -1),
              (troop_sort_inventory, ":merchant"),
              (troop_set_slot, "trp_player", ":order_warn", -1),
              (str_store_party_name, s1, ":order_town_no"),

              (troop_get_slot, ":reach_time", "trp_player", ":order_reach"),
              (troop_get_slot, ":found_time", "trp_player", ":order_hours"),              
              (store_sub, reg0, ":reach_time", ":found_time"),
              (val_div, reg0, 24),
              (store_sub, reg1, reg0, 1),
        
              (str_store_party_name, s2, ":town"),
              (str_store_troop_name, s3, ":merchant"),
              (str_store_item_name, s4, ":item"),
              (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s3}.\
 '{reg0?Your {s4} will be reach within {reg0} {reg1?days:day} to {s1}. But if you close enought to {s2}, you can collect your {s4} from {s3} in a day.\
 Tomorrow, your {s4} will be sent out with a notable merchant. You can come and collect your {s4} anytime you want after {reg0} {reg1?days:day}:Your {s4} is now ready at {s1} you can come and collect it anytime you want.}'"),
            (try_end),
          (try_end),
          # Horse Merchant
          (party_get_slot, ":merchant", ":town", slot_town_horse_merchant),
          (try_for_range, ":slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":item", ":merchant", ":slot"),
            (troop_get_inventory_slot_modifier, ":modifier", ":merchant", ":slot"),
            (try_for_range, ":order", 0, 25),
              (store_add, ":order_item", ":order", slot_player_order_item),
              (store_add, ":order_mod", ":order", slot_player_order_modifier),
              (store_add, ":order_found", ":order", slot_player_order_found),
              (store_add, ":order_hours", ":order", slot_player_order_hours),
              (store_add, ":order_slot", ":order", slot_player_order_slot),
              (store_add, ":order_town", ":order", slot_player_order_town),
              (store_add, ":order_reach", ":order", slot_player_order_reach),
              (store_add, ":order_warn", ":order", slot_player_order_warned),
              (troop_get_slot, ":order_town_no", "trp_player", ":order_town"),
              (troop_slot_eq, "trp_player", ":order_slot", slot_town_horse_merchant),
              (troop_slot_lt, "trp_player", ":order_found", 0),
              (troop_slot_eq, "trp_player", ":order_item", ":item"),
              (troop_slot_eq, "trp_player", ":order_mod", ":modifier"),
              (troop_set_slot, "trp_player", ":order_found", ":town"),
              (store_current_hours, ":hour"),
              (troop_set_slot, "trp_player", ":order_hours", ":hour"),
              (store_distance_to_party_from_party, ":dist", ":order_town_no", ":town"),
              (val_mul, ":dist", 2),
              (val_add, ":dist", ":hour"),
              (troop_set_slot, "trp_player", ":order_reach", ":dist"),
              (try_begin),
                (troop_slot_eq, "trp_player", ":order_town", ":town"),
                (troop_set_slot, "trp_player", ":order_reach", ":hour"),
              (try_end),
              (troop_set_inventory_slot, ":merchant", ":slot", -1),
              (troop_sort_inventory, ":merchant"),
              (troop_set_slot, "trp_player", ":order_warn", -1),
              (str_store_party_name, s1, ":order_town_no"),

              (troop_get_slot, ":reach_time", "trp_player", ":order_reach"),
              (troop_get_slot, ":found_time", "trp_player", ":order_hours"),              
              (store_sub, reg0, ":reach_time", ":found_time"),
              (val_div, reg0, 24),
              (store_sub, reg1, reg0, 1),
        
              (str_store_party_name, s2, ":town"),
              (str_store_troop_name, s3, ":merchant"),
              (str_store_item_name, s4, ":item"),
              (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s3}.\
 '{reg0?Your {s4} will be reach within {reg0} {reg1?days:day} to {s1}. But if you close enought to {s2}, you can collect your {s4} from {s3} in a day.\
 Tomorrow, your {s4} will be sent out with a notable merchant. You can come and collect your {s4} anytime you want after {reg0} {reg1?days:day}:Your {s4} is now ready at {s1} you can come and collect it anytime you want.}'"),
            (try_end),
          (try_end),
        (try_end),
    ]),
        
##  (12.0, 0, 0.0, [
##      (gt, "$g_item_ordered", 0),
##      (le, "$g_item_ordered_bought", 0),
##      (map_free, 0),
##    ], [
##      (try_for_range, ":town", towns_begin, towns_end),
##        (party_get_slot, ":merchant", ":town", "$g_item_ordered_slot"),
##
##        (try_for_range, ":slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
##          (le, "$g_item_ordered_bought", 0), #Make sure it only removes item one time.
##          (troop_get_inventory_slot, ":item", ":merchant", ":slot"),
##          (troop_get_inventory_slot_modifier, ":modifier", ":merchant", ":slot"),
##          (eq, ":item", "$g_item_ordered"),
##          (eq, ":modifier", "$g_item_ordered_modifier"),
##
##          (try_begin),
##            (le, "$g_item_ordered_bought", 0),
##            (assign, "$g_item_ordered_bought", ":town"),
##          (else_try),
##            (store_distance_to_party_from_party, ":distnew", "$g_item_ordered_party", ":town"),
##            (store_distance_to_party_from_party, ":distcur", "$g_item_ordered_party", "$g_item_ordered_bought"),
##            (lt, ":distnew", ":distcur"), #Current town is nearest than already setted?
##            (assign, "$g_item_ordered_bought", ":town"),
##          (try_end),
##        (try_end),
##      (try_end),
##
##      (gt, "$g_item_ordered_bought", 0), #Does any town have the ordered item?
##      (party_get_slot, ":merchant", "$g_item_ordered_bought", "$g_item_ordered_slot"), #Get the merchant from nearest party.
##      (assign, ":continue", 1),
##      (try_for_range, ":slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
##        (eq, ":continue", 1), #Make sure it only removes item one time.
##        (troop_get_inventory_slot, ":item", ":merchant", ":slot"),
##        (troop_get_inventory_slot_modifier, ":modifier", ":merchant", ":slot"),
##        (eq, ":item", "$g_item_ordered"),
##        (eq, ":modifier", "$g_item_ordered_modifier"),
##      
##        (store_current_hours, ":hour"),
##        (assign, "$g_item_ordered_bought_hours", ":hour"), #Set the current time.
##
##        (store_distance_to_party_from_party, ":dist", "$g_item_ordered_party", "$g_item_ordered_bought"), 
##        (val_mul, ":dist", 2),
##        (val_add, ":dist", ":hour"),
##        (assign, "$g_item_ordered_bought_reach", ":dist"), #When will the item reached?
##        (try_begin),
##          (eq, "$g_item_ordered_party", "$g_item_ordered_bought"), #Item found at same party, where player ordered item?
##          (assign, "$g_item_ordered_bought_reach", ":hour"), #Item is ready
##        (try_end),
##
##        (troop_set_inventory_slot, ":merchant", ":slot", -1),
##        (troop_sort_inventory, ":merchant"),
##
##        (assign, ":continue", 0),
##        (assign, "$g_item_ordered_warned", 0),
##        (str_store_party_name, s1, "$g_item_ordered_party"),
##        (store_sub, reg0, "$g_item_ordered_bought_reach", "$g_item_ordered_bought_hours"),
##        (val_div, reg0, 24),
##        (store_sub, reg1, reg0, 1),
##        (str_store_party_name, s2, "$g_item_ordered_bought"),
##        (str_store_troop_name, s3, ":merchant"),
##        (str_store_item_name, s4, "$g_item_ordered"),
##        (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s3}.\
## '{reg0?Your {s4} will be reach within {reg0} {reg1?days:day} to {s1}. But if you close enought to {s2}, you can collect your {s4} from {s3} in a day.\
## Tomorrow, your {s4} will be sent out with a notable merchant. You can come and collect your {s4} anytime you want after {reg0} {reg1?days:day}:Your {s4} is now ready at {s1} you can come and collect it anytime you want.}'"),
##      (try_end),
##    ]),

  (12.0, 0, 0.0, [
      (assign, ":cont", 0),
      (try_for_range, ":rand", 0, 25),
        (eq, ":cont", 0),
        (store_add, ":item", ":rand", slot_player_order_item),
        (store_add, ":found", ":rand", slot_player_order_found),
        (store_add, ":warn", ":rand", slot_player_order_warned),
        (troop_slot_ge, "trp_player", ":item", 1),
        (troop_slot_ge, "trp_player", ":found", 1),
        (troop_slot_lt, "trp_player", ":warn", 0),
        (assign, ":cont", 1),
      (try_end),
      (eq, ":cont", 1),
      (map_free, 0),
    ], [
      (try_for_range, ":order", 0, 25),
        (store_add, ":item", ":order", slot_player_order_item),
        (store_add, ":found", ":order", slot_player_order_found),
        (store_add, ":warn", ":order", slot_player_order_warned),
        (store_add, ":reach", ":order", slot_player_order_reach),
        (store_add, ":slot", ":order", slot_player_order_slot),
        (store_add, ":town", ":order", slot_player_order_town),

        (troop_slot_ge, "trp_player", ":item", 1),
        (troop_slot_ge, "trp_player", ":found", 1),
        (troop_slot_lt, "trp_player", ":warn", 0),
        (store_current_hours, ":hour"),
        (troop_get_slot, ":oreach", "trp_player", ":reach"),
        (ge, ":hour", ":oreach"),
        (troop_get_slot, ":item_no", "trp_player", ":item"),
        (troop_get_slot, ":town_no", "trp_player", ":town"),
        (troop_get_slot, ":slot_no", "trp_player", ":slot"),
        (party_get_slot, ":merchant", ":town_no", ":slot_no"),
        (str_store_party_name, s1, ":town_no"),
        (str_store_troop_name, s2, ":merchant"),
        (str_store_item_name, s3, ":item_no"),
        (troop_set_slot, "trp_player", ":warn", 1),
        (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s2}.\
 'Your {s3} is now ready at {s1}, you can come and collect it anytime you want.'"),
      (try_end),
    ]),

##  (12.0, 0, 0.0, [
##      (gt, "$g_item_ordered", 0),
##      (gt, "$g_item_ordered_bought", 0),
##      (le, "$g_item_ordered_warned", 0),
##      (map_free, 0),
##    ], [
##        (assign, ":reach", "$g_item_ordered_bought_reach"),
##        (store_current_hours, ":hour"),
##        (ge, ":hour", ":reach"),
##        (party_get_slot, ":merchant", "$g_item_ordered_party", "$g_item_ordered_slot"),
##        (str_store_party_name, s1, "$g_item_ordered_party"),
##        (str_store_troop_name, s2, ":merchant"),
##        (str_store_item_name, s3, "$g_item_ordered"),
##        (assign, "$g_item_ordered_warned", 1),
##        (dialog_box, "@You saw the messenger reached your party and gives you a paper which came from {s1} {s2}.\
## 'Your {s3} is now ready at {s1}, you can come and collect it anytime you want.'"),
##    ]),
  #
  ## UID: 100 - End
  #
  ## UID: 78 - End

  ## UID: 63 - Begin
  #
  # Just set name to default one daily, if he changed his name.
  (24.0, 0, 0.0, [(gt, "$players_kingdom", 0)], [(call_script, "script_set_prefix")]),
  #
  ## UID: 63 - End

  ## UID: 43 - Begin
  #
    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),
    ],
    [
        (assign, "$freelancer_state", 0),
        (call_script, "script_freelancer_detach_party"),
		
		#to prevent companions from being lost forever
		(call_script, "script_party_restore"), 
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
			(neg|troop_is_hero, ":return_troop"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
			(party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
		(try_end),

        #removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

		(assign, "$g_encountered_party", "$g_enemy_party"),
		(jump_to_menu, "mnu_captivity_start_wilderness"),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		
		#collected nearby enemies->detach (post-battle)
		(try_begin), 
			(party_slot_ge, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
			(map_free),
			(party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 0),
			(party_get_num_attached_parties, ":num_attached", "p_main_party"),
			(try_for_range_backwards, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
				(party_detach, ":party"),
			(try_end),
		(try_end),
		
		#Is currently in battle
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
		
		#checks that the player's health is high enough to join battle
        (store_troop_health, ":player_health", "trp_player"),
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT

    (1.0, 0, 0, [
        (eq, "$freelancer_state", 0),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),

		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":commander_faction"),
        (lt, ":relation", 0),

        (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
        (eq, "p_temp_party_2", ":attached_party"),
    ],
    [
        (assign, "$enlisted_party", -1),
        (party_detach, "p_temp_party_2"),
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
        (val_add, ":chance", 10),
        (store_random_in_range, ":prisoner_state", 0, ":chance"),

        (try_begin),
            (is_between, ":prisoner_state", 0, 5),
            (call_script, "script_party_calculate_strength", "p_main_party", 0),
            (assign, ":main_strength", reg0),
            (call_script, "script_party_calculate_strength", "p_temp_party_2", 0),
            (assign, ":temp_strength", reg0),
            (ge, ":temp_strength", ":main_strength"),

            (party_get_num_prisoner_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_prisoner_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_remove_prisoners, "p_temp_party_2", ":cur_troops", ":cur_size"),
            (try_end),

            (tutorial_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
            (start_encounter, "p_temp_party_2"),
            (change_screen_map),
        (else_try),
            (is_between, ":prisoner_state", 5, 10),
            (tutorial_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
            (party_clear, "p_temp_party_2"),
        (else_try),
            (tutorial_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_add_members, "p_main_party", ":cur_troops", ":cur_size"),
            (try_end),
            (party_clear, "p_temp_party_2"),
        (try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

  (24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
		(troop_get_slot, ":days_left", "trp_player", slot_troop_days_on_mission),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left till you are declared as a deserter!"),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_deserts"),
          (display_message, "@You have now been declared as a deserter!"),
		(try_end),  
    ]),
  #
  ## UID: 43 - End

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),
  
  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_swadian_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_vaegir_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [
      (store_random_party_of_template, reg(2), "pt_messenger_party"),
      (party_is_in_any_town,reg(2)),
    ], [
        (store_faction_of_party, ":faction_no", reg(2)),
        (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
        (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
        ## UID: 152 - Begin
        #
        #(party_set_ai_object,reg(2),reg0),
        (call_script, "script_party_set_ai_object", reg(2), reg0),
        #
        ## UID: 152 - End
        (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

  #Kingdom Parties
  (1.0, 0, 0.0, [], [
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),

##        (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##        (try_begin),
##          (store_random_in_range, ":random_no", 0, 100),
##          (lt, ":random_no", 10),
##          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##        (try_end),
##        (try_begin),
##          (store_random_in_range, ":random_no", 0, 100),
##          (lt, ":random_no", 10),
##          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##        (try_end),
##        (try_begin),
##          (store_random_in_range, ":random_no", 0, 100),
##          (lt, ":random_no", 10),
##          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##        (try_end),
##        (try_begin),
##          (store_random_in_range, ":random_no", 0, 100),
##          (lt, ":random_no", 10),
##          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##        (try_end),
        (try_begin),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 10),
          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
        (try_end),
        ## UID: 79 - Begin
        #
        (try_begin),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 10),
          (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_merchant_caravan),
        (try_end),
        #
        ## UID: 79 - End
        #(try_begin),
          #(store_random_in_range, ":random_no", 0, 100),
          #(lt, ":random_no", 10),
          #(call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
        #(try_end),
      (try_end),
    ]),


#Swadians
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),


#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_foragers"),
#                         (assign, "$pin_limit", "$peak_swadian_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_scouts"),
#                         (assign, "$pin_limit", "$peak_swadian_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_patrol"),
#                         (assign, "$pin_limit", "$peak_swadian_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_war_party"),
#                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
#Vaegirs
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
  

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
#                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
#                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
#                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
#                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Villains etc.
#  (14.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_sea_raiders"),
#                         (assign, "$pin_party_template", "pt_sea_raiders"),
#                         (assign, "$pin_limit", 5),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),


#
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_refugees"),
##                         (assign, "$pin_limit", 5),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),
##
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_farmers"),
##                         (assign, "$pin_limit", 6),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
  
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_dark_hunters"),
##                         (assign, "$pin_limit", "$peak_dark_hunters"),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#Companion quests

##  (0, 0, ti_once,
##   [
##       (entering_town,"p_town_1"),
##       (main_party_has_troop,"trp_borcha"),
##       (eq,"$borcha_freed",0)
##    ],
##   
##   [
##       (assign,"$borcha_arrive_sargoth_as_prisoner", 1),
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##
##  (1, 0, ti_once,
##   [
##      (map_free,0),
##      (eq,"$borcha_asked_for_freedom",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##  
##  (2, 0, ti_once,
##   [
##      (map_free, 0),
##      (neq,"$borcha_asked_for_freedom",0),
##      (eq,"$borcha_freed",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),

  # Runaway Peasants quest
  (0.2, 0.0, 0.0, [
      (check_quest_active, "qst_bring_back_runaway_serfs"),
      (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
      (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
      (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
      (try_begin),
        (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
        (try_begin),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
        (else_try),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
        (else_try),
          (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
          (gt, ":cur_distance", 3),
          ## UID: 152 - Begin
          #
          #(party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
          (call_script, "script_party_set_ai_object", "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
          #
          ## UID: 152 - End
        (try_end),
      (try_end),
      (try_begin),
        (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
        (try_begin),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
        (else_try),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
        (else_try),
          (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
          (gt, ":cur_distance", 3),
          ## UID: 152 - Begin
          #
          #(party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
          (call_script, "script_party_set_ai_object", "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
          #
          ## UID: 152 - End
        (try_end),
      (try_end),
      (try_begin),
        (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
        (try_begin),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
        (else_try),
          (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
          (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
          (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
        (else_try),
          (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
          (gt, ":cur_distance", 3),
          ## UID: 152 - Begin
          #
          #(party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
          (call_script, "script_party_set_ai_object", "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
          #
          ## UID: 152 - End
        (try_end),
      (try_end),
      (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
      (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
      (ge, ":sum_removed", 3),
      (try_begin),
        (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
        (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
      (else_try),
        (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
        (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
      (else_try),
        (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
      (try_end),
   ],
  []
  ),
### Defend Nobles Against Peasants quest
##  (0.2, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", slot_quest_target_center),
##       (assign, ":num_active_parties", 0),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (eq, ":num_active_parties", 0),
##       (try_begin),
##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
##       (try_end),
##    ],
##   []
##   ),
### Capture Conspirators quest
##  (0.15, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_capture_conspirators"),
##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
##       (neg|check_quest_failed, "qst_capture_conspirators"),
##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", slot_quest_target_center),
##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", slot_quest_target_faction),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##         (store_random_in_range, ":random_no", 0, 100),
##         (lt, ":random_no", 20),
##         (set_spawn_radius, 3),
##         (spawn_around_party,":quest_target_center","pt_conspirator"),
##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
##         (party_get_num_companions, ":num_companions", reg0),
##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
##         (party_set_flags, reg0, pf_default_behavior, 0),
##         (try_begin),
##           (le, "$qst_capture_conspirators_party_2", 0),
##           (assign, "$qst_capture_conspirators_party_2", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_3", 0),
##           (assign, "$qst_capture_conspirators_party_3", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_4", 0),
##           (assign, "$qst_capture_conspirators_party_4", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_5", 0),
##           (assign, "$qst_capture_conspirators_party_5", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_6", 0),
##           (assign, "$qst_capture_conspirators_party_6", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_7", 0),
##           (assign, "$qst_capture_conspirators_party_7", reg0),
##         (try_end),
##       (try_end),
##
##       (assign, ":num_active_parties", 0),
##
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_1", 0),
##         (party_is_active, "$qst_capture_conspirators_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
##           (remove_party, "$qst_capture_conspirators_party_1"),
##         (else_try),
##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
##           (gt, ":num_attachments", 0),
##           (assign, ":leave_meeting", 0),
##           (try_begin),
##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
##             (eq, ":num_attachments", ":required_attachments"),
##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (try_begin),
##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
##             (assign, ":min_distance", 3),
##             (try_begin),
##               (is_currently_night),
##               (assign, ":min_distance", 2),
##             (try_end),
##             (lt, ":cur_distance", ":min_distance"),
##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (eq, ":leave_meeting", 1),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_2", 0),
##             (party_detach, "$qst_capture_conspirators_party_2"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_3", 0),
##             (party_detach, "$qst_capture_conspirators_party_3"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_4", 0),
##             (party_detach, "$qst_capture_conspirators_party_4"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_5", 0),
##             (party_detach, "$qst_capture_conspirators_party_5"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_6", 0),
##             (party_detach, "$qst_capture_conspirators_party_6"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_7", 0),
##             (party_detach, "$qst_capture_conspirators_party_7"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_2", 0),
##         (party_is_active, "$qst_capture_conspirators_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_2"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_3", 0),
##         (party_is_active, "$qst_capture_conspirators_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_3"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_4", 0),
##         (party_is_active, "$qst_capture_conspirators_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_4"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_5", 0),
##         (party_is_active, "$qst_capture_conspirators_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_5"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_6", 0),
##         (party_is_active, "$qst_capture_conspirators_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_6"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_7", 0),
##         (party_is_active, "$qst_capture_conspirators_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_7"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##
##       (eq, ":num_active_parties", 0),
##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
##       (try_begin),
##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
##         (gt, ":count_captured_conspirators", ":limit"),
##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
##       (try_end),
##    ],
##   []
##   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         ## UID: 152 - Begin
         #
         #(party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (call_script, "script_party_set_ai_object", "$qst_follow_spy_spy_party", ":quest_giver_center"),
         #(party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (call_script, "script_party_set_ai_object", "$qst_follow_spy_spy_partners_party", ":quest_giver_center"),
         #
         ## UID: 152 - End
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),

  (0.1, 0.0, 0.1, [
      (check_quest_active, "qst_escort_merchant_caravan"),
      (eq, "$escort_merchant_caravan_mode", 0),
    ], [
        (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
        (try_begin),
          (party_is_active, ":quest_target_party"),
          (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
          (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
          ## UID: 152 - Begin
          #
          #(party_set_ai_object, ":quest_target_party", "p_main_party"),
          (call_script, "script_party_set_ai_object", ":quest_target_party", "p_main_party"),
          #
          ## UID: 152 - End
          (try_end),
    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          (try_for_range, ":unused", 0, 30),
            (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies
           
            (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

  #NPC system changes begin
  #Move unemployed NPCs around taverns
  (24 * 15 , 0, 0, [(call_script, "script_update_companion_candidates_in_taverns")], []),

  #Process morale and determine personality clashes
  (0, 0, 24, [], [
      #Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
      #Set their relation to the player
      (assign, ":npcs_in_party", 0),
      (assign, ":grievance_divisor", 100),
      (try_for_range, ":npc1", companions_begin, companions_end),
        (main_party_has_troop, ":npc1"),
        (val_add, ":npcs_in_party", 1),
      (try_end),
      (val_sub, ":grievance_divisor", ":npcs_in_party"),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (val_add, ":grievance_divisor", ":persuasion_level"),
      (assign, reg7, ":grievance_divisor"),
      #(display_message, "@{!}Process NPC changes. GD: {reg7}"),

      #Activate personality clash from 24 hours ago
      (try_begin), #scheduled personality clashes require at least 24hrs together
        (gt, "$personality_clash_after_24_hrs", 0),
        (eq, "$disable_npc_complaints", 0),
        (try_begin),
          (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
          (main_party_has_troop, "$personality_clash_after_24_hrs"),
          (main_party_has_troop, ":other_npc"),
          (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
        (try_end),
      (assign, "$personality_clash_after_24_hrs", 0),
      (try_end),

      (try_for_range, ":npc", companions_begin, companions_end),
        #Reset meeting variables
        (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
        (try_begin),
          (troop_slot_eq, ":npc", slot_troop_met, 1),
          (troop_set_slot, ":npc", slot_troop_met_previously, 1),
        (try_end),

        #Check for coming out of retirement
        (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
        (try_begin),
          (eq, ":occupation", slto_retirement),
          (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),
          (str_store_troop_name, s31, ":npc"),
          (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
          (assign, reg4, ":player_renown"),
          (assign, reg5, ":renown_min"),
          #(display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),
          (gt, ":player_renown", ":renown_min"),
          (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
          (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
          (troop_set_slot, ":npc", slot_troop_occupation, 0),
        (try_end),

        #Check for political issues
        (try_begin), #does npc's opponent pipe up?
          (troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
          (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),
          (troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
          (troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
          (troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),
          (str_store_troop_name, s3, ":npc"),
          (str_store_troop_name, s4, ":other_npc"),

          (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
          (try_end),
        (try_end),

        #Check for quitting
        (try_begin),
          (main_party_has_troop, ":npc"),
          (call_script, "script_npc_morale", ":npc"),
          (assign, ":npc_morale", reg0),
          (try_begin),
            (lt, ":npc_morale", 20),
            (store_random_in_range, ":random", 0, 100),
            (val_add, ":npc_morale", ":random"),
            (lt, ":npc_morale", 20),
            (assign, "$npc_is_quitting", ":npc"),
          (try_end),

          #Reduce grievance over time (or augment, if party is overcrowded
          (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
          (val_mul, ":grievance", 90),
          (val_div, ":grievance", ":grievance_divisor"),
          (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
          (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
          (val_mul, ":grievance", 90),
          (val_div, ":grievance", ":grievance_divisor"),
          (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),

          #Change personality grievance levels
          (try_begin),
            (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
            (             eq, "$disable_npc_complaints", 1),
            (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
            (main_party_has_troop, ":object"),
            (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
          (try_end),
      
          (try_begin),
            (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
            (             eq, "$disable_npc_complaints", 1),
            (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
            (main_party_has_troop, ":object"),
            (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
          (try_end),

          (try_begin),
            (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
            (             eq, "$disable_npc_complaints", 1),
            (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
            (main_party_has_troop, ":object"),
            (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
            (val_mul, ":grievance", 9),
            (val_div, ":grievance", 10),
            (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
          (try_end),

          #Check for new personality clashes
          #Active personality clash 1 if at least 24 hours have passed
          (try_begin),
            (eq, "$disable_npc_complaints", 0),
            (eq, "$npc_with_personality_clash", 0),
            (eq, "$npc_with_personality_clash_2", 0),
            (eq, "$personality_clash_after_24_hrs", 0),
            (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
            (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
            (main_party_has_troop, ":other_npc"),
            (assign, "$personality_clash_after_24_hrs", ":npc"),
          (try_end),

          #Personality clash 2 and personality match is triggered by battles
          (try_begin),
            (eq, "$npc_with_political_grievance", 0),
            (troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
            (assign, "$npc_with_political_grievance", ":npc"),
          (try_end),

        #main party does not have troop, and the troop is a companion
        (else_try),
          (neg|main_party_has_troop, ":npc"),
          (eq, ":occupation", slto_player_companion),
          (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
          (try_begin),
            (gt, ":days_on_mission", 0),
            (val_sub, ":days_on_mission", 1),
            (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
          (else_try),
            (troop_slot_ge, ":npc", slot_troop_current_mission, 1),
            #If the hero can join
            (this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
            (hero_can_join, ":npc"),
            (assign, "$npc_to_rejoin_party", ":npc"),
          (try_end),
        (try_end),
      (try_end),
    ]),


#NPC system changes end

# Lady of the lake achievement
   (1, 0, 0,
   [
     (troop_get_type, ":is_female", "trp_player"),
     (eq, ":is_female", 1),       
     (try_for_range, ":companion", companions_begin, companions_end),
       (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

       (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       (try_for_range, ":i_slot", 0, ":inv_cap"),
         (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 (ge, ":item_id", 0),

	 	 (this_or_next|eq, ":item_id", "itm_great_sword"),
	 	 (this_or_next|eq, ":item_id", "itm_sword_two_handed_a"),
		 (eq, ":item_id", "itm_strange_great_sword"),
		 		 
		 (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
		 (assign, ":inv_cap", 0),
	   (try_end),
	 (try_end),
    ],
   []
   ),





 
]
