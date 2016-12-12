import sys
from collections import *
from functools import partial

Machine = namedtuple('Machine', 'a b c d pc')

def step1(inp):
    instructions = parse_instructions(inp)
    m = execute(Machine(0, 0, 0, 0, 0), instructions)
    return m.a

def parse_instructions(inp):
    if not inp:
        return []
    else:
        xs = inp[0].strip().split()
        if xs[0] == 'cpy':
            return [lambda m : increment_pc(set_register(m, xs[2], register_or_constant(m, xs[1])))] + parse_instructions(inp[1:])
        elif xs[0] == 'inc':
            return [lambda m : increment_pc(set_register(m, xs[1], get_register(m, xs[1]) + 1))] + parse_instructions(inp[1:])
        elif xs[0] == 'dec':
            return [lambda m : increment_pc(set_register(m, xs[1], get_register(m, xs[1]) - 1))] + parse_instructions(inp[1:])
        elif xs[0] == 'jnz':
            return [lambda m : jump(m, register_or_constant(m, xs[1]), int(xs[2]))] + parse_instructions(inp[1:])
        else:
            raise ValueError('Unexpected instruction [%s]' % s)

def execute(machine, instructions):
    while machine.pc < len(instructions):
        instruction = instructions[machine.pc]
        machine = instruction(machine)
    return machine

def register_or_constant(machine, unknown):
    if unknown in ('a', 'b', 'c', 'd'):
        return get_register(machine, unknown)
    else:
        return int(unknown)

def increment_pc(machine):
    return Machine(machine.a, machine.b, machine.c, machine.d, machine.pc + 1)

def get_register(machine, register):
    if register == 'a':
        return machine.a
    if register == 'b':
        return machine.b
    if register == 'c':
        return machine.c
    if register == 'd':
        return machine.d
    raise ValueError('Unexpected register %s' % register)

def set_register(machine, register, value):
    if register == 'a':
        return Machine(value, machine.b, machine.c, machine.d, machine.pc)
    if register == 'b':
        return Machine(machine.a, value, machine.c, machine.d, machine.pc)
    if register == 'c':
        return Machine(machine.a, machine.b, value, machine.d, machine.pc)
    if register == 'd':
        return Machine(machine.a, machine.b, machine.c, value, machine.pc)
    raise ValueError('Unexpected register %s' % register)

def jump(machine, check, delta):
    if check == 0:
        return Machine(machine.a, machine.b, machine.c, machine.d, machine.pc + 1)
    else:
        return Machine(machine.a, machine.b, machine.c, machine.d, machine.pc + delta)

inp = sys.stdin.readlines()
print(step1(inp))
