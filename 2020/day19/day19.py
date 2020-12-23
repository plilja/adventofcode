import sys
from collections import namedtuple

Rule = namedtuple('Rule', 'id sub_groups pattern')


def matches(rule_id, rules, s, i):
    rule = rules[rule_id]
    if rule.pattern:
        if s.find(rule.pattern, i) == i:
            return {i + len(rule.pattern)}
        else:
            return set()
    else:
        result = set()
        for sub_group in rule.sub_groups:
            x = {i}
            for sub_rule in sub_group:
                y = set()
                for j in x:
                    y |= matches(sub_rule, rules, s, j)
                x = y
            if i in x:
                x.remove(i)
            result |= x
        return result


def step1(rules, inp):
    result = 0
    for x in inp:
        if len(x) in matches(0, rules, x, 0):
            result += 1
    return result


def read_input():
    def parse_rule(line):
        id_, r = line.split(': ')
        if '|' in r:
            sub_group = []
            for sub in r.split('|'):
                sub_group.append([int(x) for x in sub.strip().split(' ')])
            return Rule(int(id_), sub_group, None)
        if '"' in r:
            return Rule(int(id_), [], r.replace('"', '').strip())
        else:
            return Rule(int(id_), [[int(x) for x in r.split(' ')]], None)

    rules = {}
    inp = []
    in_rules = True
    for line in sys.stdin:
        if line.strip() == '':
            in_rules = False
        elif in_rules:
            r = parse_rule(line)
            rules[r.id] = r
        else:
            inp.append(line.strip())
    return rules, inp


rules, inp = read_input()
print(step1(rules, inp))
