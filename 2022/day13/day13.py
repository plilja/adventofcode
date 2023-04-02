import sys
import re


def step1(inp):
    result = 0
    for i in range(0, len(inp)):
        x, y = inp[i]
        t = compare_to(x, y)
        if t <= 0:
            result += i + 1
    return result


def compare_to(x, y):
    if isinstance(x, list) and isinstance(y, list):
        if len(x) == 0 or len(y) == 0:
            return len(x) - len(y)
        t = compare_to(x[0], y[0])
        if t == 0:
            return compare_to(x[1:], y[1:])
        else:
            return t
    elif isinstance(x, int) and isinstance(y, int):
        return x - y
    elif isinstance(x, list) and isinstance(y, int):
        return compare_to(x, [y])
    else:
        assert isinstance(x, int) and isinstance(y, list)
        return compare_to([x], y)


def read_input():
    result = []
    lines = sys.stdin.readlines()
    for i in range(0, len(lines), 3):
        result.append((parse(lines[i].strip()), parse(lines[i + 1].strip())))
    return result


def parse(line):
    if not re.match('^[\\[\\],0-9]+$', line):
        raise ValueError("expected input to only contain brackets numbers and commas, got " + line)
    return eval(line)


inp = read_input()
print(step1(inp))
