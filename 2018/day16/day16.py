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



def step1(inp):
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
    def candidate(sample):
        c = 0
        for op in ops:
            if op(sample.before, sample.args[1:]) == sample.after:
                c += 1
        return c >= 3

    return len(list(filter(candidate, inp)))


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
    return samples

samples = parse_input()
print(step1(samples))
