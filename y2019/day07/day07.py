from itertools import product
from y2019.intcode import IntcodeProcess


def step1(program):
    result = 0
    for settings in product(*[[0, 1, 2, 3, 4] for _ in range(0, 5)]):
        if len(set(settings)) == 5:
            signal = 0
            for setting in settings:
                process = IntcodeProcess(program)
                process.add_input(setting)
                process.add_input(signal)
                process.run_until_complete()
                signal = process.pop_output()
            result = max(result, signal)
    return result


def step2(program):
    result = 0
    for settings in product(*[[5, 6, 7, 8, 9] for _ in range(0, 5)]):
        if len(set(settings)) == 5:
            amps = [IntcodeProcess(program) for _ in settings]
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


def main():
    program = list(map(int, input().split(',')))
    print(step1(program))
    print(step2(program))


if __name__ == '__main__':
    main()

