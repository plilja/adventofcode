import sys
from collections import defaultdict, deque

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def step1(coordinates):
    closest = defaultdict(lambda: defaultdict(set))
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    visited = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))

    edge_left_x = min(map(lambda p: p[0], coordinates))
    edge_right_x = max(map(lambda p: p[0], coordinates))
    edge_bottom_y = min(map(lambda p: p[1], coordinates))
    edge_top_y = max(map(lambda p: p[1], coordinates))
    q = deque()

    # Initialize queue with all locations in input
    for i, (x, y) in enumerate(coordinates):
        q.append((x, y, i, 0))

    # Iterate while we haven't reached edge
    while q:
        x, y, i, d = q.popleft()
        if visited[y][x][i] or dist[y][x] < d:
            continue
        closest[y][x] |= {i}
        dist[y][x] = d
        visited[y][x][i] = True
        for dx, dy in deltas:
            if edge_left_x <= x + dx <= edge_right_x and edge_bottom_y <= y + dy <= edge_top_y:
                q.append((x + dx, y + dy, i, d + 1))

    # Find area for each coordinate
    coordinates_area = defaultdict(int)
    at_edge = set()
    for y in closest.keys():
        for x in closest[y].keys():
            coords = closest[y][x]
            if len(coords) == 1 and (x in [edge_left_x, edge_right_x] or y in [edge_bottom_y, edge_top_y]):
                at_edge |= coords
            coordinates_area[coords.pop()] += 1

    # Find max area of coordinate that is not at edge
    ans = 0
    for i, _ in enumerate(coordinates):
        if i not in at_edge:
            ans = max(ans, coordinates_area[i])

    return ans


def step2(coordinates):
    x1 = min(map(lambda p: p[0], coordinates))
    x2 = max(map(lambda p: p[0], coordinates))
    y1 = min(map(lambda p: p[1], coordinates))
    y2 = max(map(lambda p: p[1], coordinates))
    ans = 0
    for a in range(x1, x2 + 1):
        for b in range(y1, y2 + 1):
            total_dist = 0
            in_region = True
            for x, y in coordinates:
                total_dist += abs(a - x) + abs(b - y)
                if total_dist >= 10000:
                    in_region = False
                    break
            if in_region:
                ans += 1
    return ans


coordinates = [tuple(map(int, s.split(', '))) for s in sys.stdin.readlines()]
print(step1(coordinates))
print(step2(coordinates))

