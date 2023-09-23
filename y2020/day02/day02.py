import re
import sys
from collections import namedtuple, Counter

Pattern = namedtuple('Pattern', 'a b char')


def parse_input(inp):
    result = []
    for line in inp:
        [a, b, char, password] = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups()
        result += [(Pattern(int(a), int(b), char), password)]
    return result


def step1(inp):
    result = 0
    for pattern, password in parse_input(inp):
        counter = Counter(password)
        if pattern.a <= counter[pattern.char] <= pattern.b:
            result += 1
    return result


def step2(inp):
    result = 0
    for pattern, password in parse_input(inp):
        x = password[pattern.a - 1] == pattern.char
        y = password[pattern.b - 1] == pattern.char
        if x != y:
            result += 1
    return result


inp = sys.stdin.readlines()
print(step1(inp))
print(step2(inp))
