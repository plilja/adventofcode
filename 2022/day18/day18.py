import sys
from collections import defaultdict


def step1(inp):
    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
    for x, y, z in inp:
        grid[x][y][z] = True
    result = 0
    for x, y, z in inp:
        if not grid[x - 1][y][z]:
            result += 1
        if not grid[x + 1][y][z]:
            result += 1
        if not grid[x][y - 1][z]:
            result += 1
        if not grid[x][y + 1][z]:
            result += 1
        if not grid[x][y][z - 1]:
            result += 1
        if not grid[x][y][z + 1]:
            result += 1
    return result


def read_input():
    result = []
    for line in sys.stdin:
        x, y, z = list(map(int, line.strip().split(',')))
        result.append((x, y, z))
    return result


inp = read_input()
print(step1(inp))
