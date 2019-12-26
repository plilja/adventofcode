import sys
import heapq
from collections import defaultdict

DELTAS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]


def find(grid, what):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == what:
                return x, y
    raise ValueError('Not found')


def is_key(c):
    return c >= 'a' and c <= 'z'


def is_door(c):
    return c >= 'A' and c <= 'Z'


def get_all_keys(grid):
    keys = set()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if is_key(grid[y][x]):
                keys.add(grid[y][x])
    return keys


def dist(grid, initial_x, initial_y, all_keys):
    q = [(initial_x, initial_y, 0, set())]
    result = []
    v = set()
    while q:
        x, y, d, needed_keys = q.pop(0)
        v_key = (x, y)
        if v_key in v:
            continue
        v.add(v_key)
        if is_key(grid[y][x]) and (x, y) != (initial_x, initial_y):
            result.append((d, x, y, needed_keys))
        for dx, dy in DELTAS:
            x2 = x + dx
            y2 = y + dy
            if y2 < 0 or y2 >= len(grid):
                continue
            if x2 < 0 or x2 >= len(grid[y2]):
                continue
            c = grid[y2][x2]
            if c in ['.', '@'] or is_key(c):
                q.append((x2, y2, d + 1, needed_keys))
            elif is_door(c):
                q.append((x2, y2, d + 1, needed_keys | {c.lower()}))
    result.sort()
    return result


def solve(grid, initial_robots):
    all_keys = get_all_keys(grid)
    dists = {}
    for x, y in list(map(lambda k: find(grid, k), all_keys)) + initial_robots:
        dists[(x, y)] = defaultdict(list)
        for d, x2, y2, needed_keys in dist(grid, x, y, all_keys):
            dists[(x, y)][grid[y2][x2]].append((d, x2, y2, needed_keys))

    pq = [(0, initial_robots, set())]
    visited = {}
    best = float('inf')
    while pq:
        d, robots, keys = heapq.heappop(pq)
        cache_key = (tuple(robots), tuple(sorted(keys)))
        if cache_key in visited and visited[cache_key] <= d:
            continue
        visited[cache_key] = d
        if d >= best:
            continue
        if len(all_keys) == len(keys):
            best = min(best, d)
            continue
        for missing_key in all_keys - keys:
            for i in range(0, len(robots)):
                x, y = robots[i]
                for d2, x2, y2, needed_keys in dists[(x, y)][missing_key]:
                    if grid[y2][x2] not in keys and len(needed_keys - keys) == 0:
                        new_robots = robots[:i] + [(x2, y2)] + robots[i + 1:]
                        heapq.heappush(pq, (d + d2, new_robots, keys | {missing_key}))
                        break
    return best


def step1(grid):
    start_x, start_y = find(grid, '@')
    return solve(grid, [(start_x, start_y)])


def step2(grid):
    x, y = find(grid, '@')
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            grid[i][j] = '#'
    robots = [(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
    for x, y in robots:
        grid[y][x] = '@'
    return solve(grid, robots)


grid = [[c for c in s] for s in sys.stdin.readlines()]
print(step1(grid))
print(step2(grid))
