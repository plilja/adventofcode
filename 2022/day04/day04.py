import sys
import re


def step1(inp):
    result = 0
    for (a1, a2), (b1, b2) in inp:
        if a1 <= b1 <= a2 and a1 <= b2 <= a2:
            result += 1
        elif b1 <= a1 <= b2 and b1 <= a2 <= b2:
            result += 1
    return result


def step2(inp):
    result = 0
    for (a1, a2), (b1, b2) in inp:
        if a1 <= b1 <= a2:
            result += 1
        elif b1 <= a1 <= b2:
            result += 1
    return result


def read_input():
    result = []
    for line in sys.stdin:
        [a1, a2, b1, b2] = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()
        result.append(((int(a1), int(a2)), (int(b1), int(b2))))
    return result


inp = read_input()
print(step1(inp))
print(step2(inp))
