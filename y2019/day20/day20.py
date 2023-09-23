import sys
from functools import lru_cache

DELTAS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

grid = sys.stdin.readlines()


def get_or(x, y, default):
    if y < 0 or y >= len(grid):
        return default
    if x < 0 or x >= len(grid[y]):
        return default
    return grid[y][x]


@lru_cache(maxsize=None)
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
def get_label(x, y):
    c1 = grid[y][x]
    for dy, dx in DELTAS:
        c2 = get_or(x + dx, y + dy, '-')
        if c2 >= 'A' and c2 <= 'Z':
            return min(c1, c2) + max(c1, c2)
    raise ValueError('Unable to get label at %d %d' % (x, y))


@lru_cache(maxsize=None)
def other_end(x, y):
    label = get_label(x, y)
    ends = find(label)
    for x2, y2 in ends:
        if abs(x - x2) + abs(y - y2) > 2:
            return x2, y2
    return None


def step1():
    [(start_x, start_y)] = find('AA')
    [(end_x, end_y)] = find('ZZ')
    q = [(0, start_x, start_y)]
    v = set()
    while q:
        dist, x, y = q.pop(0)
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
                q.append((dist + 1, x2, y2))
            elif 'A' <= c <= 'Z':
                end = other_end(x2, y2)
                if end:
                    q.append((dist + 1, end[0], end[1]))
    raise ValueError('Unable to find path to end')


def is_outer_edge(x, y):
    return y < 5 or len(grid) - 1 - y < 5 or \
            x < 5 or len(grid[0]) - 1 - x < 5


def step2():
    [(start_x, start_y)] = find('AA')
    [(end_x, end_y)] = find('ZZ')
    q = [(0, 0, start_x, start_y)]
    v = set()
    while q:
        dist, level, x, y = q.pop(0)
        if (x, y, level) in v:
            continue
        v.add((x, y, level))
        if (x, y) == (end_x, end_y) and level == 0:
            return dist
        for dx, dy in DELTAS:
            x2 = x + dx
            y2 = y + dy
            c = get_or(x2, y2, '-')
            if c == '.':
                q.append((dist + 1, level, x2, y2))
            elif 'A' <= c <= 'Z':
                label = get_label(x2, y2)
                if label not in ['AA', 'ZZ']:
                    x3, y3 = other_end(x2, y2)
                    if is_outer_edge(x2, y2):
                        if level > 0:
                            q.append((dist + 1, level - 1, x3, y3))
                    else:
                        q.append((dist + 1, level + 1, x3, y3))

    raise ValueError('Unable to find path to end')


print(step1())
print(step2())
