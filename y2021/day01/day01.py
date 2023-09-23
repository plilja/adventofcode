import sys


def step1(inp):
    result = 0
    for x, y in zip(inp, inp[1:]):
        if x < y:
            result += 1
    return result


def step2(inp):
    result = 0
    for i in range(3, len(inp)):
        if inp[i - 3] < inp[i]:
            result += 1
    return result


inp = [int(i) for i in sys.stdin]
print(step1(inp))
print(step2(inp))
