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


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
