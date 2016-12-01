import sys
from collections import defaultdict
from copy import copy

clues = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1}


def solve(sues, predicates):
    for k in sues.keys():
        match = True
        for (a, v) in sues[k].items():
            if not predicates[a](clues[a], v):
                match = False
        if match:
            return k


def read_input():
    sues = {}
    for s in sys.stdin.readlines():
        args = s.replace(':', '').replace(',', '').split()
        nr = int(args[1])
        sues[nr] = {}
        for i in range(2, len(args), 2):
            sues[nr][args[i]] = int(args[i + 1])
    return sues


inp = read_input()

step1 = defaultdict(lambda: lambda x, y: x == y)
print(solve(inp, step1))

step2 = copy(step1) 
step2['cats'] = lambda x, y : x < y
step2['trees'] = lambda x, y : x < y
step2['pomeranians'] = lambda x, y : x > y
step2['goldfish'] = lambda x, y : x > y
print(solve(inp, step2))
