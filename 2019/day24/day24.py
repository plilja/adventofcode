import sys
import copy
from collections import defaultdict


DELTAS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]


def biodiversity(grid):
    r = 0
    d = 1
    for y in range(0, 5):
        for x in range(0, 5):
            if grid[y][x]:
                r += d
            d *= 2
    return r


#def p(grid):
#    for y in range(0, 5):
#        for x in range(0, 5):
#
#            print('#' if grid[y][x] else '.', end='')
#        print()
#    print()


def step1(initial_grid):
    grids = [copy.deepcopy(initial_grid), copy.deepcopy(initial_grid)]
    seen = set()
    i = 0
    while True:
        grid = grids[i % 2]
        next_grid = grids[(i + 1) % 2]
        b = biodiversity(grid)
        if b in seen:
            return b
        seen.add(b)
        for y in range(0, 5):
            for x in range(0, 5):
                c = 0
                for dx, dy in DELTAS:
                    if grid[y + dy][x + dx]:
                        c += 1
                next_grid[y][x] = grid[y][x]
                if grid[y][x] and c != 1:
                    next_grid[y][x] = False
                if not grid[y][x] and c in [1, 2]:
                    next_grid[y][x] = True
        i += 1


def read_grid():
    grid = defaultdict(lambda: defaultdict(lambda: False))
    for y, line in enumerate(sys.stdin.readlines()):
        for x, v in enumerate(line.strip()):
            grid[y][x] = True if v == '#' else False
    return grid


grid = read_grid()
print(step1(grid))
