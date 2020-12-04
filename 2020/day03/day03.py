import sys


def count_trees(grid, dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#':
            trees += 1
        x = (x + dx) % len(grid[0])
        y += dy
    return trees


def step1(grid):
    return count_trees(grid, 3, 1)


def step2(grid):
    result = 1
    slopes = [(1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)]
    for dx, dy in slopes:
        result *= count_trees(grid, dx, dy)
    return result


grid = [s.strip() for s in sys.stdin.readlines()]
print(step1(grid))
print(step2(grid))
