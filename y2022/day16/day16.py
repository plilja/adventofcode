import sys
import re


def step1(layout):
    dists = calc_dists(layout)
    all_valves_sum = 0
    for k, (v, tunnels) in layout.items():
        all_valves_sum += v
    return solve('AA', layout, dists, 30, set(layout.keys()), all_valves_sum, 0, 0, 0)


def step2(layout):
    count_non_zero_valves = 0
    non_zero_valves = {}
    for k, (valve, tunnels) in layout.items():
        if valve > 0:
            non_zero_valves[count_non_zero_valves] = k
            count_non_zero_valves += 1
    result = 0

    dists = calc_dists(layout)

    all_valves = 0
    for k, (v, tunnels) in layout.items():
        all_valves += v
    maximum = solve('AA', layout, dists, 26, set(layout.keys()), all_valves, 0, 0, 0)
    cache = {}
    for j in range(0, pow(2, count_non_zero_valves)):
        binary = bin(j)[2:]
        valves1 = set()
        valves1_sum = 0
        valves1_cache_key = ''
        valves2 = set()
        valves2_sum = 0
        valves2_cache_key = ''
        for b in range(0, count_non_zero_valves):
            if b < len(binary) and binary[b] == '1':
                valves1.add(non_zero_valves[b])
                valves1_sum += layout[non_zero_valves[b]][0]
                valves1_cache_key += '1'
                valves2_cache_key += '0'
            else:
                valves2.add(non_zero_valves[b])
                valves2_sum += layout[non_zero_valves[b]][0]
                valves1_cache_key += '0'
                valves2_cache_key += '1'

        if valves1_cache_key in cache or valves2_cache_key in cache:
            continue

        if len(valves1) < len(valves2):
            sub1 = solve('AA', layout, dists, 26, valves1, valves1_sum, 0, 0, 0)
            cache[valves1_cache_key] = sub1
        else:
            sub1 = solve('AA', layout, dists, 26, valves2, valves2_sum, 0, 0, 0)
            cache[valves2_cache_key] = sub1
        if sub1 + maximum > result:
            if len(valves1) < len(valves2):
                sub2 = solve('AA', layout, dists, 26, valves2, valves2_sum, 0, 0, result - sub1)
                cache[valves2_cache_key] = sub1
            else:
                sub2 = solve('AA', layout, dists, 26, valves1, valves1_sum, 0, 0, result - sub1)
                cache[valves1_cache_key] = sub1
            result = max(result, sub1 + sub2)

    return result


def solve(position, layout, dists, total_time, valves, all_valves_sum, total, rate, limit):
    if total + all_valves_sum * total_time <= limit:
        return limit

    result = total + total_time * rate
    totest = []
    for position2 in valves:
        d = dists[position][position2]
        valve = layout[position2][0]
        if d < total_time and valve > 0:
            totest.append(position2)

    for position2 in totest:
        d = dists[position][position2]
        valve = layout[position2][0]
        valves.remove(position2)
        new_total = total + d * rate
        sub = solve(position2,
                    layout,
                    dists,
                    total_time - d,
                    valves,
                    all_valves_sum,
                    new_total,
                    rate + valve,
                    max(result, limit))
        valves.add(position2)
        result = max(result, sub)

    return result


def calc_dists(layout):
    # dists[a][b] == time to move from valve a to valve b and open valve b
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


def main():
    layout = read_input()
    print(step1(layout))
    print('This one is slow. Wait for it...', file=sys.stderr)
    print(step2(layout))


if __name__ == '__main__':
    main()
