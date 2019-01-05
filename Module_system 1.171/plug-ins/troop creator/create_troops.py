import random
import os
from headers.header_items import *
from module_items import *

iarmor_head = 7
iarmor_body = 9
iarmor_legs = 6
iarmor_hand = 1

iweapon_one_handed = 140 #One handed
iweapon_two_handed = 65
iweapon_one_handed_ranged = 150
iweapon_two_handed_ranged = 275
iweapon_bow = 110
iweapon_crossbow = 60
iweapon_shield = 80
iweapon_horse = 32

islot_uid = 0
islot_name = 1
islot_list = 2
islot_flags = 3
islot_value = 5
islot_info = 6
islot_imod = 7

upgrade_slot_1  = 0x000001
upgrade_slot_2  = 0x000002
upgrade_slot_3  = 0x000004
upgrade_slot_4  = 0x000008
upgrade_slot_5  = 0x000010
upgrade_slot_6  = 0x000020
upgrade_slot_7  = 0x000040
upgrade_slot_8  = 0x000080
upgrade_slot_9  = 0x000100
upgrade_slot_10 = 0x000200
upgrade_slot_11 = 0x000400
upgrade_slot_12 = 0x000800
upgrade_slot_13 = 0x001000
upgrade_slot_14 = 0x002000
upgrade_slot_15 = 0x004000
upgrade_slot_16 = 0x008000
upgrade_slot_17 = 0x010000
upgrade_slot_18 = 0x020000
upgrade_slot_19 = 0x040000
upgrade_slot_20 = 0x080000

stp_one_handed_weapon = 0x01
stp_two_handed_weapon = 0x02
stp_ranged_one_handed_weapon = 0x04
stp_ranged_two_handed_weapon = 0x08
stp_bow = 0x010
stp_arrow = 0x020
stp_shield = 0x040
stp_head_armor = 0x080
stp_hand_armor = 0x0100
stp_leg_armor = 0x0200
stp_body_armor = 0x0400
stp_horse      = 0x0800
stp_shield_horse = 0x01000 #Shield can use on horse
stp_crossbow = 0x02000
stp_bolt = 0x04000

ifaction_id = "fac_neutral"
ifaction_name = 0
ifaction_suffix_0 = 1

ifaction_suffix_1 = "Bounty Hunter" #String
ifaction_suffix_1_pl = "Bounty Hunters" #String
ifaction_suffix_1_tier = 5 #Integer
ifaction_suffix_1_upgrade = 0 #Hexadecimal
ifaction_suffix_1_weapons = stp_two_handed_weapon #Hexadecimal
ifaction_suffix_1_armors = stp_head_armor|stp_body_armor|stp_leg_armor|stp_hand_armor #Hexadecimal
ifaction_suffix_1_multiplier = 1 #Float
ifaction_suffix_1_knows = "knows_ironflesh_4|knows_athletics_4|knows_power_strike_5" #String

def get_armor(type, min, max):
    #1 = head
    #2 = hand
    #3 = body
    #4 = legs
    result = ""
    if (type == 1):
        for item in items:
            if is_head_armor(item[3]) == 1 and itp_merchandise&int(item[3]):
               value = int(get_head_armor(item[6]))
               if value <= max and value > min:
                   if not result:
                       result = "itm_" + item[0]
                   elif (int(random.randint(0, 100)) < 15):
                       result = "itm_" + item[0]
    elif (type == 2):
        for item in items:
            if is_hand_armor(item[3]) == 1 and itp_merchandise&int(item[3]):
               value = int(get_body_armor(item[6]))
               if value <= max and value > min:
                   if not result:
                       result = "itm_" + item[0]
                   elif (int(random.randint(0, 100)) < 15):
                       result = "itm_" + item[0]
    elif (type == 3):
        for item in items:
            if is_body_armor(item[3]) == 1 and itp_merchandise&int(item[3]):
               value = int(get_body_armor(item[6]))
               if value <= max and value > min:
                   if not result:
                       result = "itm_" + item[0]
                   elif (int(random.randint(0, 100)) < 15):
                       result = "itm_" + item[0]
    elif (type == 4):
        for item in items:
            if is_leg_armor(item[3]) == 1 and itp_merchandise&int(item[3]):
               value = int(get_leg_armor(item[6]))
               if value <= max and value > min:
                   if not result:
                       result = "itm_" + item[0]
                   elif (int(random.randint(0, 100)) < 15):
                       result = "itm_" + item[0]
    return result

