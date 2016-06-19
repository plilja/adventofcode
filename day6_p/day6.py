from collections import defaultdict
import sys

grid = defaultdict(lambda : defaultdict(int))

def transform(y1, x1, y2, x2, f):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            grid[y][x] = f(grid[y][x])


def coord(s):
    [y, x] = s.split(',')
    return (int(y), int(x))


for inp in sys.stdin.readlines():
    args = inp.split()
    if args[0] == 'toggle':
        [y1, x1] = coord(args[1])
        [y2, x2] = coord(args[3])
        transform(y1, x1, y2, x2, lambda x : (x + 1) % 2)
    else:
        [y1, x1] = coord(args[2])
        [y2, x2] = coord(args[4])
        if args[1] == 'on':
            transform(y1, x1, y2, x2, lambda x : 1)
        else:
            transform(y1, x1, y2, x2, lambda x : 0)

ans = 0
for y in range(0, 1000):
    for x in range(0, 1000):
        ans += grid[y][x]

print(ans)
