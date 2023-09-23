import re
import sys
from collections import namedtuple

Rule = namedtuple('Rule', 'name ranges')


def step1(rules, nearby_tickets):
    result = 0
    for ticket in nearby_tickets:
        for num in ticket:
            valid = False
            for rule in rules:
                for fr, to in rule.ranges:
                    if fr <= num <= to:
                        valid = True
            if not valid:
                result += num
    return result


def step2(rules, your_ticket, nearby_tickets):
    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for num in ticket:
            valid_num = False
            for rule in rules:
                for fr, to in rule.ranges:
                    if fr <= num <= to:
                        valid_num = True
            valid = valid and valid_num
        if valid:
            valid_tickets.append(ticket)

    rule_idx = {}
    idx_rule = {}
    while len(rules) != len(rule_idx):
        xs = [[] for i in range(0, len(valid_tickets[0]))]
        for ticket in valid_tickets:
            for i, num in enumerate(ticket):
                xs[i].append(num)

        for i, ys in enumerate(xs):
            if i in idx_rule:
                continue
            possible_rules = []
            for rule in rules:
                if rule.name in rule_idx:
                    continue
                valid = True
                for num in ys:
                    num_valid = False
                    for fr, to in rule.ranges:
                        if fr <= num <= to:
                            num_valid = True
                    valid = valid and num_valid
                if valid:
                    possible_rules.append(rule)
            if len(possible_rules) == 1:
                rule_idx[possible_rules[0].name] = i
                idx_rule[i] = possible_rules[0]

    result = 1
    for rule in rules:
        if rule.name.startswith('departure '):
            result *= your_ticket[rule_idx[rule.name]]
    return result


def read_input():
    rules = []
    your_ticket = []
    nearby_tickets = []
    in_nearby_tickets = False
    for line in sys.stdin:
        if line.startswith('nearby tickets:'):
            in_nearby_tickets = True

        m1 = re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', line)
        if m1:
            [name, from1, to1, from2, to2] = m1.groups()
            ranges = [(int(from1), int(to1)), (int(from2), int(to2))]
            rules.append(Rule(name, ranges))
        else:
            numbers = list(map(int, re.findall(r'\d+', line)))
            if numbers:
                if in_nearby_tickets:
                    nearby_tickets.append(numbers)
                else:
                    your_ticket = numbers
    return rules, your_ticket, nearby_tickets


rules, your_ticket, nearby_tickets = read_input()
print(step1(rules, nearby_tickets))
print(step2(rules, your_ticket, nearby_tickets))
