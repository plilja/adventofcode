import re
import sys
from collections import namedtuple


Program = namedtuple('Program', 'name children weight')


def read_input():
    programs = []
    for line in sys.stdin.readlines():
        program, weight, rest = re.match(r'(.+) \((\d+)\)(.*)', line).groups()
        if '->' in rest:
            children = rest[4:].strip().split(', ')
        else:
            children = []
        programs += [Program(program, children, int(weight))]
    return programs


def step1(programs):
    all_names = set()
    children_names = set()
    for program in programs:
        all_names |= {program.name}
        for child in program.children:
            children_names |= {child}
    return list(all_names - children_names)[0]


programs = read_input()
print(step1(programs))
