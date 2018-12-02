import sys
from collections import *

def step1(inp):
    r = defaultdict(int)
    for line in inp:
        c = set(Counter(line).values())
        for i in c:
            r[i] += 1
    return r[2] * r[3]


inp = sys.stdin.readlines()
print(step1(inp))
