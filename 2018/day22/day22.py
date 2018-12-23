from collections import deque, defaultdict
import re

UNKNOWN = -1
M = 20183

def step1(depth, tx, ty):
    erosion_levels = defaultdict(lambda: defaultdict(lambda: UNKNOWN))
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if erosion_levels[y][x] != UNKNOWN or x == tx + 1 or y == ty + 1:
            continue
        if (x, y) == (tx, ty):
            geo_index = 0
        elif y == 0:
            geo_index = x * 16807
        elif x == 0:
            geo_index = y * 48271
        else:
            assert erosion_levels[y][x - 1] != UNKNOWN
            assert erosion_levels[y - 1][x] != UNKNOWN
            geo_index = erosion_levels[y][x - 1] * erosion_levels[y - 1][x]
        erosion_level = ((geo_index % M) + (depth % M)) % M
        erosion_levels[y][x] = erosion_level
        for dx, dy in [(1, 0), (0, 1)]:
            q.append((x + dx, y + dy))

    r = 0
    riskyness = {0: 0, 1:1, 2:2}
    for y in range(0, ty + 1):
        for x in range(0, tx + 1):
            t = erosion_levels[y][x] % 3
            r += riskyness[t]
    return r


depth = int(input().split()[1])
tx, ty = list(map(int, re.findall(r'\d+', input())))
print(step1(depth, tx, ty))
