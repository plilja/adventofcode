import heapq
import sys

from common.util import deltas4

COST = {'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000}

CORRECT_X = {'A': 3,
             'B': 5,
             'C': 7,
             'D': 9}

GRID1 = ['#############',
         '#  . . . .  #',
         '###.#.#.#.###',
         '  #.#.#.#.#',
         '  #########']

GRID2 = ['#############',
         '#  . . . .  #',
         '###.#.#.#.###',
         '  #.#.#.#.#',
         '  #.#.#.#.#',
         '  #.#.#.#.#',
         '  #########']


def step1(inp):
    return solve(GRID1, inp)


def step2(inp):
    return solve(GRID2, inp)


def solve(grid, inp):
    incorrect_initially = set()
    correct_initially = set()
    for y in range(len(inp) - 1, -1, -1):
        for x in range(0, len(inp[y])):
            c = inp[y][x]
            if c in 'ABCD':
                if is_final_target(grid, correct_initially, x, y, c):
                    correct_initially.add((x, y, c))
                else:
                    incorrect_initially.add((x, y, c))
    pq = [(0, frozenset(correct_initially), frozenset(incorrect_initially))]
    result = float('inf')
    cache = {}
    while pq:
        cost, correct, incorrect = heapq.heappop(pq)
        if cost >= result:
            continue
        key = (correct, incorrect)
        if cache.get(key, float('inf')) <= cost:
            continue
        cache[key] = cost
        if len(incorrect) == 0:
            result = min(result, cost)
            continue
        for fr, to, move_cost in possible_moves(grid, correct, incorrect):
            if is_final_target(grid, correct, to[0], to[1], to[2]):
                heapq.heappush(pq, (cost + move_cost, correct | {to}, incorrect - {fr}))
            else:
                heapq.heappush(pq, (cost + move_cost, correct, (incorrect - {fr}) | {to}))
    return result


def possible_moves(grid, correct, incorrect):
    result = []
    occupied = set()
    for (x, y, c) in correct:
        occupied.add((x, y))
    for (x, y, c) in incorrect:
        occupied.add((x, y))
    for init_pos in incorrect:
        vis = {(init_pos[0], init_pos[1])}
        q = [(0, init_pos)]
        while q:
            move_cost, (x, y, c) = q.pop(0)
            vis.add((x, y))
            if init_pos != (x, y, c):
                if is_final_target(grid, correct, x, y, c):
                    result.append((init_pos, (x, y, c), move_cost))
                elif init_pos[1] != 1 and grid[y][x] == ' ':
                    result.append((init_pos, (x, y, c), move_cost))  # can rest at this position
            for dx, dy in deltas4():
                new_pos = (x + dx, y + dy, c)
                if grid[y + dy][x + dx] != '#' and (x + dx, y + dy) not in vis and (x + dx, y + dy) not in occupied:
                    vis.add((x, y))
                    q.append((move_cost + COST[c], new_pos))
    return result


def is_final_target(grid, correct, x, y, c):
    assert c in 'ABCD'
    y2 = y + 1
    valid = True
    while grid[y2][x] != '#':
        valid = valid and (x, y2, c) in correct
        y2 += 1
    return valid and CORRECT_X[c] == x


def read_input():
    inp = []
    for y in range(0, 5):
        row = input()
        inp.append(tuple(row))
    return tuple(inp)


print('This one is slow. Wait for it...', file=sys.stderr)
inp1 = read_input()
print(step1(inp1))
inp2 = tuple(list(inp1[:3]) + [tuple('  #D#C#B#A#'), tuple('  #D#B#A#C#')] + list(inp1[3:]))
print(step2(inp2))
