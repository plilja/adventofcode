import sys
sys.path.append("..")
from collections import defaultdict
from intcode import IntcodeProcess


def enter(process, command):
    for c in command:
        process.add_input(ord(c))
    process.add_input(ord('\n'))


def step1(instructions):
    process = IntcodeProcess(instructions)
    enter(process, 'NOT C T')
    enter(process, 'NOT B J')
    enter(process, 'OR T J')
    enter(process, 'NOT A T')
    enter(process, 'OR T J')
    enter(process, 'OR D T')  # Do we have ground 4 away?
    enter(process, 'AND T J')  # Do we have ground 4 away and a reason to jump?
    enter(process, 'WALK')
    process.run_until_complete()
    return process.output[-1]


instructions = list(map(int, input().split(',')))
print(step1(instructions))
