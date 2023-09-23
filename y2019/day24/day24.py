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


def step1(initial_grid):
    grids = [copy.deepcopy(initial_grid), make_grid()]
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


def step2(initial_grid):
    levels = [[], []]
    for i in range(0, 402):
        levels[0].append(make_grid())
        levels[1].append(make_grid())
    levels[0][200] = copy.deepcopy(initial_grid)
    for i in range(0, 200):
        levels1 = levels[i % 2]
        levels2 = levels[(i + 1) % 2]
        for j in range(1, 401):
            level1 = levels1[j]
            level2 = levels2[j]
            prev_level = levels1[j - 1]
            next_level = levels1[j + 1]
            for y in range(0, 5):
                for x in range(0, 5):
                    if (x, y) == (2, 2):
                        continue
                    c = 0
                    for dx, dy in DELTAS:
                        x2 = x + dx
                        y2 = y + dy
                        if (x2, y2) == (2, 2):
                            for k in range(0, 5):
                                y3 = 4 if dy == -1 else abs(dx) * k
                                x3 = 4 if dx == -1 else abs(dy) * k
                                if next_level[y3][x3]:
                                    c += 1
                        elif x2 < 0 or x2 >= 5 or y2 < 0 or y2 >= 5:
                            c += 1 if prev_level[2 + dy][2 + dx] else 0
                        elif level1[y2][x2]:
                            c += 1
                    level2[y][x] = level1[y][x]
                    if level1[y][x] and c != 1:
                        level2[y][x] = False
                    if not level1[y][x] and c in [1, 2]:
                        level2[y][x] = True

    r = 0
    for level in levels[200 % 2]:
        for y in range(0, 5):
            for x in range(0, 5):
                if (x, y) == (2, 2):
                    continue
                if level[y][x]:
                    r += 1
    return r


def make_grid():
    return defaultdict(lambda: defaultdict(lambda: False))


def read_grid():
    grid = make_grid()
    for y, line in enumerate(sys.stdin.readlines()):
        for x, v in enumerate(line.strip()):
            grid[y][x] = True if v == '#' else False
    return grid


grid = read_grid()
print(step1(grid))
print(step2(grid))
