import sys

sys.path.append("../..")
from common.util import cycle

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


def can_move(shape, grid, x, y):
    shape_height = len(shape)
    shape_width = len(shape[0])
    for dy in range(0, shape_height):
        for dx in range(0, shape_width):
            if shape[shape_height - dy - 1][dx] == '#' and grid[y + dy][x + dx]:
                return False
    return True


def step1(jet_stream):
    grid = {}

    highest = 0
    next_shape = cycle(SHAPES)
    next_jet = cycle(jet_stream)
    for i in range(0, 2022):
        shape = next_shape()
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
            direction = -1 if next_jet() == '<' else 1
            if can_move(shape, grid, x + direction, y):
                x += direction

            if y == 0 or not can_move(shape, grid, x, y - 1):
                break
            else:
                y -= 1
        for dy in range(0, shape_height):
            for dx in range(0, shape_width):
                if shape[dy][dx] == '#':
                    grid[y - dy + shape_height - 1][x + dx] = True
        highest = max(highest, y + shape_height)
    return highest


jet_stream = input()
print(step1(jet_stream))
