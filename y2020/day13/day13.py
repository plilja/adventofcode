from common.math_util import chinese_remainder_theorem
from math import ceil


def step1(x, busses):
    busses_ints = [int(y) for y in busses if y != 'x']
    m = min(map(lambda y: (y * ceil(x / y), y), busses_ints))
    return m[1] * (m[0] - x)


def step2(busses):
    # The problem asks to solve this equation system.
    # This can be done efficiently using the chinese remainder theorem.
    # x == 0 % busses[0]
    # x == busses[1] - 1 % busses[1]
    # ...
    # x == busses[n] - n % busses[n]
    r = None
    for i, buss in enumerate(busses):
        if buss != 'x':
            if r:
                r = chinese_remainder_theorem(r[0], r[1], int(buss) - i, int(buss))
            else:
                r = (0, int(buss))
    return r[0]


def main():
    x = int(input())
    busses = [y.strip() for y in input().split(',')]
    print(step1(x, busses))
    print(step2(busses))


if __name__ == '__main__':
    main()

