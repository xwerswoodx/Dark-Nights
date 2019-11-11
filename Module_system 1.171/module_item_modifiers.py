# -*- coding: cp1254 -*-
imods = [
    #("uid", "Name", pricing, unknown (could be chance to get), specificName),
    ("plain", "Plain", 1, 1), #Armor(6), Shield(3), Weapon(6), Ammo(2), Horse(5), Food(2)
    ("cracked", "Cracked", 0.5, 1), #Armor(12), Shield(5), Weapon(10)
    ("rusty", "Rusty", 0.55, 1), #Armor(10), Weapon(8)
    ("bent", "Bent", 0.65, 1), #Weapon(9), Ammo(3)
    ("chipped", "Chipped", 0.72, 1), #Weapon(7)
    ("battered", "Battered", 0.75, 1), #Armor(8), Shield(4)
    ("poor", "Poor", 0.8, 1),
    ("crude", "Crude", 0.83, 1), #Armor(7)
    ("old", "Old", 0.86, 1),
    ("cheap", "Cheap", 0.9, 1),
    ("fine", "Fine", 1.9, 0.6),
    ("well_made", "Well Made", 2.5, 0.5),
    ("sharp", "Sharp", 1.6, 0.6),
    ("balanced", "Balanced", 3.5, 0.5), #Weapon(4), Ammo
    ("tempered", "Tempered", 6.7, 0.4), #Weapon(2)
    ("deadly", "Deadly", 8.5, 0.3),
    ("exquisite", "Exquisite", 14.5, 0.3),
    ("masterwork", "Masterwork", 17.5, 0.3), #Weapon(1)
    ("heavy", "Heavy", 1.9, 0.7), #Weapon(5), Horse(3)
    ("strong", "Strong", 4.9, 0.4), #Weapon(3)
    ("powerful", "Powerful", 3.2, 0.4),
    ("tattered", "Tattered", 0.5, 1), #Armor(11)
    ("ragged", "Ragged", 0.7, 1), #Armor(9)
    ("rough", "Rough", 0.6, 1),
    ("sturdy", "Sturdy", 1.7, 0.5), #Armor(5)
    ("thick", "Thick", 2.6, 0.35), #Armor(4), Shield(2)
    ("hardened", "Hardened", 3.9, 0.3), #Armor(3)
    ("reinforced", "Reinforced", 6.5, 0.25), #Armor(2), Shield(1)
    ("superb", "Superb", 2.5, 0.25),
    ("lordly", "Lordly", 11.5, 0.25), #Armor(1)
    ("lame", "Lame", 0.4, 1), #Horse(7)
    ("swaybacked", "Swaybacked", 0.6, 1),
    ("stubborn", "Stubborn", 0.9, 1), #Horse(4)
    ("timid", "Timid", 1.8, 1), #Horse(6)
    ("meek", "Meek", 1.8, 1),
    ("spirited", "Spirited", 6.5, 0.6), #Horse(2)
    ("champion", "Champion", 14.5, 0.2), #Horse(1)
    ("fresh", "Fresh", 1, 1), #Food(1)
    ("day_old", "Day Old", 1, 1), #Food(3)
    ("two_day_old", "Two Days Old", 0.9, 1), #Food(4)
    ("smelling", "Smelling", 0.4, 1), #Food(5)
    ("rotten", "Rotten", 0.05, 1), #Food(6)
    ("large_bag", "Large Bag", 1.9, 0.3), #Ammo(1)
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
# 7. imod_swaybacked
# 8. imod_lame
#
# Food:
# 1. imod_fresh
# 2. imod_plain
# 3. imod_day_old
# 4. imod_two_day_old
# 5. imod_smelling
# 6. imod_rotten
