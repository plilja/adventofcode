import sys
from collections import defaultdict

# Hex grid will look like this in memory
#  72     6   7
# 613  = 5  1  2
# 54      4   3

DIRECTIONS = {'e':  (1, -1),
              'se': (1, 0),
              'sw': (0, 1),
              'w': (-1, 1),
              'nw': (-1, 0),
              'ne': (0, -1)}


def initial_grid(inp):
    grid = defaultdict(int)
    for line in inp:
        rem = line
        x, y = 0, 0
        while rem:
            for key, (dx, dy) in DIRECTIONS.items():
                if rem.startswith(key):
                    rem = rem[len(key):]
                    x += dx
                    y += dy
        assert rem == ''
        grid[(x, y)] = (grid[(x, y)] + 1) % 2
    return grid


def step1(inp):
    grid = initial_grid(inp)
    return sum(grid.values())


def step2(inp):
    grids = [initial_grid(inp), defaultdict(int)]
    to_check = set()
    for i in range(0, 100):
        for (x, y) in grids[i % 2].keys():
            to_check.add((x, y))
            for dx, dy in DIRECTIONS.values():
                to_check.add((x + dx, y + dy))

        for (x, y) in to_check:
            current = grids[i % 2][(x, y)]
            new = current
            blacks = 0
            for dx, dy in DIRECTIONS.values():
                blacks += grids[i % 2][(x + dx, y + dy)]
            if current == 1 and (blacks == 0 or blacks > 2):
                new = 0
            if current == 0 and blacks == 2:
                new = 1
            grids[(i + 1) % 2][(x, y)] = new
    return sum(grids[100 % 2].values())


inp = [line.strip() for line in sys.stdin]
print(step1(inp))
print(step2(inp))
