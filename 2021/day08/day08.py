import sys

WIRES = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
VALID = {'abcefg': 0,
         'cf': 1,
         'acdeg': 2,
         'acdfg': 3,
         'bcdf': 4,
         'abdfg': 5,
         'abdefg': 6,
         'acf': 7,
         'abcdefg': 8,
         'abcdfg': 9}


def step1(inp):
    result = 0
    for signal_values, output_values in inp:
        for s in output_values:
            if len(s) in [2, 3, 4, 7]:
                result += 1
    return result


def step2(inp):
    def picks(wires):
        if not wires:
            yield []
        for wire in wires:
            sub = list(picks(wires - {wire}))
            for pick in sub:
                yield [wire] + pick

    result = 0
    for signal_values, output_values in inp:
        for pick in picks(WIRES):
            m = {}
            for i in range(0, len(pick)):
                m[chr(ord('a') + i)] = pick[i]
            valid = True
            for s in signal_values + output_values:
                sp = ''
                for c in s:
                    sp += m[c]
                key = ''.join(sorted(sp))
                if key not in VALID:
                    valid = False
                    break
            if valid:
                sub = ''
                for output_value in output_values:
                    sp = ''
                    for c in output_value:
                        sp += m[c]
                    key = ''.join(sorted(sp))
                    sub += str(VALID[key])
                result += int(sub)
                break
    return result


def read_input():
    result = []
    for line in sys.stdin.readlines():
        a, b = line.split('|')
        signal_values = a.split()
        output_values = b.split()
        result.append((signal_values, output_values))
    return result


inp = read_input()
print(step1(inp))
print(step2(inp))
