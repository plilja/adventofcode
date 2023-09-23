def step1(fishes):
    return calculate_fishes(fishes, 80)


def step2(fishes):
    return calculate_fishes(fishes, 256)


def calculate_fishes(fishes, days):
    ages = {i: 0 for i in range(0, 9)}
    for age in fishes:
        ages[age] += 1
    for i in range(0, days):
        new_fishes = ages[0]
        for age in range(1, 9):
            ages[age - 1] = ages[age]
        ages[6] += new_fishes
        ages[8] = new_fishes
    return sum(ages.values())


def main():
    fishes = [int(i) for i in input().split(',')]
    print(step1(fishes))
    print(step2(fishes))


if __name__ == '__main__':
    main()

