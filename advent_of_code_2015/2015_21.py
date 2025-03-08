# This code could be much shorter and does not really benefit from the use of dictionaries.
# My purpose was to practice the use of dictionaries and to also make the nice main function, where you can
# modify player hp and boss stats to experiment with different starting conditions.

# Also, decided to take into account cases where it is impossible to win boss with any combination of gear

import math
import itertools
from utils import get_input_path


def main():
    file_path = get_input_path(__file__, '2015_21_input.txt')
    file = open(file_path)
    shop = file.read().splitlines()
    weapons_dict, armor_dict, rings_dict = parse_shop(shop)
    all_gear_combinations = generate_gear_combinations(weapons_dict, armor_dict, rings_dict)
    boss_stats = {'Hit points': 109, 'Damage': 8, 'Armor': 2}
    player_hp = 100
    minimum_to_win, maximum_to_lose = calculate_minimal_gold_for_win(all_gear_combinations, boss_stats, player_hp)

    # Part 1 and Part 2 solutions
    print('Least gold to win boss is', minimum_to_win, 'and maximum gold spent to lose is', maximum_to_lose)


def parse_shop(input_file):
    weapons = {}
    for line in input_file[1:6]:
        stats = line.split()
        weapons[stats[0]] = {'Cost': int(stats[1]), 'Damage': int(stats[2]), 'Armor': int(stats[3])}
    armor = {'No Armor': {'Cost': 0, 'Damage': 0, 'Armor': 0}}
    # I could exclude 'Damage' stat from armour, but who knows, we might find unique armor with damage stats some day
    for line in input_file[8:13]:
        stats = line.split()
        armor[stats[0]] = {'Cost': int(stats[1]), 'Damage': int(stats[2]), 'Armor': int(stats[3])}
    rings = {}
    ring = 1
    for _ in range(2):
        rings['Ring ' + str(ring)] = {'Cost': 0, 'Damage': 0, 'Armor': 0}
        ring += 1
    for line in input_file[15:21]:
        stats = line.split()
        rings['Ring ' + str(ring)] = {'Cost': int(stats[2]), 'Damage': int(stats[3]), 'Armor': int(stats[4])}
        ring += 1
    return weapons, armor, rings


def generate_gear_combinations(weapons, armor, rings):
    all_combinations = []
    for r in range(1, 3):
        for ring_combination in itertools.combinations(rings.items(), r):
            for weapon_name, weapon_stats in weapons.items():
                for armor_name, armor_stats in armor.items():
                    combination = {'Weapon': weapon_name, 'Weapon stats': weapon_stats, 'Armor': armor_name,
                                   'Armor stat': armor_stats, 'Rings': ring_combination}
                    all_combinations.append(combination)
    return all_combinations


def damage_to_boss(total_damage, boss_defence):
    damage = max(1, total_damage - boss_defence)
    return damage


def damage_to_player(boss_damage, total_player_defence):
    damage = max(1, boss_damage - total_player_defence)
    return damage


def calculate_minimal_gold_for_win(gear_combinations, boss_stats, player_health):
    boss_hp = boss_stats['Hit points']
    boss_def = boss_stats['Armor']
    boss_damage = boss_stats['Damage']
    gold_spent_to_win_boss = []
    gold_spent_to_lose_fight = []
    for combination in gear_combinations:
        total_damage = combination['Weapon stats']['Damage'] + sum(ring[1]['Damage'] for ring in combination['Rings'])
        player_total_defence = (sum(ring[1]['Armor'] for ring in combination['Rings'])
                                + combination['Armor stat']['Armor'])
        damage_we_deal_to_boss = damage_to_boss(total_damage, boss_def)
        damage_boss_deals_to_us = damage_to_player(boss_damage, player_total_defence)

        rounds_to_slay_boss = math.ceil(boss_hp / damage_we_deal_to_boss)
        rounds_for_boss_to_slay_us = math.ceil(player_health / damage_boss_deals_to_us)

        if rounds_to_slay_boss <= rounds_for_boss_to_slay_us:
            gold_spent_to_win = (sum(ring[1]['Cost'] for ring in combination['Rings'])
                                 + combination['Weapon stats']['Cost'] + combination['Armor stat']['Cost'])
            gold_spent_to_win_boss.append(gold_spent_to_win)

        if rounds_to_slay_boss >= rounds_for_boss_to_slay_us:
            gold_spent_to_lose = (sum(ring[1]['Cost'] for ring in combination['Rings'])
                                  + combination['Weapon stats']['Cost'] + combination['Armor stat']['Cost'])
            gold_spent_to_lose_fight.append(gold_spent_to_lose)

    maximum_gold_spent_to_lose = max(gold_spent_to_lose_fight)
    if not gold_spent_to_win_boss:
        print("Ouch, no gear combination to win this boss, go and level up more or find a better shop")
        return None, maximum_gold_spent_to_lose
    minimum_gold_spent_to_win = min(gold_spent_to_win_boss)
    return minimum_gold_spent_to_win, maximum_gold_spent_to_lose


if __name__ == "__main__":
    main()




