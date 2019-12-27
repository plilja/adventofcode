import sys
import heapq
from functools import lru_cache

DELTAS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]


def step1(grid):
    def get_or(x, y, default):
        if y < 0 or y >= len(grid):
            return default
        if x < 0 or x >= len(grid[y]):
            return default
        return grid[y][x]

    def find(what):
        result = []
        assert len(what) == 2
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                c1 = grid[y][x]
                if c1 in what:
                    for dy, dx in DELTAS:
                        c2 = get_or(x + dx, y + dy, '-')
                        c3 = get_or(x + 2 * dx, y + 2 * dy, '-')
                        if (c1 + c2 == what or c2 + c1 == what) and c3 == '.':
                            result.append((x + 2 * dx, y + 2 * dy))
        return result

    @lru_cache(maxsize=None)
    def other_end(x, y):
        c1 = grid[y][x]
        for dy, dx in DELTAS:
            c2 = get_or(x + dx, y + dy, '-')
            if c2 >= 'A' and c2 <= 'Z':
                ends = find(c1 + c2)
                if not ends:
                    ends = find(c2 + c1)
                for end in ends:
                    if end != (x - dx, y - dy):
                        return end
        return None

    [(start_x, start_y)] = find('AA')
    [(end_x, end_y)] = find('ZZ')
    pq = [(0, start_x, start_y, None, None)]
    v = set()
    while pq:
        dist, x, y, pre_x, pre_y = heapq.heappop(pq)
        if (x, y) in v:
            continue
        v.add((x, y))
        if (x, y) == (end_x, end_y):
            return dist
        for dx, dy in DELTAS:
            x2 = x + dx
            y2 = y + dy
            c = get_or(x2, y2, '-')
            if c == '.':
                heapq.heappush(pq, (dist + 1, x2, y2, x, y))
            elif c >= 'A' and c <= 'Z':
                end = other_end(x2, y2)
                if end:
                    heapq.heappush(pq, (dist + 1, end[0], end[1], x, y))
    raise ValueError('Unable to find path to end')


grid = sys.stdin.readlines()
print(step1(grid))
