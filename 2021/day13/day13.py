import re
import sys
from collections import defaultdict


def step1(grid, folds):
    x_or_y, coord = folds[0]
    for y in list(grid.keys()):
        for x in list(grid[y].keys()):
            if x_or_y == 'x' and x > coord:
                grid[y][x] = False
                grid[y][2 * coord - x] = True
            elif x_or_y == 'y' and y > coord:
                grid[y][x] = False
                grid[2 * coord - y][x] = True
    result = 0
    for y in grid.keys():
        for x in grid[y].keys():
            if grid[y][x]:
                result += 1
    return result


def read_input():
    grid = defaultdict(lambda: defaultdict(lambda: False))
    folds = []
    for line in sys.stdin:
        if ',' in line:
            x, y = line.split(',')
            grid[int(y)][int(x)] = True
        elif 'fold' in line:
            x_or_y, coord = re.match(r'fold along (.)=(\d+)', line).groups()
            folds.append((x_or_y, int(coord)))
    return grid, folds


grid, folds = read_input()
print(step1(grid, folds))