def get_item_type_as_int(types):
    value = int(types)
    if itp_unique&value:
        value -= itp_unique
    if itp_always_loot&value:
        value -= itp_always_loot
    if itp_no_parry&value:
        value -= itp_no_parry
    if itp_default_ammo&value:
        value -= itp_default_ammo
    if itp_merchandise&value:
        value -= itp_merchandise
    if itp_wooden_attack&value:
        value -= itp_wooden_attack
    if itp_wooden_parry&value:
        value -= itp_wooden_parry
    if itp_cant_reload_on_horseback&value:
        value -= itp_cant_reload_on_horseback
    if itp_two_handed&value:
        value -= itp_two_handed
    if itp_primary&value:
        value -= itp_primary
    if itp_secondary&value:
        value -= itp_secondary
    if itp_covers_legs&value:
        value -= itp_covers_legs
    if itp_consumable&value:
        value -= itp_consumable
    if itp_bonus_against_shield&value:
        value -= itp_bonus_against_shield
    if itp_penalty_with_shield&value:
        value -= itp_penalty_with_shield
    if itp_cant_use_on_horseback&value:
        value -= itp_cant_use_on_horseback
    if itp_civilian&value:
        value -= itp_civilian
    if itp_fit_to_head&value:
        value -= itp_fit_to_head
    if itp_covers_head&value:
        value -= itp_covers_head
    if itp_crush_through&value:
        value -= itp_crush_through
    if itp_remove_item_on_use&value:
        value -= itp_remove_item_on_use
    if itp_unbalanced&value:
        value -= itp_unbalanced
    if itp_covers_beard&value:
        value -= itp_covers_beard
    if itp_no_pick_up_from_ground&value:
        value -= itp_no_pick_up_from_ground
    if itp_can_knock_down&value:
        value -= itp_can_knock_down
    if itp_covers_hair&value:
        value -= itp_covers_hair
    if itp_force_show_body&value:
        value -= itp_force_show_body
    if itp_force_show_left_hand&value:
        value -= itp_force_show_left_hand
    if itp_force_show_right_hand&value:
        value -= itp_force_show_right_hand
    if itp_covers_hair_partially&value:
        value -= itp_covers_hair_partially
    if itp_extra_penetration&value:
        value -= itp_extra_penetration
    if itp_has_bayonet&value:
        value -= itp_has_bayonet
    if itp_cant_reload_while_moving&value:
        value -= itp_cant_reload_while_moving
    if itp_ignore_gravity&value:
        value -= itp_ignore_gravity
    if itp_ignore_friction&value:
        value -= itp_ignore_friction
    if itp_is_pike&value:
        value -= itp_is_pike
    if itp_offset_musket&value:
        value -= itp_offset_musket
    if itp_no_blur&value:
        value -= itp_no_blur
    if itp_cant_reload_while_moving_mounted&value:
        value -= itp_cant_reload_while_moving_mounted
    if itp_has_upper_stab&value:
        value -= itp_has_upper_stab
    if itp_disable_agent_sounds&value:
        value -= itp_disable_agent_sounds

    if value > int(itp_attach_armature):
        value -= int(itp_attach_armature)
        
    return value

