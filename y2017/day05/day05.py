import sys


def step1(inp):
    copy = inp[::]
    i = 0
    ans = 0
    while 0 <= i < len(copy):
        off = copy[i]
        copy[i] += 1
        i += off
        ans += 1
    return ans


def step2(inp):
    copy = inp[::]
    i = 0
    ans = 0
    while 0 <= i < len(copy):
        off = copy[i]
        if off >= 3:
            copy[i] -= 1
        else:
            copy[i] += 1
        i += off
        ans += 1
    return ans


def main():
    inp = [int(s) for s in sys.stdin.readlines()]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
