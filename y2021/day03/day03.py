import sys
from collections import Counter


def step1(inp):
    assert len(inp) % 2 == 0
    n = len(inp[0])
    gamma = ''
    epsilon = ''
    for i in range(0, n):
        c = Counter(map(lambda s: s[i], inp))
        gamma += c.most_common()[0][0]
        epsilon += c.most_common()[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def step2(inp):
    n = len(inp[0])

    oxygen = inp[::]
    for i in range(0, n):
        c = Counter(map(lambda s: s[i], oxygen))
        common = c.most_common()
        k = common[0][0]
        if common[0][1] == common[1][1]:
            k = '1'  # tie, favor 1
        oxygen = list(filter(lambda s: s[i] == k, oxygen))
        if len(oxygen) == 1:
            break

    co2 = inp[::]
    for i in range(0, n):
        c = Counter(map(lambda s: s[i], co2))
        common = c.most_common()
        k = common[1][0]
        if common[0][1] == common[1][1]:
            k = '0'  # tie, favor 0
        co2 = list(filter(lambda s: s[i] == k, co2))
        if len(co2) == 1:
            break

    return int(oxygen[0], 2) * int(co2[0], 2)


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
print(step2(inp))
