import sys
import heapq
from collections import defaultdict


def step1(graph):
    incoming = defaultdict(int)
    for v1 in graph:
        for v2 in graph[v1]:
            incoming[v2] += 1
    pq = []
    for v in graph:
        if incoming[v] == 0:
            heapq.heappush(pq, v)
    res = ''
    while pq:
        v1 = heapq.heappop(pq)
        res += v1
        for v2 in graph[v1]:
            incoming[v2] -= 1
            if incoming[v2] == 0:
                heapq.heappush(pq, v2)
    return res


def step2(graph, num_workers, step_offset):
    incoming = defaultdict(int)
    for v1 in graph:
        for v2 in graph[v1]:
            incoming[v2] += 1
    free_jobs = []
    for v in graph:
        if incoming[v] == 0:
            heapq.heappush(free_jobs, v)

    free_workers = num_workers
    busy_workers = []
    time = 0
    while free_jobs or busy_workers:
        while free_jobs and free_workers > 0:
            next_task = heapq.heappop(free_jobs)
            cost = ord(next_task) - ord('A') + 1 + step_offset
            free_workers -= 1
            busy_workers += [(next_task, cost)]

        wait = min([t for _, t in busy_workers])
        time += wait
        busy_workers = [(task, task_time - wait)
                        for task, task_time in busy_workers]
        i = 0
        while i < len(busy_workers):
            task, task_time = busy_workers[i]
            if task_time == 0:
                for v in graph[task]:
                    incoming[v] -= 1
                    if incoming[v] == 0:
                        heapq.heappush(free_jobs, v)
                free_workers += 1
                busy_workers.pop(i)
                continue
            i += 1

    return time


def parse_input(inp):
    g = defaultdict(list)
    for s in inp:
        v = s.split()
        a = v[1]
        b = v[7]
        g[a] += [b]
    return g


graph = parse_input(sys.stdin.readlines())
print(step1(graph))
print(step2(graph, 5, 60))

