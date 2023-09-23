import sys
from collections import Counter


def step1(adapters):
    xs = [0] + sorted(adapters) + [max(adapters) + 3]
    diffs = map(lambda x: abs(x[0] - x[1]), zip(xs, xs[1:]))
    c = Counter(diffs)
    return c[1] * c[3]


def step2(adapters):
    xs = reversed(sorted([0] + adapters))
    built_in = max(adapters) + 3
    ms = [0] * (built_in + 1)
    ms[built_in] = 1
    for adapter in xs:
        for i in range(1, 4):
            t = ms[adapter + i]
            ms[adapter] += t
    return ms[0]


adapters = [int(x) for x in sys.stdin]
print(step1(adapters))
print(step2(adapters))
