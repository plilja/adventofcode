import re
import sys
import copy
from collections import defaultdict


def step1(grid, folds):
    one_fold(grid, folds[0])
    result = 0
    for y in grid.keys():
        for x in grid[y].keys():
            if grid[y][x]:
                result += 1
    return result


def step2(grid, folds):
    for fold in folds:
        one_fold(grid, fold)
    max_x, max_y = 0, 0
    for y in grid.keys():
        for x in grid[y].keys():
            if grid[y][x]:
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if grid[y][x]:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def one_fold(grid, fold):
    x_or_y, coord = fold
    for y in list(grid.keys()):
        for x in list(grid[y].keys()):
            if grid[y][x]:
                if x_or_y == 'x' and x > coord:
                    grid[y][x] = False
                    grid[y][2 * coord - x] = True
                elif x_or_y == 'y' and y > coord:
                    grid[y][x] = False
                    grid[2 * coord - y][x] = True


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
print(step1(copy.deepcopy(grid), folds))
step2(copy.deepcopy(grid), folds)
