import sys


def step1(inp):
    return sum([x // 3 - 2 for x in inp])


def step2(inp):
    ans = 0
    for x in inp:
        mass = x
        while mass > 0:
            fuel = max(mass // 3 - 2, 0)
            mass = fuel
            ans += fuel
    return ans


inp = list(map(int, sys.stdin.readlines()))
print(step1(inp))
print(step2(inp))
