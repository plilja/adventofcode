import sys
from collections import defaultdict


def neighbours(point):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx != 0 or dy != 0 or dz != 0:
                    yield (point[0] + dx, point[1] + dy, point[2] + dz)


def step1(initial_state):
    space = [defaultdict(int), defaultdict(int)]
    for y, xs in enumerate(initial_state):
        for x, c in enumerate(xs):
            space[0][(x, y, 0)] = 1 if c == '#' else 0
    for i in range(1, 8):
        nodes = set()
        for point in space[(i - 1) % 2].keys():
            for neigh in neighbours(point):
                nodes.add(neigh)
                nodes.add(point)
        for node in nodes:
            state = space[(i - 1) % 2][node]
            s = sum([space[(i - 1) % 2][neigh] for neigh in neighbours(node)])
            if state == 1:
                if 2 <= s <= 3:
                    new_state = 1
                else:
                    new_state = 0
            else:
                if s == 3:
                    new_state = 1
                else:
                    new_state = 0
            space[i % 2][node] = new_state
    return sum([x for x in space[8 % 2].values()])


initial_state = [x.strip() for x in sys.stdin]
print(step1(initial_state))
