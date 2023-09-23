import sys
from collections import defaultdict

TARGET = 150


def step1(containers):
    m = defaultdict(lambda: defaultdict(int))
    m[-1][0] = 1
    for i in range(0, len(containers)):
        c = containers[i]
        for j in range(0, TARGET + 1):
            m[i][j] = m[i - 1][j]
            if j >= c:
                m[i][j] += m[i - 1][j - c]
    return m[len(containers) - 1][TARGET]


def step2(containers):
    m = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for k in range(0, len(containers) + 1):
        for j in range(0, len(containers)):
            m[k][j - 1][0] = 1
    for k in range(1, len(containers) + 1):
        for i in range(0, len(containers)):
            c = containers[i]
            for j in range(0, TARGET + 1):
                m[k][i][j] = m[k][i - 1][j]
                if j >= c:
                    m[k][i][j] += m[k - 1][i - 1][j - c]
        if m[k][len(containers) - 1][TARGET] > 0:
            return m[k][len(containers) - 1][TARGET]
    return 0


def main():
    containers = [int(s) for s in sys.stdin.readlines()]
    print(step1(containers))
    print(step2(containers))


if __name__ == '__main__':
    main()
