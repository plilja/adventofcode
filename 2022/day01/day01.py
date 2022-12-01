import sys


def step1(inp):
    result = 0
    curr = 0
    for line in inp:
        if line.strip() == '':
            curr = 0
        else:
            curr += int(line)
            result = max(result, curr)
    return result


inp = sys.stdin.readlines()
print(step1(inp))
