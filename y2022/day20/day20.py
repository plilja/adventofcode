import sys


def step1(inp):
    return solve(inp, 1, 1)


def step2(inp):
    return solve(inp, 811589153, 10)


def solve(inp, decryption_key, iterations):
    ls = []
    for i, v in enumerate(inp):
        if v == 0:
            zero_key = '{}|{}'.format(0, i)
        ls.append('{}|{}'.format(v * decryption_key, i))
    for _ in range(0, iterations):
        for i, v in enumerate(inp):
            shift(ls, '{}|{}'.format(v * decryption_key, i))
    zero = ls.index(zero_key)
    result = 0
    for off in [1000, 2000, 3000]:
        result += int(ls[(zero + off) % len(inp)].split('|')[0])
    return result


def shift(ls, value):
    n = len(ls) - 1
    v, _ = list(map(int, value.split('|')))
    i = ls.index(value)
    ls.remove(value)
    new_i = (i + v) % n
    ls.insert(new_i, value)


if __name__ == '__main__':
    inp = list(map(int, sys.stdin.readlines()))
    print(step1(inp))
    print(step2(inp))
