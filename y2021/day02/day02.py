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


def step2(inp):
    horizontal = 0
    depth = 0
    aim = 0
    for line in inp:
        command, i = line.split(' ')
        if command == 'forward':
            horizontal += int(i)
            depth += aim * int(i)
        if command == 'down':
            aim += int(i)
        if command == 'up':
            aim -= int(i)
    return horizontal * depth


def main():
    inp = sys.stdin.readlines()
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
