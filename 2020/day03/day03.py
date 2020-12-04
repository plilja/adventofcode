import sys


def step1(grid):
    x, y = 0, 0
    dx, dy = 3, 1
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#':
            trees += 1
        x = (x + dx) % len(grid[0])
        y += dy
    return trees


grid = [s.strip() for s in sys.stdin.readlines()]
print(step1(grid))
