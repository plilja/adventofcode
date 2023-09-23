import sys
from collections import defaultdict

DIM = 100


def new_grid():
    return defaultdict(lambda: defaultdict(lambda: 0))


def solve(inp, exceptions):
    def step(n, grid):
        if n == 0:
            return grid
        else:
            grid_ = new_grid()
            for i in range(0, DIM):
                for j in range(0, DIM):
                    if (j, i) in exceptions:
                        grid_[i][j] = grid[i][j]
                        continue
                    neighbours = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + \
                                 grid[i][j - 1] + grid[i][j + 1] + \
                                 grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                    if grid[i][j]:
                        grid_[i][j] = 1 if neighbours in [2, 3] else 0
                    else:
                        grid_[i][j] = 1 if neighbours == 3 else 0
            return step(n - 1, grid_)

    def count_on(grid):
        r = 0
        for i in range(0, DIM):
            for j in range(0, DIM):
                r += grid[i][j]
        return r

    return count_on(step(100, inp))


def read_input():
    grid = new_grid()
    raw = [s.strip() for s in sys.stdin.readlines()]
    for i in range(0, DIM):
        for j in range(0, DIM):
            grid[i][j] = 0 if raw[i][j] == '.' else 1
    return grid


grid = read_input()
print(solve(grid, set()))

grid[0][0] = 1
grid[0][DIM - 1] = 1
grid[DIM - 1][0] = 1
grid[DIM - 1][DIM - 1] = 1
print(solve(grid, {(0, 0), (DIM - 1, 0), (0, DIM - 1), (DIM - 1, DIM - 1)}))
