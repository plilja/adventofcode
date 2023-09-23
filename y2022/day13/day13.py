import sys
import re
from functools import cmp_to_key


def step1(inp):
    result = 0
    for i in range(0, len(inp), 2):
        x = inp[i]
        y = inp[i + 1]
        t = compare_to(x, y)
        if t <= 0:
            result += i // 2 + 1
    return result


def step2(inp):
    inp_copy = inp
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    inp_copy.append(divider_packet1)
    inp_copy.append(divider_packet2)
    inp.sort(key=cmp_to_key(compare_to))
    idx1 = inp_copy.index(divider_packet1) + 1
    idx2 = inp_copy.index(divider_packet2) + 1
    return idx1 * idx2


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
        result.append(parse(lines[i].strip()))
        result.append(parse(lines[i + 1].strip()))
    return result


def parse(line):
    if not re.match('^[\\[\\],0-9]+$', line):
        raise ValueError("expected input to only contain brackets numbers and commas, got " + line)
    return eval(line)


def main():
    inp = read_input()
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
