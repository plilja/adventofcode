import sys
from collections import defaultdict, deque


class NumberMonkey:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def done(self, monkeys):
        return True

    def eval(self, monkeys):
        return self.value


class OperationMonkey:
    def __init__(self, name, operation, operand1, operand2):
        self.name = name
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2

    def done(self, monkeys):
        return monkeys[self.operand1].done(monkeys) and monkeys[self.operand2].done(monkeys)

    def eval(self, monkeys):
        return self.operation(monkeys[self.operand1].eval(monkeys), monkeys[self.operand2].eval(monkeys))


def step1(graph, monkeys):
    q = deque()
    for name, monkey in monkeys.items():
        if monkey.done(monkeys):
            q.append(monkey)
    while q:
        monkey = q.popleft()
        if not monkey.done(monkeys):
            continue
        if monkey.name == 'root':
            return monkey.eval(monkeys)
        for neighbour in graph[monkey.name]:
            q.append(monkeys[neighbour])
    raise ValueError('Unable to find outcome of root monkey')


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
                    monkeys[name] = OperationMonkey(name, op, operand1, operand2)
                    graph[operand1].append(name)
                    graph[operand2].append(name)
                    break
    return graph, monkeys


graph, monkeys = read_input()
print(step1(graph, monkeys))