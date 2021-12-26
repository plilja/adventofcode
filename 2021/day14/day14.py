import sys
from collections import Counter


def step1(template, rules):
    for i in range(0, 10):
        new_template = [template[0]]
        for x, y in zip(template, template[1:]):
            key = x + y
            if key in rules:
                new_template.append(rules[key])
            new_template.append(y)
        template = new_template
    counter = Counter(template).most_common()
    return counter[0][1] - counter[-1][1]


def read_input():
    inp = sys.stdin.readlines()
    template = list(inp[0].strip())
    rules = {}
    for line in inp[2:]:
        args = line.split()
        rules[args[0]] = args[2]
    return template, rules


template, rules = read_input()
print(step1(template, rules))
