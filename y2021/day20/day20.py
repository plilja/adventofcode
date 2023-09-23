import sys


def step1(enhancement, grid):
    return enhance(enhancement, grid, 2)


def step2(enhancement, grid):
    return enhance(enhancement, grid, 50)


def enhance(enhancement, grid, steps):
    lit = set([(x, y) for y in range(0, len(grid)) for x in range(0, len(grid[0])) if grid[y][x] == '#'])
    visited = set(lit)
    assert enhancement[0] == '.' or enhancement[511] == '.'
    for i in range(0, steps):
        next_lit = set()
        to_check = set()
        for x, y in lit:
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    to_check.add((x + dx, y + dy))

        for x, y in to_check:
            mask = ''
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (x + dx, y + dy) in lit:
                        mask += '1'
                    else:
                        if enhancement[0] == '.' or (x + dx, y + dy) in visited:
                            mask += '0'
                        else:
                            mask += '1' if i % 2 == 1 else '0'
            n = int(mask, 2)
            if enhancement[n] == '#':
                next_lit.add((x, y))
        visited = to_check
        lit = next_lit
    return len(lit)


def main():
    inp = sys.stdin.readlines()
    enhancement = inp[0]
    grid = inp[2:]
    print(step1(enhancement, grid))
    print(step2(enhancement, grid))


if __name__ == '__main__':
    main()
