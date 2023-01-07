import sys


def step1(grid):
    res = set()
    for y in range(0, len(grid)):
        minimum = -1
        for x in range(0, len(grid[0])):
            v = int(grid[y][x])
            if v > minimum:
                res.add((x, y))
                minimum = v
    for y in range(0, len(grid)):
        minimum = -1
        for x in range(len(grid[0]) - 1, -1, -1):
            v = int(grid[y][x])
            if v > minimum:
                res.add((x, y))
                minimum = v
    for x in range(0, len(grid[0])):
        minimum = -1
        for y in range(0, len(grid)):
            v = int(grid[y][x])
            if v > minimum:
                res.add((x, y))
                minimum = v
    for x in range(0, len(grid[0])):
        minimum = -1
        for y in range(len(grid) - 1, -1, -1):
            v = int(grid[y][x])
            if v > minimum:
                res.add((x, y))
                minimum = v
    return len(res)


grid = [s.strip() for s in sys.stdin.readlines()]
print(step1(grid))
