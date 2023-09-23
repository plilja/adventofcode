import sys

sys.path.append("../..")
from common.util import neighbors4
from collections import deque


def step1(grid):
    return dist_to_goal(grid, ['S'])


def step2(grid):
    return dist_to_goal(grid, ['a', 'S'])


def dist_to_goal(grid, starts):
    q = deque([])
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] in starts:
                q.append(((x, y), 0))
    visited = set()
    while q:
        (x, y), d = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        c = grid[y][x]
        if c == 'E':
            return d
        for x2, y2 in neighbors4(x, y):
            if y2 < 0 or y2 >= len(grid):
                continue
            if x2 < 0 or x2 >= len(grid[y]):
                continue
            c2 = grid[y2][x2]
            if elevation(c2) - elevation(c) <= 1:
                q.append(((x2, y2), d + 1))
    return float('inf')


def elevation(c):
    if c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')
    else:
        return ord(c)


grid = [s.strip() for s in sys.stdin]
print(step1(grid))
print(step2(grid))
