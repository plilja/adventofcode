import sys
import heapq

DELTAS = [(1, 0),
          (0, 1),
          (-1, 0),
          (0, -1)]


def step1(grid):
    return dijkstra(grid)


def step2(grid):
    new_grid = [[0] * 5 * len(grid[0]) for _ in range(0, 5 * len(grid))]
    assert len(grid) == len(grid[0])
    n = len(grid)
    for y in range(0, 5*n):
        for x in range(0, 5*n):
            offset_x = x // n
            offset_y = y // n
            new_grid[y][x] = (grid[y % n][x % n] + offset_x + offset_y - 1) % 9
            new_grid[y][x] += 1
    return dijkstra(new_grid)


def dijkstra(grid):
    pq = [(0, 0, 0)]
    costs = {}
    n = len(grid)
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
    return costs[(n - 1, n - 1)]


grid = [list(map(int, s.strip())) for s in sys.stdin]
print(step1(grid))
print(step2(grid))
