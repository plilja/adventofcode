import sys


def parse(inp):
    result = [{}]
    for line in inp:
        if line == '':
            result.append({})
            continue
        for arg in line.split(' '):
            field, value = arg.split(':')
            result[-1][field] = value
    return result


def step1(inp):
    result = 0
    for passport in parse(inp):
        if len(passport) == 8:
            result += 1
        elif len(passport) == 7 and 'cid' not in passport:
            result += 1
    return result


inp = [line.strip() for line in sys.stdin.readlines()]
print(step1(inp))
