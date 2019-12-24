import sys
sys.path.append("..")
from collections import defaultdict
from intcode import IntcodeProcess

deltas = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]


def step1(instructions):
    process = IntcodeProcess(instructions)
    process.run_until_complete()
    space = defaultdict(lambda: defaultdict(lambda: '.'))
    x = 0
    y = 0
    while process.has_output():
        o = process.pop_output()
        if o == 10:
            x = 0
            y += 1
        else:
            space[y][x] = chr(o)
            x += 1
    result = 0
    for y in list(space.keys()):
        for x in list(space[y].keys()):
            if all([space[y + dy][x + dx] == '#' for dx, dy in deltas]):
                result += x * y
    return result


instructions = list(map(int, input().split(',')))
print(step1(instructions))
