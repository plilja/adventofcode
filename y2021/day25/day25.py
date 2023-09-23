import sys


DELTAS = {'>': (1, 0),
          'v': (0, 1)}


def step1(grid):
    moved = True
    steps = 0
    while moved:
        steps += 1
        moved = False
        for c in ['>', 'v']:
            next_grid = [['.'] * len(grid[i]) for i in range(0, len(grid))]
            dx, dy = DELTAS[c]
            for y in range(0, len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x] == c:
                        x2 = (x + dx) % len(grid[y])
                        y2 = (y + dy) % len(grid)
                        if grid[y2][x2] == '.':
                            next_grid[y2][x2] = c
                            next_grid[y][x] = '.'
                            moved = True
                        else:
                            next_grid[y][x] = c
                    elif grid[y][x] != '.':
                        next_grid[y][x] = grid[y][x]
            grid = next_grid
    return steps


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
# no step 2 this day
