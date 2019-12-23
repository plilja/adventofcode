import sys
sys.path.append("..")
from collections import defaultdict
from intcode import IntcodeProcess

UNKNOWN = -1
WALL = 0
OPEN = 1
OXYGEN_SYSTEM = 2
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def step1(instructions):
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
    q = [(0, 0, 0, initial_process)]
    space[0][0] = OPEN
    while q:
        x, y, dist, process = q[0]
        q = q[1:]
        if space[y][x] == OXYGEN_SYSTEM:
            return dist
        if space[y + 1][x] == UNKNOWN and walk(SOUTH, x, y + 1):
            q += [(x, y + 1, dist + 1, process.fork())]
            walk(NORTH, x, y)
        if space[y - 1][x] == UNKNOWN and walk(NORTH, x, y - 1):
            q += [(x, y - 1, dist + 1, process.fork())]
            walk(SOUTH, x, y)
        if space[y][x + 1] == UNKNOWN and walk(EAST, x + 1, y):
            q += [(x + 1, y, dist + 1, process.fork())]
            walk(WEST, x, y)
        if space[y][x - 1] == UNKNOWN and walk(WEST, x - 1, y):
            q += [(x - 1, y, dist + 1, process.fork())]
            walk(EAST, x, y)
    raise ValueError('No path to oxygen system found')


instructions = list(map(int, input().split(',')))
print(step1(instructions))
