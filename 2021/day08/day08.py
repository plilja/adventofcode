import sys


def step1(inp):
    result = 0
    for signal_patterns, output_values in inp:
        for s in output_values:
            if len(s) in [2, 3, 4, 7]:
                result += 1
    return result


def read_input():
    result = []
    for line in sys.stdin.readlines():
        a, b = line.split('|')
        signal_patterns = a.split()
        output_values = b.split()
        result.append((signal_patterns, output_values))
    return result


inp = read_input()
print(step1(inp))
