from y2019.intcode import IntcodeProcess


def run_program(program, first_input):
    process = IntcodeProcess(program)
    process.add_input(first_input)
    process.run_until_complete()
    return process.output[-1]


def step1(program):
    return run_program(program, 1)


def step2(program):
    return run_program(program, 5)


program = list(map(int, input().split(',')))
print(step1(program))
print(step2(program))
