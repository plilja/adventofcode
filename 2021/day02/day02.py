import sys


def step1(inp):
    horizontal = 0
    depth = 0
    for line in inp:
        command, i = line.split(' ')
        if command == 'forward':
            horizontal += int(i)
        if command == 'down':
            depth += int(i)
        if command == 'up':
            depth -= int(i)
    return horizontal * depth


inp = sys.stdin.readlines()
print(step1(inp))
