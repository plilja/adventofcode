from common.util import cycle_with_idx


SHAPES = [
    ['####'],

    ['.#.',
     '###',
     '.#.'],

    ['..#',
     '..#',
     '###'],

    ['#',
     '#',
     '#',
     '#'],

    ['##',
     '##']]

WIDTH = 7


def step1(jet_stream):
    return solve(jet_stream, 2022)


def step2(jet_stream):
    return solve(jet_stream, 1000000000000)


def solve(jet_stream, iterations):
    grid = {}
    skylines = {}
    highest = 0
    next_shape = cycle_with_idx(SHAPES)
    next_jet = cycle_with_idx(jet_stream)
    cycle_offset = 0
    i = 0
    while i < iterations:
        shape, idx = next_shape()
        shape_height = len(shape)
        shape_width = len(shape[0])
        y = highest + 3
        x = 2
        for y2 in range(y + shape_height - 1, -1, -1):
            if y2 in grid:
                break
            grid[y2] = {}
            for x2 in range(0, WIDTH):
                grid[y2][x2] = False
            grid[y2][-1] = True
            grid[y2][WIDTH] = True
        while True:
            direction, jet_idx = next_jet()
            direction_dx = -1 if direction == '<' else 1
            if can_move(shape, grid, x + direction_dx, y):
                x += direction_dx

            if y == 0 or not can_move(shape, grid, x, y - 1):
                break
            else:
                y -= 1
        for dy in range(0, shape_height):
            for dx in range(0, shape_width):
                if shape[dy][dx] == '#':
                    grid[y - dy + shape_height - 1][x + dx] = True
        highest = max(highest, y + shape_height)
        skyline = get_skyline(grid, highest)
        key = (skyline, idx, jet_idx)
        if key in skylines and cycle_offset == 0:
            prev_highest, prev_idx, jet_idx = skylines[key]
            diff = i - prev_idx
            height_diff = highest - prev_highest
            rem = iterations - i - 1
            cycles = rem // diff
            cycle_offset = cycles * height_diff
            i += cycles * diff
        skylines[key] = (highest, i, jet_idx)
        i += 1
    return highest + cycle_offset


def can_move(shape, grid, x, y):
    shape_height = len(shape)
    shape_width = len(shape[0])
    for dy in range(0, shape_height):
        for dx in range(0, shape_width):
            if shape[shape_height - dy - 1][dx] == '#' and grid[y + dy][x + dx]:
                return False
    return True


def get_skyline(grid, highest):
    res = []
    for x in range(0, WIDTH):
        for y in range(highest, -1, -1):
            if y == 0 or grid[y][x]:
                res.append(y)
                break
    lowest = min(res)
    for i in range(0, WIDTH):
        res[i] -= lowest
    return tuple(res)


jet_stream = input()
print(step1(jet_stream))
print(step2(jet_stream))
