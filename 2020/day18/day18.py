import sys
import re


def simple_expression(inp):
    args = re.split(r'(\+|\*)', inp)
    result = int(args[0])
    for i in range(1, len(args), 2):
        arg = args[i]
        if arg == '*':
            result = result * int(args[i + 1])
        elif arg == '+':
            result = result + int(args[i + 1])
        else:
            raise ValueError('Unknown operator', arg)
    return result


def expression(inp):
    balance = 0
    start, end = None, None
    for i, c in enumerate(inp):
        if c == '(':
            if start is None:
                start = i
            balance += 1
        if c == ')':
            balance -= 1
        if start is not None and balance == 0:
            end = i
            break
    if start is not None and end is not None:
        return expression(inp[:start] + str(expression(inp[start+1:end])) + inp[end+1:])
    else:
        return simple_expression(inp)


def step1(inp):
    return sum([expression(x.replace(' ', '')) for x in inp])


assert expression('1') == 1
assert expression('1+2') == 3
assert expression('(1+3)') == 4
assert expression('(1*3)') == 3
assert expression('(1)') == 1
assert expression('(1)*2') == 2
assert expression('(1+2)*2') == 6
assert expression('(1+2)*(2+3)') == 15
assert expression('((1+2)*(2+3))*2') == 30
assert expression('1+2*2') == 6
inp = [x.strip() for x in sys.stdin]
print(step1(inp))
