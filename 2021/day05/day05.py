import sys
import re
from collections import defaultdict


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def step1(lines):
    grid = defaultdict(lambda: defaultdict(int))
    for (x1, y1), (x2, y2) in lines:
        if x1 != x2 and y1 != y2:
            continue  # as per instructions these should be ignored in step1
        x, y = x1, y1
        dx = sign(x2 - x1)
        dy = sign(y2 - y1)
        while x != x2 + dx or y != y2 + dy:
            grid[y][x] += 1
            x += dx
            y += dy
    result = 0
    for row in grid.values():
        for c in row.values():
            if c >= 2:
                result += 1
    return result


def read_input():
    result = []
    for line in sys.stdin.readlines():
        x1, y1, x2, y2 = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()
        result.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return result


lines = read_input()
print(step1(lines))
