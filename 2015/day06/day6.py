import sys
from collections import defaultdict


def solve(lines, toggle, turn_on, turn_off):
    grid = defaultdict(lambda: defaultdict(int))

    def transform(y1, x1, y2, x2, f):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                grid[y][x] = f(grid[y][x])

    def coord(s):
        [y, x] = s.split(',')
        return (int(y), int(x))

    for inp in lines:
        args = inp.split()
        if args[0] == 'toggle':
            [y1, x1] = coord(args[1])
            [y2, x2] = coord(args[3])
            transform(y1, x1, y2, x2, toggle)
        else:
            [y1, x1] = coord(args[2])
            [y2, x2] = coord(args[4])
            if args[1] == 'on':
                transform(y1, x1, y2, x2, turn_on)
            else:
                transform(y1, x1, y2, x2, turn_off)

    ans = 0
    for y in range(0, 1000):
        for x in range(0, 1000):
            ans += grid[y][x]
    return ans


lines = sys.stdin.readlines()
print(solve(lines, lambda x: (x + 1) % 2, lambda x: 1, lambda x: 0))
print(solve(lines, lambda x: x + 2, lambda x: x + 1, lambda x: max(0, x - 1)))
