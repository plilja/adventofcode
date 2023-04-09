import sys
import re
from collections import deque


def step1(layout):
    dists = calc_dists(layout)
    q = deque([(0, 0, 0, 'AA', frozenset(layout.keys()))])
    result = 0
    total_valves = 0
    for k, (valve, tunnels) in layout.items():
        total_valves += valve
    while q:
        (total, rate, time, position, closed_valves) = q.popleft()
        if time >= 30:
            continue
        rem_time = 30 - time
        result = max(result, total + rate * rem_time)
        if total_valves * rem_time + total <= result:
            continue
        for position2 in closed_valves:
            d = dists[position][position2]
            valve_rate = layout[position2][0]
            if time + d < 30 and valve_rate > 0:
                new_rate = rate + valve_rate
                new_total = total + d * rate
                q.append((new_total, new_rate, time + d, position2, closed_valves - {position2}))
    return result


def calc_dists(layout):
    dists = {}
    for k in layout.keys():
        dists[k] = {}
        q = [(k, 0)]
        while q:
            (n, d) = q.pop()
            prev = dists[k].get(n)
            if prev is not None and prev <= d + 1:
                continue
            dists[k][n] = d + 1
            for n2 in layout[n][1]:
                q.append((n2, d + 1))
    return dists


def read_input():
    result = {}
    for line in sys.stdin:
        [valve, rate, tunnels] = re.match(
            r'Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z, ]+)',
            line
        ).groups()
        result[valve] = (int(rate), tunnels.split(', '))
    return result


layout = read_input()
print(step1(layout))