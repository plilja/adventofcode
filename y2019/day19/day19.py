from y2019.intcode import IntcodeProcess


def is_pulled(instructions, x, y):
    process = IntcodeProcess(instructions)
    process.add_input(x)
    process.add_input(y)
    process.run_until_complete()
    return process.pop_output() == 1


def step1(instructions):
    result = 0
    for y in range(0, 50):
        for x in range(0, 50):
            result += 1 if is_pulled(instructions, x, y) else 0
    return result


def find_slope(instructions):
    min_x = float('inf')
    max_x = 0
    for x in range(0, 100):
        if is_pulled(instructions, x, 50):
            min_x = min(min_x, x)
            max_x = max(max_x, x)
    dy = 1
    dx = (min_x + max_x) / 100
    return dx, dy


def step2(instructions):
    dx, dy = find_slope(instructions)

    def fits(top_y):
        y = top_y + 99
        x = int(y * dx)
        while is_pulled(instructions, x - 1, y):
            x -= 1
        if is_pulled(instructions, x + 99, top_y):
            return (x, top_y)
        else:
            return None

    assert(fits(5000))
    a = 100
    b = 5000
    while a < b:
        m = (a + b + 1) // 2
        t = fits(m)
        if t:
            b = m
        else:
            a = m + 1
    assert not fits(a - 1)
    x, y = fits(a)
    return 10000 * x + y


instructions = list(map(int, input().split(',')))
print(step1(instructions))
print(step2(instructions))
