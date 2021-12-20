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


def step2(inp):
    def dfs(x, y, visited):
        if x < 0 or len(inp[0]) <= x or \
                y < 0 or len(inp) <= y or \
                (x, y) in visited or \
                inp[y][x] == 9:
            return 0
        result = 1
        visited.add((x, y))
        for dx, dy in deltas:
            result += dfs(x + dx, y + dy, visited)
        return result

    visited = set()
    basins = []
    for y in range(0, len(inp)):
        for x in range(0, len(inp[y])):
            basin = dfs(x, y, visited)
            basins.append(basin)
    basins.sort(key=lambda x: -x)
    return basins[0] * basins[1] * basins[2]


inp = [list(map(int, line.strip())) for line in sys.stdin]
print(step1(inp))
print(step2(inp))
