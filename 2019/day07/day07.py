from itertools import product


class Process:

    def __init__(self, program):
        self.position = 0
        self.inputs = []
        self.output = []
        self.program = program
        self.running = True

    def tick(self):
        """ Run program one instruction. """

        def read(arg, mode):
            if mode == '0':
                return self.program[self.program[arg]]
            else:
                return self.program[arg]

        def write(arg, mode, value):
            assert mode == '0'
            self.program[self.program[arg]] = value

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
            if len(self.inputs) > 0:
                write(self.position + 1, m1, self.inputs[0])
                self.inputs = self.inputs[1:]
                self.position += 2
            # else tick does nothing
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
        else:
            assert op == '08'
            value = 1 if read(self.position + 1, m1) == read(self.position + 2, m2) else 0
            write(self.position + 3, m3, value)
            self.position += 4

    def run(self):
        """ Run program until it terminates. """
        while self.running:
            self.tick()

    def has_output(self):
        return len(self.output) > 0

    def pop_output(self):
        res = self.output[0]
        self.output = self.output[1:]
        return res

    def add_input(self, value):
        self.inputs.append(value)

    def is_running(self):
        return self.running


def step1(program):
    result = 0
    for settings in product(*[[0, 1, 2, 3, 4] for _ in range(0, 5)]):
        if len(set(settings)) == 5:
            signal = 0
            for setting in settings:
                process = Process(program[::])
                process.add_input(setting)
                process.add_input(signal)
                process.run()
                signal = process.pop_output()
            result = max(result, signal)
    return result


def step2(program):
    result = 0
    for settings in product(*[[5, 6, 7, 8, 9] for _ in range(0, 5)]):
        if len(set(settings)) == 5:
            amps = [Process(program[::]) for _ in settings]
            for amp, setting in zip(amps, settings):
                amp.add_input(setting)
            amps[0].add_input(0)

            last_output = None
            while amps[-1].is_running():
                for i in range(0, 5):
                    amps[i].tick()
                    if amps[i].has_output():
                        output = amps[i].pop_output()
                        if i == 4:
                            last_output = output
                        amps[(i + 1) % 5].add_input(output)
            result = max(result, last_output)

    return result


program = list(map(int, input().split(',')))
print(step1(program))
print(step2(program))
