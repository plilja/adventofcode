import sys


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


inp = [tuple(x.strip().split(')')) for x in sys.stdin]
print(step1(inp))
