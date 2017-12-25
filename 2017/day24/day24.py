import sys
from collections import defaultdict

def step1(inp):
    def f(components, connector, cache):
        key = (components, connector)
        if key in cache:
            return cache[key]
        else:
            ans = 0
            for c in components:
                a, b = c
                if a == connector:
                    ans = max(ans, a + b + f(components - {c}, b, cache))
                if b == connector:
                    ans = max(ans, a + b + f(components - {c}, a, cache))
            cache[key] = ans
            return ans

    components = frozenset()
    for c in inp:
        assert(c not in components)
        components = components | {c}
    return f(components, 0, {})


def get_input():
    res = []
    for s in sys.stdin:
        [a, b] = list(map(int, s.strip().split('/')))
        res += [(a, b)]
    return res

inp = get_input()
print(step1(inp))

