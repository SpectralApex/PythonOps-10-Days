# Loot Drop Simulator
import random

loot_table = {
    "Common": ["Bandage", "Ammo", "Water"],
    "Rare": ["Medkit", "Grenade", "Armor"],
    "Epic": ["Sniper", "Drone", "Stealth Suit"],
    "Legendary": ["Exo-Suit", "Plasma Cannon", "Time Warp"]
}

def drop_loot():
    tier = random.choices(["Common", "Rare", "Epic", "Legendary"], weights=[60, 25, 10, 5])[0]
    item = random.choice(loot_table[tier])
    print(f" Drop: {item} ({tier})")

for _ in range(5):
    drop_loot()
