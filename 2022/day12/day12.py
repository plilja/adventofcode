import sys

sys.path.append("../..")
from common.util import neighbors4
from collections import deque


def step1(grid):
    start = find(grid, 'S')
    q = deque([(start, 0)])
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
    return -1


def elevation(c):
    if c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')
    else:
        return ord(c)


def find(grid, c):
    for y in range(0, len(grid[0])):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 'S':
                return (x, y)
    raise ValueError('Not found')


grid = [s.strip() for s in sys.stdin]
print(step1(grid))
