from collections import defaultdict
from y2019.intcode import IntcodeProcess

TILE_TYPES = {0: ' ', 1: '#', 2: '^', 3: '-', 4: 'o'}


def step1(program):
    process = IntcodeProcess(program)
    process.run_until_complete()
    grid = defaultdict(lambda: defaultdict(int))
    for i in range(0, len(process.output), 3):
        x = process.output[i]
        y = process.output[i + 1]
        tile = process.output[i + 2]
        grid[y][x] = tile
    result = 0
    for y in grid.keys():
        result += sum([1 for x in grid[y].keys() if grid[y][x] == 2])
    return result


def find(grid, what):
    for y in grid.keys():
        for x in grid[y].keys():
            if grid[y][x] == what:
                return (x, y)


def step2(program):
    program_copy = program[::]
    program_copy[0] = 2
    process = IntcodeProcess(program_copy)
    grid = defaultdict(lambda: defaultdict(int))
    score = None
    while process.is_running():
        while process.is_running() and not process.needs_input() and len(process.output) < 3:
            process.tick()

        if len(process.output) >= 3:
            x = process.pop_output()
            y = process.pop_output()
            tile = process.pop_output()
            if (-1, 0) == (x, y): 
                score = tile
            else:
                grid[y][x] = tile

        if process.needs_input():
            # Keep paddle under ball at all times
            bx, _ = find(grid, 4)
            px, _ = find(grid, 3)
            if bx < px:
                process.add_input(-1)
            elif px == bx:
                process.add_input(0)
            else:
                process.add_input(1)
    return score


program = list(map(int, input().split(',')))
print(step1(program))
print(step2(program))
