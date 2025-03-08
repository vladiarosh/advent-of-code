import string


def main():
    old_password = 'vzbxxyzz'
    new_password = increment_character(old_password)
    print(new_password)
    valid_password = check_conditions(new_password)
    print(valid_password)


def increment_character(old_pass):
    letters = string.ascii_lowercase
    old_pass = list(old_pass)
    i = len(old_pass) - 1
    while i >= 0:
        index = letters.index(old_pass[i])
        if old_pass[i] == 'z':
            old_pass[i] = 'a'
            i -= 1
        else:
            old_pass[i] = letters[index + 1]
            break
    return ''.join(old_pass)


def check_conditions(new_pass):
    while True:
        nice_chars = check_for_i_o_l_absence(new_pass)
        nice_pairs = check_non_overlapping_pairs(new_pass)
        nice_triplet = check_sequential_letter_triplets(new_pass)

        if nice_pairs and nice_triplet and nice_chars:
            return new_pass
        else:
            new_pass = increment_character(new_pass)


def check_sequential_letter_triplets(new_pass):
    letters = string.ascii_lowercase
    i = 0
    check_state = False
    while i < len(new_pass) - 2:
        index = letters.index(new_pass[i])
        if index <= 23:
            triplet = new_pass[i: i + 3]
            if triplet[1] == letters[index + 1] and triplet[2] == letters[index + 2]:
                check_state = True
                break
        i += 1
    return check_state


def check_non_overlapping_pairs(new_pass):
    pair_count = 0
    i = 0
    check_state = False
    while i < len(new_pass) - 1:
        pair = new_pass[i: i + 2]

        if pair[0] == pair[1]:
            pair_count += 1
            i += 2
        else:
            i += 1
    if pair_count >= 2:
        check_state = True
    return check_state


def check_for_i_o_l_absence(new_pass):
    check_state = True
    if 'i' in new_pass or 'o' in new_pass or 'l' in new_pass:
        check_state = False
    return check_state


if __name__ == "__main__":
    main()




