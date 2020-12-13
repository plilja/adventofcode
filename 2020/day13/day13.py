from math import ceil


def step1(x, busses):
    m = min(map(lambda y: (y * ceil(x / y), y), busses))
    return m[1] * (m[0] - x)


x = int(input())
busses = [int(y) for y in input().split(',') if y != 'x']
print(step1(x, busses))
