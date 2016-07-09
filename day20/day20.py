from math import *
from array import *

def solve(n, lim = 10000):
    arr = array('i', [10 for i in range(0, lim + 1)])

    for i in range(2, lim):
        q = floor(lim / i)
        for j in range(1, q + 1):
            arr[j * i] += 10 * i

    for i in range(1, lim):
        if arr[i] >= n:
            return i

    # didn't find solution, try increasing limit
    return solve(n, lim * 2)

n = int(input())
a = solve(n)
print(a)
