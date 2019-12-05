def step1(program):

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
            write(position + 1, m1, 1)
            position += 2
        else:
            assert op == '04'
            last_output = read(position + 1, m1)
            position += 2
    return last_output


program = list(map(int, input().split(',')))
print(step1(program))
