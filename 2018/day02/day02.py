import sys
from collections import defaultdict, Counter


def step1(inp):
    r = defaultdict(int)
    for line in inp:
        c = set(Counter(line).values())
        for i in c:
            r[i] += 1
    return r[2] * r[3]


def step2(inp):
    def str_common(s1, s2):
        return ''.join([a if a == b else '' for a, b in zip(s1, s2)])

    for i in range(0, len(inp)):
        for j in range(i + 1, len(inp)):
            s = str_common(inp[i], inp[j])
            if len(s) == len(inp[j]) - 1:
                return s
    raise ValueError('No solution found')


inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
print(step2(inp))
