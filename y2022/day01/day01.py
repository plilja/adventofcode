import sys


def step1(inp):
    return max(parse(inp))


def step2(inp):
    return sum(list(sorted(parse(inp)))[-3:])


def parse(inp):
    result = []
    curr = 0
    for line in inp:
        if line.strip() == '':
            result.append(curr)
            curr = 0
        else:
            curr += int(line)
    if curr > 0:
        result.append(curr)
    return result


def main():
    inp = sys.stdin.readlines()
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
