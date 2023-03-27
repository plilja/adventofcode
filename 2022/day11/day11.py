import sys
import re
from collections import namedtuple, Counter

Monkey = namedtuple('Monkey', 'id items operator operator_amount divisor if_true if_false')


def step1(monkeys):
    monkey_counts = Counter()
    for i in range(0, 20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop(0)
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

                new_item //= 3
                if new_item % monkey.divisor == 0:
                    monkeys[monkey.if_true].items.append(new_item)
                else:
                    monkeys[monkey.if_false].items.append(new_item)
    two_most_common = monkey_counts.most_common(2)
    return two_most_common[0][1] * two_most_common[1][1]


def read_input():
    lines = sys.stdin.readlines()
    i = 0
    result = []
    while i < len(lines):
        [_, monkey_id] = lines[i].split()
        items = list(map(int, lines[i + 1].split(': ')[1].split(', ')))
        [operator, amount] = re.match('\s*Operation: new = old ([+*]) (\d+|old)\s*', lines[i + 2]).groups()
        [divisor] = re.match('\s*Test: divisible by (\d+)\s*', lines[i + 3]).groups()
        [if_true] = re.match('\s*If true: throw to monkey (\d+)\s*', lines[i + 4]).groups()
        [if_false] = re.match('\s*If false: throw to monkey (\d+)\s*', lines[i + 5]).groups()
        result.append(Monkey(monkey_id, items, operator, amount, int(divisor), int(if_true), int(if_false)))
        i += 7
    return result


monkeys = read_input()
print(step1(monkeys))
