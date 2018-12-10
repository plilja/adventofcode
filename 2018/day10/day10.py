import sys
import re
from collections import defaultdict

def bounds(inp):
    min_x = min([point[0] for point in inp])
    max_x = max([point[0] for point in inp])
    min_y = min([point[1] for point in inp])
    max_y = max([point[1] for point in inp])
    return (min_x, max_x, min_y, max_y)


def print_matrix(inp):
    grid = defaultdict(lambda: defaultdict(lambda: '.'))
    for point in inp:
        grid[point[1]][point[0]] = '#'
    min_x, max_x, min_y, max_y = bounds(inp)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[y][x], end='')
        print()
    print()


def step1(inp, iterations):
    prev = None
    curr = [point[::] for point in inp] # copy to ensure original list in not modified
    res = None
    res_size = float('inf')
    for i in range(0, iterations):
        min_x, max_x, min_y, max_y = bounds(curr)
        t = max_x - min_x + max_y - min_y
        if t < res_size:
            res = [point[::] for point in curr]
            res_size = t
        for point in curr:
            point[0] += point[2]
            point[1] += point[3]
        prev = t
    print_matrix(res)

def parse_inp():
    res = []
    for s in sys.stdin:
        x, y, dx, dy = list(map(int, re.findall(r'-?\d+', s)))
        res += [[x, y, dx, dy]]
    return res

inp = parse_inp()
step1(inp, 15000)
