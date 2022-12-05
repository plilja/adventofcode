import sys


def step1(inp):
    result = 0
    for line in inp:
        middle = len(line) // 2
        c1 = {c for c in line[:middle]}
        c2 = {c for c in line[middle:]}
        common = c1 & c2
        for c in common:
            if c.islower():
                prio = ord(c) - ord('a') + 1
                result += prio
            else:
                prio = ord(c) - ord('A') + 27
                result += prio
    return result


inp = [line.strip() for line in sys.stdin.readlines()]
print(step1(inp))
