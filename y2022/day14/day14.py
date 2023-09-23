import sys


def step1(paths):
    return simulate(paths)


def step2(paths):
    lowest = float('-inf')
    for path in paths:
        for x, y in path:
            lowest = max(lowest, y)
    return simulate(paths + [[(-10000, lowest + 2), (10000, lowest + 2)]])


def simulate(paths):
    # find lowest
    lowest = float('-inf')
    for path in paths:
        for x, y in path:
            lowest = max(lowest, y)

    # build grid
    grid = set()
    for path in paths:
        if len(path) == 1:
            grid.add(path[0])
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            dx = signum(x2 - x1)
            dy = signum(y2 - y1)
            x, y = x1, y1
            grid.add((x, y))
            while x != x2 or y != y2:
                x += dx
                y += dy
                grid.add((x, y))

    # simulate sand falling
    result = 0
    while True:
        x, y = 500, 0
        result += 1
        while y <= lowest:
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                break
        if (x, y) == (500, 0):
            return result
        if y > lowest:
            return result - 1
        grid.add((x, y))


def signum(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


def read_input():
    paths = []
    for line in sys.stdin:
        paths.append([])
        for rock in line.split(' -> '):
            [x, y] = rock.split(',')
            paths[-1].append((int(x), int(y)))
    return paths


def main():
    paths = read_input()
    print(step1(paths))
    print(step2(paths))


if __name__ == '__main__':
    main()
