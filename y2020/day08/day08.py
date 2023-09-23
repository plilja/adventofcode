import sys


def read_program():
    result = []
    for line in sys.stdin:
        [inst, arg] = line.split(' ')
        result.append((inst, int(arg)))
    return result


def run_program(program):
    pointer = 0
    acc = 0
    seen = set()
    while True:
        if pointer in seen:
            return (False, acc)
        if pointer >= len(program):
            return (True, acc)
        seen.add(pointer)
        inst, arg = program[pointer]
        if inst == 'jmp':
            pointer += arg
        else:
            pointer += 1
            if inst == 'acc':
                acc += arg
            else:
                assert inst == 'nop'


def step1(program):
    return run_program(program)[1]


def step2(program):
    def switch(i):
        t = program[i]
        if t[0] == 'nop':
            program[i] = ('jmp', t[1])
        else:
            assert t[0] == 'jmp'
            program[i] = ('nop', t[1])

    for i in range(0, len(program)):
        if program[i][0] == 'jmp':
            switch(i)
            t = run_program(program)
            switch(i)
            if t[0]:
                return t[1]
        if program[i][0] == 'nop':
            switch(i)
            t = run_program(program)
            switch(i)
            if t[0]:
                return t[1]
    raise ValueError('Unable to fix program')


program = read_program()
print(step1(program))
print(step2(program))
