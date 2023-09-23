import sys
import re


def simple_expression_step1(inp):
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


def simple_expression_step2(inp):
    args = inp.split('*')
    result = 1
    for arg in args:
        result *= eval(arg)
    return result


def expression(inp, simple_expression):
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
        return expression(inp[:start] + str(expression(inp[start+1:end], simple_expression)) + inp[end+1:], simple_expression)
    else:
        return simple_expression(inp)


def step1(inp):
    return sum([expression(x.replace(' ', ''), simple_expression_step1) for x in inp])


def step2(inp):
    return sum([expression(x.replace(' ', ''), simple_expression_step2) for x in inp])


def main():
    inp = [x.strip() for x in sys.stdin]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
