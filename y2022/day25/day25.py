import sys
from heapq import heappop, heappush

from common.util import ever


def step1(inp):
    v = sum(map(from_snafu, inp))
    return to_snafu(v)


def from_snafu(s):
    r = 0
    e = 1
    for c in reversed(s):
        if c == '1':
            r += e
        elif c == '2':
            r += 2 * e
        elif c == '-':
            r -= e
        elif c == '=':
            r -= 2 * e
        else:
            assert c == '0'
        e *= 5
    return r


def to_snafu(target):
    q = [(abs(target), '0', 0)]
    for i in ever(1):
        e = 5 ** i
        if e > 5 * abs(target):
            break
        heappush(q, (abs(target - e), '1' + '0' * i, e))
        heappush(q, (abs(target - 2 * e), '2' + '0' * i, 2 * e))
        heappush(q, (abs(target + e), '-' + '0' * i, -e))
        heappush(q, (abs(target + 2 * e), '1' + '0' * i, - 2 * e))

    visited = set()
    while q:
        dist, snapu, decimal = heappop(q)
        if decimal == target:
            return snapu
        if decimal in visited:
            continue
        visited.add(decimal)
        for i in range(0, len(snapu)):
            if snapu[i] == '0':  # try exchanging 0 for other char
                digits = len(snapu)
                e = 5 ** (digits - i - 1)
                for c, fact in [('1', 1), ('2', 2), ('-', -1), ('=', -2)]:
                    new_num = decimal + fact * e
                    new_snapu = snapu[:i] + c + snapu[i + 1:]
                    heappush(q, (abs(target - new_num), new_snapu, new_num))
    raise ValueError("No solution found")


def main():
    inp = [line.strip() for line in sys.stdin]
    print(step1(inp))


if __name__ == '__main__':
    main()
