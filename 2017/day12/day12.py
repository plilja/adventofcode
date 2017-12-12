import re
import sys

def step1(g):
    visited = set()
    q = [0]
    while q:
        v = q[0]
        q = q[1:]
        if v in visited:
            continue
        visited |= {v}
        for v2 in g[v]:
            q += [v2]
    return len(visited)


def read_input():
    res = {}
    for s in sys.stdin:
        program, communicates_with = re.match(r'(\d+) <-> (.*)', s).groups()
        res[int(program)] = [int(i) for i in communicates_with.split(',')]
    return res

g = read_input()
print(step1(g))


