# # inventory.py
# weapons = {
#     "Swords": [
#         {"material":"Mithril", "damage":20, "durability":240, "cost":1025},
#         {"material":"Steel", "damage":12, "durability":100, "cost":185},
#         {"material":"Iron", "damage":7, "durability":75, "cost":64},
#         {"material":"Wooden", "damage":2, "durability":15, "cost":12}
#     ],
#     "Bows": [
#         {"material":"Yggdrasil", "damage":45, "durability":380, "cost":2020},
#         {"material":"Elvish", "damage":28, "durability":200, "cost":385},
#         {"material":"Oak", "damage":15, "durability":90, "cost":48},
#         {"material":"Stick", "damage":6, "durability":15, "cost":12}
#     ],
#     "Axes": [
#         {"material":"Bone Steel", "damage":30, "durability":380, "cost":480},
#         {"material":"Iron", "damage":18, "durability":60, "cost":1875},
#         {"material":"Flint", "damage":12, "durability":20, "cost":48},
#     ]
# }

# inventory.py
weapons = {
    "Swords": [
        {"material": "Mithril",     "durability": 670, "attack speed": 1.2, "damage type": "slashing", "physical damage": 60, "magic damage": 12, "cost": 3500},
        {"material": "Obsidian",    "durability": 310, "attack speed": 1.5, "damage type": "slashing", "physical damage": 43, "magic damage": 4,  "cost": 1800},
        {"material": "Adamantium",  "durability": 420, "attack speed": 0.8, "damage type": "slashing", "physical damage": 32,                     "cost": 900},
        {"material": "Steel",       "durability": 290, "attack speed": 1.0, "damage type": "slashing", "physical damage": 18,                     "cost": 250},
        {"material": "Iron",        "durability": 130, "attack speed": 0.8, "damage type": "slashing", "physical damage": 15,                     "cost": 150},
        {"material": "Wooden",      "durability": 50,  "attack speed": 1.5, "damage type": "blunt",    "physical damage": 5,                      "cost": 20}
    ],
    "Bows":[
        {"material": "Elven", "durability": 300, "attackspeed": 1.2, "damagetype": "piercing", "physicaldamage": 35, "magicdamage": 15, "cost": 4000},
        {"material": "Magic Yew", "durability": 350, "attackspeed": 1.5, "damagetype": "piercing", "physicaldamage": 15, "magicdamage": 20, "cost": 3800},
        {"material": "Bone", "durability": 250, "attackspeed": 1.0, "damagetype": "piercing", "physicaldamage": 30, "magicdamage": 0, "cost": 2800},
        {"material": "Silver", "durability": 200, "attackspeed": 0.8, "damagetype": "piercing", "physicaldamage": 25, "magicdamage": 10, "cost": 3500},
        {"material": "Oak", "durability": 150, "attackspeed": 0.6, "damagetype": "piercing", "physicaldamage": 20, "magicdamage": 0, "cost": 2000},
    ],
    "Axes": [
        {"material": "Dwarven", "durability": 400, "attackspeed": 1.0, "damagetype": "slashing", "physicaldamage": 40, "magicdamage": 10, "cost": 4500},
        {"material": "Steel Axe", "durability": 200, "attackspeed": 0.8, "damagetype": "slashing", "physicaldamage": 25, "magicdamage": 0, "cost": 2800},
        {"material": "Bronze Axe", "durability": 150, "attackspeed": 0.6, "damagetype": "slashing", "physicaldamage": 20, "magicdamage": 0, "cost": 2000},
        {"material": "Double-bladed Axe", "durability": 300, "attackspeed": 1.2, "damagetype": "slashing", "physicaldamage": 35, "magicdamage": 0, "cost": 3800},
        {"material": "Iron Axe", "durability": 250, "attackspeed": 1.0, "damagetype": "slashing", "physicaldamage": 30, "magicdamage": 0, "cost": 3200}
    ],
    "Maces": [
        {"material": "Steel Mace", "durability": 250, "attackspeed": 0.8, "damagetype": "blunt", "physicaldamage": 30, "magicdamage": 0, "cost": 3000},
        {"material": "Gold Mace", "durability": 300, "attackspeed": 1.0, "damagetype": "blunt", "physicaldamage": 35, "magicdamage": 15, "cost": 4000},
        {"material": "Spiked Mace", "durability": 200, "attackspeed": 0.6, "damagetype": "piercing", "physicaldamage": 25, "magicdamage": 0, "cost": 2500},
        {"material": "Bone Mace", "durability": 150, "attackspeed": 0.5, "damagetype": "blunt", "physicaldamage": 20, "magicdamage": 0, "cost": 1800},
        {"material": "Obsidian Mace", "durability": 350, "attackspeed": 1.2, "damagetype": "blunt", "physicaldamage": 40, "magicdamage": 20, "cost": 5000}
    ],
    "Staffs": [
        {"material": "Wizard Staff", "durability": 200, "attackspeed": 0, "damagetype": "blunt", "physicaldamage": 15, "magicdamage": 40, "cost": 4500},
        {"material": "Elemental Staff", "durability": 180, "attackspeed": 0, "damagetype": "blunt", "physicaldamage": 20, "magicdamage": 50, "cost": 5500},
        {"material": "Necromancer Staff", "durability": 150, "attackspeed": 0, "damagetype": "blunt", "physicaldamage": 10, "magicdamage": 60, "cost": 6500}
    ],
    "Daggers": [
        {"material":"Assassin's Dagger", "durability":150, "attack speed":1.5, "damage type":"piercing", "physical damage":25, "magic damage":0, "cost":3000},
        {"material":"Poisoned Dagger", "durability":120, "attack speed":1.3, "damage type":"piercing", "physical damage":20, "magic damage":0, "poison damage":10, "cost":3500},
        {"material":"Dual Daggers", "durability":100, "attack speed":1.7, "damage type":"piercing", "physical damage":15, "magic damage":0, "cost":2500}
    ],
    "Spears": [
        {"material":"Dragonsteel Spear", "durability":300, "attack speed":1.2, "damage type":"piercing", "physical damage":35, "magic damage":10, "cost":4800},
        {"material":"Bone Spear", "durability":250, "attack speed":1.0, "damage type":"piercing", "physical damage":30, "magic damage":0, "cost":3200},
        {"material":"Crystal Spear", "durability":200, "attack speed":0.8, "damage type":"piercing", "physical damage":25, "magic damage":15, "cost":4000}
    ],
    "Hammers": [
        {"material":"Thunder Hammer", "durability":350, "attack speed":0.8, "damage type":"blunt", "physical damage":40, "magic damage":20, "cost":5000},
        {"material":"War Hammer", "durability":300, "attack speed":1.0, "damage type":"blunt", "physical damage":35, "magic damage":0, "cost":3800},
        {"material":"Stone Maul", "durability":250, "attack speed":0.6, "damage type":"blunt", "physical damage":30, "magic damage":0, "cost":3000}
    ],
    "Wands": [
        {"material":"Fire Wand", "durability":200, "attack speed":0, "damage type":"magic", "physical damage":15, "magic damage":40, "spell power":25, "cost":4500},
        {"material":"Ice Wand", "durability":180, "attack speed":0, "damage type":"magic", "physical damage":20, "magic damage":50, "spell power":30, "cost":5500},
        {"material":"Lightning Wand", "durability":150, "attack speed":0, "damage type":"magic", "physical damage":10, "magic damage":60, "spell power":35, "cost":6500}
    ],
    "Whips": [
        {"material":"Flame Whip", "durability":150, "attack speed": 1.5, "damage type": "slashing", "physical damage":25, "magic damage": 10, "cost": 3500},
        {"material":"Shadow Whip", "durability":120, "attack speed": 1.3, "damage type": "piercing", "physical damage":20, "magic damage": 15, "cost": 4200},
        {"material":"Chain Whip", "durability":100, "attack speed": 1.7, "damage type": "blunt", "physical damage":15, "cost": 2800}
    ],
    "Cross": [
        {"material":"Heavy Cros", "durability":300, "attack speed": 0.8, "damage type": "piercing", "physical damage":40, "cost": 4500},
        {"material":"Sniper Cros", "durability":250, "attack speed": 1.0, "damage type": "piercing", "physical damage":35, "magic damage": 10, "cost": 3800},
        {"material":"Repeating Cros", "durability":200, "attack speed": 0.6, "damage type": "piercing", "physical damage":30, "cost": 3000}
    ]
}
