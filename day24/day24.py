import sys
from math import *

INF = float('inf')

def solve(packages):
    packages.sort()
    n = len(packages)
    target = floor(sum(packages) / 3)
    def g(x, i, used):
        if x == 0:
            return True
        if x < 0:
            return False
        for j in range(i, n):
            if j in used:
                continue
            p = packages[j]
            if p > x:
                break
            if g(x - p, j + 1, used):
                return True
        return False

    def f(x, c, i, used):
        if c == 0:
            if x == 0 and g(target, 0, used):
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
            used.add(p)
            (a, b) = f(x - p, c - 1, j + 1, used)
            used.remove(p)
            a += 1
            b *= p
            if a < ans or (a == ans and b < ent):
                ans = a
                ent = b
        return (ans, ent)

    for c in range(1, floor(n / 3) + 1):
        s = set()
        (a, b) = f(target, c, 0, s)
        if a < INF:
            return b

    return INF

packages = list(map(int, sys.stdin.readlines()))
print(solve(packages))
