import sys
from collections import defaultdict, deque


class NumberMonkey:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class OperationMonkey:
    def __init__(self, name, operation, operand1, operand2, op_name):
        self.name = name
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.op_name = op_name


def step1(graph, monkeys):
    results = solve(graph, monkeys)
    return results['root']


def step2(graph, monkeys):
    humn_monkey = monkeys['humn']
    root_monkey = monkeys['root']
    constants = set(monkeys.keys())
    for i in range(0, 100):
        # find which monkeys that never change value regardless of
        # what value humn_monkey has
        humn_monkey.value = i
        r1 = solve(graph, monkeys)
        humn_monkey.value = i + 1
        r2 = solve(graph, monkeys)
        for m in monkeys.keys():
            if r1[m] != r2[m] and m in constants:
                constants.remove(m)

    def helper(monkey, target):
        """
        Go backwards from root monkey until we come to humn_monkey
        """
        if monkey == humn_monkey:
            return target
        if monkey.operand1 in constants and monkey.operand2 in constants:
            raise ValueError('Unsolveable both sides are contant')
        if monkey.operand1 in constants:
            if monkey == root_monkey:
                return helper(monkeys[monkey.operand2], r1[monkey.operand1])
            elif monkey.op_name == '-':
                return helper(monkeys[monkey.operand2], r1[monkey.operand1] - target)
            elif monkey.op_name == '+':
                return helper(monkeys[monkey.operand2], target - r1[monkey.operand1])
            elif monkey.op_name == '*':
                return helper(monkeys[monkey.operand2], target // r1[monkey.operand1])
            else:
                assert monkey.op_name == '/'
                return helper(monkeys[monkey.operand2], r1[monkey.operand1] // target)
        else:
            assert monkey.operand2 in constants
            if monkey == root_monkey:
                return helper(monkeys[monkey.operand1], r1[monkey.operand2])
            elif monkey.op_name == '-':
                return helper(monkeys[monkey.operand1], target + r1[monkey.operand2])
            elif monkey.op_name == '+':
                return helper(monkeys[monkey.operand1], target - r1[monkey.operand2])
            elif monkey.op_name == '*':
                return helper(monkeys[monkey.operand1], target // r1[monkey.operand2])
            else:
                assert monkey.op_name == '/'
                return helper(monkeys[monkey.operand1], r1[monkey.operand2] * target)

    return helper(root_monkey, None)


def solve(graph, monkeys):
    q = deque()
    for name, monkey in monkeys.items():
        if isinstance(monkey, NumberMonkey):
            q.append(monkey)
    results = {}
    done = set()
    while q:
        monkey = q.popleft()
        done.add(monkey.name)
        if isinstance(monkey, NumberMonkey):
            results[monkey.name] = monkey.value
        else:
            results[monkey.name] = monkey.operation(results[monkey.operand1], results[monkey.operand2])
        for neighbour_name in graph[monkey.name]:
            neighbour = monkeys[neighbour_name]
            if neighbour.operand1 in done and neighbour.operand2 in done:
                q.append(neighbour)
    return results


def read_input():
    graph = defaultdict(list)
    monkeys = {}
    for line in map(str.strip, sys.stdin.readlines()):
        [name, operation] = line.split(':')
        try:
            monkeys[name] = NumberMonkey(int(operation), name)
        except ValueError:
            operations = [('+', lambda x, y: x + y),
                          ('-', lambda x, y: x - y),
                          ('*', lambda x, y: x * y),
                          ('/', lambda x, y: x // y)]
            for c, op in operations:
                if c in operation:
                    [operand1, operand2] = operation.strip().split(' {} '.format(c))
                    monkeys[name] = OperationMonkey(name, op, operand1, operand2, c)
                    graph[operand1].append(name)
                    graph[operand2].append(name)
                    break
    return monkeys, graph


monkeys, graph = read_input()
print(step1(graph, monkeys))
print(step2(graph, monkeys))