def get_item_type(types):
    value = get_item_type_as_int(types)
    if value == 1:
        return "itp_type_horse"
    elif value == 2:
        return "itp_type_one_handed_wpn"
    elif value == 3:
        return "itp_type_two_handed_wpn"
    elif value == 4:
        return "itp_type_polearm"
    elif value == 5:
        return "itp_type_arrows"
    elif value == 6:
        return "itp_type_bolts"
    elif value == 7:
        return "itp_type_shield"
    elif value == 8:
        return "itp_type_bow"
    elif value == 9:
        return "itp_type_crossbow"
    elif value == 10:
        return "itp_type_thrown"
    elif value == 11:
        return "itp_type_goods"
    elif value == 12:
        return "itp_type_head_armor"
    elif value == 13:
        return "itp_type_body_armor"
    elif value == 14:
        return "itp_type_foot_armor"
    elif value == 15:
        return "itp_type_hand_armor"
    elif value == 16:
        return "itp_type_pistol"
    elif value == 17:
        return "itp_type_musket"
    elif value == 18:
        return "itp_type_bullets"
    elif value == 19:
        return "itp_type_animal"
    else:
        return "itp_type_book"

def is_head_armor(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_head_armor):
        return 1
    return 0

def is_body_armor(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_body_armor):
        return 1
    return 0

def is_leg_armor(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_foot_armor):
        return 1
    return 0

def is_hand_armor(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_hand_armor):
        return 1
    return 0

#Deprecated, use create_troop(number) instead.
##def create_troop(tier, type):
##    array = []
##    if tier == 1:
##        array.append(get_armor(1, 0, 8)) #Head
##        array.append(get_armor(2, 4, 16)) #Body
##        array.append(get_armor(3, 4, 12)) #Legs
##        array.append("") #Hand
##    return array

##def test():
##    for item in items:
####        print("%s is a %s"%(item[1], get_item_type(item[3])))
##        print("%s is a head armor %d"%(item[1], is_head_armor(item[3])))
##
##test()

def getValue(number, arg):
    if arg == 0:
        return globals()["ifaction_suffix_" + str(number)]
    else:
        return globals()["ifaction_suffix_" + str(number) + "_" + arg]

def getName(number):
    return getValue(number, 0)

def getNameByFaction(number):
    if ifaction_name == 0:
        return getName(number)
    return ifaction_name + " " + getName(number)

def getId(number):
    return getNameByFaction(number).replace(" ", "_").lower()

def getPluralName(number):
    return getValue(number, "pl")

def getPluralNameByFaction(number):
    if ifaction_name == 0:
        return getPluralName(number)
    return ifaction_name + " " + getPluralName(number)

def getTier(number):
    return getValue(number, "tier")

def getUpgrades(number):
    return getValue(number, "upgrade")

def getWeapons(number):
    return getValue(number, "weapons")

def getArmors(number):
    return getValue(number, "armors")

def getMultiplier(number):
    return getValue(number, "multiplier")

def getKnows(number):
    return getValue(number, "knows")

def getLevel(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)

    level = (3 + tier - 1) * tier
    level = level * multiplier
    return int(level)

def getWeaponProficiency(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)

    prof = 60 + ((15 * tier) * multiplier)
    return int(prof)

def getSpecificProficiency(number):
    return int(getWeaponProficiency(number) + 25)

def checkUpgrade(number, upgrade):
    slots = int(getUpgrades(number))
    if upgrade&slots:
        return 1
    return 0

