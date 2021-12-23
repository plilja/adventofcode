import sys
import copy

deltas = [(1, 0),
          (1, 1),
          (0, 1),
          (-1, 1),
          (-1, 0),
          (-1, -1),
          (0, -1),
          (1, -1)]


def one_step(grid):
    flashes = []
    for y in range(0, 10):
        for x in range(0, 10):
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashes.append((x, y))
    result = 0
    while flashes:
        x, y = flashes.pop(0)
        grid[y][x] = 0
        result += 1
        for dx, dy in deltas:
            if 0 <= x + dx < 10 and 0 <= y + dy < 10:
                if 0 < grid[y + dy][x + dx] < 10:
                    grid[y + dy][x + dx] += 1
                    if grid[y + dy][x + dx] == 10:
                        flashes.append((x + dx, y + dy))
    return result


def step1(grid):
    result = 0
    for i in range(0, 100):
        result += one_step(grid)
    return result


def step2(grid):
    i = 0
    while True:
        x = one_step(grid)
        i += 1
        if x == 100:
            return i


grid = [list(map(int, s.strip())) for s in sys.stdin]
print(step1(copy.deepcopy(grid)))
print(step2(copy.deepcopy(grid)))
