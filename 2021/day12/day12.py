import sys
from collections import defaultdict


def step1(graph):
    q = [['start']]
    result = 0
    while q:
        path = q.pop()
        last = path[-1]
        if last == 'end':
            result += 1
        else:
            for neighbour in graph[last]:
                if 'a' <= neighbour[0] <= 'z' and neighbour in path:
                    continue
                q.append(path + [neighbour])
    return result


def read_input():
    result = defaultdict(list)
    for line in sys.stdin:
        a, b = line.strip().split('-')
        result[a].append(b)
        result[b].append(a)
    return result


graph = read_input()
print(step1(graph))
