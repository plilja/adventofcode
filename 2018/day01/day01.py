import sys

def step1(rows):
    return sum(rows)


def step2(rows):
    i = 0
    f = 0
    v = set()
    while f not in v:
        v |= {f}
        f += rows[i]
        i = (i + 1) % len(rows)
    return f


inp = list(map(int, sys.stdin.readlines()))
print(step1(inp))
print(step2(inp))
