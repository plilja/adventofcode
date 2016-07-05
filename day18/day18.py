import sys
from collections import defaultdict

def solve():
    def new_grid():
        return defaultdict(lambda : defaultdict(lambda : 0))

    def read_input():
        grid = new_grid()
        raw = [s.strip() for s in sys.stdin.readlines()]
        for i in range(0, 100):
            for j in range(0, 100):
                grid[i][j] = 0 if raw[i][j] == '.' else 1
        return grid

    def step(n, grid):
        if n == 0:
            return grid
        else:
            grid_ = new_grid()
            for i in range(0, 100):
                for j in range(0, 100):
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
        for i in range(0, 100):
            for j in range(0, 100):
                r += grid[i][j]
        return r


    return count_on(step(100, read_input()))

print(solve())
