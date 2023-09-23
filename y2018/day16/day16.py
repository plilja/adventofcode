import sys
import re
from collections import namedtuple

Sample = namedtuple('Sample', 'before args after')


def is_reg(*args):
    r = True
    for arg in args:
        r = r and (0 <= arg <= 3)
    return r


def opr(f):
    def op(registers, args):
        if is_reg(args[0], args[1], args[2]):
            res = registers[::]
            res[args[2]] = f(registers[args[0]], registers[args[1]])
            return res
        else:
            return None
    return op


def opi(f):
    def op(registers, args):
        if is_reg(args[0], args[2]):
            res = registers[::]
            res[args[2]] = f(registers[args[0]], args[1])
            return res
        else:
            return None
    return op


def opir(f):
    def op(registers, args):
        if is_reg(args[1], args[2]):
            res = registers[::]
            res[args[2]] = f(args[0], registers[args[1]])
            return res
        else:
            return None
    return op


def setr(registers, args):
    if is_reg(args[0], args[2]):
        res = registers[::]
        res[args[2]] = registers[args[0]]
        return res
    else:
        return None


def seti(registers, args):
    if is_reg(args[2]):
        res = registers[::]
        res[args[2]] = args[0]
        return res
    else:
        return None


ops = [
    opr(lambda a, b: a + b),
    opi(lambda a, b: a + b),
    opr(lambda a, b: a * b),
    opi(lambda a, b: a * b),
    opr(lambda a, b: a & b),
    opi(lambda a, b: a & b),
    opr(lambda a, b: a | b),
    opi(lambda a, b: a | b),
    setr,
    seti,
    opr(lambda a, b: 1 if a > b else 0),
    opi(lambda a, b: 1 if a > b else 0),
    opir(lambda a, b: 1 if a > b else 0),
    opr(lambda a, b: 1 if a == b else 0),
    opi(lambda a, b: 1 if a == b else 0),
    opir(lambda a, b: 1 if a == b else 0)
]


def step1(samples):
    def candidate(sample):
        c = 0
        for op in ops:
            if op(sample.before, sample.args[1:]) == sample.after:
                c += 1
        return c >= 3
    return len(list(filter(candidate, samples)))


def step2(samples, program):
    opcodes = {i: list(range(0, len(ops))) for i in range(0, len(ops))}
    # Determine impossible opcode mappings from sample observations
    for sample in samples:
        xs = opcodes[sample.args[0]]
        rem = []
        for o in xs:
            op = ops[o]
            if op(sample.before, sample.args[1:]) != sample.after:
                rem.append(o)
        for r in rem:
            xs.remove(r)

    # From previous step, use uniquely determined opcodes to further narrow down opcodes.
    # For example if previous step determined that opcode 2 is addr, then opcode 3 can't also be addr.
    unstable = True
    while unstable:
        unstable = False
        determined = []
        for i, xs in opcodes.items():
            if len(xs) == 1:
                determined.append((i, xs[0]))
        for i, o in determined:
            for j, xs in opcodes.items():
                if i != j:
                    if o in xs:
                        unstable = True
                        xs.remove(o)
    for v in opcodes.values():
        assert(len(v) == 1)

    # Run program
    state = [0, 0, 0, 0]
    for instr in program:
        op = ops[opcodes[instr[0]][0]]
        state = op(state, instr[1:])
    return state[0]


def parse_input():
    def ints(s):
        return [int(i) for i in re.findall(r'\d+', s)]

    samples = []
    inp = sys.stdin.readlines()
    i = 0
    while i < len(inp) and 'Before' in inp[i]:
        a, b, c = list(map(ints, inp[i:i+3]))
        samples.append(Sample(a, b, c))
        i += 4
    program = list(filter(lambda s: len(s) > 0, map(ints, inp[i:])))
    return samples, program


samples, program = parse_input()
print(step1(samples))
print(step2(samples, program))

