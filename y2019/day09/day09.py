from collections import defaultdict
import sys
sys.path.append("..")
from intcode import IntcodeProcess


def run_program(inp, first_input):
    process = IntcodeProcess(inp)
    process.add_input(first_input)
    process.run_until_complete()
    return ''.join(map(str, process.output))


def step1(program):
    return run_program(program, 1)


def step2(program):
    return run_program(program, 2)


program = list(map(int, input().split(',')))
print(step1(program))
print(step2(program))
