import sys
import re
from collections import namedtuple, Counter, deque
from math import gcd

Monkey = namedtuple('Monkey', 'id items operator operator_amount divisor if_true if_false')


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def step1(monkeys):
    return simulate(monkeys, 20, 3)


def step2(monkeys):
    return simulate(monkeys, 10000, 1)


def simulate(monkeys, rounds, divisor):
    modder = 1
    for m in monkeys:
        modder = lcm(modder, m.divisor)
    monkey_counts = Counter()
    for i in range(0, rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey_counts[monkey.id] += 1
                if monkey.operator == '+':
                    if monkey.operator_amount == 'old':
                        new_item = item + item
                    else:
                        new_item = item + int(monkey.operator_amount)
                elif monkey.operator == '*':
                    if monkey.operator_amount == 'old':
                        new_item = item * item
                    else:
                        new_item = item * int(monkey.operator_amount)
                else:
                    raise ValueError('Unknown operator ' + monkey.operator)

                new_item //= divisor
                new_item %= modder
                if new_item % monkey.divisor == 0:
                    monkeys[monkey.if_true].items.append(new_item)
                else:
                    monkeys[monkey.if_false].items.append(new_item)
    two_most_common = monkey_counts.most_common(2)
    return two_most_common[0][1] * two_most_common[1][1]


def parse_input(lines):
    i = 0
    result = []
    while i < len(lines):
        [_, monkey_id] = lines[i].split()
        items = deque(map(int, lines[i + 1].split(': ')[1].split(', ')))
        [operator, amount] = re.match('\s*Operation: new = old ([+*]) (\d+|old)\s*', lines[i + 2]).groups()
        [divisor] = re.match('\s*Test: divisible by (\d+)\s*', lines[i + 3]).groups()
        [if_true] = re.match('\s*If true: throw to monkey (\d+)\s*', lines[i + 4]).groups()
        [if_false] = re.match('\s*If false: throw to monkey (\d+)\s*', lines[i + 5]).groups()
        result.append(Monkey(monkey_id, items, operator, amount, int(divisor), int(if_true), int(if_false)))
        i += 7
    return result


lines = sys.stdin.readlines()
print(step1(parse_input(lines)))
print(step2(parse_input(lines)))
