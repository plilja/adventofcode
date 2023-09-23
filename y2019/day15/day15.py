from collections import defaultdict
from y2019.intcode import IntcodeProcess

UNKNOWN = -1
WALL = 0
OPEN = 1
OXYGEN_SYSTEM = 2
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def explore(instructions):
    space = defaultdict(lambda: defaultdict(lambda: UNKNOWN))

    def walk(direction, x, y):
        process.add_input(direction)
        while not process.needs_input():
            process.tick()
        assert process.has_output()
        output = process.pop_output()
        space[y][x] = output
        return output != WALL

    initial_process = IntcodeProcess(instructions)
    q = [(0, 0, initial_process)]
    space[0][0] = OPEN
    while q:
        x, y, process = q[0]
        q = q[1:]
        if space[y + 1][x] == UNKNOWN and walk(SOUTH, x, y + 1):
            q += [(x, y + 1, process.fork())]
            walk(NORTH, x, y)
        if space[y - 1][x] == UNKNOWN and walk(NORTH, x, y - 1):
            q += [(x, y - 1, process.fork())]
            walk(SOUTH, x, y)
        if space[y][x + 1] == UNKNOWN and walk(EAST, x + 1, y):
            q += [(x + 1, y, process.fork())]
            walk(WEST, x, y)
        if space[y][x - 1] == UNKNOWN and walk(WEST, x - 1, y):
            q += [(x - 1, y, process.fork())]
            walk(EAST, x, y)
    return space


def find(space, what):
    for y in space.keys():
        for x in space[y].keys():
            if space[y][x] == what:
                return (x, y)
    raise ValueError('Value not found')


def dists(space, start_x, start_y):
    res = defaultdict(lambda: defaultdict(lambda: float('inf')))
    q = [(start_x, start_y, 0)]
    visited = set()
    while q:
        x, y, dist = q[0]
        q = q[1:]
        if (x, y) in visited:
            continue
        visited.add((x, y))
        res[y][x] = dist
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if space[y + dy][x + dx] != WALL:
                q += [(x + dx, y + dy, dist + 1)]
    return res


def step1(instructions):
    space = explore(instructions)
    x, y = find(space, OXYGEN_SYSTEM)
    return dists(space, 0, 0)[y][x]


def step2(instructions):
    space = explore(instructions)
    x, y = find(space, OXYGEN_SYSTEM)
    d = dists(space, x, y)
    result = 0
    for y in d.keys():
        for x in d[y].keys():
            result = max(result, d[y][x])
    return result


instructions = list(map(int, input().split(',')))
print(step1(instructions))
print(step2(instructions))
