import sys
import re


def step1(grid, path):
    dx, dy = 1, 0
    y = 0
    for i in range(0, len(grid[0])):
        if grid[0][i] == '.':
            x = i
            break
    assert grid[y][x] == '.'
    for inst in path:
        if inst == 'R':
            dx, dy = -dy, dx
        elif inst == 'L':
            dx, dy = dy, -dx
        else:
            assert inst[0] >= '0' and inst[0] <= '9'
            steps = int(inst)
            for i in range(0, steps):
                x2, y2 = deduce_next_pos(grid, x, y, dx, dy)
                if (x2, y2) == (x, y):
                    break
                else:
                    x, y = x2, y2
    return (x + 1) * 4 + (y + 1) * 1000 + facing_score(dx, dy)


def facing_score(dx, dy):
    return {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }[(dx, dy)]


def deduce_next_pos(grid, x, y, dx, dy):
    if x + dx < 0 \
            or x + dx >= len(grid[y]) \
            or y + dy < 0 \
            or y + dy >= len(grid) \
            or len(grid[y + dy]) <= x + dx \
            or grid[y + dy][x + dx].isspace():
        x2, y2 = x, y
        if dx > 0:
            x2 = 0
        elif dx < 0:
            x2 = len(grid[y]) - 1
        elif dy > 0:
            y2 = 0
        else:
            assert dy < 0
            y2 = len(grid) - 1
        while len(grid[y2]) <= x2 or grid[y2][x2].isspace():
            x2 += dx
            y2 += dy
        if grid[y2][x2] == '#':
            return x, y
        else:
            assert grid[y2][x2] == '.'
            return x2, y2
    elif grid[y + dy][x + dx] == '#':
        return x, y
    else:
        return x + dx, y + dy


def read_input():
    lines = sys.stdin.readlines()
    grid = [row for row in lines[:-2]]
    path = re.findall(r'(\d+|L|R)', lines[-1])
    return grid, path


if __name__ == '__main__':
    grid, path = read_input()
    print(step1(grid, path))
