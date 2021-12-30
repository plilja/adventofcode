import sys
from math import ceil, floor
from copy import deepcopy


def step1(inp):
    x = parse_input_line(inp[0])
    for line in inp[1:]:
        y = parse_input_line(line)
        x = add(x, y)
    return magnitude(x)


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
    result = deepcopy(x)
    if isinstance(x, list):
        for i in range(0, len(x)):
            result[i] = split(x[i])
            if x[i] != result[i]:
                break
        return result
    else:
        if x >= 10:
            return [floor(x/2), ceil(x/2)]
        else:
            return result


def magnitude(x):
    if isinstance(x, list):
        return 3*magnitude(x[0]) + 2*magnitude(x[1])
    else:
        return x


assert split([10, 0]) == [[5, 5], 0]
assert split([11, 0]) == [[5, 6], 0]
assert split([10, 10]) == [[5, 5], 10]
assert split([[10, 0], 10]) == [[[5, 5], 0], 10]
assert magnitude([[1,2],[[3,4],5]]) == 143
assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
assert magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
assert magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
assert magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

assert flatten([10, 0]) == ['[', 10, 0, ']']
assert flatten([[10, 0], 10]) == ['[', '[', 10, 0, ']', 10, ']']
assert flatten([[1,2],[[3,4],5]]) == ['[', '[', 1, 2, ']', '[', '[', 3, 4, ']', 5, ']', ']']
assert unflatten(['[', 10, 0, ']']) == [10, 0]
assert unflatten(['[', '[', 10, 0, ']', 10, ']']) == [[10, 0], 10]
assert unflatten(['[', '[', 1, 2, ']', '[', '[', 3, 4, ']', 5, ']', ']']) == [[1,2],[[3,4],5]]
assert(unflatten(flatten([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])) == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])

assert explode([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
assert explode([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
assert explode([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
assert explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]

inp = sys.stdin.readlines()
print(step1(inp))
