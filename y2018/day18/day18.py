import copy
import sys

deltas = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
        ]


def step1(inp):
    return solve(inp, 10)


def step2(inp):
    return solve(inp, 1000000000)


def solve(inp, iterations):
    cache = {}
    g = copy.deepcopy(inp)
    g_next = copy.deepcopy(inp)
    i = 0
    while i < iterations:
        for y in range(0, len(g)):
            for x in range(0, len(g[y])):
                num_trees, num_lumber, num_open = 0, 0, 0
                for dx, dy in deltas:
                    if 0 <= y + dy < len(g) and 0 <= x + dx < len(g[y]):
                        num_trees += 1 if g[y + dy][x + dx] == '|' else 0
                        num_open += 1 if g[y + dy][x + dx] == '.' else 0
                        num_lumber += 1 if g[y + dy][x + dx] == '#' else 0

                g_next[y][x] = g[y][x]  # default, just copy
                if g[y][x] == '.' and num_trees >= 3:
                    g_next[y][x] = '|'
                if g[y][x] == '|' and num_lumber >= 3:
                    g_next[y][x] = '#'
                if g[y][x] == '#' and (num_lumber < 1 or num_trees < 1):
                    g_next[y][x] = '.'

        cache_key = ''.join([''.join(x) for x in g_next])
        if cache_key in cache:
            j = cache[cache_key]
            d = i - j
            i += d * ((iterations - i) // d)
        cache[cache_key] = i
        g, g_next = g_next, g
        i += 1
    
    trees, lumber = 0, 0
    for row in g:
        trees += len(list(filter(lambda x: x == '|', row)))
        lumber += len(list(filter(lambda x: x == '#', row)))
    return trees * lumber


def main():
    inp = list(map(lambda s: list(s.strip()), sys.stdin.readlines()))
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
