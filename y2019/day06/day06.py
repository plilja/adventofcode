import sys
from collections import defaultdict


def step1(inp):
    g = {}
    for a, b in inp:
        g[b] = a

    cache = {}

    def orbits(node):
        if node in cache:
            return cache[node]
        if g[node] == 'COM':
            return 1
        else:
            cache[node] = orbits(g[node]) + 1
            return cache[node]

    return sum([orbits(node) for node in g])


def step2(inp):
    g = defaultdict(list)
    for a, b in inp:
        g[b].append(a)
        g[a].append(b)

    q = ['YOU']
    dist = {'YOU': 0}
    while 'SAN' not in dist:
        n = q[0]
        q = q[1:]
        d = dist[n]
        for n2 in g[n]:
            if n2 not in dist:
                dist[n2] = d + 1
                q.append(n2)
    return dist['SAN'] - 2


def main():
    inp = [tuple(x.strip().split(')')) for x in sys.stdin]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()

