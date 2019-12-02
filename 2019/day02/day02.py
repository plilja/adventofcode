def run_program(program):
    position = 0
    while program[position] != 99:
        op = program[position]
        arg1 = program[program[position + 1]]
        arg2 = program[program[position + 2]]
        target = program[position + 3]
        if op == 1:
            program[target] = arg1 + arg2
        else:
            assert op == 2
            program[target] = arg1 * arg2
        position += 4

    return program[0]


def step1(program):
    program_copy = program[::]
    program_copy[1] = 12
    program_copy[2] = 2
    return run_program(program_copy)


def step2(program):
    for noun in range(0, 100):
        for verb in range(0, 100):
            program_copy = program[::]
            program_copy[1] = noun
            program_copy[2] = verb
            result = run_program(program_copy)
            if result == 19690720:
                return 100 * noun + verb
    raise ValueError('No solution found')


program = list(map(int, input().split(',')))
print(step1(program))
print(step2(program))
