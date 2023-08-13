import sys
from collections import defaultdict, deque

DELTAS = [(1, 0, 0), 
          (-1, 0, 0), 
          (0, 1, 0), 
          (0, -1, 0),
          (0, 0, 1),
          (0, 0, -1)]


def step1(inp):
    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
    for x, y, z in inp:
        grid[x][y][z] = True
    return count_exposed_sides(inp, grid)


def step2(inp):
    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))
    for x, y, z in inp:
        grid[x][y][z] = True
    for x, y, z in inp:
        for dx, dy, dz in DELTAS:
            vis = set()
            limit = len(inp) // 2
            dfs(grid, x + dx, y + dy, z + dz, vis, limit)
            if len(vis) < limit and len(vis) > 0:
                for x2, y2, z2 in vis:
                    grid[x2][y2][z2] = True
    return count_exposed_sides(inp, grid)


def dfs(grid, x, y, z, vis, limit):
    if grid[x][y][z]:
        return
    if (x, y, z) in vis:
        return
    vis.add((x, y, z))
    if len(vis) >= limit:
        return
    for dx, dy, dz in DELTAS:
        dfs(grid, x + dx, y + dy, z + dz, vis, limit)


def count_exposed_sides(inp, grid):
    result = 0
    for x, y, z in inp:
        if not grid[x - 1][y][z]:
            result += 1
        if not grid[x + 1][y][z]:
            result += 1
        if not grid[x][y - 1][z]:
            result += 1
        if not grid[x][y + 1][z]:
            result += 1
        if not grid[x][y][z - 1]:
            result += 1
        if not grid[x][y][z + 1]:
            result += 1
    return result


def read_input():
    result = []
    for line in sys.stdin:
        x, y, z = list(map(int, line.strip().split(',')))
        result.append((x, y, z))
    return result


inp = read_input()
sys.setrecursionlimit(2 * len(inp) + 1)
print(step1(inp))
print(step2(inp))
