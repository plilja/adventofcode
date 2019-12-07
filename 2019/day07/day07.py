from itertools import product


def run_program(program, inputs):

    def read(arg, mode):
        if mode == '0':
            return program[program[arg]]
        else:
            return program[arg]

    def write(arg, mode, value):
        assert mode == '0'
        program[program[arg]] = value

    last_output = None
    position = 0
    while program[position] != 99:
        arg = ('0000' + str(program[position]))[-5:]
        if arg == '00099':
            break
        op = arg[3:5]
        m1 = arg[2]
        m2 = arg[1]
        m3 = arg[0]
        if op == '01':
            value = read(position + 1, m1) + read(position + 2, m2)
            write(position + 3, m3, value)
            position += 4
        elif op == '02':
            value = read(position + 1, m1) * read(position + 2, m2)
            write(position + 3, m3, value)
            position += 4
        elif op == '03':
            write(position + 1, m1, inputs[0])
            inputs = inputs[1:]
            position += 2
        elif op == '04':
            last_output = read(position + 1, m1)
            position += 2
        elif op == '05':
            value = read(position + 1, m1)
            if value != 0:
                position = read(position + 2, m2)
            else:
                position += 3
        elif op == '06':
            value = read(position + 1, m1)
            if value == 0:
                position = read(position + 2, m2)
            else:
                position += 3
        elif op == '07':
            value = 1 if read(position + 1, m1) < read(position + 2, m2) else 0
            write(position + 3, m3, value)
            position += 4
        else:
            assert op == '08'
            value = 1 if read(position + 1, m1) == read(position + 2, m2) else 0
            write(position + 3, m3, value)
            position += 4
    return last_output


def step1(program):
    result = 0
    for settings in product(*[[0, 1, 2, 3, 4] for _ in range(0, 5)]):
        if len(set(settings)) == 5:
            signal = 0
            for setting in settings:
                signal = run_program(program[::], [setting, signal])
            if signal > result:
                result = signal
    return result


program = list(map(int, input().split(',')))
print(step1(program))
