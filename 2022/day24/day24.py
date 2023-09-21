import sys
from heapq import heappop, heappush

sys.path.append("../..")
from common.util import neighbors4


def step1(inp):
    target_x = len(inp[0]) - 2
    target_y = len(inp) - 1
    return solve(inp, [(target_x, target_y)])


def step2(inp):
    target_x = len(inp[0]) - 2
    target_y = len(inp) - 1
    return solve(inp, [(target_x, target_y), (1, 0), (target_x, target_y)])


def solve(inp, waypoints):
    initial_grid = [[[c] if c != '.' else [] for c in s] for s in inp]
    result = 1
    start_x = 1
    start_y = 0
    dist_to_grid = {}
    dist_to_grid[0] = initial_grid
    for target_x, target_y in waypoints:
        q = [(abs(target_y - start_y) + abs(target_x - start_x), result, start_x, start_y)]
        visited = set()

        best = float('inf')
        while q:
            (to_goal, d, x, y) = heappop(q)
            if (x, y, d) in visited:
                continue
            visited.add((x, y, d))
            if d + to_goal >= best:
                continue
            if d not in dist_to_grid:
                dist_to_grid[d] = advance_avalanches(dist_to_grid[d - 1])
            grid = dist_to_grid[d]
            if grid[y][x]:
                continue
            if y == target_y and x == target_x:
                best = min(best, d)
                continue
            heappush(q, (to_goal, d + 1, x, y))  # wait without moving
            for x2, y2 in neighbors4(x, y):
                if y2 >= 0 and y2 < len(grid):
                    heappush(q, (abs(target_y - y2) + abs(target_x - x2), d + 1, x2, y2))
        result = best
        start_x = target_x
        start_y = target_y
    return result


def advance_avalanches(grid):
    new_grid = [[[] for c in row] for row in grid]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            for c in cell:
                if c == '.' or c == '#':
                    new_grid[y][x].append(c)
                    continue
                elif c == 'v':
                    dx, dy, wrap_x, wrap_y = 0, 1, x, 1
                elif c == '^':
                    dx, dy, wrap_x, wrap_y = 0, -1, x, len(grid) - 2
                elif c == '<':
                    dx, dy, wrap_x, wrap_y = -1, 0, len(row) - 2, y
                elif c == '>':
                    dx, dy, wrap_x, wrap_y = 1, 0, 1, y
                else:
                    raise ValueError('Unable to determine direction for {}'.format(c))

                if grid[y + dy][x + dx] == ['#']:
                    new_grid[wrap_y][wrap_x].append(c)
                else:
                    new_grid[y + dy][x + dx].append(c)
    return new_grid


if __name__ == '__main__':
    grid = [line.strip() for line in sys.stdin]
    print(step1(grid))
    print(step2(grid))