def getUpgradeByIndex(number, index):
    slots = int(getUpgrades(number))
    result = []
    if upgrade_slot_1&slots:
        result.append("upgrade_slot_1")
    if upgrade_slot_2&slots:
        result.append("upgrade_slot_2")
    if upgrade_slot_3&slots:
        result.append("upgrade_slot_3")
    if upgrade_slot_4&slots:
        result.append("upgrade_slot_4")
    if upgrade_slot_5&slots:
        result.append("upgrade_slot_5")
    if upgrade_slot_6&slots:
        result.append("upgrade_slot_6")
    if upgrade_slot_7&slots:
        result.append("upgrade_slot_7")
    if upgrade_slot_8&slots:
        result.append("upgrade_slot_8")
    if upgrade_slot_9&slots:
        result.append("upgrade_slot_9")
    if upgrade_slot_10&slots:
        result.append("upgrade_slot_10")
    if upgrade_slot_11&slots:
        result.append("upgrade_slot_11")
    if upgrade_slot_12&slots:
        result.append("upgrade_slot_12")
    if upgrade_slot_13&slots:
        result.append("upgrade_slot_13")
    if upgrade_slot_14&slots:
        result.append("upgrade_slot_14")
    if upgrade_slot_15&slots:
        result.append("upgrade_slot_15")
    if upgrade_slot_16&slots:
        result.append("upgrade_slot_16")
    if upgrade_slot_17&slots:
        result.append("upgrade_slot_17")
    if upgrade_slot_18&slots:
        result.append("upgrade_slot_18")
    if upgrade_slot_19&slots:
        result.append("upgrade_slot_19")
    if upgrade_slot_20&slots:
        result.append("upgrade_slot_20")
    if index == -1:
        return len(result)
    if len(result) > index:
        return result[index]
    else:
        return ""

def getUpgradeIdByIndex(number, index):
    if not getUpgradeByIndex(number, index):
        return 0
    return int(getUpgradeByIndex(number, index)[13:])

def getHeadMin(number):
    multiplier = getMultiplier(number)
    tier = getTier(number)

    base = iarmor_head * multiplier
    base = base * tier
    return int(base)

def getHeadMax(number):
    return getHeadMin(number) + iarmor_head

def getHandMin(number):
    multiplier = getMultiplier(number)
    tier = getTier(number)

    base = iarmor_hand * multiplier
    base = base * tier
    return int(base)

def getHandMax(number):
    return getHandMin(number) + (iarmor_hand * 3)

def getBodyMin(number):
    multiplier = getMultiplier(number)
    tier = getTier(number)

    base = iarmor_body * multiplier
    base = base * tier
    return int(base)

def getBodyMax(number):
    return getBodyMin(number) + iarmor_body

def getLegsMin(number):
    multiplier = getMultiplier(number)
    tier = getTier(number)

    base = iarmor_legs * multiplier
    base = base * tier
    return int(base)

def getLegsMax(number):
    return getLegsMin(number) + iarmor_legs

def getMinById(number, type):
    if type == 1:
        return getHeadMin(number)
    elif type == 2:
        return getHandMin(number)
    elif type == 3:
        return getBodyMin(number)
    elif type == 4:
        return getLegsMin(number)
    else:
        return 0

def getMaxById(number, type):
    if type == 1:
        return getHeadMax(number)
    elif type == 2:
        return getHandMax(number)
    elif type == 3:
        return getBodyMax(number)
    elif type == 4:
        return getLegsMax(number)
    else:
        return 0

def getWeaponMin(number, hand):
    tier = getTier(number)
    multiplier = getMultiplier(number)

    base = 0
    if hand == 1:
        base = iweapon_one_handed
    else:
        base = iweapon_two_handed

    base = (base * tier) * multiplier
    return int(base)

def getWeaponMax(number, hand):
    base = 0
    if hand == 1:
        base = iweapon_one_handed
    else:
        base = iweapon_two_handed
    return int(getWeaponMin(number, hand) + (base * 2))

def getRangedWeaponMin(number, hand):
    tier = getTier(number)
    multiplier = getMultiplier(number)

    base = 0
    if hand == 1:
        base = iweapon_one_handed_ranged
    else:
        base = iweapon_two_handed_ranged

    base = (base * tier) * multiplier
    return int(base)

def getRangedWeaponMax(number, hand):
    base = 0
    if hand == 1:
        base = iweapon_one_handed_ranged
    else:
        base = iweapon_two_handed_ranged
    return int(getRangedWeaponMin(number, hand) + base)

