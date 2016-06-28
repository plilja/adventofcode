import sys
from collections import defaultdict


g = defaultdict(dict)
for s in sys.stdin.readlines():
    [fr, foo, to, eq, dist] = s.split()
    g[fr][to] = int(dist)
    g[to][fr] = int(dist)


def h():
    INF = 1
    for a in g.values():
        for v in a.values():
            INF += v

    def f(i, v = set()):
        if len(v) == len(g):
            return 0
        r = INF
        for j in g[i].keys():
            if j not in v:
                r = min(r, f(j, v | {j}) + g[i][j])
        return r

    r = INF
    for i in g:
        r = min(r, f(i, {i}))

    return r


print(h())
