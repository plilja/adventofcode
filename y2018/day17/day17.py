from collections import defaultdict
import sys
import re
import copy


def step1(grid):
    return solve(grid)[0]


def step2(grid):
    return solve(grid)[1]


def solve(grid):
    grid = copy.deepcopy(grid)
    min_y = min(grid.keys())
    max_y = max(grid.keys())

    def mark_neighbours(x, y):
        if grid[y][x + 1] in '#~' and grid[y][x - 1] in '#~/':
            grid[y][x] = '~'
        elif grid[y][x + 1] == '|' or grid[y][x - 1] == '|':
            grid[y][x] = '|'
        else:
            grid[y][x] = '/'  # Don't know yet, mark as inconclusive

    def dfs(x, y):
        assert(grid[y][x] in './')
        if y > max_y:
            return
        if grid[y + 1][x] in '.|':
            grid[y][x] = '|'
            if grid[y + 1][x] == '.':
                dfs(x, y + 1)

        if grid[y + 1][x] in '#~':
            mark_neighbours(x, y)

            if grid[y][x - 1] in '.':
                dfs(x - 1, y)

            mark_neighbours(x, y)

            if grid[y][x + 1] in '.':
                dfs(x + 1, y)

            mark_neighbours(x, y)

            if grid[y][x - 1] in '/' and grid[y][x] in '|~':
                dfs(x - 1, y)

            mark_neighbours(x, y)

    dfs(500, 1)
    wet, resting = 0, 0
    for y, row in grid.items():
        if y >= min_y:
            wet += sum([1 for v in row.values() if v in '~|'])
            resting += sum([1 for v in row.values() if v in '~'])
    return wet, resting


def parse_inp():
    grid = defaultdict(lambda: defaultdict(lambda: '.'))
    for s in sys.stdin:
        (a, v, b, t1, t2) = re.match(
            r'([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)', s).groups()
        for i in range(int(t1), int(t2) + 1):
            if a == 'x':
                grid[i][int(v)] = '#'
            else:
                assert a == 'y'
                grid[int(v)][i] = '#'
    return grid


sys.setrecursionlimit(4000)
grid = parse_inp()
print(step1(grid))
print(step2(grid))