def getBowMin(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)
    base = (iweapon_bow * tier) * multiplier
    return int(base)

def getBowMax(number):
    return int(getBowMin(number) + iweapon_bow)

def getCrossbowMin(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)
    base = (iweapon_crossbow * tier) * multiplier
    return int(base)

def getCrossbowMax(number):
    return int(getCrossbowMin(number) + (iweapon_crossbow * 2))

def getShieldMin(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)
    base = (iweapon_shield * tier) * multiplier
    return int(base)

def getShieldMax(number):
    return int(getShieldMin(number) + iweapon_shield)

def getHorseMin(number):
    tier = getTier(number)
    multiplier = getMultiplier(number)
    base = (iweapon_horse * tier) * multiplier
    return int(base)

def getHorseMax(number):
    return int(getHorseMin(number) + iweapon_horse)

def isOneHandedWeapon(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_one_handed_wpn):
        return 1
    return 0

def isTwoHandedWeapon(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_two_handed_wpn):
        return 1
    return 0

def isOneHandedRangedWeapon(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_polearm) and not itp_two_handed&int(types):
        return 1
    return 0

def isTwoHandedRangedWeapon(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_polearm) and itp_two_handed&int(types):
        return 1
    return 0

def isArrow(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_arrows):
        return 1
    return 0

def isBolt(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_bolts):
        return 1
    return 0

def isBow(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_bow):
        return 1
    return 0

def isCrossbow(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_crossbow):
        return 1
    return 0

def isShield(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_shield):
        return 1
    return 0

def isHorse(types):
    type = get_item_type_as_int(types)
    if type == int(itp_type_horse):
        return 1
    return 0

