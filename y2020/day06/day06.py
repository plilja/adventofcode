import sys
from collections import Counter


def divide_groups(inp):
    result = [[]]
    for line in inp:
        if not line:
            result.append([])
        else:
            result[-1].append(line)
    return result


def step1(inp):
    result = 0
    for group in divide_groups(inp):
        group_counter = Counter()
        for line in group:
            group_counter += Counter(line)
        result += len(group_counter)
    return result


def step2(inp):
    result = 0
    for group in divide_groups(inp):
        distinct_answers = set([c for c in group[0]])
        for line in group[1:]:
            distinct_answers = distinct_answers & set([c for c in line])
        result += len(distinct_answers)
    return result


def main():
    inp = [line.strip() for line in sys.stdin.readlines()]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()

