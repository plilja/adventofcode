from collections import defaultdict
from y2019.intcode import IntcodeProcess


def paint(program, canvas):
    process = IntcodeProcess(program)
    x, y = 0, 0
    dx, dy = 0, -1
    painted_at_least_once = set()
    while process.is_running():
        while process.is_running() and not process.needs_input():
            process.tick()
        if process.has_output():
            color = process.pop_output()
            canvas[y][x] = color
            painted_at_least_once |= {(x, y)}
            assert process.has_output()
            turn = process.pop_output()
            if turn == 0:  # left
                dx, dy = dy, -dx
            else:  # right
                dx, dy = -dy, dx
            x += dx
            y += dy
        if process.needs_input():
            process.add_input(canvas[y][x])

    return len(painted_at_least_once)


def step1(program):
    canvas = defaultdict(lambda: defaultdict(int))
    return paint(program, canvas)


def step2(program):
    canvas = defaultdict(lambda: defaultdict(int))
    canvas[0][0] = 1
    paint(program, canvas)
    min_y = min(canvas.keys())
    max_y = max(canvas.keys())
    min_x = min([min(canvas[i].keys()) for i in canvas.keys()])
    max_x = max([max(canvas[i].keys()) for i in canvas.keys()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print('#' if canvas[y][x] == 1 else ' ', end='')
        print()


program = list(map(int, input().split(',')))
print(step1(program))
step2(program)
