import sys


def step1(inp):
    ans = 0
    for row in inp:
        smallest = min(row)
        largest = max(row)
        ans += largest - smallest
    return ans


def read_input():
    ans = []
    for row in sys.stdin.readlines():
        ans += [list(map(int, row.split()))]
    return ans

inp = read_input()
print(step1(inp))
