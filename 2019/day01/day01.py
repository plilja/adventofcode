import sys


def step1(inp):
    return sum([x // 3 - 2 for x in inp])


inp = list(map(int, sys.stdin.readlines()))
print(step1(inp))
