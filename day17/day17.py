import sys
from collections import defaultdict

TARGET = 150

def solve():
    containers = [int(s) for s in sys.stdin.readlines()]
    m = defaultdict(lambda: defaultdict(int))
    m[-1][0] = 1
    for i in range(0, len(containers)):
        c = containers[i]
        for j in range(0, TARGET + 1):
            m[i][j] = m[i - 1][j]
            if j >= c:
                m[i][j] += m[i - 1][j - c]
    return m[len(containers) - 1][TARGET]

print(solve())
