# -*- coding: cp1254 -*-
imods = [
    #("uid", "Name", multiplier, divider, ["Special Name"]),
    # multiplier: 1 = 1, 0.5 = 5, 0.55 = 55, 1.9 = 19
    # divider: 1 = 1 0.5 = 10, 0.55 = 100, 1.9 = 10
    ("plain", "Plain", 1, 1), #Armor(6), Shield(3), Weapon(6), Ammo(2), Horse(5), Food(2)
    ("cracked", "Cracked", 5, 10), #Armor(12), Shield(5), Weapon(10)
    ("rusty", "Rusty", 55, 100), #Armor(10), Weapon(8)
    ("bent", "Bent", 65, 100), #Weapon(9), Ammo(3)
    ("chipped", "Chipped", 72, 100), #Weapon(7)
    ("battered", "Battered", 75, 100), #Armor(8), Shield(4)
    ("poor", "Poor", 80, 10),
    ("crude", "Crude", 83, 100), #Armor(7)
    ("old", "Old", 86, 100),
    ("cheap", "Cheap", 9, 10),
    ("fine", "Fine", 19, 10),
    ("well_made", "Well Made", 25, 10),
    ("sharp", "Sharp", 16, 10),
    ("balanced", "Balanced", 35, 10), #Weapon(4), Ammo
    ("tempered", "Tempered", 67, 10), #Weapon(2)
    ("deadly", "Deadly", 85, 10),
    ("exquisite", "Exquisite", 145, 10),
    ("masterwork", "Masterwork", 175, 10), #Weapon(1)
    ("heavy", "Heavy", 19, 10), #Weapon(5), Horse(3)
    ("strong", "Strong", 49, 10), #Weapon(3)
    ("powerful", "Powerful", 32, 10),
    ("tattered", "Tattered", 5, 10), #Armor(11)
    ("ragged", "Ragged", 7, 10), #Armor(9)
    ("rough", "Rough", 6, 10),
    ("sturdy", "Sturdy", 17, 10), #Armor(5)
    ("thick", "Thick", 26, 10), #Armor(4), Shield(2)
    ("hardened", "Hardened", 39, 10), #Armor(3)
    ("reinforced", "Reinforced", 65, 10), #Armor(2), Shield(1)
    ("superb", "Superb", 25, 10),
    ("lordly", "Lordly", 115, 10), #Armor(1)
    ("lame", "Lame", 4, 10), #Horse(7)
    ("swaybacked", "Swaybacked", 6, 10),
    ("stubborn", "Stubborn", 9, 10), #Horse(4)
    ("timid", "Timid", 18, 10), #Horse(6)
    ("meek", "Meek", 18, 10),
    ("spirited", "Spirited", 65, 10), #Horse(2)
    ("champion", "Champion", 145, 10), #Horse(1)
    ("fresh", "Fresh", 1, 1), #Food(1)
    ("day_old", "Day Old", 1, 1), #Food(3)
    ("two_day_old", "Two Day Old", 9, 10), #Food(4)
    ("smelling", "Smelling", 4, 10), #Food(5)
    ("rotten", "Rotten", 5, 100), #Food(6)
    ("large_bag", "Large Bag", 19, 10), #Ammo(1)
]

## Sorted list of modifiers
# Armor:
# 1. imod_lordly
# 2. imod_reinforced
# 3. imod_hardened
# 4. imod_thick
# 5. imod_sturdy
# 6. imod_plain
# 7. imod_crude
# 8. imod_battered
# 9. imod_ragged
# 10. imod_rusty
# 11. imod_tattered
# 12. imod_cracked
#
# Shield:
# 1. imod_reinforced
# 2. imod_thick
# 3. imod_plain
# 4. imod_battered
# 5. imod_cracked
#
# Weapon:
# 1. imod_masterwork
# 2. imod_tempered
# 3. imod_strong
# 4. imod_balanced
# 5. imod_heavy
# 6. imod_plain
# 7. imod_chipped
# 8. imod_rusty
# 9. imod_bent
# 10. imod_cracked
#
# Ammo:
# 1. imod_large_bag
# 2. imod_plain
# 3. imod_bent
#
# Horse:
# 1. imod_champion
# 2. imod_spirited
# 3. imod_heavy
# 4. imod_stubborn
# 5. imod_plain
# 6. imod_timid
# 7. imod_lame
#
# Food:
# 1. imod_fresh
# 2. imod_plain
# 3. imod_day_old
# 4. imod_two_day_old
# 5. imod_smelling
# 6. imod_rotten
