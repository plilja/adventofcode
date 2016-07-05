import sys

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

def solve():
    def read_input():
        sues = {}
        for s in sys.stdin.readlines():
            args = s.replace(':', '').replace(',', '').split()
            nr = int(args[1])
            sues[nr] = {}
            for i in range(2, len(args), 2):
                sues[nr][args[i]] = int(args[i + 1])
        return sues

    def f(sues):
        for k in sues.keys():
            match = True
            for (a, v) in sues[k].items():
                if clues[a] != v:
                    match = False
            if match:
                return k

    return f(read_input())

print(solve())
