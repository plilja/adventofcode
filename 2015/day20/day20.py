from array import *
from math import *

INF = 10 ** 10


def solve(n, m, fact, lim=10000):
    arr = array('i', [10 for i in range(0, lim + 1)])

    for i in range(2, lim):
        q = min(m, floor(lim / i))
        for j in range(1, q + 1):
            arr[j * i] += fact * i

    for i in range(1, lim):
        if arr[i] >= n:
            return i

    # didn't find solution, try increasing limit
    return solve(n, m, fact, 2 * lim)


n = int(input())
a = solve(n, INF, 10)
print(a)
b = solve(n, 50, 11)
print(b)
