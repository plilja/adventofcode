import sys

def opr(f):
    def op(registers, args):
        registers[args[2]] = f(registers[args[0]], registers[args[1]])
    return op


def opi(f):
    def op(registers, args):
        registers[args[2]] = f(registers[args[0]], args[1])
    return op


def opir(f):
    def op(registers, args):
        registers[args[2]] = f(args[0], registers[args[1]])
    return op


def setr(registers, args):
    registers[args[2]] = registers[args[0]]


def seti(registers, args):
    registers[args[2]] = args[0]


ops = {
        'addr': opr(lambda a, b: a + b),
        'addi': opi(lambda a, b: a + b),
        'mulr': opr(lambda a, b: a * b),
        'muli': opi(lambda a, b: a * b),
        'banr': opr(lambda a, b: a & b),
        'bani': opi(lambda a, b: a & b),
        'borr': opr(lambda a, b: a | b),
        'bori': opi(lambda a, b: a | b),
        'setr': setr,
        'seti': seti,
        'gtrr': opr(lambda a, b: 1 if a > b else 0),
        'gtri': opi(lambda a, b: 1 if a > b else 0),
        'gtir': opir(lambda a, b: 1 if a > b else 0),
        'eqrr': opr(lambda a, b: 1 if a == b else 0),
        'eqri': opi(lambda a, b: 1 if a == b else 0),
        'eqir': opir(lambda a, b: 1 if a == b else 0)
        }


def step1(ip, instructions):
    registers = [0, 0, 0, 0, 0, 0]
    while 0 <= registers[ip] < len(instructions):
        instruction = instructions[registers[ip]]
        op = ops[instruction[0]]
        op(registers, instruction[1:])
        if registers[ip] + 1 >= len(instructions):
            break
        registers[ip] += 1
    return registers[0]


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
print(step1(ip, instructions))
