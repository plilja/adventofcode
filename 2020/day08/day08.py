import sys

def read_program():
    result = []
    for line in sys.stdin:
        [inst, arg] = line.split(' ')
        result.append((inst, int(arg)))
    return result


def step1(program):
    pointer = 0
    acc = 0
    seen = set()
    while True:
        if pointer in seen:
            return acc
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


program = read_program()
print(step1(program))
