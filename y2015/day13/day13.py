import sys
from collections import defaultdict
from copy import copy


def read_input():
    g = defaultdict(dict)
    for s in sys.stdin.readlines():
        [a, would, rel, amount, happiness, units, by, sitting, _next, to, b] = s.split()
        b = b[:-1]
        if rel == 'gain':
            g[a][b] = int(amount)
        else:
            g[a][b] = -int(amount)
    return g


def step1(g):
    def f(people, seating=[]):
        if len(people) == 0:
            r = 0
            for (a, b) in zip(seating, [seating[-1]] + seating[:-1]):
                r += g[a][b]
                r += g[b][a]
            return r
        r = -float('inf')
        for p in people:
            r = max(r, f(people - {p}, seating + [p]))
        return r

    return f(set([p for p in g.keys()]))


def step2(g):
    g_ = copy(g)
    for p in g.keys():
        g_[p]['me'] = 0
        g_['me'][p] = 0
    return step1(g_)


def main():
    g = read_input()
    print(step1(g))
    print(step2(g))


if __name__ == '__main__':
    main()
