import sys


def step1(grid):
    deltas = [[(0, 0), (1, 0), (0, 1)],
              [(0, 0), (0, 1), (1, 0)],
              [(len(grid[0]) - 1, 0), (-1, 0), (0, 1)],
              [(0, len(grid) - 1), (0, -1), (1, 0)]]
    res = set()
    for [(startx, starty), (dx, dy), (loopdx, loopdy)] in deltas:
        while 0 <= startx < len(grid[0]) and 0 <= starty < len(grid):
            x = startx
            y = starty
            minimum = -1
            while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                v = int(grid[y][x])
                if v > minimum:
                    res.add((x, y))
                    minimum = v
                x += dx
                y += dy
            startx += loopdx
            starty += loopdy
    return len(res)


def step2(grid):
    dxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            score = 1
            height = int(grid[y][x])
            for dx, dy in dxs:
                count = 0
                x2 = x + dx
                y2 = y + dy
                while 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                    count += 1
                    if int(grid[y2][x2]) >= height:
                        break
                    x2 += dx
                    y2 += dy
                score *= count
            result = max(result, score)
    return result


def main():
    grid = [s.strip() for s in sys.stdin.readlines()]
    print(step1(grid))
    print(step2(grid))


if __name__ == '__main__':
    main()
