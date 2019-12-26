import sys
import heapq

DELTAS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]


def find(inp, what):
    for y in range(0, len(inp)):
        for x in range(0, len(inp[0])):
            if inp[y][x] == '@':
                return x, y
    raise ValueError('Not found')


def is_key(c):
    return c >= 'a' and c <= 'z'


def is_door(c):
    return c >= 'A' and c <= 'Z'


def get_all_keys(inp):
    keys = set()
    for y in range(0, len(inp)):
        for x in range(0, len(inp[0])):
            if is_key(inp[y][x]):
                keys.add(inp[y][x])
    return keys


def step1(grid):
    all_keys = get_all_keys(grid)
    start_x, start_y = find(grid, '@')
    pq = [(0, 0, start_x, start_y, set())]
    visited = set()
    best = float('inf')
    while pq:
        num_keys, dist, x, y, keys = heapq.heappop(pq)
        cache_key = (x, y, tuple(sorted(keys)))
        if cache_key in visited:
            continue
        visited.add(cache_key)
        if len(all_keys) == num_keys:
            best = min(best, dist)
            continue
        for dx, dy in DELTAS:
            x2 = x + dx
            y2 = y + dy
            if y2 < 0 or y2 >= len(inp):
                continue
            if x2 < 0 or x2 >= len(inp[y2]):
                continue
            c = inp[y2][x2]
            if c in ['.', '@']:
                heapq.heappush(pq, (num_keys, dist + 1, x2, y2, keys))
            elif is_key(c):
                if c in keys:
                    heapq.heappush(pq, (num_keys, dist + 1, x2, y2, keys))
                else:
                    heapq.heappush(pq, (num_keys + 1, dist + 1, x2, y2, keys | {c}))
            elif is_door(c) and c.lower() in keys:
                heapq.heappush(pq, (num_keys, dist + 1, x2, y2, keys))
    return best


inp = sys.stdin.readlines()
print(step1(inp))
