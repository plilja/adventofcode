from collections import defaultdict


def run_program(inp, first_input):
    program = defaultdict(int, zip(range(0, len(inp)), inp))

    def read(arg, mode, relative_base):
        if mode == '0':
            return program[program[arg]]
        elif mode == '1':
            return program[arg]
        else:
            assert mode == '2'
            return program[program[arg] + relative_base]

    def write(arg, mode, relative_base, value):
        if mode == '0':
            program[program[arg]] = value
        else:
            assert mode == '2'
            program[program[arg] + relative_base] = value

    output = ''
    position = 0
    relative_base = 0
    while True:
        arg = ('0000' + str(program[position]))[-5:]
        op = arg[3:5]
        if op == '99':
            break
        m1 = arg[2]
        m2 = arg[1]
        m3 = arg[0]
        if op == '01':
            value = read(position + 1, m1, relative_base) + read(position + 2, m2, relative_base)
            write(position + 3, m3, relative_base, value)
            position += 4
        elif op == '02':
            value = read(position + 1, m1, relative_base) * read(position + 2, m2, relative_base)
            write(position + 3, m3, relative_base, value)
            position += 4
        elif op == '03':
            write(position + 1, m1, relative_base, first_input)
            position += 2
        elif op == '04':
            output += ' ' + str(read(position + 1, m1, relative_base))
            position += 2
        elif op == '05':
            value = read(position + 1, m1, relative_base)
            if value != 0:
                position = read(position + 2, m2, relative_base)
            else:
                position += 3
        elif op == '06':
            value = read(position + 1, m1, relative_base)
            if value == 0:
                position = read(position + 2, m2, relative_base)
            else:
                position += 3
        elif op == '07':
            value = 1 if read(position + 1, m1, relative_base) < read(position + 2, m2, relative_base) else 0
            write(position + 3, m3, relative_base, value)
            position += 4
        elif op == '08':
            value = 1 if read(position + 1, m1, relative_base) == read(position + 2, m2, relative_base) else 0
            write(position + 3, m3, relative_base, value)
            position += 4
        else:
            assert op == '09'
            value = read(position + 1, m1, relative_base)
            relative_base += value
            position += 2
    return output.strip()


def step1(program):
    return run_program(program[::], 1)


program = list(map(int, input().split(',')))
print(step1(program))
