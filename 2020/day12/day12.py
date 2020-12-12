import sys


def step1(instructions):
    x, y = 0, 0
    dx, dy = 1, 0  # starts east
    for instruction in instructions:
        d = instruction[0]
        n = int(instruction[1:])
        if d == 'F':
            x += dx * n
            y += dy * n
        elif d == 'N':
            y -= n  # unintuitively north means decreasing y
        elif d == 'S':
            y += n
        elif d == 'E':
            x += n
        elif d == 'W':
            x -= n
        elif d == 'L':
            for i in range(0, n // 90):
                dx, dy = dy, -dx
        else:
            assert d == 'R'
            for i in range(0, n // 90):
                dx, dy = -dy, dx
    return abs(x) + abs(y)


instructions = [x.strip() for x in sys.stdin]
print(step1(instructions))
