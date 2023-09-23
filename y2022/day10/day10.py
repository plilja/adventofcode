import sys


def step1(inp):
    result = 0
    cycle = 1
    signal = 1
    for line in inp:
        args = line.split(' ')
        if args[0] == 'noop':
            cycle_diff = 1
            signal_diff = 0
        elif args[0] == 'addx':
            cycle_diff = 2
            signal_diff = int(args[1])
        else:
            raise ValueError('Found unexpected instruction ' + args[0])
        for i in range(1, cycle_diff + 1):
            cycle += 1
            if i == cycle_diff:
                signal += signal_diff
            if (cycle - 20) % 40 == 0:
                result += cycle * signal
    return result


def step2(inp):
    cycle = 0
    signal = 1
    for line in inp:
        args = line.split(' ')
        if args[0] == 'noop':
            cycle_diff = 1
            signal_diff = 0
        elif args[0] == 'addx':
            cycle_diff = 2
            signal_diff = int(args[1])
        else:
            raise ValueError('Found unexpected instruction ' + args[0])
        for i in range(1, cycle_diff + 1):
            cycle += 1
            if signal <= (cycle % 40) <= signal + 2:
                print('#', end='')
            else:
                print('.', end='')
            if cycle % 40 == 0:
                print()
            if i == cycle_diff:
                signal += signal_diff


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
step2(inp)
