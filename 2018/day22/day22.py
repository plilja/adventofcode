from collections import deque, defaultdict
import re
import sys
import heapq

UNKNOWN = -1
ROCKY = 0
WET = 1
NARROW = 2
M = 20183
CLIMBING = 0
TORCH = 1
NEITHER = 2
CHANGING_COST = 7
TRAVEL_COST = 1
INF = float('inf')

def step1(depth, tx, ty):
    terrain = determine_terrain(depth, tx, ty, tx, ty)
    r = 0
    riskyness = {ROCKY:0, WET:1, NARROW:2}
    for y in range(0, ty + 1):
        for x in range(0, tx + 1):
            r += riskyness[terrain[y][x]]
    return r


def step2(depth, tx, ty):
    valid_eqip = {
            ROCKY:{CLIMBING, TORCH},
            WET:{CLIMBING, NEITHER},
            NARROW:{TORCH, NEITHER}
            }

    edge = int(1.2 * max(tx, ty))
    terrain = determine_terrain(depth, tx, ty, edge, edge)

    dist = defaultdict(lambda: INF)
    pq = [(0, (0, 0, TORCH))]
    while pq:
        d, (x, y, gear) = heapq.heappop(pq)
        if dist[(x, y, gear)] <= d:
            continue

        dist[(x, y, gear)] = d
        gear1 = valid_eqip[terrain[y][x]]
        for g in gear1 - {gear}:
            heapq.heappush(pq, (d + CHANGING_COST, (x, y, g)))

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= x + dx <= edge and 0 <= y + dy <= edge:
                gear2 = valid_eqip[terrain[y + dy][x + dx]]
                for g in gear1 & gear2:
                    d2 = d + TRAVEL_COST
                    if gear == g and dist[(x + dx, y + dy, g)] > d2:
                        heapq.heappush(pq, (d2, (x + dx, y + dy, g)))
    return dist[(tx, ty, TORCH)]


def determine_terrain(depth, tx, ty, maxx, maxy):
    erosion_levels = defaultdict(lambda: defaultdict(lambda: UNKNOWN))
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if erosion_levels[y][x] != UNKNOWN or x == maxx + 1 or y == maxy + 1:
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

    terrain = {}
    for y in range(0, maxy + 1):
        terrain[y] = {}
        for x in range(0, maxx + 1):
            t = erosion_levels[y][x] % 3
            terrain[y][x] = t
    return terrain


depth = int(input().split()[1])
tx, ty = list(map(int, re.findall(r'\d+', input())))
print(step1(depth, tx, ty))
print(step2(depth, tx, ty)) # This one is slow
