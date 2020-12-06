import sys
from collections import Counter


def step1(inp):
    result = 0
    group = Counter()
    for line in inp:
        if not line:
            result += len(group)
            group = Counter()
        else:
            group += Counter(line)
    result += len(group)
    return result


inp = [line.strip() for line in sys.stdin.readlines()]
print(step1(inp))
