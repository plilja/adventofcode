import sys
from math import *

INF = float('inf')

def solve(packages, groups):
    packages.sort()
    n = len(packages)
    target = floor(sum(packages) / groups)

    def g(x, i, used, gr):
        if x == 0:
            if gr == 1:
                return True
            else:
                return g(target, 0, used, gr - 1)
        if x < 0:
            return False
        for j in range(i, n):
            if j in used:
                continue
            p = packages[j]
            if p > x:
                break
            used.add(j)
            t = g(x - p, j + 1, used, gr)
            used.remove(j)
            if t:
                return True
        return False

    def f(x, c, i, used):
        if c == 0:
            if x == 0 and g(target, 0, used, groups - 1):
                return (0, 1)
            else:
                return (INF, INF)

        ans = INF
        ent = INF
        for j in range(i, n):
            if j in used:
                continue
            p = packages[j]
            if p > x:
                break
            used.add(j)
            (a, b) = f(x - p, c - 1, j + 1, used)
            used.remove(j)
            a += 1
            b *= p
            if a < ans or (a == ans and b < ent):
                ans = a
                ent = b
        return (ans, ent)

    for c in range(1, floor(n / groups) + 1):
        s = set()
        (a, b) = f(target, c, 0, s)
        if a < INF:
            return b

    return INF

packages = list(map(int, sys.stdin.readlines()))
print(solve(packages, 3))
print(solve(packages, 4))
