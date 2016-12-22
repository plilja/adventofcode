import sys
from collections import namedtuple


Node = namedtuple('Node', 'x y size used avail')


def step1(inp):
    nodes = []
    for [node, size, used, avail, percentage] in map(str.split, inp):
        [x_str, y_str] = node[node.index('-') + 1:].split('-')
        x = int(x_str[1:])
        y = int(y_str[1:])
        size = int(size[:-1])
        used = int(used[:-1])
        avail = size - used
        nodes += [Node(x, y, size, used, avail)]
    r = 0
    for n1 in nodes:
        for n2 in nodes:
            if n1 == n2:
                continue
            if n1.used > 0 and n2.avail >= n1.used:
                r += 1
    return r


input() # skip
input() # skip
df = sys.stdin.readlines()
print(step1(df))
