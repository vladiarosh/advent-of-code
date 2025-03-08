import re
from utils import get_input_path

file_path = get_input_path(__file__, '2015_05_input.txt')
with open(file_path) as file:
    lines = [line.rstrip() for line in file]


def vowels_counter():
    vowels_res = False
    all_vowels = re.findall("[aeiou]", i)
    num_of_allowed_vowels = len(all_vowels)
    if num_of_allowed_vowels >= 3:
        vowels_res = True
    return vowels_res


def double_letter_counter():
    double_letter_res = False
    for k in range(len(i) - 1):
        if i[k] == i[k + 1]:
            double_letter_res = True
            break
    return double_letter_res


def bad_diphthongs_counter():
    bad_diphthongs = ['ab', 'cd', 'pq', 'xy']
    diphthongs_res = False
    c = 0
    for x in bad_diphthongs:
        if (i.find(x)) != -1:
            c += 1
    if c >= 1:
        diphthongs_res = True
    return diphthongs_res


nice_strings = []
for i in lines:
    vowels_result = vowels_counter()
    double_letter_result = double_letter_counter()
    diphthongs_result = bad_diphthongs_counter()
    if vowels_result and double_letter_result and not diphthongs_result:
        nice_strings.append(i)
print("Number of nice strings is", len(nice_strings))

# PART TWO


def pairs_counter(string, window_size):
    doublets_list = []
    res1 = False
    res2 = False
    res3 = False
    for g in range(len(string) - window_size + 1):
        doublet = string[g:g + window_size]
        doublets_list.append(doublet)
        if len(doublets_list) != len(set(doublets_list)):
            res1 = True
    for m in range(len(doublets_list) - 1):
        current_doublet = doublets_list[m]
        next_doublet = doublets_list[m + 1]
        first_character_current = current_doublet[0]
        second_character_next = next_doublet[1]
        if first_character_current == second_character_next:
            res2 = True
    for m in range(len(doublets_list) - 2):
        current_doublet = doublets_list[m]
        for n in range(m + 2, len(doublets_list)):
            if current_doublet == doublets_list[n]:
                res3 = True
    return res1, res2, res3


nice_strings_2 = []
for i in lines:
    rule1, rule2, rule3 = pairs_counter(i, 2)
    if rule1 and rule2 and rule3:
        nice_strings_2.append(i)
print(len(nice_strings_2))


def string_is_nice(line):
    non_overlapping_identical_pairs_found = False
    three_letter_sandwich_found = False

    pair_freq_dict = {}
    last_pair_skipped = False
    previous_pair = '00'  # invalid pair to always fail first loop equality check

    for g in range(len(line) - 2 + 1):
        pair = line[g:g + 2]
        if pair == previous_pair and not last_pair_skipped:
            last_pair_skipped = True
        else:
            if pair in pair_freq_dict:
                pair_freq_dict[pair] += 1
            else:
                pair_freq_dict[pair] = 1
            last_pair_skipped = False

        if previous_pair[0] == pair[1]:
            three_letter_sandwich_found = True
        previous_pair = pair

    for p in pair_freq_dict:
        if pair_freq_dict[p] >= 2:
            non_overlapping_identical_pairs_found = True

    return non_overlapping_identical_pairs_found and three_letter_sandwich_found


nice_strings_3 = 0
for i in lines:
    if string_is_nice(i):
        nice_strings_3 += 1

print('number of nice strings is', nice_strings_3)











