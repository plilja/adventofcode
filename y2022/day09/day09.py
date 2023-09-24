import sys

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1)
}


def step1(inp):
    return snake(inp, 2)


def step2(inp):
    return snake(inp, 10)


def snake(inp, ropelen):
    rope = [[0, 0] for _ in range(0, ropelen)]
    visited = set()
    for directory, steps in inp:
        dx, dy = dirs[directory]
        for _ in range(0, steps):
            rope[0][0] += dx
            rope[0][1] += dy
            for i in range(1, ropelen):
                if abs(rope[i - 1][0] - rope[i][0]) > 1 or abs(rope[i - 1][1] - rope[i][1]) > 1:
                    dx2 = signum(rope[i - 1][0] - rope[i][0])
                    dy2 = signum(rope[i - 1][1] - rope[i][1])
                    rope[i][0] += dx2
                    rope[i][1] += dy2
            visited.add(tuple(rope[-1]))
    return len(visited)


def signum(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


def main():
    inp = [(x.split()[0], int(x.split()[1])) for x in sys.stdin]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
