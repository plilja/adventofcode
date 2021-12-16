def step1(fishes):
    ages = {i: 0 for i in range(0, 9)}
    for age in fishes:
        ages[age] += 1
    for i in range(0, 80):
        new_fishes = ages[0]
        for age in range(1, 9):
            ages[age - 1] = ages[age]
        ages[6] += new_fishes
        ages[8] = new_fishes
    return sum(ages.values())


fishes = [int(i) for i in input().split(',')]
print(step1(fishes))
