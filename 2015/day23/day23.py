import sys
from math import floor

def run(a, b, instructions, pointer):
    while pointer < len(instructions):
        arg = instructions[pointer]
        if arg[0] in ['hlf', 'tpl', 'inc']:
            if arg[0] == 'hlf':
                op = lambda x : floor(x / 2)
            elif arg[0] == 'tpl':
                op = lambda x : 3 * x
            else:
                assert arg[0] == 'inc'
                op = lambda x : x + 1
            if arg[1] == 'a':
                a = op(a)
            else:
                assert arg[1] == 'b'
                b = op(b)
            pointer += 1
        elif arg[0] == 'jmp':
            pointer += int(arg[1])
        else:
            assert arg[0] in ['jie', 'jio']
            if arg[0] == 'jie':
                pred = lambda x : x % 2 == 0
            else:
                assert arg[0] == 'jio'
                pred = lambda x : x == 1
            if arg[1] == 'a':
                jump = pred(a)
            else:
                assert arg[1] == 'b'
                jump = pred(b)
            if jump:
                pointer += int(arg[2])
            else:
                pointer += 1
    return (a, b)

instructions = [s.replace(',', '').split() for s in sys.stdin.readlines()]
print(run(0, 0, instructions, 0)[1])
print(run(1, 0, instructions, 0)[1])
