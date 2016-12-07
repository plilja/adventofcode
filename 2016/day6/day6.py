from collections import Counter
import sys

def step1(inp):
    counters = [Counter() for i in range(0, len(inp[0]))]
    for line in inp:
        for i in range(0, len(line)):
            counters[i][line[i]] += 1
    ans = ''
    for c in counters:
        ans += c.most_common(1)[0][0]
    return ans

inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
