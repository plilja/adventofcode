import sys
import heapq

DELTAS = [(1, 0),
          (0, 1),
          (-1, 0),
          (0, -1)]


def step1(grid):
    pq = [(0, 0, 0)]
    costs = {}
    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x, y) in costs:
            continue
        costs[(x, y)] = cost
        for dx, dy in DELTAS:
            x2 = x + dx
            y2 = y + dy
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                heapq.heappush(pq, (cost + grid[y2][x2], x2, y2))
    return costs[(len(grid[0]) - 1, len(grid) - 1)]


grid = [list(map(int, s.strip())) for s in sys.stdin]
print(step1(grid))
