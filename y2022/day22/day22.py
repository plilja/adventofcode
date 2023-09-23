import sys
import re


def step1(grid, path):
    return solve(grid, path, deduce_next_pos_step1)


def step2(grid, path):
    m = calc_next_step_matrix_step2(grid)

    def next_pos(grid, x, y, dx, dy):
        x2, y2, dx2, dy2 = m[(x, y, dx, dy)]
        if grid[y2][x2] == '#':
            return (x, y, dx, dy)
        else:
            return (x2, y2, dx2, dy2)

    return solve(grid, path, next_pos)


def solve(grid, path, deduce_next_pos):
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
            assert '0' <= inst[0] <= '9'
            steps = int(inst)
            for i in range(0, steps):
                x2, y2, dx2, dy2 = deduce_next_pos(grid, x, y, dx, dy)
                if (x2, y2, dx2, dy2) == (x, y, dx, dy):
                    break
                else:
                    x, y, dx, dy = x2, y2, dx2, dy2
    return 4 * (x + 1) + 1000 * (y + 1) + facing_score(dx, dy)


def facing_score(dx, dy):
    return {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }[(dx, dy)]


def deduce_next_pos_step1(grid, x, y, dx, dy):
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
            x2 = len(grid[y2]) - 1
        elif dy > 0:
            y2 = 0
        else:
            assert dy < 0
            y2 = len(grid) - 1
        while len(grid[y2]) <= x2 or grid[y2][x2].isspace():
            x2 += dx
            y2 += dy
        if grid[y2][x2] == '#':
            return x, y, dx, dy
        else:
            assert grid[y2][x2] == '.'
            return x2, y2, dx, dy
    elif grid[y + dy][x + dx] == '#':
        return x, y, dx, dy
    else:
        return x + dx, y + dy, dx, dy


def calc_next_step_matrix_step2(grid):
    def seven_sides(x, y, dx, dy):
        if y == 0 and 50 <= x < 100 and dy < 0:
            x2 = 0
            y2 = 150 + x - 50
            dx2, dy2 = 1, 0
            return (x2, y2, dx2, dy2)
        elif y == 0 and dy < 0:
            assert 100 <= x < 150
            x2 = x - 100
            y2 = 199
            dx2, dy2 = 0, -1
            return (x2, y2, dx2, dy2)
        elif x == 50 and 0 <= y < 50 and dx < 0:
            x2 = 0
            y2 = 149 - y
            dx2, dy2 = 1, 0
            return (x2, y2, dx2, dy2)
        elif x == 50 and 50 <= y < 100 and dx < 0:
            x2 = y - 50
            y2 = 100
            dx2, dy2 = 0, 1
            return (x2, y2, dx2, dy2)
        elif y == 49 and 100 <= x < 150 and dy > 0:
            y2 = x - 50
            x2 = 99
            dx2, dy2 = -1, 0
            return (x2, y2, dx2, dy2)
        elif x == 149 and dx > 0:
            assert 0 <= y < 50
            x2 = 99
            y2 = 149 - y
            dx2, dy2 = -1, 0
            return (x2, y2, dx2, dy2)
        elif y == 149 and 50 <= x < 100 and dy > 0:
            x2 = 49
            y2 = 150 + x - 50
            dx2, dy2 = -1, 0
            return (x2, y2, dx2, dy2)
        else:
            return None

    m = {}
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x].isspace():
                continue
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                delta = seven_sides(x, y, dx, dy)
                if delta:
                    x2, y2, dx2, dy2 = delta
                    m[(x, y, dx, dy)] = delta
                    # Calculate inverse movement so that we don't
                    # have to implement if-else logic above for all
                    # 14 possible edge movements
                    m[(x2, y2, -dx2, -dy2)] = (x, y, -dx, -dy)
                    assert get_or_space(grid, x + dx, y + dy).isspace()
                    assert not get_or_space(grid, x2, y2).isspace()
                    assert not get_or_space(grid, x2 + dx2, y2 + dy2).isspace()
                    assert get_or_space(grid, x2 - dx2, y2 - dy2).isspace()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x].isspace():
                continue
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (x, y, dx, dy) not in m:
                    # Not on a border, just apply deltas
                    m[(x, y, dx, dy)] = (x + dx, y + dy, dx, dy)
    return m


def get_or_space(grid, x, y):
    if y < 0 or len(grid) <= y:
        return ' '
    if x < 0 or len(grid[y]) <= x:
        return ' '
    return grid[y][x]


def read_input():
    lines = sys.stdin.readlines()
    grid = [row for row in lines[:-2]]
    path = re.findall(r'(\d+|L|R)', lines[-1])
    return grid, path


if __name__ == '__main__':
    grid, path = read_input()
    print(step1(grid, path))
    print(step2(grid, path))
