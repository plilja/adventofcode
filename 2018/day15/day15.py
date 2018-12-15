import sys
import copy
from collections import deque

deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def step1(grid):
    (winner, rounds, remaining) = solve(grid, 3, 3)
    return rounds * sum(remaining)


def step2(grid):
    elves = 0
    for row in grid:
        for c in row:
            if c == 'E':
                elves += 1
    i = 3
    while True:
        (winner, rounds, remaining) = solve(grid, i, 3)
        if winner == 'E' and len(remaining) == elves:
            return rounds * sum(remaining)
        i += 1


def solve(grid, elves_hit, goblins_hit):
    grid = copy.deepcopy(grid) 

    def bfs(start_x, start_y, targets):
        v = {(start_x, start_y)}
        q = deque([(start_x, start_y)])
        pre = {}
        while q:
            x, y = q.popleft()
            for dx, dy in deltas:
                if (x + dx, y + dy) in targets:
                    p = (x, y)
                    if (x, y) == (start_x, start_y):
                        return None
                    while pre[p] != (start_x, start_y):
                        p = pre[p]
                    return p
                if grid[y + dy][x + dx] == '.' and (x + dx, y + dy) not in v:
                    q.append((x + dx, y + dy))
                    pre[(x + dx, y + dy)] = (x, y)
                    v.add((x + dx, y + dy))
        return None


    goblins = {}
    elves = {}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'G':
                goblins[(x, y)] = 200
            elif c == 'E':
                elves[(x, y)] = 200

    r = 0
    while elves and goblins:
        units = sorted(list(elves.keys()) + list(goblins.keys()), key=lambda p: (p[1], p[0]))
        r += 1
        for x, y in units:
            if (x, y) not in elves and (x, y) not in goblins:
                continue
            if (x, y) in elves:
                friends = elves
                targets = goblins
            else:
                friends = goblins
                targets = elves

            move = bfs(x, y, targets)
            if move:
                points = friends[(x, y)]
                friends[move] = points
                del friends[(x, y)]
                grid[move[1]][move[0]] = grid[y][x]
                grid[y][x] = '.'
                x, y = move

            attacking_dist = [(x + dx, y + dy) for dx, dy in deltas]
            possible_attacks = sorted([p for p in attacking_dist if p in targets], key=lambda p: (targets[p], p[1], p[0]))
            if possible_attacks:
                p = possible_attacks[0]
                targets[p] -= elves_hit if (x, y) in elves else goblins_hit
                if targets[p] <= 0:
                    del targets[p]
                    grid[p[1]][p[0]] = '.'
            if not elves or not goblins:
                if (x, y) != units[-1]:
                    r -=1 # round was not fully completed
                    break

    winner = 'E' if len(elves) > 0 else 'G'
    return winner, r, list(elves.values()) + list(goblins.values())


# Spread input across a matrix for mutability
inp = [[c for c in s.strip()] for s in sys.stdin.readlines()]
print(step1(inp))
print(step2(inp))
