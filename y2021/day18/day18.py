import sys
from math import ceil, floor
from copy import deepcopy


def step1(inp):
    x = parse_input_line(inp[0])
    for line in inp[1:]:
        y = parse_input_line(line)
        x = add(x, y)
    return magnitude(x)


def step2(inp):
    parsed = list(map(parse_input_line, inp))
    result = 0
    for i in range(0, len(parsed)):
        for j in range(0, len(parsed)):
            if i == j:
                continue
            result = max(result, magnitude(add(parsed[i], parsed[j])))
    return result


def parse_input_line(line):
    return unflatten(list(filter(lambda x: x != ',', list(line.strip()))))


def add(x, y):
    return reduc([x, y])


def reduc(x):
    res = x
    while True:
        bef = res
        res = explode(bef)
        if bef != res:
            continue
        res = split(bef)
        if bef == res:
            return res


def flatten(x):
    result = ['[']
    for y in x:
        if isinstance(y, list):
            result += flatten(y)
        else:
            result.append(y)
    result.append(']')
    return result


def unflatten(x):
    result = None
    stacks = []
    for y in x:
        if y == '[':
            stacks.append([])
            if result is None:
                result = stacks[-1]
        elif y == ']':
            tmp = stacks.pop()
            if stacks:
                stacks[-1].append(tmp)
        else:
            stacks[-1].append(int(y))
    return result


def explode(x):
    flattened = flatten(x)
    depth = 0
    for i in range(0, len(flattened)):
        y = flattened[i]
        if y == '[':
            depth += 1
        elif y == ']':
            depth -= 1
        else:
            if depth > 4 and i + 1 < len(flattened) and flattened[i + 1] not in ['[', ']']:
                for j in range(i - 1, -1, -1):
                    if flattened[j] not in ['[', ']']:
                        flattened[j] += y
                        break
                for j in range(i + 2, len(flattened)):
                    if flattened[j] not in ['[', ']']:
                        flattened[j] += flattened[i + 1]
                        break
                flattened[i] = 0
                flattened.pop(i + 2)
                flattened.pop(i + 1)
                flattened.pop(i - 1)
                return unflatten(flattened)
    return x  # nothing to explode


def split(x):
    def helper(y):
        if isinstance(y, list):
            for i in range(0, len(y)):
                tmp = split(y[i])
                stop = y[i] != tmp
                y[i] = tmp
                if stop:
                    break
            return y
        else:
            if y >= 10:
                return [floor(y/2), ceil(y/2)]
            else:
                return y
    return helper(deepcopy(x))


def magnitude(x):
    if isinstance(x, list):
        return 3*magnitude(x[0]) + 2*magnitude(x[1])
    else:
        return x


def main():
    inp = sys.stdin.readlines()
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
