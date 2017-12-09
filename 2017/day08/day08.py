import sys
from collections import defaultdict


def step1(inp):
    registers = defaultdict(int)
    for row in inp:
        [reg1, op, val, _if, reg2, comp, comp_val] = row.split()
        reg2_val = registers[reg2]
        if comp == '>':
            b = reg2_val > int(comp_val)
        elif comp == '<':
            b = reg2_val < int(comp_val)
        elif comp == '>=':
            b = reg2_val >= int(comp_val)
        elif comp == '<=':
            b = reg2_val <= int(comp_val)
        elif comp == '==':
            b = reg2_val == int(comp_val)
        elif comp == '!=':
            b = reg2_val != int(comp_val)
        else:
            raise ValueError('Unknown comparison ' + comp)

        if b:
            if op == 'inc':
                registers[reg1] += int(val)
            elif op == 'dec':
                registers[reg1] -= int(val)
            else:
                raise ValueError('Unknown operation ' + op)
    return max(registers.items(), key=lambda x: x[1])[1]


inp = sys.stdin.readlines()
print(step1(inp))
