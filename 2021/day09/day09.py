import sys

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def step1(inp):
    result = 0
    for y in range(0, len(inp)):
        for x in range(0, len(inp[y])):
            lowest = True
            for dx, dy in deltas:
                if 0 <= x + dx < len(inp[y]) and 0 <= y + dy < len(inp):
                    lowest = lowest and inp[y][x] < inp[y + dy][x + dx]
            if lowest:
                result += inp[y][x] + 1
    return result


inp = [list(map(int, line.strip())) for line in sys.stdin]
print(step1(inp))
