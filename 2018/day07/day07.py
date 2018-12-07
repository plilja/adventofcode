import sys
import re
import heapq

def step1(graph):
    rev_graph = {v:set() for v in graph}
    for v1 in graph:
        for v2 in graph[v1]:
            rev_graph[v2] |= {v1}
    pq = []
    for v in graph:
        if not rev_graph[v]:
            heapq.heappush(pq, v)
    res = ''
    while pq:
        v1 = heapq.heappop(pq)
        res += v1
        for v2 in graph[v1]:
            rev_graph[v2] -= {v1}
        for v2 in graph[v1]:
            if not rev_graph[v2]:
                heapq.heappush(pq, v2)
    return res


def parse_input(inp):
    g = {}
    for s in inp:
        v = s.split()
        a = v[1]
        b = v[7]
        g.setdefault(a, []).append(b)
        g.setdefault(b, [])
    return g

graph = parse_input(sys.stdin.readlines())
print(step1(graph))
