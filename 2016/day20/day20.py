import sys


def step1(inp):
    blacklist = []
    for [lower, upper] in map(lambda s: s.split('-'), inp):
        blacklist += [(int(lower), int(upper))]
    blacklist.sort()
    r = 0
    for lower, upper in blacklist:
        if lower > r:
            return r
        else:
            r = upper + 1
    return r


inp = sys.stdin.readlines()
print(step1(inp))
