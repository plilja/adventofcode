import sys
sys.path.append("..")
from collections import defaultdict
from intcode import IntcodeProcess


def step1(instructions):
    result = 0
    for y in range(0, 50):
        for x in range(0, 50):
            process = IntcodeProcess(instructions)
            process.add_input(x)
            process.add_input(y)
            process.run_until_complete()
            result += process.pop_output()
    return result


instructions = list(map(int, input().split(',')))
print(step1(instructions))
