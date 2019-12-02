def step1(program):
    program[1] = 12
    program[2] = 2
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


program = list(map(int, input().split(',')))
print(step1(program))