def get_weapon(type, number):
    #1: One Handed
    #2: Two Handed
    #3: One Handed Polearm
    #4: Two Handed Polearm
    result = ""
    if (type == 1):
        for item in items:
            if isOneHandedWeapon(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
                if value <= getWeaponMax(number, 1) and value > getWeaponMin(number, 1):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    elif (type == 2):
        for item in items:
            if isTwoHandedWeapon(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
                print item[1] + " " + str(value) + " " + str(getWeaponMin(number, 2)) + " " + str(getWeaponMax(number, 2))
                if value <= getWeaponMax(number, 2) and value > getWeaponMin(number, 2):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    elif (type == 3):
        for item in items:
            if isOneHandedRangedWeapon(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
##                print("%s - %d (%d + %d)"%(item[0], value, int(get_swing_damage(item[6])), int(get_thrust_damage(item[6]))))
                if value <= getRangedWeaponMax(number, 1) and value > getRangedWeaponMin(number, 1):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    elif (type == 4):
        for item in items:
            if isTwoHandedRangedWeapon(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
                if value <= getRangedWeaponMax(number, 2) and value > getRangedWeaponMin(number, 2):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    return result

def get_arrow(type):
    #1: Arrow
    #2: Bolt
    result = ""
    if (type == 1):
        for item in items:
            if isArrow(item[3]) == 1 and itp_merchandise&int(item[3]):
                if not result:
                    result = "itm_" + item[0]
                elif (int(random.randint(0, 100)) < 15):
                    result = "itm_" + item[0]
    elif (type == 2):
        for item in items:
            if isBolt(item[3]) == 1 and itp_merchandise&int(item[3]):
                if not result:
                    result = "itm_" + item[0]
                elif (int(random.randint(0, 100)) < 15):
                    result = "itm_" + item[0]
    return result

def get_bow(type, number):
    #1: Bow
    #2: Crossbow
    result = ""
    if (type == 1):
        for item in items:
            if isBow(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
                if value <= getBowMax(number) and value > getBowMin(number):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    elif (type == 2):
        for item in items:
            if isCrossbow(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = 0
                value += int(get_swing_damage(item[6]))
                value += int(get_thrust_damage(item[6]))
                if value <= getCrossbowMax(number) and value > getCrossbowMin(number):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    return result

def get_shield(type, number):
    #1: All Shield
    #2: Shield can use on Horse
    result = ""
    if (type == 1):
        for item in items:
            if isShield(item[3]) == 1 and itp_merchandise&int(item[3]):
                value = int(get_hit_points(item[6]))
                if value <= getShieldMax(number) and value > getShieldMin(number):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    elif (type == 2):
        for item in items:
            if isShield(item[3]) == 1 and itp_merchandise&int(item[3]) and not itp_cant_use_on_horseback&int(item[3]):
                value = int(get_hit_points(item[6]))
                if value <= getShieldMax(number) and value > getShieldMin(number):
                    if not result:
                        result = "itm_" + item[0]
                    elif (int(random.randint(0, 100)) < 15):
                        result = "itm_" + item[0]
    return result

def get_horse(number):
    result = ""
    for item in items:
        if isHorse(item[3]) == 1 and itp_merchandise&int(item[3]):
            value = int(get_hit_points(item[6]))
            if value <= getHorseMax(number) and value > getHorseMin(number):
                if not result:
                    result = "itm_" + item[0]
                elif (int(random.randint(0, 100)) < 15):
                    result = "itm_" + item[0]
    return result

def getKnownLevel(number):
    tier = getTier(number)
    multiplier = getMultiplier(multiplier)

    return int(random.randint(int(tier * multiplier), int((tier + 1) * multiplier)))

def create_troop(number):
    ar = ""
    wp = ""
    knows = "knows_common"
    if getKnows(number):
        knows = knows + "|" + getKnows(number)
    grant = ""
    result = "["
    x = 1
    armors = int(getArmors(number))
    weapons = int(getWeapons(number))

    if stp_head_armor&armors:
        item = get_armor(1, getHeadMin(number), getHeadMax(number))
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_helmet"
        else:
            print("[Error]: No suitable head armor for %s"%getNameByFaction(number))

    if stp_hand_armor&armors:
        item = get_armor(2, getHandMin(number), getHandMax(number))
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_gloves"
        else:
            print("[Error]: No suitable hand armor for %s"%getNameByFaction(number))

    if stp_body_armor&armors:
        item = get_armor(3, getBodyMin(number), getBodyMax(number))
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_armor"
        else:
            print("[Error]: No suitable body armor for %s"%getNameByFaction(number))

    if stp_leg_armor&armors:
        item = get_armor(4, getLegsMin(number), getLegsMax(number))
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_boots"
        else:
            print("[Error]: No suitable leg armor for %s"%getNameByFaction(number))

    if stp_horse&armors:
        item = get_horse(number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_mounted|tf_guarantee_horse"
        else:
            print("[Error]: No suitable horse for %s"%getNameByFaction(number))

    if stp_one_handed_weapon&weapons:
        item = get_weapon(1, number)
        if item:
            ar = ar + ", " + item
            wp = wp + "|wp_one_handed(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable one handed weapon for %s"%getNameByFaction(number))

    if stp_two_handed_weapon&weapons:
        item = get_weapon(2, number)
        if item:
            ar = ar + ", " + item
            wp = wp + "|wp_two_handed(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable two handed weapon for %s"%getNameByFaction(number))

    if stp_ranged_one_handed_weapon&weapons:
        item = get_weapon(3, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_polearm"
            wp = wp + "|wp_polearm(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable one handed polearm for %s"%getNameByFaction(number))

    if stp_ranged_two_handed_weapon&weapons:
        item = get_weapon(4, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_polearm"
            wp = wp + "|wp_polearm(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable two handed polearm for %s"%getNameByFaction(number))

    if stp_bow&weapons:
        item = get_bow(1, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_ranged"
            wp = wp + "|wp_archery(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable bow for %s"%getNameByFaction(number))

    if stp_crossbow&weapons:
        item = get_bow(2, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_ranged"
            wp = wp + "|wp_crossbow(" + str(getWeaponProficiency(number)) + ")"
        else:
            print("[Error]: No suitable crossbow for %s"%getNameByFaction(number))
        
    if stp_arrow&weapons:
        item = get_arrow(1)
        if item:
            ar = ar + ", " + item
        else:
            print("[Error]: No suitable arrows for %s"%getNameByFaction(number))

    if stp_bolt&weapons:
        item = get_arrow(2)
        if item:
            ar = ar + ", " + item
        else:
            print("[Error]: No suitable bolts for %s"%getNameByFaction(number))

    if stp_shield&weapons:
        item = get_shield(1, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_shield"
        else:
            print("[Error]: No suitable shield for %s"%getNameByFaction(number))

    if stp_shield_horse&weapons:
        item = get_shield(2, number)
        if item:
            ar = ar + ", " + item
            grant = grant + "|tf_guarantee_shield"
        else:
            print("[Error]: No suitable shield that can use on horse for %s"%getNameByFaction(number))

    if not wp:
        wp = "|wp(60)"

##    print("%s - %s"%(grant[1:], ar[2:]))
    result = result + "\"" + getId(number) + "\", \"" + getNameByFaction(number) + "\", \"" + getPluralNameByFaction(number) + "\", " + grant[1:] + ", 0, 0, " + ifaction_id + ", "
    result = result + "[" + ar[2:] + "], def_attrib|level(" + str(getLevel(number)) + "), " + wp[1:] + ", " + knows + ", swadian_face_young_1, swadian_face_old_2],"
##    print("%s"%result)
    file = open("troops.txt", "a")
    file.write(result + "\n")
    file.close()
    print("%s troop code is now creating..."%getNameByFaction(number))

##  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
##   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
##   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
    
def make():
    if os.path.isfile("troops.txt"):
        os.remove("troops.txt")
    x = 1
    while x <= ifaction_suffix_0:
##        print("Name: %s(%s), Tier: %d, Upgrades: %d, Weapons: %d, Armors: %d, Multiplier: %.2f"%(getNameByFaction(x), getPluralNameByFaction(x), getTier(x), getUpgrades(x), getWeapons(x), getArmors(x), getMultiplier(x)))
##        print("Head: %d-%d, Hand: %d-%d, Body: %d-%d, Legs: %d-%d"%(getHeadMin(x), getHeadMax(x),getHandMin(x), getHandMax(x),getBodyMin(x), getBodyMax(x),getLegsMin(x), getLegsMax(x)))
        create_troop(x)
##        print("Upgrade: %d"%(getUpgradeByIndex(x, -1))) #Get upgrade count
##        print("Upgrade: %s"%(getUpgradeByIndex(x, 0))) #Get first upgrade
##        print("Upgrade: %d"%(getUpgradeIdByIndex(x, 1))) #Get second upgrade's id
        x += 1
    print("Your troop code successfully created.")
    print("Checking if troops need upgrades...")
    x = 1
    result = ""
    file = open("troops.txt", "a")
    file.write("\n")
    while x <= ifaction_suffix_0:
        if getUpgradeByIndex(x, -1) > 0:
            print("Creating upgrades for %s..."%getNameByFaction(x))
##            print("%d upgrade found for %s..."%(getUpgradeByIndex(x, -1), getNameByFaction(x)))
            variable = "upgrade"
            if getUpgradeByIndex(x, -1) == 2:
                variable = "upgrade2"
                
            result = variable + "(troops, \"" + getId(x) + "\", \"" + getId(getUpgradeIdByIndex(x, 0)) + "\""
            if getUpgradeByIndex(x, -1) == 2:
                result = result + ", \"" + getId(getUpgradeIdByIndex(x, 1)) + "\""
            result = result + ")"
            file.write(result + "\n")
        x += 1
    file.close()
    print("Upgrades successfully created.")

            

make()
