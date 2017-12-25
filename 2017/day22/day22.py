import sys
from collections import defaultdict


def step1(inp):
    x = len(inp) // 2
    y = x
    dx = 0
    dy = -1
    ans = 0

    grid = defaultdict(lambda: defaultdict(lambda: False))
    for i in range(0, len(inp)):
        for j in range(0, len(inp[0])):
            grid[i][j] = False if inp[i][j] == '.' else True

    for _ in range(0, 10000):
        if grid[y][x]:
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        if not grid[y][x]:
            ans += 1
        grid[y][x] = not grid[y][x]
        x += dx
        y += dy

    return ans


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
