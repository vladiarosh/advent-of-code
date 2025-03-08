def main():
    target_presents_number = 36000000
    # Part 1
    number_of_house = 1
    while True:
        elves_that_can_visit_house = check_divisibility(number_of_house)
        total_presents = sum(elf * 10 for elf in elves_that_can_visit_house)
        if total_presents >= target_presents_number:
            break
        number_of_house += 1
    print("Lowest house number for part 1 is", number_of_house)
    # Part 2
    number_of_house = 1
    elves_visits = {}
    while True:
        elves_that_might_visit_house = check_divisibility(number_of_house)
        elves_actually_visiting_house = []
        for elf in elves_that_might_visit_house:
            if elf not in elves_visits:
                elves_visits[elf] = 1
            else:
                elves_visits[elf] += 1
            if elves_visits[elf] <= 50:
                elves_actually_visiting_house.append(elf)
        total_presents = sum(elf * 11 for elf in elves_actually_visiting_house)
        if total_presents >= target_presents_number:
            break
        number_of_house += 1
    print("Lowest house number for part 2 is", number_of_house)


def check_divisibility(house_number):
    list_of_divisors = []
    for i in range(1, int(house_number ** 0.5) + 1):
        if house_number % i == 0:
            list_of_divisors.append(i)
            divisor_pair = house_number / i
            if divisor_pair != i:
                list_of_divisors.append(divisor_pair)
    return list_of_divisors


if __name__ == "__main__":
    main()
