import sys
from math import *

def solve(ip, instructions):
    seen_order = []
    seen = set()
    reg3, reg4, reg5 = 0, 0, 0
    start_from_top = True
    while True:
        if start_from_top:
            reg3 = reg4 | 65536
            reg4 = 10552971

        reg5 = reg3 & 255
        reg4 += reg5
        reg4 &= 16777215
        reg4 *= 65899
        reg4 &= 16777215
        if 256 > reg3:
            reg5 = 1
            if reg4 in seen:
                return seen_order[0], seen_order[-1]
            last_seen = reg4
            seen.add(reg4)
            seen_order.append(reg4)
            start_from_top = True
        else:
            # Loop between 18 and 25 ends when (reg5 + 1) * 256 > reg3
            reg5 = ceil((reg3 + 0.5) / 256) - 1
            reg3 = reg5
            start_from_top = False


def parse_input():
    instructions = []
    ip = None
    for s in sys.stdin:
        args = s.split()
        if args[0] == '#ip':
            ip = int(args[1])
        else:
            instructions += [[args[0]] + list(map(int, args[1:]))]
    return ip, instructions
        

ip, instructions = parse_input()
a, b = solve(ip, instructions)
print(a)
print(b)
