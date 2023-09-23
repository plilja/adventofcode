import sys


def step1(inp):
    groups = []
    for line in inp:
        middle = len(line) // 2
        groups.append((line[:middle], line[middle:]))
    return calc(groups)


def step2(inp):
    groups = []
    for i in range(0, len(inp), 3):
        groups.append(inp[i:i + 3])
    return calc(groups)


def calc(groups):
    result = 0
    for group in groups:
        common = {c for c in group[0]}
        for member in group[1:]:
            c2 = {c for c in member}
            common = common & c2
        for c in common:
            result += get_prio(c)
    return result


def get_prio(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def main():
    inp = [line.strip() for line in sys.stdin.readlines()]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
