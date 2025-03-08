import heapq

# Define the available spells
SPELLS = {
    "Magic Missile": {"cost": 53, "damage": 4, "healing": 0, "duration": 0, "mana": 0},
    "Drain": {"cost": 73, "damage": 2, "healing": 2, "duration": 0, "mana": 0},
    "Shield": {"cost": 113, "damage": 0, "healing": 0, "duration": 6, "mana": 0, "armor": 7},
    "Poison": {"cost": 173, "damage": 3, "healing": 0, "duration": 6, "mana": 0},
    "Recharge": {"cost": 229, "damage": 0, "healing": 0, "duration": 5, "mana": 101},
}

# Initial conditions
PLAYER_HP = 50
PLAYER_MANA = 500
BOSS_HP = 71  # Replace with your input
BOSS_DAMAGE = 10  # Replace with your input

# Priority queue for BFS: (mana_spent, player_hp, player_mana, boss_hp, active_effects, is_player_turn)
queue = []
heapq.heappush(queue, (0, PLAYER_HP, PLAYER_MANA, BOSS_HP, {}, True))  # Initial state (min-heap based on mana_spent)

# Track the minimum mana to win
min_mana_spent = float("inf")

# BFS Loop with Priority Queue
while queue:
    mana_spent, player_hp, player_mana, boss_hp, active_effects, is_player_turn = heapq.heappop(queue)
    if player_hp <= 0:
        continue

    # Apply active effects
    new_effects = {}
    player_armor = 0
    for effect, details in active_effects.items():
        if "armor" in SPELLS[effect]:
            player_armor = SPELLS[effect]["armor"]
        boss_hp -= SPELLS[effect]["damage"]
        player_mana += SPELLS[effect]["mana"]
        if details > 1:
            new_effects[effect] = details - 1

    # Check if boss is dead immediately after effects
    if boss_hp <= 0:
        min_mana_spent = min(min_mana_spent, mana_spent)
        continue  # No need to continue this path

    if is_player_turn:
        # Player's turn: Try casting spells
        for spell, details in SPELLS.items():
            if spell in new_effects or player_mana < details["cost"]:
                continue  # Skip if effect is active or not enough mana

            # Apply spell effect
            next_hp = player_hp + details["healing"]
            next_mana = player_mana - details["cost"]
            next_boss_hp = boss_hp - details["damage"]
            next_effects = new_effects.copy()
            if details["duration"] > 0:
                next_effects[spell] = details["duration"]

            heapq.heappush(queue, (mana_spent + details["cost"], next_hp, next_mana, next_boss_hp, next_effects, False))

    else:
        # Boss's turn: Attack if player is still alive
        next_hp = player_hp - max(1, BOSS_DAMAGE - player_armor)

        # Apply the Hard Mode penalty if required
        next_hp -= 1  # Player loses 1 HP at the start of their turn (Hard Mode)

        if next_hp > 0:
            heapq.heappush(queue, (mana_spent, next_hp, player_mana, boss_hp, new_effects, True))

# Print result
print("Minimum mana spent to win:", min_mana_spent)
