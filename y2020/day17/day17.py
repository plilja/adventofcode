import sys
from collections import defaultdict

DELTAS = [[] for i in range(0, 7)]

for i in range(1, 6):
    if i == 1:
        DELTAS[i] = [(-1,), (0,), (1,)]
    else:
        DELTAS[i] += [x + (-1,) for x in DELTAS[i - 1]]
        DELTAS[i] += [x + (0,) for x in DELTAS[i - 1]]
        DELTAS[i] += [x + (1,) for x in DELTAS[i - 1]]


def neighbours(point):
    for deltas in DELTAS[len(point)]:
        xs = []
        for i in range(0, len(point)):
            xs.append(point[i] + deltas[i])
        yield tuple(xs)


def run(initial_state, dim):
    neighbours_cache = {}
    space = [defaultdict(int), defaultdict(int)]
    for y, xs in enumerate(initial_state):
        for x, c in enumerate(xs):
            key = (x, y) + tuple(0 for _ in range(0, dim - 2))
            space[0][key] = 1 if c == '#' else 0
    for i in range(1, 8):
        nodes = set()
        for point in space[(i - 1) % 2].keys():
            for neigh in neighbours(point):
                nodes.add(neigh)
        for node in nodes:
            state = space[(i - 1) % 2][node]
            neighs = neighbours_cache.get(node, None)
            if not neighs:
                neighs = list(neighbours(node))
                neighbours_cache[node] = neighs
            s = sum([space[(i - 1) % 2][neigh] for neigh in neighs])
            s -= state
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


def step1(initial_state):
    return run(initial_state, 3)


def step2(initial_state):
    return run(initial_state, 4)


def main():
    initial_state = [x.strip() for x in sys.stdin]
    print(step1(initial_state))
    print(step2(initial_state))
    # this one is really slow


if __name__ == '__main__':
    main()
