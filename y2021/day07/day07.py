def step1(crabs):
    result = float('inf')
    for pos in range(min(crabs), max(crabs) + 1):
        cost = 0
        for crab in crabs:
            cost += abs(crab - pos)
        result = min(result, cost)
    return result


def step2(crabs):
    result = float('inf')
    for pos in range(min(crabs), max(crabs) + 1):
        cost = 0
        for crab in crabs:
            n = abs(crab - pos)
            cost += int(n * (n + 1) / 2)
        result = min(result, cost)
    return result


crabs = [int(i) for i in input().split(',')]
print(step1(crabs))
print(step2(crabs))
