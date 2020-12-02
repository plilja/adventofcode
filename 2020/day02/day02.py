import re
import sys
from collections import namedtuple, Counter

Pattern = namedtuple('Pattern', 'minimum maximum char')


def parse_input(inp):
    result = []
    for line in inp:
        [minimum, maximum, char, password] = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups()
        result += [(Pattern(int(minimum), int(maximum), char), password)]
    return result


def step1(inp):
    result = 0
    for pattern, password in parse_input(inp):
        counter = Counter(password)
        if pattern.minimum <= counter[pattern.char] and pattern.maximum >= counter[pattern.char]:
            result += 1
    return result


inp = sys.stdin.readlines()
print(step1(inp))
