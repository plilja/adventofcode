from collections import defaultdict

class Process:
    def __init__(self, inp):
        self.position = 0
        self.program = defaultdict(int, zip(range(0, len(inp)), inp))
        self.input = []
        self.output = []
        self._needs_input = False
        self.relative_base = 0
        self.running = True

    def tick(self):
        def read(arg, mode):
            if mode == '0':
                return self.program[self.program[arg]]
            elif mode == '1':
                return self.program[arg]
            else:
                assert mode == '2'
                return self.program[self.program[arg] + self.relative_base]

        def write(arg, mode, value):
            if mode == '0':
                self.program[self.program[arg]] = value
            else:
                assert mode == '2'
                self.program[self.program[arg] + self.relative_base] = value

        arg = ('0000' + str(self.program[self.position]))[-5:]
        op = arg[3:5]
        if op == '99':
            self.running = False
            return
        m1 = arg[2]
        m2 = arg[1]
        m3 = arg[0]
        if op == '01':
            value = read(self.position + 1, m1) + read(self.position + 2, m2)
            write(self.position + 3, m3, value)
            self.position += 4
        elif op == '02':
            value = read(self.position + 1, m1) * read(self.position + 2, m2)
            write(self.position + 3, m3, value)
            self.position += 4
        elif op == '03':
            if len(self.input) == 0:
                self._needs_input = True
            else:
                i = self.input[0]
                self.input = self.input[1:]
                write(self.position + 1, m1, i)
                self.position += 2
        elif op == '04':
            self.output.append(read(self.position + 1, m1))
            self.position += 2
        elif op == '05':
            value = read(self.position + 1, m1)
            if value != 0:
                self.position = read(self.position + 2, m2)
            else:
                self.position += 3
        elif op == '06':
            value = read(self.position + 1, m1)
            if value == 0:
                self.position = read(self.position + 2, m2)
            else:
                self.position += 3
        elif op == '07':
            value = 1 if read(self.position + 1, m1) < read(self.position + 2, m2) else 0
            write(self.position + 3, m3, value)
            self.position += 4
        elif op == '08':
            value = 1 if read(self.position + 1, m1) == read(self.position + 2, m2) else 0
            write(self.position + 3, m3, value)
            self.position += 4
        else:
            assert op == '09'
            value = read(self.position + 1, m1)
            self.relative_base += value
            self.position += 2

    def needs_input(self):
        return self._needs_input

    def add_input(self, value):
        self._needs_input = False
        self.input.append(value)

    def has_output(self):
        return len(self.output) > 0

    def pop_output(self):
        value = self.output[0]
        self.output = self.output[1:]
        return value

    def is_running(self):
        return self.running

    def run_until_complete(self):
        while self.is_running():
            self.tick()


def step1(program):
    process = Process(program)
    process.run_until_complete()
    grid = defaultdict(lambda: defaultdict(int))
    for i in range(0, len(process.output), 3):
        x = process.output[i]
        y = process.output[i + 1]
        tile = process.output[i + 2]
        grid[y][x] = tile
    result = 0
    for y in grid.keys():
        result += sum([1 for x in grid[y].keys() if grid[y][x] == 2])
    return result


program = list(map(int, input().split(',')))
print(step1(program))
