def run(starting_numbers, end):
    xs = {}
    for i, num in enumerate(starting_numbers):
        xs[num] = i + 1
    last = starting_numbers[-1]
    for i in range(len(starting_numbers) + 1, end + 1):
        if last in xs:
            prev_idx = xs[last]
            diff = i - 1 - prev_idx
            new = diff
        else:
            new = 0
        xs[last] = i - 1
        last = new
    return last


def step1(starting_numbers):
    return run(starting_numbers, 2020)


def step2(starting_numbers):
    # Python really isn't the right language for big loops like this,
    # but too lazy to implement loop detection
    return run(starting_numbers, 30000000)


starting_numbers = [int(x) for x in input().split(',')]
print(step1(starting_numbers))
print(step2(starting_numbers))
